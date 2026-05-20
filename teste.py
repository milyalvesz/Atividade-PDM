import streamlit as st

# =========================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================
st.set_page_config(
    page_title="Marcas de Luxo",
    page_icon="🌐",
    layout="wide"
)

# =========================================
# TÍTULO
# =========================================
st.title("Marcas de Luxo")
st.write("Confira algumas marcas de moda luxuosas")

# =========================================
# COLUNAS
# =========================================
col1, col2, col3 = st.columns(3)

# =========================================
# EMPRESA 1
# =========================================
with col1:
    st.image("empresa1.png", use_container_width=True)
    st.subheader("GUCCI")
    st.write("Uma das marcas de luxo mais famosas e valiosas do mundo")
    st.link_button(
        "Acessar Site",
        "https://www.gucci.com/int/en/st/brazil-landing"
    )

# =========================================
# EMPRESA 2
# =========================================
with col2:
    st.image("empresa2.png", use_container_width=True)
    st.subheader("ZARA")
    st.write("Uma das maiores redes de varejo de moda do mundo, pertencente ao grupo espanhol Inditex")
    st.link_button(
        "Acessar Site",
        "https://www.zara.com/br/"
    )

# =========================================
# EMPRESA 3
# =========================================
with col3:
    st.image("empresa3.png", use_container_width=True)
    st.subheader("PRADA")
    st.write("Uma das marcas de luxo mais influentes do mundo, sinônimo de sofisticação, minimalismo inteligente e status")
    st.link_button(
        "Acessar Site",
        "https://www.prada.com/br/pt/womens/days-of-summer/c/10996BR?utm_campaign=GoogleShopping_BR&utm_medium=CPC&utm_source=Google&utm_content=PMax&s_kwcid=AL!8549!3!!!!x!!&gclsrc=aw.ds&gad_source=1&gad_campaignid=20037972387&gbraid=0AAAAADgVuh9D9JDetvGloxWFfazKMJhP9&gclid=CjwKCAjwt7XQBhBkEiwAtStppwSHvFAKqzHUeY6AkD4sc3Sbj2Tqtxtoo9BowVxYWiJwYjXIAy1ykRoCeMwQAvD_BwE"
    )

# =========================================
# RODAPÉ
# =========================================
st.write("---")
st.write("Desenvolvido por Jamily Alves")
