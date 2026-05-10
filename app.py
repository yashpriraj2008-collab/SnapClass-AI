
import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

from src.components.dialog_auto_enroll import auto_enroll_dialog

def main():
    
    # Global fix: ensure ALL Streamlit button text + headings + dialog text are visible
    st.markdown(
        """
        <style>
        /* Fix ALL button text */
        .stButton > button {
            color: #ffffff !important;
            font-weight: 600 !important;
        }

        /* Fix ALL dialog/popup text (white-on-dark) */
        css[data-testid="stDialog"] * {
            color: #ffffff !important;
        }
        [data-testid="stDialog"] h1,
        [data-testid="stDialog"] h2,
        [data-testid="stDialog"] p,
        [data-testid="stDialog"] label,
        [data-testid="stDialog"] span {
            color: #ffffff !important;
        }

        /* Ensure toast notifications are white-on-dark */
        [data-testid="stToast"] {
            color: #ffffff !important;
            background-color: #1a1a2e !important;
        }
        [data-testid="stToast"] p {
            color: #ffffff !important;
        }

        /* Fix nav buttons */
        [data-testid="baseButton-primary"],
        [data-testid="baseButton-secondary"] {
            color: #ffffff !important;
        }

        /* Fix welcome text */
        .welcome-text {
            color: #1a1a2e !important;
            font-weight: 700 !important;
        }

        /* Fix nav buttons specifically */
        div[data-testid="column"] .stButton > button {
            color: #ffffff !important;
        }

        /* Fix all headings */
        h1, h2, h3, h4 {
            color: #1a1a2e !important;
        }

        /* Fix toast button/labels if any */
        [data-testid="stToast"] label,
        [data-testid="stToast"] span {
            color: #ffffff !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.set_page_config(
        page_title='SnapClass - Making Attendance faster using AI',
        page_icon= "https://i.ibb.co/YTYGn5qV/logo.png"
    )
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()
        
        case None:
            home_screen()


    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)
main()