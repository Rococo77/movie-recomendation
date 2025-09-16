# System Design - SensCritique Recommandation de Critiques Similaires

## Légende du schéma

- **User** : L'utilisateur consulte une critique via l'interface (Streamlit).  
- **Selection / Lecture critique** : L'utilisateur choisit une critique à lire dans l'UI.
- **Suggestions similaires** : Le système affiche les critiques les plus proches de celle consultée.
- **process-data/process.py** : Script Python qui nettoie le CSV brut (suppression HTML, accents, URLs, etc.) et génère un CSV propre.
- **CSV clean** : Fichier CSV nettoyé, prêt pour la vectorisation.
- **process-data/vectorise.py** : Script Python qui vectorise les reviews du CSV nettoyé avec TF-IDF (scikit-learn, stopwords français).
- **TF-IDF matrix** : Matrice de vecteurs TF-IDF, stockée en pickle.
- **modelisation/model.py** : Script Python qui effectue la recherche de similarité (cosine similarity) et retourne les indices des critiques les plus proches.

## Choix techniques

- **Python** : Langage principal pour la rapidité de prototypage et l'écosystème NLP.
- **Polars** : Pour la gestion rapide des DataFrames.
- **scikit-learn** : Pour la vectorisation TF-IDF et le calcul de similarité cosinus.
- **stop-words** : Pour la gestion des stopwords français.
- **BeautifulSoup** : Pour le nettoyage des balises HTML dans les avis.
- **Streamlit** : Pour l'interface utilisateur interactive. Afin de simuler un cas en production.

## Flux de données

1. **CSV brut** : Fichier source contenant les critiques brutes.
2. **process.py** : Nettoie le CSV brut et génère le CSV clean.
3. **vectorise.py** : Vectorise le CSV clean et génère la matrice TF-IDF.
4. **model.py** : Utilise la matrice TF-IDF pour trouver les critiques similaires à celle consultée.
5. **UI** : L'utilisateur sélectionne une critique et visualise les suggestions similaires.

## Remarques

- Le système recommande uniquement des critiques du même film.
- Les fichiers intermédiaires (CSV clean, TF-IDF matrix) ne sont pas présents sur le repo, ils sont générés à partir des CSV bruts.
- L'architecture est modulaire et chaque étape est séparée dans un fichier dédié pour faciliter la maintenance et l'évolution du projet.

---

## Améliorations possibles pour une version production

Pour rendre le système plus robuste, performant et évolutif en production, plusieurs axes d'amélioration sont envisageables :

- **Prétraitement linguistique avancé**  
  Utiliser spaCy pour la lemmatisation, la suppression des stopwords, la reconnaissance d'entités et un nettoyage linguistique plus précis, surtout pour le français.  
  **Racinisation (stemming)** : appliquer la racinisation (ex : avec NLTK ou SnowballStemmer) sur les reviews permet de ramener les mots à leur racine, ce qui peut améliorer la qualité de la similarité en réduisant la variance liée aux différentes formes d’un même mot.

- **Embeddings sémantiques avancés**  
  Utiliser des modèles comme Sentence Transformers pour générer des vecteurs de critiques plus riches et pertinents que le simple TF-IDF.

- **Base de données vectorielle**  
  Intégrer une solution comme Weaviate pour stocker et interroger efficacement les embeddings.  
  Weaviate propose une API GraphQL, ce qui permet une intégration directe avec Apollo pour exposer les recommandations via une API flexible et moderne.  
  Alternativement, si l'entreprise utilise déjà PostgreSQL comme base de données SQL, pgvector peut être utilisé pour éviter la gestion de multiples bases et centraliser le stockage des données et des vecteurs.

- **Algorithmes de similarité et d'analyse avancés**  
  Explorer des approches comme l'approximate nearest neighbors (ANN), la recherche hybride (mélange de sémantique et de mots-clés), ou des modèles de recommandation personnalisés pour améliorer la pertinence des suggestions.  
  **Analyse de sentiment** : intégrer un algorithme d’analyse de sentiment pour filtrer ou pondérer les recommandations selon la tonalité des critiques (positive, négative, neutre), ce qui peut affiner la pertinence des suggestions pour l’utilisateur.

- **API GraphQL**  
  Exposer le service de recommandation via une API GraphQL (Apollo), facilitant l'intégration avec des frontends modernes et d'autres services.

- **Monitoring, logs et tests**  
  Ajouter des outils de monitoring, des logs détaillés et des tests unitaires pour garantir la stabilité et la maintenabilité du système.

---

*Ce document et le schéma associé répondent aux exigences du test technique et expliquent le fonctionnement global du système de recommandation de critiques similaires, ainsi que les pistes d'amélioration pour une version production.*