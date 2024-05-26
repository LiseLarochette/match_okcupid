import streamlit as st
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Charger les données
final_df_cupid = pd.read_csv('hearthack_final_df.csv')


# Préparer l'interface utilisateur
st.title("💘 Application de Recommandation de Match Idéal")
st.header("Entrez vos informations pour trouver votre match parfait !")

# Entrées utilisateur
age = st.slider("Âge", 18, 100, 28)
status = st.selectbox("Statut", ["Single", "In a relationship"])
sex = st.selectbox("Sexe", ["Male", "Female"])
orientation = st.selectbox("Orientation", ["Straight", "Gay", "Bisexual"])
body_type = st.selectbox("Type de corps", ["Fit", "Average", "Athletic", "Overweight"])
diet = st.selectbox("Régime alimentaire", ["Anything", "Vegetarian", "Vegan"])
education = st.selectbox("Niveau d'éducation", ["High school", "College", "Wildcodeschool", "Graduate"])
height = st.slider("Taille (en cm)", 140, 220, 180)
job = st.selectbox("Métier", ["Other", "Computer / hardware / software", "Art / music / writing", "Sales / marketing / biz dev"])
pets = st.selectbox("Animaux de compagnie", ["Likes pets", "Does not like pets"])
smokes = st.selectbox("Fume", ["No", "Yes"])
