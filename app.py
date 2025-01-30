import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# Configuración de la página (debe ir al principio del script)
st.set_page_config(page_title="Evaluación de Controles Internos", layout="wide")

# Inicializar sesión para almacenar respuestas
if "respuestas" not in st.session_state:
    st.session_state["respuestas"] = {}

# Sidebar de navegación
st.sidebar.title("Navegación")
paginas = ["Ambiente de Control", "Evaluación de Riesgos", "Actividades de Control", "Información y Comunicación", "Monitoreo de Actividades", "Resultados"]
seleccion = st.sidebar.radio("Selecciona un componente:", paginas)

# Botón de cálculo en la barra lateral
if st.sidebar.button("Calcular Nivel de Madurez"):
    df = pd.DataFrame(list(st.session_state["respuestas"].items()), columns=["Pregunta", "Puntuación"])
    st.session_state["df_resultados"] = df
    st.sidebar.success("Resultados calculados. Ve a la pestaña de Resultados.")

if seleccion == "Resultados":
    st.header("📊 Resultados de la Evaluación")
    if "df_resultados" in st.session_state:
        df = st.session_state["df_resultados"]
        st.dataframe(df)
        
        # Calcular el promedio de cada componente
        componentes = {
            "Ambiente de Control": ["Compromiso con la integridad y valores éticos", "Independencia y supervisión del consejo", "Estructura organizativa y asignación de responsabilidades", "Atracción, desarrollo y retención de talento", "Rendición de cuentas en la organización"],
            "Evaluación de Riesgos": ["Especificación de objetivos claros", "Identificación y evaluación de riesgos", "Consideración del potencial de fraude", "Evaluación de cambios en el entorno"],
            "Actividades de Control": ["Desarrollo de actividades de control", "Uso de tecnología en actividades de control", "Implementación de políticas y procedimientos"],
            "Información y Comunicación": ["Obtención y uso de información relevante", "Comunicación interna eficaz", "Comunicación externa sobre riesgos y control"],
            "Monitoreo de Actividades": ["Monitoreo continuo y evaluación de controles", "Reporte y corrección de deficiencias de control"]
        }
        
        promedios = {}
        for componente, principios in componentes.items():
            valores = [int(df[df["Pregunta"].str.contains(principio)]["Puntuación"].iloc[0].split(" - ")[0]) for principio in principios if not df[df["Pregunta"].str.contains(principio)]["Puntuación"].empty]
            promedios[componente] = sum(valores) / len(valores) if valores else 0
        
        # Crear diagrama de radar
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=list(promedios.values()) + [list(promedios.values())[0]],
            theta=list(promedios.keys()) + [list(promedios.keys())[0]],
            fill='toself',
            name='Nivel de Madurez'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[1, 5])
            ),
            showlegend=False,
            title="📌 Gráfico de Radar - Nivel de Madurez por Componente"
        )
        
        st.plotly_chart(fig)
    else:
        st.warning("Aún no has calculado los resultados. Completa las evaluaciones y presiona 'Calcular Nivel de Madurez'.")
else:
    # Definir los principios de COSO 2013 agrupados en los 5 componentes
    preguntas = {
        "Ambiente de Control": {
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
            ]
        },
        "Evaluación de Riesgos": {
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
            ]
        }
    }

    opciones_puntuacion = ["1 - No implementado", "2 - Parcialmente implementado", "3 - Moderadamente implementado", "4 - Casi totalmente implementado", "5 - Totalmente implementado"]
    
    st.header(f"🛠 {seleccion}")
    for principio, preguntas_lista in preguntas.get(seleccion, {}).items():
        st.subheader(f"📋 {principio}")
        for pregunta in preguntas_lista:
            st.session_state["respuestas"][pregunta] = st.selectbox(pregunta, opciones_puntuacion, key=pregunta)
