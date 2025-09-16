# SensCritique - Recommandation de Critiques Similaires

## Objectif

Ce projet propose un algorithme permettant de recommander des critiques similaires à une critique en cours de lecture pour **un film** (ex : Fight Club, Interstellar).  
L'utilisateur consulte une critique, et le système lui suggère les avis les plus proches parmi ceux du même film.

---

## Architecture & System Design

L'explication détaillée du system design se trouve dans le sous-dossier `./system-design`.

---

## Installation

1. **Cloner le repo**
   ```bash
   git clone https://github.com/Rococo77/movie-recommendation.git
   cd movie-recommendation
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

---

## Utilisation

### 1. Nettoyer le fichier CSV brut

Le repo contient uniquement les fichiers CSV bruts (ex : `fight_club_critiques.csv`, `interstellar_critiques.csv`) dans `./dataset/raw/`.

Pour générer les fichiers nettoyés :

```bash
python app/process-data/process.py
```
Le fichier nettoyé sera généré dans `./dataset/clean/<nom_du_film>_critiques_cleaned.csv`.

### 2. Vectoriser les critiques

Pour générer la matrice TF-IDF et le vectorizer :

```bash
python app/process-data/vectorise.py
```
Le fichier vectorisé sera généré dans `./dataset/clean/<nom_du_film>_tfidf.pkl`.

### 3. Lancer l'interface Streamlit

Pour utiliser l'interface de recommandation :

```bash
streamlit run app/app.py
```
Sélectionnez une critique dans la liste pour obtenir les suggestions les plus proches.

---

## Exemple

```
1. Nettoyage du CSV brut
2. Vectorisation des reviews
3. Lancement de l'interface Streamlit
4. Sélection d'une critique et affichage des suggestions similaires
```

---

## Améliorations

Toutes les améliorations envisagées pour la production sont détaillées dans le README du sous-dossier `./system-design`.

---

## Segments générés par IA

- L'IA est intervenue dans la mise en forme des fichiers Markdown, l'écriture des docstrings, l'amélioration légère de l'interface Streamlit.
- L'auto-complétion via GitHub Copilot a été utilisée pour accélérer le développement.
- L'IA m'a également servi de "canard en plastique" pour clarifier et structurer mes idées lors de la conception du projet.

---

## Auteur
Corentin ROSSETTO
Projet réalisé dans le cadre d'un test technique pour SensCritique.