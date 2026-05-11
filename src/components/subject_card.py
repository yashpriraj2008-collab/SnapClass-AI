import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="
            background: #ffffff;
            border: 1px solid rgba(229,231,235,1);
            box-shadow: 0 10px 25px rgba(31,41,55,0.06);
            border-radius: 20px;
            padding: 22px;
            margin-bottom: 18px;
            color: var(--snap-text);
        ">
        <div style="
            border-left: 8px solid rgba(255,79,163,1);
            padding-left: 18px;
        ">
            <h3 style="
                margin:0;
                color: var(--snap-text);
                font-size: 1.35rem;
                font-weight: 750;
                line-height: 1.2;
            ">{name}</h3>

            <p style="color: var(--snap-text); margin:10px 0 0 0; opacity:0.9; font-weight: 600;">
                Code :
                <span style="
                    background: rgba(224,227,255,1);
                    color: var(--snap-primary);
                    padding: 2px 8px;
                    border-radius: 8px;
                    font-weight: 800;
                ">{code}</span>
                &nbsp;|&nbsp; Section : {section}
            </p>

    """

    if stats:
        html += """
            <div style="display:flex; gap:10px; flex-wrap:wrap; margin-top:14px;">
        """
        for icon, label, value in stats:
            html += f"""
                <div style="
                    background: rgba(255,79,163,0.09);
                    padding: 7px 12px;
                    border-radius: 14px;
                    font-size: 0.95rem;
                    color: var(--snap-text);
                    font-weight: 650;
                    border: 1px solid rgba(255,79,163,0.12);
                ">
                    {icon} <b style="color: var(--snap-text); font-weight: 850;">{value}</b> {label}
                </div>
            """

        html += "</div>"

    html += """
        </div>
        </div>
    """

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
