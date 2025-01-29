import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# Configuración de la página (debe ir al principio del script)
st.set_page_config(page_title="Evaluación de Controles Internos", layout="wide")

# Definir estilos de PwC
st.markdown("""
    <style>
    .main {background-color: #f8f9fa;}
    h1 {color: #bb3f00; text-align: center; font-size: 36px;}
    .stButton>button {background-color: #bb3f00; color: white; font-size: 16px;}
    </style>
""", unsafe_allow_html=True)

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
    
    # Convertir las puntuaciones a valores numéricos
    df["Puntuación"] = df["Puntuación"].apply(lambda x: int(x[0]))
    
    # Agrupar por principio y calcular la media
    df_grouped = df.groupby(df["Pregunta"].apply(lambda x: x.split(" ")[0]))["Puntuación"].mean().reset_index()
    
    # Crear el gráfico de radar
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=df_grouped["Puntuación"].tolist() + [df_grouped["Puntuación"].iloc[0]],
        theta=df_grouped["Pregunta"].tolist() + [df_grouped["Pregunta"].iloc[0]],
        fill='toself',
        name='Nivel de Madurez'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[1, 5])
        ),
        showlegend=False,
        title="📌 Gráfico de Radar - Nivel de Madurez"
    )
    
    st.plotly_chart(fig)
    
    st.dataframe(df)
