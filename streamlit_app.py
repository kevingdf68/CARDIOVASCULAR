import streamlit as st
import base64

# =========================================================
# FUNDO DA APLICAÇÃO
# =========================================================

def set_background():
    with open("fundo.png", "rb") as image:
        encoded = base64.b64encode(image.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="Triagem de Risco Cardiovascular",
    page_icon="❤️",
    layout="centered"
)

set_background()

# =========================================================
# ESTILO DOS TEXTOS E CONTAINER
# =========================================================

st.markdown("""
<style>

/* Caixa principal branca/translúcida */
.main > div {
    background-color: rgba(255,255,255,0.88);
    padding: 2rem;
    border-radius: 20px;
}

/* Texto geral */
html, body, [class*="css"] {
    color: black !important;
}

/* Títulos */
h1, h2, h3, h4, h5, h6 {
    color: black !important;
}

/* Labels */
label {
    color: black !important;
    font-weight: 600 !important;
}

/* Parágrafos e textos */
p, span, div {
    color: black !important;
}

/* Inputs */
.stTextInput input,
.stNumberInput input {
    color: black !important;
}

/* Selectbox */
.stSelectbox div {
    color: black !important;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* Texto digitado nos inputs */
.stTextInput input {
    color: white !important;
}

/* Número */
.stNumberInput input {
    color: white !important;
}

/* Selectbox */
[data-baseweb="select"] {
    color: white !important;
}

/* Valor selecionado */
[data-baseweb="select"] span {
    color: white !important;
}

/* Placeholder */
input::placeholder {
    color: rgba(255,255,255,0.8) !important;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TÍTULO
# =========================================================

st.title("Triagem Inicial de Risco Cardiovascular")

st.write("""
Este sistema realiza uma triagem inicial de risco cardiovascular com base
em sintomas, histórico familiar e hábitos de vida.
""")

st.warning("""
Este sistema é apenas um protótipo acadêmico e não substitui avaliação médica profissional.
""")

# =========================================================
# FORMULÁRIO
# =========================================================

st.subheader("Informe seus dados")

nome = st.text_input("1. Nome")

idade = st.number_input(
    "2. Idade",
    min_value=1,
    max_value=120,
    value=20
)

genero = st.selectbox(
    "3. Gênero",
    [
        "Feminino",
        "Masculino",
        "Outro / Prefiro não informar"
    ]
)

dor_peito = st.selectbox(
    "4. Teve dor no peito nos últimos 30 dias?",
    [
        "Não",
        "Sim, leve",
        "Sim, moderada",
        "Sim, forte"
    ]
)

historico_familiar = st.selectbox(
    "5. Tem histórico de doença cardiovascular na família?",
    [
        "Não",
        "Sim",
        "Não sei"
    ]
)

exercicio = st.selectbox(
    "6. Você pratica exercícios físicos?",
    [
        "Não pratico",
        "Sim, 1 a 2 vezes por semana",
        "Sim, 3 a 4 vezes por semana",
        "Sim, 5 vezes ou mais por semana"
    ]
)

alimentacao = st.selectbox(
    "7. Em um almoço comum no seu dia a dia, qual opção melhor te atende?",
    [
        "Arroz, feijão, salada e frango",
        "Macarrão, carne e molho de tomate",
        "Fast food (cachorro-quente, hambúrguer, pizza, etc.)",
        "Parmegiana de frango"
    ]
)

cigarro = st.selectbox(
    "8. Você faz uso de cigarro?",
    [
        "Não",
        "Sim, raramente",
        "Sim, algumas vezes por semana",
        "Sim, todos os dias"
    ]
)

alcool = st.selectbox(
    "9. Você faz uso de bebida alcoólica?",
    [
        "Não",
        "Sim, raramente",
        "Sim, algumas vezes por semana",
        "Sim, todos os dias"
    ]
)

ansiedade = st.selectbox(
    "10. Você tem se sentido ansioso frequentemente?",
    [
        "Não",
        "Às vezes",
        "Frequentemente"
    ]
)

sono = st.selectbox(
    "11. Você está tendo dificuldades para dormir?",
    [
        "Não",
        "Às vezes",
        "Frequentemente"
    ]
)

# =========================================================
# CÁLCULO DO RISCO
# =========================================================

if st.button("Calcular risco cardiovascular"):

    score = 0

    if idade >= 60:
        score += 3
    elif idade >= 45:
        score += 2
    elif idade >= 30:
        score += 1

    if dor_peito == "Sim, leve":
        score += 2
    elif dor_peito == "Sim, moderada":
        score += 4
    elif dor_peito == "Sim, forte":
        score += 6

    if historico_familiar == "Sim":
        score += 3
    elif historico_familiar == "Não sei":
        score += 1

    if exercicio == "Não pratico":
        score += 3
    elif exercicio == "Sim, 1 a 2 vezes por semana":
        score += 1

    if alimentacao == "Macarrão, carne e molho de tomate":
        score += 1
    elif alimentacao == "Parmegiana de frango":
        score += 2
    elif alimentacao == "Fast food (cachorro-quente, hambúrguer, pizza, etc.)":
        score += 4

    if cigarro == "Sim, raramente":
        score += 1
    elif cigarro == "Sim, algumas vezes por semana":
        score += 3
    elif cigarro == "Sim, todos os dias":
        score += 5

    if alcool == "Sim, raramente":
        score += 1
    elif alcool == "Sim, algumas vezes por semana":
        score += 2
    elif alcool == "Sim, todos os dias":
        score += 3

    if ansiedade == "Às vezes":
        score += 1
    elif ansiedade == "Frequentemente":
        score += 2

    if sono == "Às vezes":
        score += 1
    elif sono == "Frequentemente":
        score += 2

    # =====================================================
    # RESULTADO
    # =====================================================

    st.subheader("Resultado da Triagem")

    st.write(f"Paciente: **{nome}**")
    st.write(f"Pontuação de risco: **{score} pontos**")

    if score <= 7:

        st.image("baixo_risco.png", use_container_width=True)
        st.success("Baixo risco cardiovascular")
        st.write("Recomenda-se manter hábitos saudáveis e realizar check-up de rotina.")

    elif score <= 15:

        st.image("medio_risco.png", use_container_width=True)
        st.warning("Médio risco cardiovascular")
        st.write("Recomenda-se realizar um novo check-up e, se possível, consultar um cardiologista.")

    else:

        st.image("alto_risco.png", use_container_width=True)
        st.error("Alto risco cardiovascular")
        st.write("Recomenda-se procurar um cardiologista o mais rápido possível.")

    st.info("Este resultado é apenas uma triagem inicial e não representa diagnóstico médico.")
