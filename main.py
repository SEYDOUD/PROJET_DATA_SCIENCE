import streamlit as st
import pandas as pd
from requests import get
from bs4 import BeautifulSoup as bs

table = pd.DataFrame({"Column 1":[1,2,3,4,5,6,7,8,9],"Column 2":[10,11,12,13,14,15,16,17,18]})

st.markdown("""
<style>
    .st-emotion-cache-10trblm e1nzilvr1{
        text-color:'red'
    }
</style>            
""",unsafe_allow_html=True)

def scrap(id,nb_page):
    df = pd.DataFrame()
    for p in range(1,nb_page):
        url = f'https://dakarvente.com/index.php?page=annonces_categorie&id={id}&sort=&nb={p}'
        resp = get(url)
        soup = bs(resp.text,'html.parser')
        articles = soup.find_all('article', id = 'div-desktop')
        data=[]
        for article in articles:
            try:
                content_price = article.findAll('div', class_ = 'content-price')
                marque = article.find('div',class_ = 'content-desc').find("a",class_ = "mv-overflow-ellipsis").text

                try:
                    prix = content_price[0].find("span").text.replace(" FCFA","")
                except:
                    pass

                adresse = content_price[1].find("span").text
                img = article.find('div',class_ = '').find("h2").find("a").find("img" ).get('src')

                obj = {
                    "marque":marque,
                    "prix":prix,
                    "adresse":adresse,
                    "img":img
                }
                data.append(obj)
            except:
                pass
    DF = pd.DataFrame(data)
    df = pd.concat([df, DF],axis=0).reset_index(drop = True)
        
    return df

st.sidebar.subheader("Filtrer le scraping")
nb_page = st.sidebar.slider("Choisissez le nombre de page a scraper" , min_value=0,max_value=100)
print(nb_page)
st.sidebar.markdown("---")
res = st.sidebar.selectbox("Naviguez sur l'application",options=("Scrapper les données","Dashboard","Telecharger les données","Formulaire de contact"))

if res == "Scrapper les données":
    st.title("Dashboard de scrapping")
    st.markdown("Ces données sont scrapées sur le site [dakarvente](https://www.dakarvente.com)")
    st.text("Ci-dessous se trouve les données disponible pour le scraping")
    st.markdown("---")
    # st.table(table)
    st.header("Voiture")
    
    st.image("mustang.jpg")
    click = st.button("Scrapper les données des voitures en location")

    if click:
        sc = scrap(8,nb_page)
        st.dataframe(sc)

    click = st.button("Scrapper les données des voitures en ventes")

    if click:
        sc = scrap(2,nb_page)
        st.dataframe(sc)


    st.header("Motos")
    st.image("moto2.jpg")
    click = st.button("Scrapper les données des motos")

    if click:
        sc = scrap(3,nb_page)
        st.dataframe(sc)

    st.header("Telephone")
    st.image("telep.jpg")
    click = st.button("Scrapper les données des telephones")

    if click:
        sc = scrap(32,nb_page)
        st.dataframe(sc)

elif res == "Formulaire de contact":
    st.markdown("""<iframe src="https://ee.kobotoolbox.org/i/cXvfevZE" width="800" height="600"></iframe>""",unsafe_allow_html=True)

