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

base = Path(__file__).parent
candidatos = [base / "index.html"] + sorted(base.glob("*.html")) + sorted(base.glob("*/*.html"))
archivo = next((c for c in candidatos if c.exists()), None)

if archivo is None:
    st.error(
        "No se encontró el archivo **index.html** junto a app.py. "
        "Súbelo a la misma carpeta del repositorio (en la raíz) y reinicia la app."
    )
    st.write("Archivos que sí hay en esta carpeta:", sorted(p.name for p in base.iterdir()))
else:
    html = archivo.read_text(encoding="utf-8")
    components.html(html, height=800, scrolling=True)
