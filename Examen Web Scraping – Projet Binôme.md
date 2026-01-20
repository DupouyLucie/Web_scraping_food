# Examen Web Scraping – Projet Binôme

## Objectif du projet
**Durée :** 5 heures  
**Travail :** en binôme  

L'objectif est de créer un **scraper web en Python** pour récupérer des données depuis un site au choix, stocker les données dans une **base SQLite**, analyser et visualiser les résultats.

---

## 🔹 Livrables attendus
- `scraper.py` : script Python pour extraire les données  
- `database`: script Python pour gérer les interactions avec la base de donnée
- `analyse.py` : script Python pour analyse et statistiques  
- `visualisation.py` pour afficher les analyses using matplotlib  
- Base SQLite : `data/nom_bdd.db` 
- Les visuels produits : `output/***.png`
- Documentation : `rapport.md`  

---

## 🔹 Sites possibles à scraper
| Site | URL | Données à extraire |
|------|-----|------------------|
| IMDB Top 250 (FR) | [https://www.imdb.com/fr/chart/top/](https://www.imdb.com/fr/chart/top/) | Film, Année, Note |
| Pokémon Database | [https://pokemondb.net/pokedex/all](https://pokemondb.net/pokedex/all) | Nom, Types, Statistiques |
| Open Brewery DB | [https://www.openbrewerydb.org/breweries?query=Montana](https://www.openbrewerydb.org/breweries?query=Montana) | Nom, Ville, Type |
| Books to Scrape | [https://books.toscrape.com/](https://books.toscrape.com/) | Titre, Prix, Note, Catégorie |
| Quotes to Scrape | [https://quotes.toscrape.com/](https://quotes.toscrape.com/) | Citation, Auteur, Tags |
| Open Food Facts | [https://world.openfoodfacts.org/product/6111035002175/sidi-ali](https://world.openfoodfacts.org/product/6111035002175/sidi-ali) | Nom, Ingrédients, Nutri-score |
| Open Library | [https://openlibrary.org/](https://openlibrary.org/) | Titre, Auteur, Sujet |

---

## 🔹 Organisation du projet
1. Choisir un site parmi ceux proposés.  
2. Écrire le scraper Python pour extraire les informations demandées.  
3. Nettoyer et structurer les données extraites.  
4. Stocker les données dans une **base SQLite**.  
5. Analyser les données avec `pandas` (statistiques, filtres, comparaisons).  
6. Produire des visualisations avec `matplotlib`.  
7. Rédiger la documentation expliquant le fonctionnement du scraper et de l’analyse.

---

## Règles de l’examen
- Chaque binôme doit travailler **en collaboration** et doivent se répartir la charge de travaille de manière **équitable**.  
- Utilisation de bibliothèques Python autorisées :  
  `requests`, `BeautifulSoup`, `pandas`, `sqlite3`, `matplotlib`.  
- Les fichiers remis doivent respecter la **structure suivante** :

```text
examen-webscraping/
├── src/
│   ├── scraper.py
│   ├── analyse.py
│   ├── visualisation.py
│   └── database.py
├── data/
│   └── nom_bdd.bd
├── output/
│   └── ***.png
├── rapport.md
└── requirements.txt
```
- Les scripts doivent être commentés et lisibles, respecter PEP8.

- Le rendu doit inclure au moins 4 visualisations différentes et des statistiques pertinentes.