import pandas as pd
import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()

def accueil():
    st.title("Bienvenu sur ma page !")

# Création du menu qui va afficher les choix qui se trouvent dans la variable options
with st.sidebar:
    authenticator.logout("Déconnexion")
    st.text(f"Bienvenu {lesDonneesDesComptes['usernames']['utilisateur']['name']} !")
    selection = option_menu(
                menu_title=None,
                options = [" 😍 Accueil", " 😻 Les photos de mon chat"]
            )

if st.session_state["authentication_status"]:

    # On indique au programme quoi faire en fonction du choix
    if selection == " 😍 Accueil":
        st.title("Bienvenue sur ma page !")
        st.image("/Users/kilian/Documents/WCS/Quêtes/Streamlit/Applause.jpg")
        
    elif selection == " 😻 Les photos de mon chat":
        st.title("Bienvenue dans l'album de mon chat! 😸")


        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("/Users/kilian/Documents/WCS/Quêtes/Streamlit/Grumpy Cat.jpg")

        with col2:
            st.image("/Users/kilian/Documents/WCS/Quêtes/Streamlit/Ugly cat.jpg")

        with col3:
            st.image("/Users/kilian/Documents/WCS/Quêtes/Streamlit/Funny cat.jpg")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')

