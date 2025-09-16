"""
Interface Streamlit pour la recommandation de critiques similaires.
Permet à l'utilisateur de sélectionner une critique et d'afficher les suggestions les plus proches.
"""

import streamlit as st
from modelisation.model import find_similar_reviews_tfidf
import polars as pl

def preview(text, length=120):
    """
    Retourne un aperçu tronqué de la review pour l'affichage.
    """
    return text[:length] + "..." if len(text) > length else text

st.title("Recommandation de critiques similaires")

tfidf_path = "./dataset/clean/fight_club_tfidf.pkl"
csv_path = "./dataset/clean/fight_club_critiques_cleaned.csv"


df = pl.read_csv(csv_path)
review_options = [r for r in df['review'].to_list() if isinstance(r, str) and r.strip()]
selected_idx = st.selectbox(
    "Choisissez une critique à consulter :",
    range(len(review_options)),
    format_func=lambda i: review_options[i][:80] + "..." if len(review_options[i]) > 80 else review_options[i]
)

if st.button("Trouver les avis similaires"):
    selected_review = review_options[selected_idx]
    top_k = 5
    top_idx, df_full = find_similar_reviews_tfidf(selected_review, tfidf_path, csv_path, top_n=top_k + 1)
    filtered_idx = [int(idx) for idx in top_idx if review_options[int(idx)] != selected_review]
    filtered_idx = filtered_idx[:top_k]
    st.subheader("Avis similaires :")
    for idx in filtered_idx:
        row = df_full.select(['username', 'note', 'review_title', 'review', 'review_url']).row(idx)
        username, note, review_title, review, review_url = row
        st.markdown(
            f"**Utilisateur :** {username}  \n"
            f"**Note :** {note}  \n"
            f"**Titre :** {review_title}  \n"
            f"**Critique :** {preview(review)}  \n"
            f"[Voir la critique]({review_url})"
        )
        st.write("---")