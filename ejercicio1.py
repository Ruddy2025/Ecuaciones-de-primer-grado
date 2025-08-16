import streamlit as st
import random

st.set_page_config(page_title="Ecuaciones de primer grado", page_icon="🧮")

st.title("🧮 Resolviendo ecuaciones de primer grado")

# Inicialización de variables en session_state
if "a" not in st.session_state:
    st.session_state.a = random.randint(1, 10)
if "b" not in st.session_state:
    st.session_state.b = random.randint(-10, 10)
if "respuesta_correcta" not in st.session_state:
    st.session_state.respuesta_correcta = None
if "mensaje" not in st.session_state:
    st.session_state.mensaje = ""

# Función para generar nueva ecuación
def nueva_ecuacion():
    st.session_state.a = random.randint(1, 10)
    st.session_state.b = random.randint(-10, 10)
    st.session_state.respuesta_correcta = None
    st.session_state.mensaje = ""

# Generar la ecuación
a = st.session_state.a
b = st.session_state.b

st.write(f"Resuelve la siguiente ecuación para **x**:")
st.latex(f"{a}x + {b} = 0")

# Campo de entrada para la respuesta
respuesta = st.text_input("Tu respuesta para x:", "")

# Botón para verificar la respuesta
if st.button("Verificar respuesta"):
    try:
        valor_usuario = float(respuesta)
        x_correcto = -b / a
        if abs(valor_usuario - x_correcto) < 1e-6:
            st.session_state.mensaje = "✅ ¡Correcto! 🎉"
        else:
            st.session_state.mensaje = f"❌ Incorrecto. La respuesta correcta es: {x_correcto:.2f}"
    except ValueError:
        st.session_state.mensaje = "⚠️ Ingresa un número válido."

# Mostrar el mensaje de verificación
if st.session_state.mensaje:
    st.info(st.session_state.mensaje)

# Botón para generar un nuevo ejercicio
if st.button("Nuevo ejercicio"):
    nueva_ecuacion()
    st.rerun()
