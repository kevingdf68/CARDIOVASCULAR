import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ==============================
# CONFIGURAÇÃO DA PÁGINA
# ==============================

st.set_page_config(
    page_title="Risco Cardiovascular",
    page_icon="❤️",
    layout="centered"
)

# ==============================
# TÍTULO
# ==============================

st.title("Sistema de Predição de Risco Cardiovascular")

st.write("""
Este protótipo utiliza Inteligência Artificial para estimar o risco cardiovascular
com base em dados clínicos do paciente.
""")

# ==============================
# CARREGAMENTO DO DATASET
# ==============================

df = pd.read_csv("heart (1).csv")

df = df.drop_duplicates()

X = df.drop("target", axis=1)
y = df["target"]

# ==============================
# DIVISÃO DOS DADOS
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==============================
# TREINAMENTO DO MODELO
# ==============================

modelo_rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

modelo_rf.fit(X_train, y_train)

pred_rf = modelo_rf.predict(X_test)
accuracy = accuracy_score(y_test, pred_rf)

# ==============================
# INFORMAÇÃO DO MODELO
# ==============================

st.info(f"Modelo utilizado: Random Forest | Acurácia aproximada: {accuracy:.2%}")

# ==============================
# FORMULÁRIO DE ENTRADA
# ==============================

st.subheader("Informe os dados do paciente")

age = st.number_input(
    "Idade",
    min_value=1,
    max_value=120,
    value=50
)

sex = st.selectbox(
    "Sexo",
    options=[0, 1],
    format_func=lambda x: "Feminino" if x == 0 else "Masculino"
)

cp = st.selectbox(
    "Tipo de dor no peito",
    options=[0, 1, 2, 3],
    format_func=lambda x: {
        0: "0 - Assintomática",
        1: "1 - Angina típica",
        2: "2 - Angina atípica",
        3: "3 - Dor não anginosa"
    }[x]
)

trestbps = st.number_input(
    "Pressão arterial em repouso",
    min_value=80,
    max_value=220,
    value=120
)

chol = st.number_input(
    "Colesterol",
    min_value=100,
    max_value=600,
    value=200
)

fbs = st.selectbox(
    "Glicemia em jejum maior que 120 mg/dl?",
    options=[0, 1],
    format_func=lambda x: "Não" if x == 0 else "Sim"
)

restecg = st.selectbox(
    "Resultado do eletrocardiograma",
    options=[0, 1, 2]
)

thalach = st.number_input(
    "Frequência cardíaca máxima",
    min_value=60,
    max_value=250,
    value=150
)

exang = st.selectbox(
    "Angina induzida por exercício?",
    options=[0, 1],
    format_func=lambda x: "Não" if x == 0 else "Sim"
)

oldpeak = st.number_input(
    "Oldpeak",
    min_value=0.0,
    max_value=10.0,
    value=1.0,
    step=0.1
)

slope = st.selectbox(
    "Inclinação do segmento ST",
    options=[0, 1, 2]
)

ca = st.selectbox(
    "Número de vasos principais",
    options=[0, 1, 2, 3, 4]
)

thal = st.selectbox(
    "Resultado do teste Thal",
    options=[0, 1, 2, 3]
)

# ==============================
# PREVISÃO
# ==============================

if st.button("Prever risco cardiovascular"):

    dados_paciente = pd.DataFrame([{
        "age": age,
        "sex": sex,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": ca,
        "thal": thal
    }])

    previsao = modelo_rf.predict(dados_paciente)[0]
    probabilidade = modelo_rf.predict_proba(dados_paciente)[0][1]

    st.subheader("Resultado da Predição")

    if previsao == 1:
        st.error("Alto risco cardiovascular")
    else:
        st.success("Baixo risco cardiovascular")

    st.write(f"Probabilidade estimada de risco: {probabilidade:.2%}")

    st.warning("""
Este sistema é apenas um protótipo acadêmico e não substitui avaliação médica profissional.
""")