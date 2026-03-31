import streamlit as st
import pandas as pd
import requests
from datetime import date

df_parcours = pd.read_csv("parcours.csv")

# FONCTION ###################
@st.cache_data
def temperature_eau () :
# Remplace cette clé par la tienne
    api_key = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJCZXJzZWdlYXlhbnRvaW5lQHlhaG9vLmZyIiwianRpIjoiM2MwYmZhNjEtOWU5ZC00ZDZlLTllY2ItNTU3ZmMzMzA4ZmRmIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE3NDczMjc4NjEsInVzZXJJZCI6IjNjMGJmYTYxLTllOWQtNGQ2ZS05ZWNiLTU1N2ZjMzMwOGZkZiIsInJvbGUiOiIifQ.azUDk7xMml34w5dK9krF-LmL6XZ1Q1_7MzT6MVMW3SU'

# Code de la plage de Zarautz (identifiant AEMET)
    url_petition = 'https://opendata.aemet.es/opendata/api/prediccion/especifica/playa/2007901/?api_key=' + api_key

# Étape 1 : Demande l'URL des données
    response = requests.get(url_petition)

    if response.status_code == 200:
        json_data = response.json()
        data_url = json_data['datos']  # URL réelle des données météo
    

    # Étape 2 : Obtenir les vraies données météo
        response_data = requests.get(data_url)
        if response_data.status_code == 200:
            prevision = response_data.json()
        
        # Naviguer dans les données JSON (extraction dépend du format exact)
            for jour in prevision[0]['prediccion']['dia']:
            #eau = jour.get('temperaturaAgua')
                eau = jour.get('tAgua')
                t_eau = eau['valor1']
                return t_eau
temp_eau = 0
st.session_state.temp_eau = temperature_eau ()
# AFFICHAGE ###########################""    

menu = st.sidebar.radio(
    "Menu",
    ["Accueil", "Programme", "Infos pratiques", "Parcours"]
)

# ACCUEIL #############################

if menu == "Accueil":
    st.subheader("🔴⚫Bienvenue sur la page du stage Aunisud triathlon 2025 ")
    st.write("Nous serons 16 participants au stage cette année")
    st.write("Direction le Pays Basque espagnol du 29 mai au 1er juin")
    st.write("Le menu est à ouvrir sur la gauche de l'écran")
    st.image("groupe_accueil.jpg")

# PROGRAMME #############################

elif menu == "Programme":
    st.subheader("Déroulé du stage")
    jour = st.selectbox("Choix de la journée" , ["Jour 1","Jour 2","Jour 3","Jour 4"])
    if jour == "Jour 1":
        st.write("🚙 Départ ⏱️ horaire à définir de la piscine de Surgères avec 2 minibus")
        st.write("Trajet jusqu'en début d'après-midi, prévoir un pique-nique 🥪")
        st.write("Arrivée au gîte, 🚴‍♂️ première sortie vélo de 37km avec 750m D+")
        st.write("👕 Prévoir la tenue du club pour la photo de groupe du stage")
        st.write("Parcours")
        st.image("map_jour_1.jpg")
        st.write("Profil")
        st.image("Profil_jour_1.jpg")
        dropbox_link_1 = "https://www.dropbox.com/scl/fi/m1r3h1jformh1yzn0sk34/GPX_J1.gpx?rlkey=bmksnn1sld2nnlukyblt7zeu7&st=jpryw3kf&dl=1"
        st.markdown(f"[📥 Télécharger le GPX]({dropbox_link_1})", unsafe_allow_html=True)
    if jour == "Jour 2":
        st.write("🚴‍♂️ Sortie longue à vélo, 3 groupes pour 3 distances")
        st.write("Les débuts de parcours sont les mêmes donc les groupes peuvent partir ensembles ou il est possible de changer d'avis en cours de route")
        col1, col2 = st.columns(2)

        with col1:
            st.header("Version courte")
            st.write("48km pour 1360m D+")
            st.write("Parcours")
            st.image("map_jour_2_courte.jpg")
            st.write("Profil")
            st.image("Profil_jour_2_courte.jpg")
            dropbox_link_2_courte = "https://www.dropbox.com/scl/fi/7v3cmzuzm92trgucuhqe3/GPX_J2-Courte.gpx?rlkey=d4l6czzlok1nf2t7b4iqydvi5&st=s7d06qno&dl=1"
            st.markdown(f"[📥 Télécharger le GPX]({dropbox_link_2_courte})", unsafe_allow_html=True)

            st.header("Version moyenne")
            st.write("66km pour 1770m D+")
            st.write("Parcours")
            st.image("map_jour_2_moyenne.jpg")
            st.write("Profil")
            st.image("Profil_jour_2_moyenne.jpg")
            dropbox_link_2_moyenne = "https://www.dropbox.com/scl/fi/uvcyu3e7cc8onkgf66vs0/GPX_J2-Moyenne.gpx?rlkey=9m1m8jtpjp0bfxe5uj83w0pnz&st=xwv9nljc&dl=1"
            st.markdown(f"[📥 Télécharger le GPX]({dropbox_link_2_moyenne})", unsafe_allow_html=True)

        with col2:
            st.header("Version longue")
            st.write("98km pour 2990m D+")
            st.write("Parcours")
            st.image("map_jour_2_longue.jpg")
            st.write("Profil")
            st.image("Profil_jour_2_longue.jpg")
            dropbox_link_2_longue = "https://www.dropbox.com/scl/fi/0ab6t59roz4p3yctvq0lr/GPX_J2-Longue.gpx?rlkey=iwjbq2zh1co9ud9xtlcl99mjz&st=3x9k5nqs&dl=1"
            st.markdown(f"[📥 Télécharger le GPX]({dropbox_link_2_longue})", unsafe_allow_html=True)


    if jour == "Jour 3":
            st.write("En autonomie, plusieurs parcours sont disponibles dans la section Parcours 🛣️")
            #st.write("Natation en mer en fin de journée à la plage de Zarautz🏊🏖️")

    if jour == "Jour 4":
            st.write("Courte activité le matin en autonomie")
            st.write("🚙 Départ du gîte en fin de matinée pour retour à Surgères en fin de journée")

# INFO PRATIQUES ############################# 

elif menu == "Infos pratiques":
    st.subheader("🏨 Logement")
    st.write("Nous serons seul dans le gîte, le nombre de chambres mises à disposition dépend du nombre de participants")
    lien_logement = "https://www.lustou.com/camping-gite-groupe-vielle-aure/"
    st.write("3 chambres de 5 🛏️")
    st.write("Les draps sont fournis, pensez à prendre votre carte d'identité")
    st.markdown(f"[Ici les informations sur le logement]({lien_logement})", unsafe_allow_html=True)
    
    # st.subheader("🏊 Natation")
    # st.write("La plage de Zarautz est à 30 minutes en voiture et la piscine municipale d'Aya à 17 minutes.")
    # st.write(f"Aujourd'hui l'eau de l'océan à la plage de Zarautz est à {st.session_state.temp_eau}°🌡️")

    st.subheader(" 🏃‍♀️Course à pied")
    st.write("Pas de parcours tracé mais un beau terrain de jeu trail à disposition ⛰️")

# PARCOURS ############################# 

elif menu == "Parcours":
    st.subheader("🚴‍♂️ Parcours vélo")
    distance_min = df_parcours["Kilometres"].min()
    distance_max = df_parcours["Kilometres"].max()
    val_min, val_max = st.slider("Choisis une plage de nombre de kilomètres :", min_value= distance_min, max_value= distance_max, value=(distance_min, distance_max))
    df_choix = df_parcours.loc[(df_parcours["Kilometres"]>= val_min) & (df_parcours["Kilometres"]<= val_max)].sort_values("Kilometres").reset_index(drop = True)
    #st.write(df_choix)
    nb_parcours = df_choix.shape[0]
    if nb_parcours != 0 :
        st.write(f"Il y a {nb_parcours} parcours trouvés")
        list_nb_parcours = range(1,nb_parcours+1)
        st.write(f"1️⃣ long de {df_choix["Kilometres"].iloc[0]}km pour {df_choix["Denivele"].iloc[0]}mD+")
        if nb_parcours >= 2 :
            st.write(f"2️⃣ long de {df_choix["Kilometres"].iloc[1]}km pour {df_choix["Denivele"].iloc[1]}mD+")
        if nb_parcours >= 3 :
            st.write(f"3️⃣ long de {df_choix["Kilometres"].iloc[2]}km pour {df_choix["Denivele"].iloc[2]}mD+")
        if nb_parcours >= 4 :
            st.write(f"4️⃣ long de {df_choix["Kilometres"].iloc[3]}km pour {df_choix["Denivele"].iloc[3]}mD+")
        if nb_parcours >= 5 :
            st.write(f"5️⃣ long de {df_choix["Kilometres"].iloc[4]}km pour {df_choix["Denivele"].iloc[4]}mD+")
        if nb_parcours >= 6 :
            st.write(f"6️⃣ long de {df_choix["Kilometres"].iloc[5]}km pour {df_choix["Denivele"].iloc[5]}mD+")
        if nb_parcours >= 7 :
            st.write(f"7️⃣ long de {df_choix["Kilometres"].iloc[6]}km pour {df_choix["Denivele"].iloc[6]}mD+")
        if nb_parcours >= 8 :
            st.write(f"8️⃣ long de {df_choix["Kilometres"].iloc[7]}km pour {df_choix["Denivele"].iloc[7]}mD+")
        if nb_parcours >= 9 :
            st.write(f"9️⃣ long de {df_choix["Kilometres"].iloc[8]}km pour {df_choix["Denivele"].iloc[8]}mD+")

        
        choix = st.selectbox("Choisis le parcours que tu veux visualiser", list_nb_parcours)

        st.write("Parcours")
        st.image(f"{df_choix["Map"].iloc[choix-1]}")
        st.write("Profil")
        st.image(f"{df_choix["Profil"].iloc[choix-1]}")
        dropbox_link = df_choix["Lien"].iloc[choix-1]
        st.markdown(f"[📥 Télécharger le GPX]({dropbox_link})", unsafe_allow_html=True)


    else :
        st.write("❌ Pas de parcours avec ce kilométrage ❌")
    