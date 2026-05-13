import streamlit as st
import base64

# CONFIG
st.set_page_config(page_title="Perfil", layout="wide")

# FUNÇÃO base64
def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = get_base64_image("Marvel-Studios-Emblema.jpg")
zap_base64 = get_base64_image("zaplogo.png")

# TOPO (imagem clicável)
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 50px;">
            <a href="https://www.marvel.com/" target="_blank">
                <img src="data:image/png;base64,{img_base64}" 
                     width="320" 
                     style="border-radius:12px;">
            </a>
        </div>
    """, unsafe_allow_html=True)

# LAYOUT PRINCIPAL
col_left, col_right = st.columns([3,1])

with col_left:
    st.markdown("""
    <div style='margin-bottom:30px; font-size:30px;'>
        <b>Nome Jamily Alves</b>
    </div>
    """, unsafe_allow_html=True)

    # subcolunas
    subcol1, subcol2 = st.columns([1,4])

    # IMAGEM (centralizada verticalmente)
    with subcol1:
        st.markdown("""
        <div style="
            display: flex;
            align-items: center;
            height: 100%;
        ">
        """, unsafe_allow_html=True)

        st.image("mimiu.jpeg", width=800)

        st.markdown("</div>", unsafe_allow_html=True)

    # TEXTO
    with subcol2:
        st.markdown("""
        <div style="
            text-align: justify;
            font-size: 20px;
            line-height: 2.0;
            width: 100%;
            max-width: none;
        ">
            <b>Sobre Jamily:<br>
           Meu nome é Jamily Emily Alves Barbosa, tenho 17 anos. Nasci em Itabaiana, na Paraíba, e 
        atualmente moro em Salgado de São Félix. Curso o Técnico em Informática 
        integrado ao Ensino Médio no Instituto Federal da Paraíba (IFPB), 
        uma fase muito importante para o meu crescimento, pois me proporciona novos aprendizados, 
        desafios e responsabilidades que contribuem para a construção do meu futuro.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top:30px;'>", unsafe_allow_html=True)
    st.link_button("Acessar", "https://sites.google.com/academico.ifpb.edu.br/jamily/in%C3%ADcio")
    st.markdown("</div>", unsafe_allow_html=True)

with col_right:
    st.empty()

# 🔥 NOVO BLOCO (WhatsApp clicável no final)
st.markdown(f"""
    <div style="text-align: center; margin-top: 10px;">
        <a href="https://wa.me/5583987894924" target="_blank">
            <img src="data:image/png;base64,{zap_base64}" width="100">
        </a>
    </div>
""", unsafe_allow_html=True)

