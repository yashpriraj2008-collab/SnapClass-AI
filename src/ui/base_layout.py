import streamlit as st


def style_background_home():
    st.markdown(
        """
        <style>
            .stApp {
                /* subtle purple accent wash instead of solid blocks */
                background: var(--snap-bg) !important;
            }
            .stApp div[data-testid="stColumn"]{
                background-color: var(--snap-surface) !important;
                padding: 2.25rem !important;
                border-radius: 1.25rem !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_background_dashboard():
    st.markdown(
        """
        <style>
            .stApp {
                background: var(--snap-bg) !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_base_layout():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        :root{
            --snap-bg: #F5F7FF;
            --snap-primary: #5B6CFF;
            --snap-secondary: #FF4FA3;

            --snap-text: #1F2937;
            --snap-muted: #6B7280;

            --snap-surface: #FFFFFF;
            --snap-border: #E5E7EB;

            --snap-shadow: 0 10px 25px rgba(31, 41, 55, 0.08);
            --snap-radius: 16px;

            /* soft modern gradients (very subtle) */
            --snap-grad: linear-gradient(135deg, rgba(91,108,255,0.12) 0%, rgba(255,79,163,0.10) 100%);
            --snap-btn-grad: linear-gradient(180deg, rgba(91,108,255,1) 0%, rgba(91,108,255,0.94) 100%);
            --snap-focus: 0 0 0 3px rgba(91,108,255,0.25);
        }

        /* Hide Streamlit chrome */
        #MainMenu, footer, header {
            visibility: hidden;
        }

        /* Global layout paddings */
        .block-container{
            padding-top: 1.5rem !important;
            color: var(--snap-text) !important;
        }

        /* Typography */
        body, .stMarkdown, .stText, .stSubheader, .stHeader, .stTitle{
            color: var(--snap-text) !important;
            font-family: 'Outfit', sans-serif !important;
        }

        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.1rem !important;
            line-height: 1.05 !important;
            margin-bottom: 0rem !important;
            color: var(--snap-text) !important;
            font-weight: 700 !important; /* avoid ultra-bold overlap */
        }

        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2rem !important;
            line-height: 1.05 !important;
            margin-bottom: 0rem !important;
            color: var(--snap-text) !important;
            font-weight: 650 !important;
        }

        h3, h4, p {
            font-family: 'Outfit', sans-serif;
            color: var(--snap-text) !important;
        }

        /* Streamlit header/subheader wrappers */
        div[data-testid="stHeader"],
        div[data-testid="stSubheader"] {
            color: var(--snap-text) !important;
        }

        div[data-testid="stHeader"] span,
        div[data-testid="stSubheader"] span {
            color: var(--snap-text) !important;
            font-weight: 700 !important;
        }

        /* Buttons: override all kinds with readable contrast */
        button[kind="primary"],
        button[kind="secondary"],
        button,
        .stButton > button {
            border-radius: 999px !important;
            border: 1px solid rgba(91,108,255,0.15) !important;
            padding: 10px 20px !important;
            font-weight: 750 !important;
            transition: transform 120ms ease, filter 120ms ease, box-shadow 120ms ease !important;
        }

        button,
        .stButton > button{
            background: var(--snap-btn-grad) !important;
            color: #ffffff !important;
            box-shadow: 0 10px 20px rgba(91,108,255,0.15) !important;
        }

        button[kind="secondary"]{
            background: #ffffff !important;
            color: var(--snap-text) !important;
            border: 1px solid var(--snap-border) !important;
            box-shadow: 0 10px 20px rgba(31, 41, 55, 0.06) !important;
        }

        button[kind="secondary"]:hover{
            filter: brightness(0.98) !important;
        }

        button[kind="tertiary"]{
            background: rgba(91,108,255,0.08) !important;
            color: var(--snap-primary) !important;
            border: 1px solid rgba(91,108,255,0.25) !important;
            box-shadow: none !important;
        }

        button:hover{
            transform: scale(1.03) !important;
        }

        button:focus, button:focus-visible{
            outline: none !important;
            box-shadow: var(--snap-focus) !important;
        }

        /* Ensure icons/spans inside buttons match text color */
        button span, button svg, button .stMarkdown {
            color: inherit !important;
            fill: currentColor !important;
        }

        /* Cards/surfaces in general */
        [data-testid="stVerticalBlock"] > div,
        .stContainer{
            border-radius: var(--snap-radius) !important;
        }

        /* Dialog readability */
        [data-testid="stDialog"]{
            background: var(--snap-surface) !important;
            color: var(--snap-text) !important;
        }
        [data-testid="stDialog"] *{
            color: var(--snap-text) !important;
        }

        /* Toast: readable */
        [data-testid="stToast"]{
            background-color: rgba(31,41,55,0.92) !important;
            color: #ffffff !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
