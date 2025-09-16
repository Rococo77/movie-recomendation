"""
Fonctions utilitaires pour le nettoyage des textes de critiques :
- Suppression des accents
- Nettoyage HTML, URLs, espaces superflus, mise en minuscules
"""

import unicodedata
import re
from bs4 import BeautifulSoup

def remove_accents(text):
    """
    Supprime les accents des caractères dans une chaîne de texte.
    """
    nfkd_form = unicodedata.normalize('NFKD', text)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

def clean_html(text):
    """
    Nettoie le texte d'une review en supprimant les balises HTML, les URLs, 
    les espaces superflus, les accents et en mettant tout en minuscules.
    """
    soup = BeautifulSoup(text, "html.parser")
    cleaned = soup.get_text(separator=" ")
    cleaned = re.sub(r'http\S+|www\.\S+', '', cleaned)
    cleaned = re.sub(r'\s+', ' ', cleaned)
    ##cleaned = re.sub(r'\d+', '', cleaned)
    cleaned = cleaned.strip().lower()
    cleaned = remove_accents(cleaned)
    return cleaned