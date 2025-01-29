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
    ],
    "Rendición de cuentas en la organización": [
        "¿Se han definido indicadores de desempeño relacionados con el cumplimiento de los controles internos?",
        "¿Los incumplimientos a los controles internos tienen consecuencias claras y aplicables?",
        "¿Los líderes de la organización fomentan la responsabilidad en el cumplimiento de controles internos?"
    ],
    "Especificación de objetivos claros": [
        "¿Los objetivos de la empresa están alineados con el marco de control interno?",
        "¿Los objetivos operativos, financieros y de cumplimiento están claramente definidos y comunicados?",
        "¿Se evalúa periódicamente el logro de los objetivos estratégicos en relación con el control interno?"
    ],
    "Identificación y evaluación de riesgos": [
        "¿Existe un proceso formal de identificación y evaluación de riesgos?",
        "¿Se actualiza periódicamente la matriz de riesgos?",
        "¿Se consideran factores internos y externos en la evaluación de riesgos?"
    ],
    "Consideración del potencial de fraude": [
        "¿Se han implementado controles específicos para prevenir y detectar fraudes?",
        "¿Se realiza un análisis de riesgo de fraude en las áreas críticas de la organización?",
        "¿El canal de denuncias de fraudes es seguro y confidencial?"
    ],
    "Evaluación de cambios en el entorno": [
        "¿La empresa analiza el impacto de los cambios regulatorios en sus controles internos?",
        "¿Existen procedimientos para adaptar los controles internos a nuevas condiciones del mercado?",
        "¿Se revisa periódicamente la estrategia de control interno ante cambios tecnológicos?"
    ],
    "Desarrollo de actividades de control": [
        "¿Existen controles diseñados para mitigar los riesgos identificados?",
        "¿Se documentan y comunican adecuadamente las actividades de control a los responsables?",
        "¿Los controles se revisan y actualizan de manera periódica?"
    ],
    "Uso de tecnología en actividades de control": [
        "¿La empresa utiliza herramientas tecnológicas para fortalecer los controles internos?",
        "¿Se han automatizado procesos clave de control para mejorar eficiencia y precisión?",
        "¿Se monitorean los sistemas tecnológicos para evitar brechas de seguridad?"
    ],
    "Implementación de políticas y procedimientos": [
        "¿Las políticas y procedimientos de control interno están formalmente documentados?",
        "¿Se revisan y actualizan periódicamente los procedimientos de control?",
        "¿El personal conoce y aplica los procedimientos establecidos en su área de trabajo?"
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
