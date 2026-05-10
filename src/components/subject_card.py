import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:#ffffff; border-left: 8px solid #f72585; padding:25px; border-radius: 20px; border: 1px solid rgba(26,26,46,0.25); margin-bottom:20px; color:#1a1a2e;">
        <h3 style="margin:0; color: #1a1a2e; font-size: 1.5rem; font-weight:900 ">{name}</h3>
        <p style="color:#1a1a2e; margin:10px 0; opacity:0.85;">Code : <span style="background:#E0E3FF; color:#4361ee; padding:2px 8px; border-radius:5px; font-weight:700;">{code} </span> | Section : {section}</p>
        
        """
    
    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background: rgba(247,37,133,0.08); padding:5px 12px; border-radius:12px; font-size:0.95rem; color:#1a1a2e; font-weight:600">{icon} <b style="color:#1a1a2e">{value}</b> {label} </div>'
        
        html+= "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()