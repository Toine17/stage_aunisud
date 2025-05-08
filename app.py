import streamlit as st
import pandas as pd

df_parcours = pd.read_csv("parcours.csv")


menu = st.sidebar.radio(
    "Menu",
    ["Accueil", "Programme", "Infos pratiques", "Parcours"]
)

# ACCUEIL #############################

if menu == "Accueil":
    st.subheader("Bienvenue sur la page du stage Aunisud triathlon 2025 🔴⚫")
    st.write("Nous serons 16 à participer au stage cette année.")
    st.write("Direction le Pays Basques espagnol du 29 mai au 1er juin.")
    st.image("groupe_accueil.jpg")

# PROGRAMME #############################

elif menu == "Programme":
    st.subheader("Déroulé du stage")
    jour = st.selectbox("Choix de la journée" , ["Jour 1","Jour 2","Jour 3","Jour 4"])
    if jour == "Jour 1":
        st.write("🚙 Départ de la piscine de Surgères avec 2 minibus, heure à définir")
        st.write("Trajet jusqu'en début d'après-midi, prévoir un pique-nique")
        st.write("Arrivée au gîte, 🚴‍♂️ première sortie vélo 48km 1000m D+")
        st.write("Prévoir la tenue club pour faire la photo du stage")
        st.write("Parcours")
        st.image("map_jour_1.jpg")
        st.write("Profil")
        st.image("Profil_jour_1.jpg")
        dropbox_link_1 = "https://www.dropbox.com/scl/fi/4f85nhlffifvurx1i3ntn/Jour-1.gpx?rlkey=ds6h3gw7yy8ex0g7jwnu1j3aa&st=nhe3wcqc&dl=1"
        st.markdown(f"[📥 Télécharger le GPX]({dropbox_link_1})", unsafe_allow_html=True)
    if jour == "Jour 2":
        st.write("🚴‍♂️ Sortie longue à vélo, 2 groupes por 2 distances avec départ en commun")
        st.write("Les 45 premiers kilomètres sont communs aux 2 groupes")
        col1, col2 = st.columns(2)

        with col1:
            st.header("Version courte")
            st.write("65km pour 1550m D+")
            st.write("Parcours")
            st.image("map_jour_2_courte.jpg")
            st.write("Profil")
            st.image("Profil_jour_2_courte.jpg")
            dropbox_link_2_courte = "https://www.dropbox.com/scl/fi/7u6xlbv5ffxwhv4ofuryq/Jour-2-courte.gpx?rlkey=xk0k76z7o1dojs7ph2252h0qm&st=kvti2r3m&dl=1"
            st.markdown(f"[📥 Télécharger le GPX]({dropbox_link_2_courte})", unsafe_allow_html=True)

        with col2:
            st.header("Version longue")
            st.write("92km pour 2150m D+")
            st.write("Parcours")
            st.image("map_jour_2_longue.jpg")
            st.write("Profil")
            st.image("Profil_jour_2_longue.jpg")
            dropbox_link_2_longue = "https://www.dropbox.com/scl/fi/tarqflt0pd8nxyfh3qlqa/jour-2-longue.gpx?rlkey=dkod75gqul3nj54bypixpjvhy&st=ks2b427d&dl=1"
            st.markdown(f"[📥 Télécharger le GPX]({dropbox_link_2_longue})", unsafe_allow_html=True)

    if jour == "Jour 3":
            st.write("En autonomie, plusieurs parcours sont disponibles dans la section Parcours.")
            st.write("Natation en mer en fin de journée")

    if jour == "Jour 4":
            st.write("Courte activité le matin en autonomie")
            st.write("🚙 Départ du gîte en fin de matinée pour retour à Surgères en fin de journée")

# INFO PRATIQUES ############################# 

elif menu == "Infos pratiques":
    st.subheader("🏨 Logement")
    st.write("Il se peut que nous ne soyons pas seuls dans le logement.")
    lien_logement = "https://www.booking.com/hotel/es/saskarate.fr.html?aid=304142&label=gen173nr-1FCCsoggI46AdIDVgEaE2IAQGYAQ24ARfIAQzYAQHoAQH4AQaIAgGoAgO4AtbG88AGwAIB0gIkZTRmOWNkOTAtYjBmMC00ODc5LWIzODAtNzA5NDFjZGFmZjIz2AIF4AIB"
    st.write("4 chambres triples, 1 chambre quadruple")
    st.write("Selon l'agencement des chambres on essaiera de déplacer un lit pour faire une chambre double pour les filles et une deuxième chambre quadruple.")
    st.markdown(f"[Ici les informations sur le logement]({lien_logement})", unsafe_allow_html=True)
    st.subheader("🏊 Natation")
    st.write("La plage de Zarautz est à 30 minutes en voiture et la piscine municipale d'Aya à 17 minutes.")
    st.subheader(" 🏃‍♀️Course à pied")
    st.write("Pas de parcours tracé mais un beau terrain de jeu trail à disposition.")
# PARCOURS ############################# 

elif menu == "Parcours":
    st.subheader("🚴‍♂️ Parcours vélo")
    distance_min = df_parcours["Kilometres"].min()
    distance_max = df_parcours["Kilometres"].max()
    val_min, val_max = st.slider("Choisis une plage de nombre de kilomètres :", min_value= distance_min, max_value= distance_max, value=(distance_min, distance_max))
    df_choix = df_parcours.loc[(df_parcours["Kilometres"]>= val_min) & (df_parcours["Kilometres"]<= val_max)].reset_index(drop = True)
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
        
        choix = st.selectbox("Choisis le parcours que tu veux visualiser", list_nb_parcours)

        st.write("Parcours")
        st.image(f"{df_choix["Map"].iloc[choix-1]}")
        st.write("Profil")
        st.image(f"{df_choix["Profil"].iloc[choix-1]}")
        dropbox_link = df_choix["Lien"].iloc[choix-1]
        st.markdown(f"[📥 Télécharger le GPX]({dropbox_link})", unsafe_allow_html=True)


    else :
        st.write("pas de parcours")
    