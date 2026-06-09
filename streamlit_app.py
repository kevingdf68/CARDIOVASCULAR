import streamlit as st
import base64

# =========================================================
# FUNDO DA APLICAÇÃO
# =========================================================

def set_background(image_file="fundo.png"):
    try:
        with open(image_file, "rb") as image:
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
    except FileNotFoundError:
        st.warning("Imagem de fundo não encontrada. Verifique se o arquivo 'fundo.png' está na mesma pasta do app.")

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="Triagem de Risco Cardiovascular",
    page_icon="",
    layout="centered"
)

set_background()

# =========================================================
# ESTILO DA PÁGINA
# =========================================================

st.markdown("""
<style>

/* Caixa principal branca/translúcida */
.main > div {
    background-color: rgba(255,255,255,0.88);
    padding: 2rem;
    border-radius: 20px;
}

/* Textos principais pretos */
html, body, [class*="css"],
h1, h2, h3, h4, h5, h6,
p, label {
    color: black !important;
}

/* Labels das perguntas */
label {
    font-weight: 600 !important;
}

/* Campos preenchidos pelo usuário */
.stTextInput input,
.stNumberInput input {
    color: white !important;
    background-color: rgba(20,30,50,0.90) !important;
    border-radius: 10px !important;
}

/* Selectbox fechado */
[data-baseweb="select"] {
    background-color: rgba(20,30,50,0.90) !important;
    border-radius: 10px !important;
}

/* Texto da opção selecionada */
[data-baseweb="select"] span {
    color: white !important;
}

/* Lista de opções aberta */
ul[role="listbox"] {
    background-color: rgba(20,30,50,0.95) !important;
}

/* Opções dentro do dropdown */
ul[role="listbox"] li,
ul[role="listbox"] li div,
ul[role="listbox"] li span {
    color: white !important;
}

/* Placeholder */
input::placeholder {
    color: rgba(255,255,255,0.8) !important;
}

/* Botão */
.stButton button {
    background-color: #0b3d5c !important;
    color: white !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    border: none !important;
    padding: 0.6rem 1rem !important;
}

/* Texto dentro dos alertas */
[data-testid="stAlert"] div,
[data-testid="stAlert"] p {
    color: black !important;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* Botão */

.stButton > button {
    background: linear-gradient(90deg,#0b4f7d,#1f7acb) !important;
    color: white !important;
    font-size: 22px !important;
    font-weight: 700 !important;
    border-radius: 15px !important;
    height: 60px !important;
    width: 100% !important;
    border: none !important;
}

/* Texto interno do botão */

.stButton > button p {
    color: white !important;
    font-weight: 700 !important;
}

/* Hover */

.stButton > button:hover {
    color: white !important;
}

.stButton > button:hover p {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)
# =========================================================
# TÍTULO
# =========================================================

st.title("❤️Triagem Inicial de Risco Cardiovascular❤️")

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

    # Idade
    if idade >= 60:
        score += 3
    elif idade >= 45:
        score += 2
    elif idade >= 30:
        score += 1

    # Dor no peito
    if dor_peito == "Sim, leve":
        score += 2
    elif dor_peito == "Sim, moderada":
        score += 4
    elif dor_peito == "Sim, forte":
        score += 6

    # Histórico familiar
    if historico_familiar == "Sim":
        score += 3
    elif historico_familiar == "Não sei":
        score += 1

    # Exercício físico
    if exercicio == "Não pratico":
        score += 3
    elif exercicio == "Sim, 1 a 2 vezes por semana":
        score += 1

    # Alimentação
    if alimentacao == "Macarrão, carne e molho de tomate":
        score += 1
    elif alimentacao == "Parmegiana de frango":
        score += 2
    elif alimentacao == "Fast food (cachorro-quente, hambúrguer, pizza, etc.)":
        score += 4

    # Cigarro
    if cigarro == "Sim, raramente":
        score += 1
    elif cigarro == "Sim, algumas vezes por semana":
        score += 3
    elif cigarro == "Sim, todos os dias":
        score += 5

    # Álcool
    if alcool == "Sim, raramente":
        score += 1
    elif alcool == "Sim, algumas vezes por semana":
        score += 2
    elif alcool == "Sim, todos os dias":
        score += 3

    # Ansiedade
    if ansiedade == "Às vezes":
        score += 1
    elif ansiedade == "Frequentemente":
        score += 2

    # Sono
    if sono == "Às vezes":
        score += 1
    elif sono == "Frequentemente":
        score += 2

    # =====================================================
    # RESULTADO
    # =====================================================

    st.subheader("Resultado da Triagem")

    nome_exibicao = nome if nome.strip() else "Paciente"

    st.write(f"Paciente: **{nome_exibicao}**")
    st.write(f"Pontuação de risco: **{score} pontos**")

    if score <= 7:
        try:
            st.image("baixo_risco.png", use_container_width=True)
        except Exception:
            pass

        st.success("Baixo risco cardiovascular")
        st.write("Recomenda-se manter hábitos saudáveis e realizar check-up de rotina.")

    elif score <= 15:
        try:
            st.image("medio_risco.png", use_container_width=True)
        except Exception:
            pass

        st.warning("Médio risco cardiovascular")
        st.write("Recomenda-se realizar um novo check-up e, se possível, consultar um cardiologista.")

    else:
        try:
            st.image("alto_risco.png", use_container_width=True)
        except Exception:
            pass

        st.error("Alto risco cardiovascular")
        st.write("Recomenda-se procurar um cardiologista o mais rápido possível.")

    st.info("Este resultado é apenas uma triagem inicial e não representa diagnóstico médico.")
