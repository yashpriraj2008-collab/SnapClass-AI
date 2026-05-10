


import dlib


import numpy as np
import face_recognition_models
import streamlit as st

from src.database.db import get_all_students


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()

    sp = dlib.shape_predictor(face_recognition_models.pose_predictor_model_location())
    facerec = dlib.face_recognition_model_v1(face_recognition_models.face_recognition_model_location())

    return detector, sp, facerec


def get_face_embeddings(image_np: np.ndarray):
    """Return a list of 128-d face embeddings from the input image."""
    detector, sp, facerec = load_dlib_models()

    faces = detector(image_np, 1)
    encodings = []

    for face in faces:
        shape = sp(image_np, face)
        face_descriptor = facerec.compute_face_descriptor(image_np, shape, 1)  # 128-D
        encodings.append(np.asarray(face_descriptor, dtype=np.float32))

    return encodings


def _load_student_face_embeddings():
    """Load all student face embeddings as a normalized lookup table."""
    student_db = get_all_students() or []

    embeddings = []
    student_ids = []

    for student in student_db:
        emb = student.get("face_embedding")
        if emb is None:
            continue
        # Supabase may store as list of floats; enforce shape + dtype
        arr = np.asarray(emb, dtype=np.float32)
        if arr.ndim != 1 or arr.shape[0] != 128:
            continue
        embeddings.append(arr)
        # Ensure consistent ID type
        try:
            student_ids.append(int(student.get("student_id")))
        except Exception:
            continue

    if not embeddings:
        return None

    X = np.stack(embeddings, axis=0)
    # Normalize for cosine similarity
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1.0, norms)
    Xn = X / norms

    return {"Xn": Xn, "student_ids": student_ids}


@st.cache_resource
def get_embedding_store():
    return _load_student_face_embeddings()


def train_classifier():
    """Rebuild the cached embedding store."""
    st.cache_resource.clear()
    store = get_embedding_store()
    return bool(store)


def predict_attendance(class_image_np: np.ndarray):
    """Predict which students are present using nearest-neighbor matching.

    Returns:
      detected_student: dict[int, True]
      all_students: list[int]  (for UI/debug compatibility)
      num_faces: int
    """
    encodings = get_face_embeddings(class_image_np)
    detected_student = {}

    store = get_embedding_store()
    if not store:
        return detected_student, [], len(encodings)

    Xn = store["Xn"]
    student_ids = store["student_ids"]

    all_students = sorted(set(student_ids))

    # Cosine similarity threshold.
    # dlib FaceRecognitionModelV1 embeddings usually match around ~0.6-0.8.
    # Lowering/setting a strict cutoff reduces wrong matches.
    similarity_threshold = 0.45


    for encoding in encodings:
        denom = np.linalg.norm(encoding)
        if denom == 0:
            continue
        en = encoding / denom

        # cosine similarity to all stored embeddings
        sims = Xn @ en  # (N,)
        best_idx = int(np.argmax(sims))
        best_sim = float(sims[best_idx])

        if best_sim >= similarity_threshold:
            sid = int(student_ids[best_idx])
            detected_student[sid] = True

    # If nothing matched within threshold, reject the face(s).
    if not detected_student:
        return "unknown", all_students, len(encodings)

    return detected_student, all_students, len(encodings)


