import streamlit as st
import bcrypt
import traceback

from src.database.config import supabase


def _log_and_show_error(user_message: str, exc: Exception) -> None:
    full = f"{user_message}\n\nEXACT ERROR:\n{repr(exc)}\n\nTRACE:\n{traceback.format_exc()}"
    # Terminal
    print(full)
    # Streamlit
    st.error(full)


def hash_pass(pwd: str) -> str:
    return bcrypt.hashpw(pwd.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def check_pass(pwd: str, hashed: str) -> bool:
    return bcrypt.checkpw(pwd.encode("utf-8"), hashed.encode("utf-8"))


def supabase_ping() -> None:
    """Fail fast with exact error if Supabase is not reachable/auth failed."""
    # Prefer a no-op select
    _ = supabase.table("teachers").select("teacher_id").limit(1).execute()


def check_teacher_exists(username: str) -> bool:
    try:
        supabase_ping()
        response = supabase.table("teachers").select("username").eq("username", username).execute()
        return len(response.data) > 0
    except Exception as e:
        _log_and_show_error("Supabase check_teacher_exists failed.", e)
        return False


def create_teacher(username: str, password: str, name: str):
    try:
        supabase_ping()
        data = {"username": username, "password": hash_pass(password), "name": name}
        response = supabase.table("teachers").insert(data).execute()
        return response.data
    except Exception as e:
        _log_and_show_error("Supabase create_teacher failed.", e)
        raise


def teacher_login(username: str, password: str):
    try:
        # IMPORTANT: do NOT normalize username (no lower(), no strip()) here.
        # Supabase query must match EXACTLY, including internal/trailing spaces.
        print(f"Looking for teacher username (exact match): '{username}'")
        supabase_ping()
        response = (
            supabase.table("teachers")
            .select("*")
            .eq("username", username)
            .execute()
        )
        print(f"DB returned rows: {len(response.data) if response.data else 0}")
        if response.data:
            teacher = response.data[0]
            stored = teacher.get("password")
            print(f"Stored password hash present: {bool(stored)}")
            if not stored:
                return None

            # Verify password with bcrypt.checkpw (NOT our helper)
            is_valid = bcrypt.checkpw(
                password.encode("utf-8"),
                stored.encode("utf-8"),
            )
            print(f"Password valid: {is_valid}")
            if is_valid:
                return teacher

        return None
    except Exception as e:
        _log_and_show_error("Supabase teacher_login failed.", e)
        return None



def get_all_students():
    response = supabase.table('students').select("*").execute()
    return response.data

def create_student(new_name, face_embedding=None, voice_embedding=None):
    data = {'name': new_name, 'face_embedding':face_embedding, "voice_embedding": voice_embedding}
    response = supabase.table('students').insert(data).execute()
    return response.data


def create_subject(subject_code, name, section, teacher_id):
    data = {"subject_code": subject_code, "name": name, "section": section, "teacher_id": teacher_id}
    response = supabase.table("subjects").insert(data).execute()
    return response.data

def get_teacher_subjects(teacher_id):
    response = supabase.table('subjects').select("*, subject_students(count), attendance_logs(timestamp)").eq("teacher_id", teacher_id).execute()
    subjects = response.data


    for sub in subjects:
        sub['total_students'] = sub.get("subject_students", [{}])[0].get('count', 0) if sub.get('subject_students') else 0
        attendance = sub.get('attendance_logs', [])
        unique_sessions = len(set(log['timestamp'] for log in attendance))
        sub['total_classes'] = unique_sessions


        sub.pop('subject_student', None)
        sub.pop('attendance_logs', None)

    return subjects


def  enroll_student_to_subject(student_id, subject_id):
    data = {'student_id': student_id, "subject_id": subject_id}
    response= supabase.table('subject_students').insert(data).execute()
    return response.data


def  unenroll_student_to_subject(student_id, subject_id):
    response= supabase.table('subject_students').delete().eq('student_id', student_id).eq('subject_id', subject_id).execute()
    return response.data



def get_student_subjects(student_id):
    response = supabase.table('subject_students').select('*, subjects(*)').eq('student_id', student_id).execute()
    return response.data


def get_student_attendance(student_id):
    response = supabase.table('attendance_logs').select('*, subjects(*)').eq('student_id', student_id).execute()
    return response.data


def create_attendance(logs):
    response = supabase.table('attendance_logs').insert(logs).execute()
    return response.data

def get_attendance_for_teacher(teacher_id):
    response = supabase.table('attendance_logs').select("*, subjects!inner(*)").eq('subjects.teacher_id', teacher_id).execute()
    return response.data