# Guide SQLite – Base de données pour le projet de Web Scraping

## Objectif général
Ce document explique **comment utiliser une base de données SQLite en Python** pour stocker les données scrapées **au fur et à mesure du scraping**.

---

## I - Pourquoi utiliser une base de données dans ce projet ?

Dans un projet de scraping réel, on ne stocke pas les données :
- uniquement en mémoire
- uniquement dans des fichiers CSV/JSON

On utilise une **base de données** pour :

- sauvegarder les données progressivement
- éviter les pertes en cas d’erreur
- structurer proprement l’information
- permettre l’analyse par un autre membre de l’équipe

👉 Ici, nous utilisons **SQLite**, une base simple et professionnelle et surtout ... open-source ^^

---

## II - Qu’est-ce que SQLite ?

SQLite est une **base de données relationnelle** stockée dans **un simple fichier `.db`**.

Caractéristiques :
- pas de serveur
- pas de configuration
- intégrée à Python
- portable

Exemple de fichier :
```

database.db

````

---

## III - Voir la base de données : DB Browser for SQLite

### Pourquoi ?
Sans outil graphique, une base SQLite est illisible.
Pour comprendre ce qui se passe, **vous devez installer un visualiseur**.

### DB Browser for SQLite

Lien officiel :  
https://sqlitebrowser.org/

---

### Installation
1. Télécharger la version correspondant à votre système
2. Installer le logiciel
3. Lancer DB Browser for SQLite

---

### Ouvrir la base du projet (quand vous l'aurez généré)
1. Cliquer sur **Ouvrir une base de donnée**
2. Sélectionner le fichier `database.db`
3. Aller dans l’onglet **Parcourir les données**

➡️ Vous verrez les lignes s’ajouter pendant le scraping

⚠️ Ne pas modifier la base manuellement pendant que Python écrit dedans

---

## IV - Méthode du projet

> **La base de données est alimentée pendant le scraping**,  
> pas à la fin.

Chaque annonce scrapée est :
- nettoyée
- immédiatement insérée dans SQLite

➡️ La base devient la **source de vérité du projet**

---

## V - Architecture imposée du code

### Règle absolue
❌ Le scraper **ne fait jamais de SQL**  
✅ Le SQL est **centralisé dans une classe dédiée**

---

### Rôle de la classe `DatabaseManager`

La classe gère :
- la connexion SQLite
- la création des tables
- l’insertion des annonces
- la lecture des données
- la fermeture propre de la base

👉 Le scraping **utilise la classe**, sans connaître SQLite.

---

## VI - Connexion à la base (une seule fois)

```python
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
````

📌 Cette connexion est ouverte :

* une seule fois
* au début du programme

---

## VII - Utiliser une classe pour gérer la base

### Pourquoi une classe ?

Sans classe :

* duplication de code
* mélange scraping / base de données
* erreurs fréquentes

Avec une classe :

* code clair
* responsabilités séparées
* maintenance facile

---

### Création de l’objet base de données

```python
db = DatabaseManager("database.db")
```

Cette ligne :

* ouvre la base
* crée la table si nécessaire
* prépare la base pour le scraping

---

## VIII - Structure de la table `annonces`
On prend ici l'exemple d'une table contenant des annonces immobilères. 

```sql
annonces (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    prix INTEGER NOT NULL,
    surface INTEGER,
    ville TEXT NOT NULL,
    nb_pieces INTEGER,
    date_scraping TEXT NOT NULL
)
```

---

## IX - Insertion immédiate pendant le scraping

### Côté scraping (simple)

```python
db.insert_annonce(
    titre,
    prix,
    surface,
    ville,
    nb_pieces
)
```

Le scraper :

* collecte les données
* les nettoie
* les envoie à la base

---

### Côté base de donnée (caché)

* ajout automatique de la date
* requête SQL sécurisée
* commit immédiat
* gestion des erreurs

---

## X - Commit et persistance

```python
conn.commit()
```

📌 Sans `commit()` :

* rien n’est enregistré
* la base reste vide

Dans ce projet :

* commit après chaque annonce
* ou après chaque page

---

## XI - Gérer les doublons

### Problème

Une annonce peut apparaître plusieurs fois.

### Solution

* champ `UNIQUE`
* gestion des erreurs SQLite

```sql
url TEXT UNIQUE
```

```python
except sqlite3.IntegrityError:
    pass
```

---

## XII - Voir la base se remplir (expérience conseillée)

1. Ouvrir `database.db` dans DB Browser
2. Lancer le scraping
3. Cliquer sur **Refresh**

➡️ Les annonces apparaissent progressivement

---

## XIII - Lire les données depuis Python

```python
db.get_all_annonces()
```

```python
db.get_annonces_by_ville("Paris")
```

---

## XIV - Fermeture propre de la base

```python
db.close()
```

⚠️ Obligatoire en fin de script

Pour votre rapport faite des captures d'écrans de DB Browser (SQLite)
