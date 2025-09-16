"""
Recherche les critiques similaires à une critique donnée en utilisant la matrice TF-IDF.
Retourne les indices des critiques les plus proches et le DataFrame complet pour affichage.
"""

import pickle
import polars as pl
from sklearn.metrics.pairwise import cosine_similarity

def find_similar_reviews_tfidf(query, tfidf_path, csv_path, top_n=5):
    """
    Trouve les critiques les plus similaires à une critique donnée.
    
    Args:
        query (str): Critique de référence.
        tfidf_path (str): Chemin du fichier pickle contenant le vectorizer et la matrice TF-IDF.
        csv_path (str): Chemin du CSV nettoyé.
        top_n (int): Nombre de suggestions à retourner.
    
    Returns:
        tuple: (indices des critiques similaires, DataFrame complet)
    """
    with open(tfidf_path, 'rb') as f:
        vectorizer, tfidf_matrix, reviews = pickle.load(f)
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, tfidf_matrix)[0]
    top_idx = scores.argsort()[::-1][:top_n]
    df = pl.read_csv(csv_path)
    return top_idx, df