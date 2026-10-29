from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Informe diario fotográfico",
    page_icon="📷",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Quita márgenes y cabecera de Streamlit y hace que la app ocupe toda la pantalla
st.markdown(
    """
    <style>
      header[data-testid="stHeader"], footer, #MainMenu {display: none !important;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      [data-testid="stVerticalBlock"] {gap: 0 !important;}
      iframe {height: 100vh !important; height: 100dvh !important; border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
components.html(html, height=800, scrolling=True)
