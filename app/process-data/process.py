"""
Nettoie le fichier CSV brut de critiques, ajoute un header, applique le nettoyage sur la colonne 'review',
et génère un nouveau fichier CSV prêt pour la vectorisation et la modélisation.
"""

import csv
import os
from utils import clean_html

def process_csv(input_file, output_file):
    """
    Lit un fichier CSV de reviews, ajoute un header, nettoie la colonne 'review',
    et écrit le résultat dans un nouveau fichier CSV.
    
    Args:
        input_file (str): Chemin du fichier CSV source.
        output_file (str): Chemin du fichier CSV nettoyé à générer.
    """
    header = ['review_id', 'review_url', 'note', 'created_at', 'updated_at', 'views', 'review', 'review_title', 'likes', 'username','user_id']
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        writer.writerow(header)
        for row in reader:
            if len(row) < 11:
                continue
            row[6] = clean_html(row[6])
            writer.writerow(row)

if __name__ == "__main__":
    input_file = "dataset/raw/fight_club_critiques.csv"
    output_dir = "./dataset/clean/"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "fight_club_critiques_cleaned.csv")
    process_csv(input_file, output_file)
    print(f"Fichier nettoyé enregistré dans : {output_file}")