"""
Vectorise les reviews du CSV nettoyé à l'aide de TF-IDF et sauvegarde la matrice ainsi que le vectorizer.
Permet la recherche de similarité textuelle dans la phase de modélisation.
"""

import polars as pl
from sklearn.feature_extraction.text import TfidfVectorizer
from stop_words import get_stop_words
import pickle

def vectorize_reviews(csv_path, output_path):
    """
    Vectorise les reviews du CSV nettoyé et sauvegarde la matrice TF-IDF.
    """
    df = pl.read_csv(csv_path)
    reviews = [r for r in df['review'].to_list() if isinstance(r, str) and r.strip()]
    stop_words = get_stop_words('french')
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    tfidf_matrix = vectorizer.fit_transform(reviews)
    with open(output_path, 'wb') as f:
        pickle.dump((vectorizer, tfidf_matrix, reviews), f)
    print(f"Matrice TF-IDF sauvegardée dans : {output_path}")

if __name__ == "__main__":
    csv_path = "./dataset/clean/fight_club_critiques_cleaned.csv"
    output_path = "./dataset/clean/fight_club_tfidf.pkl"
    vectorize_reviews(csv_path, output_path)