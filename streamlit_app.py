import base64
from pathlib import Path

import streamlit as st

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="Triagem de Risco Cardiovascular",
    page_icon="🩺",
    layout="centered"
)

# =========================================================
# FUNÇÕES AUXILIARES
# =========================================================

def escolher_imagem(*nomes):
    """
    Retorna o primeiro arquivo de imagem encontrado na pasta do projeto.
    Isso permite usar imagens otimizadas, caso existam, ou voltar para as PNG originais.
    """
    for nome in nomes:
        if Path(nome).exists():
            return nome
    return None


@st.cache_data(show_spinner=False)
def carregar_imagem_base64(image_file):
    """
    Carrega a imagem de fundo em Base64 usando cache.
    Assim, o Streamlit não precisa reprocessar a imagem a cada interação do usuário.
    """
    caminho = Path(image_file)

    with caminho.open("rb") as image:
        encoded = base64.b64encode(image.read()).decode()

    extensao = caminho.suffix.lower()

    if extensao in [".jpg", ".jpeg"]:
        mime_type = "image/jpeg"
    else:
        mime_type = "image/png"

    return mime_type, encoded


def set_background():
    """
    Define o fundo da aplicação.
    Prioriza fundo_otimizado.jpg, caso exista. Se não existir, usa fundo.png.
    """
    image_file = escolher_imagem(
        "fundo_otimizado.jpg",
        "fundo.jpg",
        "fundo.png"
    )

    if image_file is None:
        st.warning("Imagem de fundo não encontrada. Envie o arquivo 'fundo.png' ou 'fundo_otimizado.jpg'.")
        return

    mime_type, encoded = carregar_imagem_base64(image_file)

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:{mime_type};base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


def imagem_resultado(tipo):
    """
    Retorna a imagem correspondente ao resultado.
    Prioriza imagens otimizadas se existirem.
    """
    if tipo == "baixo":
        return escolher_imagem("baixo_risco_otimizado.jpg", "baixo_risco.jpg", "baixo_risco.png")

    if tipo == "medio":
        return escolher_imagem("medio_risco_otimizado.jpg", "medio_risco.jpg", "medio_risco.png")

    if tipo == "alto":
        return escolher_imagem("alto_risco_otimizado.jpg", "alto_risco.jpg", "alto_risco.png")

    return None


def calcular_score(
    idade,
    dor_peito,
    historico_familiar,
    exercicio,
    alimentacao,
    cigarro,
    alcool,
    ansiedade,
    sono
):
    """
    Calcula a pontuação de risco cardiovascular com base nas respostas do usuário.
    """
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

    return score


# =========================================================
# FUNDO E ESTILO
# =========================================================

set_background()

st.markdown(
    """
    <style>

    /* Área principal do app */
    .block-container {
        background-color: rgba(255, 255, 255, 0.65) !important;
        padding: 2.5rem !important;
        border-radius: 24px !important;
        margin-top: 2rem !important;
        margin-bottom: 2rem !important;
        box-shadow: 0px 8px 28px rgba(0,0,0,0.20) !important;
    }

    /* Textos principais */
    html, body,
    h1, h2, h3, h4, h5, h6,
    p, label, span, div {
        color: black !important;
    }

    /* Labels das perguntas */
    label {
        font-weight: 700 !important;
    }

    /* Campos de texto e número */
    .stTextInput input,
    .stNumberInput input {
        color: white !important;
        background-color: rgba(20,30,50,0.92) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255,255,255,0.20) !important;
    }

    /* Texto digitado nos campos */
    .stTextInput input *,
    .stNumberInput input * {
        color: white !important;
    }

    /* Placeholder */
    input::placeholder {
        color: rgba(255,255,255,0.80) !important;
    }

    /* Selectbox fechado */
    [data-baseweb="select"] {
        background-color: rgba(20,30,50,0.92) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255,255,255,0.20) !important;
    }

    /* Texto do selectbox */
    [data-baseweb="select"] *,
    [data-baseweb="select"] span,
    [data-baseweb="select"] div {
        color: white !important;
    }

    /* Dropdown aberto */
    ul[role="listbox"],
    div[role="listbox"] {
        background-color: rgba(20,30,50,0.98) !important;
    }

    /* Opções do dropdown */
    ul[role="listbox"] li,
    ul[role="listbox"] li *,
    div[role="listbox"] div,
    div[role="listbox"] span {
        color: white !important;
    }

    /* Botão do formulário */
    .stButton > button,
    .stFormSubmitButton > button {
        background: linear-gradient(90deg,#0b4f7d,#1f7acb) !important;
        color: white !important;
        font-size: 20px !important;
        font-weight: 800 !important;
        border-radius: 15px !important;
        min-height: 58px !important;
        width: 100% !important;
        border: none !important;
        box-shadow: 0px 4px 14px rgba(0,0,0,0.25) !important;
    }

    /* Texto interno do botão */
    .stButton > button *,
    .stFormSubmitButton > button *,
    .stButton > button p,
    .stFormSubmitButton > button p {
        color: white !important;
        font-weight: 800 !important;
    }

    /* Hover do botão */
    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        background: linear-gradient(90deg,#1565a1,#2596e6) !important;
        color: white !important;
    }

    .stButton > button:hover *,
    .stFormSubmitButton > button:hover * {
        color: white !important;
    }

    /* Alertas */
    [data-testid="stAlert"] *,
    [data-testid="stAlert"] p,
    [data-testid="stAlert"] div {
        color: black !important;
    }

    /* Imagens arredondadas */
    img {
        border-radius: 18px !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# TÍTULO
# =========================================================

st.markdown(
    """
    <h1 style='text-align:center; color:black;'>
        ❤️ Triagem Inicial de Risco Cardiovascular ❤️
    </h1>
    """,
    unsafe_allow_html=True
)

st.write(
    """
    Este sistema realiza uma triagem inicial de risco cardiovascular com base
    em sintomas, histórico familiar e hábitos de vida.
    """
)

st.warning(
    """
    Este sistema é apenas um protótipo acadêmico e não substitui avaliação médica profissional.
    """
)

# =========================================================
# FORMULÁRIO
# =========================================================

st.subheader("Informe seus dados")

with st.form("form_triagem_cardiovascular"):

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

    calcular = st.form_submit_button("Calcular risco cardiovascular")


# =========================================================
# RESULTADO
# =========================================================

if calcular:

    score = calcular_score(
        idade=idade,
        dor_peito=dor_peito,
        historico_familiar=historico_familiar,
        exercicio=exercicio,
        alimentacao=alimentacao,
        cigarro=cigarro,
        alcool=alcool,
        ansiedade=ansiedade,
        sono=sono
    )

    st.subheader("Resultado da Triagem")

    nome_exibicao = nome if nome.strip() else "Paciente"

    st.write(f"Paciente: **{nome_exibicao}**")
    st.write(f"Pontuação de risco: **{score} pontos**")

    if score <= 7:

        imagem = imagem_resultado("baixo")
        if imagem:
            st.image(imagem, use_container_width=True)

        st.success("Baixo risco cardiovascular")
        st.write("Recomenda-se manter hábitos saudáveis e realizar check-up de rotina.")

    elif score <= 15:

        imagem = imagem_resultado("medio")
        if imagem:
            st.image(imagem, use_container_width=True)

        st.warning("Médio risco cardiovascular")
        st.write("Recomenda-se realizar um novo check-up e, se possível, consultar um cardiologista.")

    else:

        imagem = imagem_resultado("alto")
        if imagem:
            st.image(imagem, use_container_width=True)

        st.error("Alto risco cardiovascular")
        st.write("Recomenda-se procurar um cardiologista o mais rápido possível.")

    st.info("Este resultado é apenas uma triagem inicial e não representa diagnóstico médico.")
