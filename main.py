import streamlit as st
import pandas as pd

table = pd.DataFrame({"Column 1":[1,2,3,4,5,6,7,8,9],"Column 2":[10,11,12,13,14,15,16,17,18]})

st.markdown("""
<style>
    .st-emotion-cache-10trblm e1nzilvr1{
        text-color:'red'
    }
</style>            
""",unsafe_allow_html=True)

st.title("Dashboard de scrapping")
st.markdown("Ces données sont scrapées sur le site [dakarvente](https://www.dakarvente.com)")
st.text("Ci-dessous se trouve les données disponible pour le scraping")
st.markdown("---")
# st.table(table)
st.header("Voiture")
st.image("mustang.jpg")

st.header("Motos")
st.image("moto2.jpg")

st.header("Telephone")
st.image("telep.jpg")
st.button("Click me")
st.selectbox("What is your favourite car ?",options=("option 1","option 2","option 3"))

st.sidebar.subheader("Filtrer le scraping")
st.sidebar.slider("Choisissez le nombre de page a scraper" , min_value=0,max_value=100)
st.sidebar.markdown("---")
st.sidebar.selectbox("Naviguez sur l'application",options=("Scrapper les données","Dashboard","Telecharger les données","Formulaire de contact"))
