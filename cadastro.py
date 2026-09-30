import streamlit as st
import pandas as pd
import os
import textwrap
import requests
import base64


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="MedInventário PRO",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# ARQUIVO DE DADOS
# ============================================================

ARQUIVO = "materiais.csv"


# ============================================================
# IMAGENS
# ============================================================

IMAGEM_HERO = (
    "https://images.unsplash.com/"
    "photo-1576091160399-112ba8d25d1d"
    "?auto=format&fit=crop&w=1800&q=90"
)

IMAGEM_FROTA = (
    "https://images.unsplash.com/"
    "photo-1584982751601-97dcc096659c"
    "?auto=format&fit=crop&w=1200&q=85"
)


# ============================================================
# CONVERTER IMAGEM PARA BASE64
# ============================================================

def imagem_base64(url):

    try:

        resposta = requests.get(
            url,
            timeout=15
        )

        resposta.raise_for_status()

        imagem = base64.b64encode(
            resposta.content
        ).decode("utf-8")

        tipo = resposta.headers.get(
            "Content-Type",
            "image/jpeg"
        )

        return f"data:{tipo};base64,{imagem}"

    except Exception:

        return None


# ============================================================
# CARREGAR SOMENTE A IMAGEM DO HERO EM BASE64
# ============================================================

HERO_BASE64 = imagem_base64(
    IMAGEM_HERO
)


# ============================================================
# FUNÇÃO PARA HTML
# ============================================================

def mostrar_html(html):

    html = textwrap.dedent(html)

    html = " ".join(
        linha.strip()
        for linha in html.splitlines()
        if linha.strip()
    )

    st.markdown(
        html,
        unsafe_allow_html=True
    )


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap'
);

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background:
        linear-gradient(
            135deg,
            #F0F0E5 0%,
            #E1E4C8 50%,
            #D4DCB5 100%
        );
}

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            #162630,
            #223944
        );

    border-right:
        2px solid #77864B;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

.logo-title {

    font-size: 28px;

    font-weight: 800;

    color: #FFFFFF !important;

    margin-bottom: 5px;
}

.logo-subtitle {

    font-size: 11px;

    font-weight: 700;

    color: #BFCB9C !important;

    letter-spacing: 1px;
}


/* ============================================================
   TÍTULOS
   ============================================================ */

.page-title {

    font-size: 38px;

    font-weight: 800;

    color: #26311F !important;

    margin-bottom: 5px;
}

.page-subtitle {

    font-size: 17px;

    color: #46513B !important;

    margin-bottom: 30px;
}


/* ============================================================
   HERO
   ============================================================ */

.hero-container {

    position: relative;

    height: 430px;

    width: 100%;

    border-radius: 28px;

    overflow: hidden;

    margin-bottom: 35px;

    background-size: cover;

    background-position: center;

    box-shadow:
        0 15px 35px rgba(0,0,0,0.22);
}

.hero-overlay {

    position: absolute;

    inset: 0;

    background:
        linear-gradient(
            90deg,
            rgba(14,28,38,0.97) 0%,
            rgba(14,28,38,0.86) 45%,
            rgba(14,28,38,0.18) 100%
        );
}

.hero-content {

    position: absolute;

    top: 50%;

    left: 7%;

    transform: translateY(-50%);

    max-width: 580px;
}

.hero-number {

    font-size: 70px;

    font-weight: 800;

    color: #A4D080 !important;

    line-height: 1;
}

.hero-title {

    font-size: 46px;

    font-weight: 800;

    color: #FFFFFF !important;

    margin-top: 12px;

    line-height: 1.1;
}

.hero-text {

    font-size: 17px;

    color: #E8EDDE !important;

    margin-top: 20px;

    line-height: 1.7;
}

.hero-badge {

    display: inline-block;

    margin-top: 24px;

    padding: 10px 22px;

    border-radius: 30px;

    background: #6E8040;

    color: #FFFFFF !important;

    font-size: 14px;

    font-weight: 700;
}


/* ============================================================
   CARDS
   ============================================================ */

.info-card {

    background: #FFFFFF;

    border-radius: 22px;

    padding: 28px;

    min-height: 170px;

    border:
        1px solid rgba(111,128,63,0.30);

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08);
}

.card-number {

    font-size: 34px;

    font-weight: 800;

    color: #26311F !important;

    margin-top: 10px;
}

.card-label {

    font-size: 14px;

    font-weight: 700;

    color: #566248 !important;

    margin-top: 5px;
}


/* ============================================================
   CARD ESCURA
   ============================================================ */

.dark-card {

    background:
        linear-gradient(
            135deg,
            #152631,
            #233C48
        );

    border-radius: 24px;

    padding: 30px;

    box-shadow:
        0 12px 30px rgba(0,0,0,0.16);
}

.dark-card h2 {

    color: #FFFFFF !important;

    margin-top: 0;
}

.dark-card p {

    color: #E2E9DA !important;

    line-height: 1.7;
}


/* ============================================================
   FORMULÁRIO
   ============================================================ */

[data-testid="stForm"] {

    background:
        rgba(255,255,255,0.85);

    padding: 30px;

    border-radius: 25px;

    border:
        1px solid #B8C391;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.08);
}

[data-testid="stWidgetLabel"] label,
.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stTextArea label {

    color: #26311F !important;

    font-size: 15px !important;

    font-weight: 700 !important;
}


/* ============================================================
   CAMPOS
   ============================================================ */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {

    background-color:
        #FFFFFF !important;

    color:
        #202820 !important;

    border:
        2px solid #7C8956 !important;

    border-radius:
        12px !important;

    font-size:
        16px !important;
}


/* ============================================================
   SELECTBOX
   ============================================================ */

[data-baseweb="select"] > div {

    background-color:
        #2F323C !important;

    border:
        2px solid #687548 !important;

    border-radius:
        12px !important;
}

[data-baseweb="select"] * {

    color:
        #FFFFFF !important;
}


/* ============================================================
   BOTÕES
   ============================================================ */

.stButton > button,
div[data-testid="stFormSubmitButton"] > button {

    background:
        linear-gradient(
            135deg,
            #52632D,
            #788B48
        ) !important;

    color:
        #FFFFFF !important;

    border:
        none !important;

    border-radius:
        14px !important;

    min-height:
        54px;

    font-weight:
        700 !important;

    box-shadow:
        0 8px 18px
        rgba(82,99,45,0.25);
}


/* ============================================================
   IMAGEM INFERIOR
   ============================================================ */

.imagem-inferior {

    width: 100%;

    border-radius: 24px;

    display: block;

    overflow: hidden;
}


/* ============================================================
   RODAPÉ
   ============================================================ */

.footer {

    margin-top: 50px;

    text-align: center;

    color: #536044 !important;

    font-size: 14px;

    font-weight: 600;
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# FUNÇÕES
# ============================================================

def carregar_dados():

    colunas = [
        "Fabricante",
        "Modelo",
        "Ano",
        "Categoria",
        "Patrimonio",
        "Quantidade",
        "Valor",
        "Observacoes"
    ]

    if os.path.exists(ARQUIVO):

        try:

            dados = pd.read_csv(
                ARQUIVO
            )

            return dados

        except Exception:

            return pd.DataFrame(
                columns=colunas
            )

    return pd.DataFrame(
        columns=colunas
    )


def salvar_dados(dados):

    dados.to_csv(
        ARQUIVO,
        index=False
    )


# ============================================================
# CARREGAR DADOS
# ============================================================

df = carregar_dados()


colunas_necessarias = [
    "Fabricante",
    "Modelo",
    "Ano",
    "Categoria",
    "Patrimonio",
    "Quantidade",
    "Valor",
    "Observacoes"
]


for coluna in colunas_necessarias:

    if coluna not in df.columns:

        df[coluna] = ""


df["Valor"] = pd.to_numeric(
    df["Valor"],
    errors="coerce"
).fillna(0)


df["Quantidade"] = pd.to_numeric(
    df["Quantidade"],
    errors="coerce"
).fillna(0)


# ============================================================
# SIDEBAR
# ============================================================

mostrar_html(
    """
    <div class="logo-title">
        MedInventário
    </div>

    <div class="logo-subtitle">
        GESTÃO DE MATERIAIS E EQUIPAMENTOS MÉDICOS
    </div>
    """
)


st.sidebar.markdown(
    "<br>",
    unsafe_allow_html=True
)


menu = st.sidebar.radio(
    "NAVEGAÇÃO",
    [
        "Dashboard",
        "+ Cadastrar Material",
        "Materiais Cadastrados"
    ]
)


st.sidebar.markdown(
    "---"
)


st.sidebar.caption(
    "MedInventário PRO 2026"
)


# ============================================================
# DASHBOARD
# ============================================================

if menu == "Dashboard":

    # --------------------------------------------------------
    # HERO
    # --------------------------------------------------------

    imagem_hero = (
        HERO_BASE64
        if HERO_BASE64
        else IMAGEM_HERO
    )

    mostrar_html(
        f"""
        <div
            class="hero-container"
            style="
                background-image:
                url('{imagem_hero}');
            "
        >

            <div class="hero-overlay"></div>

            <div class="hero-content">

                <div class="hero-number">
                    01.
                </div>

                <div class="hero-title">
                    Seus materiais.<br>
                    Total controle.
                </div>

                <div class="hero-text">

                    Gerencie materiais, insumos e
                    equipamentos médicos em um só lugar.<br>

                    Cadastre, consulte e acompanhe seu estoque
                    de forma ágil e profissional.

                </div>

                <div class="hero-badge">
                    GESTÃO MÉDICA INTELIGENTE
                </div>

            </div>

        </div>
        """
    )


    # --------------------------------------------------------
    # TÍTULO
    # --------------------------------------------------------

    mostrar_html(
        """
        <div class="page-title">
            Visão geral do estoque
        </div>

        <div class="page-subtitle">
            Acompanhe seus materiais e mantenha
            o estoque médico atualizado.
        </div>
        """
    )


    # --------------------------------------------------------
    # VALORES
    # --------------------------------------------------------

    total_itens = len(df)

    valor_total = df["Valor"].sum()

    qtd_total = df["Quantidade"].sum()


    # --------------------------------------------------------
    # CARDS
    # --------------------------------------------------------

    col1, col2, col3 = st.columns(3)


    with col1:

        mostrar_html(
            f"""
            <div class="info-card">

                <div class="card-number">
                    {total_itens}
                </div>

                <div class="card-label">
                    ITENS CADASTRADOS
                </div>

            </div>
            """
        )


    with col2:

        mostrar_html(
            f"""
            <div class="info-card">

                <div class="card-number">
                    R$ {valor_total:,.2f}
                </div>

                <div class="card-label">
                    VALOR TOTAL DO ESTOQUE
                </div>

            </div>
            """
        )


    with col3:

        mostrar_html(
            f"""
            <div class="info-card">

                <div class="card-number">
                    {qtd_total:,.0f}
                </div>

                <div class="card-label">
                    QUANTIDADE TOTAL
                </div>

            </div>
            """
        )


    st.markdown(
        "<br>",
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # INFORMAÇÕES
    # --------------------------------------------------------

    coluna1, coluna2 = st.columns(
        [1.1, 1]
    )


    with coluna1:

        mostrar_html(
            """
            <div class="dark-card">

                <h2>
                    Gestão Profissional de Materiais
                    Médicos
                </h2>

                <p>
                    O MedInventário PRO permite manter
                    materiais, insumos e equipamentos médicos
                    organizados e catalogados.
                </p>

                <p>
                    Monitore lotes, valores e quantidades
                    com facilidade através de uma interface limpa.
                </p>

            </div>
            """
        )


    # ========================================================
    # IMAGEM INFERIOR — CORRIGIDA
    # ========================================================

    with coluna2:

        st.image(
            IMAGEM_FROTA,
            use_container_width=True
        )


# ============================================================
# CADASTRAR MATERIAL
# ============================================================

elif menu == "+ Cadastrar Material":

    mostrar_html(
        """
        <div class="page-title">
            Novo Material Médico
        </div>

        <div class="page-subtitle">
            Adicione um novo material ou equipamento
            médico ao estoque.
        </div>
        """
    )


    with st.form(
        "cadastro_item",
        clear_on_submit=True
    ):

        col1, col2 = st.columns(2)


        # ----------------------------------------------------
        # COLUNA 1
        # ----------------------------------------------------

        with col1:

            fabricante = st.text_input(
                "Fabricante / Marca"
            )


            modelo = st.text_input(
                "Nome / Modelo do Material"
            )


            ano = st.number_input(
                "Ano de Fabricação",
                min_value=1950,
                max_value=2035,
                value=2026,
                step=1
            )


            categoria = st.selectbox(
                "Categoria",
                [
                    "Equipamento Médico",
                    "Instrumental Cirúrgico",
                    "Material Hospitalar",
                    "Material de Enfermagem",
                    "EPI",
                    "Descartável",
                    "Diagnóstico",
                    "Laboratório",
                    "Medicamento / Insumo",
                    "Outro"
                ]
            )


        # ----------------------------------------------------
        # COLUNA 2
        # ----------------------------------------------------

        with col2:

            patrimonio = st.text_input(
                "Lote / Nº de Série / Patrimônio"
            )


            quantidade = st.number_input(
                "Quantidade em Estoque",
                min_value=0,
                value=1,
                step=1
            )


            valor = st.number_input(
                "Valor Unitário (R$)",
                min_value=0.0,
                value=0.0,
                step=10.0
            )


            observacoes = st.text_area(
                "Observações / Local de Armazenamento / Validade"
            )


        # ----------------------------------------------------
        # BOTÃO
        # ----------------------------------------------------

        cadastrar = st.form_submit_button(
            "CADASTRAR MATERIAL"
        )


        if cadastrar:

            if (
                fabricante.strip()
                and modelo.strip()
                and patrimonio.strip()
            ):

                novo_item = pd.DataFrame(
                    [
                        {
                            "Fabricante":
                                fabricante.strip(),

                            "Modelo":
                                modelo.strip(),

                            "Ano":
                                int(ano),

                            "Categoria":
                                categoria,

                            "Patrimonio":
                                patrimonio.strip().upper(),

                            "Quantidade":
                                int(quantidade),

                            "Valor":
                                float(valor),

                            "Observacoes":
                                observacoes.strip()
                        }
                    ]
                )


                df = pd.concat(
                    [
                        df,
                        novo_item
                    ],
                    ignore_index=True
                )


                salvar_dados(
                    df
                )


                st.success(
                    "Material médico cadastrado com sucesso!"
                )


                st.rerun()


            else:

                st.warning(
                    "Preencha Fabricante/Marca, "
                    "Nome/Modelo e "
                    "Lote/Série/Patrimônio."
                )


# ============================================================
# MATERIAIS CADASTRADOS
# ============================================================

elif menu == "Materiais Cadastrados":

    mostrar_html(
        """
        <div class="page-title">
            Inventário Atual
        </div>

        <div class="page-subtitle">
            Consulte e pesquise todos os materiais
            e equipamentos médicos cadastrados.
        </div>
        """
    )


    # --------------------------------------------------------
    # ESTOQUE VAZIO
    # --------------------------------------------------------

    if df.empty:

        mostrar_html(
            """
            <div class="dark-card">

                <h2>
                    Nenhum material cadastrado
                </h2>

                <p>
                    Seu estoque ainda está vazio.
                    Cadastre seu primeiro material
                    médico para começar.
                </p>

            </div>
            """
        )


    # --------------------------------------------------------
    # ESTOQUE COM ITENS
    # --------------------------------------------------------

    else:

        busca = st.text_input(
            "Pesquisar material",
            placeholder=(
                "Digite fabricante, material, "
                "lote, patrimônio ou categoria..."
            )
        )


        # ----------------------------------------------------
        # PESQUISA
        # ----------------------------------------------------

        if busca:

            mascara = (
                df.astype(str)
                .apply(
                    lambda coluna:
                        coluna.str.contains(
                            busca,
                            case=False,
                            na=False
                        )
                )
                .any(axis=1)
            )

            df_filtrado = df[
                mascara
            ]

        else:

            df_filtrado = df


        # ----------------------------------------------------
        # TABELA
        # ----------------------------------------------------

        st.dataframe(
            df_filtrado,
            use_container_width=True,
            hide_index=True
        )


        st.markdown(
            "<br>",
            unsafe_allow_html=True
        )


        # ----------------------------------------------------
        # EXCLUIR
        # ----------------------------------------------------

        opcoes_itens = df.index.tolist()


        item_excluir = st.selectbox(

            "Selecione um material para excluir",

            options=opcoes_itens,

            format_func=lambda indice:

                (
                    f"{df.loc[indice, 'Fabricante']} "
                    f"{df.loc[indice, 'Modelo']} "
                    f"- Lote/Série: "
                    f"{df.loc[indice, 'Patrimonio']}"
                )
        )


        if st.button(
            "EXCLUIR MATERIAL"
        ):

            df = df.drop(
                item_excluir
            ).reset_index(
                drop=True
            )


            salvar_dados(
                df
            )


            st.success(
                "Material médico excluído com sucesso!"
            )


            st.rerun()


# ============================================================
# RODAPÉ
# ============================================================

mostrar_html(
    """
    <div class="footer">

        MedInventário PRO<br>

        Gestão inteligente de materiais médicos

    </div>
    """
)
