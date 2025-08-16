import streamlit as st
import random

st.set_page_config(page_title="Trivia Vargas Llosa", page_icon="📚")

st.title("📚 Trivia: Personajes en las novelas de Mario Vargas Llosa")

# Base de datos de preguntas (se pueden ampliar)
preguntas = [
    {
        "pregunta": "¿Quién es el protagonista de *La ciudad y los perros*?",
        "opciones": ["El Jaguar", "Lituma", "Pantaleón Pantoja", "Zavalita"],
        "respuesta": "El Jaguar"
    },
    {
        "pregunta": "¿Qué personaje dirige un servicio secreto en *Conversación en La Catedral*?",
        "opciones": ["Zavalita", "Cayo Bermúdez", "Fushía", "El Poeta"],
        "respuesta": "Cayo Bermúdez"
    },
    {
        "pregunta": "¿Qué personaje organiza un servicio de prostitutas en *Pantaleón y las visitadoras*?",
        "opciones": ["Lituma", "Pantaleón Pantoja", "Ricardo Arana", "Santiago Zavala"],
        "respuesta": "Pantaleón Pantoja"
    },
    {
        "pregunta": "¿Quién es el periodista en *Conversación en La Catedral*?",
        "opciones": ["Ricardo Arana", "Lituma", "Santiago Zavala (Zavalita)", "Pantaleón Pantoja"],
        "respuesta": "Santiago Zavala (Zavalita)"
    },
    {
        "pregunta": "¿Qué personaje aparece en varias novelas de Vargas Llosa, incluido *Lituma en los Andes*?",
        "opciones": ["El Jaguar", "Lituma", "Pantaleón", "Fushía"],
        "respuesta": "Lituma"
    },
    {
        "pregunta": "¿Qué personaje es contrabandista en *La casa verde*?",
        "opciones": ["Pantaleón", "Fushía", "Lituma", "Zavalita"],
        "respuesta": "Fushía"
    },
]

# Estado inicial
if "pregunta_actual" not in st.session_state:
    st.session_state.pregunta_actual = random.choice(preguntas)
if "mensaje" not in st.session_state:
    st.session_state.mensaje = ""

# Mostrar pregunta actual
pregunta = st.session_state.pregunta_actual
st.subheader(pregunta["pregunta"])

opcion = st.radio("Elige una opción:", pregunta["opciones"])

# Botón verificar
if st.button("Verificar respuesta"):
    if opcion == pregunta["respuesta"]:
        st.session_state.mensaje = "✅ ¡Correcto! 🎉"
    else:
        st.session_state.mensaje = f"❌ Incorrecto. La respuesta correcta es: {pregunta['respuesta']}"

# Mostrar resultado
if st.session_state.mensaje:
    st.info(st.session_state.mensaje)

# Botón nuevo ejercicio
if st.button("Nuevo ejercicio"):
    st.session_state.pregunta_actual = random.choice(preguntas)
    st.session_state.mensaje = ""
    st.rerun()
