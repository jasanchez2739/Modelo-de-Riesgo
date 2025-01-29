import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# Definir estilos de PwC
st.markdown("""
    <style>
    .main {background-color: #f8f9fa;}
    h1 {color: #bb3f00; text-align: center; font-size: 36px;}
    .stButton>button {background-color: #bb3f00; color: white; font-size: 16px;}
    </style>
""", unsafe_allow_html=True)

# Configuración de la página
st.set_page_config(page_title="Evaluación de Controles Internos", layout="wide")
st.title("📊 Evaluación del Nivel de Madurez de Controles Internos")

# Definir los principios de COSO 2013 con preguntas
preguntas = {
    "Compromiso con la integridad y valores éticos": [
        "¿Existe un código de ética formalmente establecido y comunicado a todos los empleados?",
        "¿Se realizan capacitaciones periódicas sobre valores éticos y conducta empresarial?",
        "¿Existen mecanismos para reportar violaciones éticas de manera anónima y segura?"
    ],
    "Independencia y supervisión del consejo": [
        "¿El consejo de administración supervisa activamente el sistema de control interno?",
        "¿El consejo de administración cuenta con miembros independientes con experiencia en auditoría y control?",
        "¿El consejo revisa periódicamente la efectividad de los controles internos y toma acciones correctivas?"
    ],
    "Estructura organizativa y asignación de responsabilidades": [
        "¿La empresa ha definido claramente roles y responsabilidades en materia de control interno?",
        "¿Existen líneas de reporte claras para comunicar temas relacionados con control interno?",
        "¿Las responsabilidades de control están segregadas para evitar conflictos de interés?"
    ],
    "Atracción, desarrollo y retención de talento": [
        "¿Existen programas de capacitación continua sobre control interno y gestión de riesgos?",
        "¿Se evalúan periódicamente las competencias del personal en materia de control interno?",
        "¿Los planes de carrera incluyen formación específica en controles internos?"
    ]
}

opciones_puntuacion = ["1 - No implementado", "2 - Parcialmente implementado", "3 - Moderadamente implementado", "4 - Casi totalmente implementado", "5 - Totalmente implementado"]

respuestas = {}
for principio, preguntas_lista in preguntas.items():
    st.subheader(f"📋 {principio}")
    for pregunta in preguntas_lista:
        respuestas[pregunta] = st.selectbox(pregunta, opciones_puntuacion)

if st.button("Calcular Nivel de Madurez"):
    df = pd.DataFrame(list(respuestas.items()), columns=["Pregunta", "Puntuación"])
    st.dataframe(df)
