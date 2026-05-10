import streamlit as st

import segno
import io
import pyperclip


@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):
    # Use the deployed Streamlit URL (no localhost)
    app_domain = "https://snapclass-main.streamlit.app"
    join_url = f"{app_domain}/?join-code={subject_code}"

    st.header("Scan to Join")

    qr = segno.make(join_url)

    out = io.BytesIO()

    qr.save(out, kind='png', scale=10, border=1)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('### Copy Link')

        # Copyable content
        st.code(join_url, language="text")
        st.code(subject_code, language="text")

        # Button to copy URL to clipboard
        if st.button('Copy class link', type='primary', width='stretch', key='copy_class_link'):
            try:
                pyperclip.copy(join_url)
                st.toast('Link copied!')
            except Exception:
                # Fallback: keep URL visible for manual copy
                st.code(join_url)

        st.info('Copy this link to share on Whatsapp or Email')

    with col2:
        st.markdown('### Scan to Join')
        st.image(out.getvalue(), caption='QRCODE for class joining')

        