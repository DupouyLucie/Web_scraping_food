# Guide Web Scraping – Introduction et Méthode

## Objectif
Ce guide explique **comment scraper un site web réel** pour récupérer des données.  
Nous l’illustrons avec des sites “annonces immobilières” fictifs ou publics, mais les concepts sont universels.

---

## I - Comment fonctionne une page web

### A - Structure générale
Une page web est composée de **HTML** et de **CSS/JS** :

```html
<!DOCTYPE html>
<html>
<head>
    <title>Exemple de page</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="annonce">
        <h2 class="titre">Appartement 3 pièces</h2>
        <span class="prix">250 000 €</span>
        <span class="ville">Paris</span>
    </div>
</body>
</html>
```
HTML : structure du contenu (titres, paragraphes, listes, images) 
CSS : mise en forme (couleurs, marges, taille de police)
JS : interactions dynamiques (menus déroulants, filtrage, chargement de données)

### B - Le DOM (Document Object Model)

Le DOM est un modèle de données qui représente une page web comme un arbre de nœuds.

Les nœuds peuvent avoir :

* balises :  ```<div>```, ```<span>```, ```<h1>```
* classes : ```class="titre"```
* id : ```id="annonce1"```

Pour scraper, on cherche des nœuds précis par balise, classe ou id

## II - Identifier les données à extraire
Exemple : site “Books to Scrape”
```
<article class="product_pod">
    <h3><a title="Livre Python avancé">Livre Python avancé</a></h3>
    <p class="price_color">£45.00</p>
    <p class="instock availability">En stock</p>
</article>
```
Titre : balise <a> avec attribut title

Prix : ```<p class="price_color">```

Disponibilité : ```<p class="instock availability">```

Astuce : utilisez l’inspecteur du navigateur (F12, ou click droit "inspecter élement") pour voir le DOM

## III - Télécharger la page web avec Python
### Utilisation de requests
```
import requests

url = "https://books.toscrape.com/"
response = requests.get(url)
html = response.text

if response.status_code != 200:
    print("Erreur :", response.status_code)
```
Toujours vérifier le code HTTP (200 = OK)

Attention aux sites dynamiques : si le contenu est chargé par JS, BeautifulSoup seul ne suffira pas (pas notre cas aujourd'hui).

## IV -  Parser le HTML avec BeautifulSoup
### A - Introduction
Parser, c’est analyser un texte brut (HTML) pour le transformer en une structure exploitable en Python.

Avant parsing :
→ une grosse chaîne de caractères (str)

Après parsing :
→ un objet BeautifulSoup qui représente le DOM (arbre HTML)

```
type(html)
-> <class 'str'>

soup = BeautifulSoup(html, "html.parser")
type(soup)s
-> <class 'bs4.BeautifulSoup'>
```

Grâce au parsing, on peut naviguer dans la page comme dans un arbre :

- parents
- enfants
- balises
- classes
- attributs

### B - Méthodes principales
```
soup.find()
```

La méthode find() retourne le premier élément correspondant
```
soup.find_all()
```

La méthode find_all() retourne une liste de tous les éléments correspondants

### C - Exemples de sortie (print)
1️⃣ Trouver un élément
```
livre = soup.find("article", class_="product_pod")
print(livre)
```

Output :
```
<article class="product_pod">
 <h3>
  <a title="Livre Python avancé">Livre Python avancé</a>
 </h3>
 <p class="price_color">£45.00</p>
 <p class="instock availability">In stock</p>
</article>
```

➡️ On récupère tout le bloc HTML

2️⃣ Trouver plusieurs éléments
```
livres = soup.find_all("article", class_="product_pod")
print(len(livres))
```

Output :
```
20
```

➡️ livres est une liste de 20 objets HTML

3️⃣ Accéder à un sous-élément
```
print(livre.h3.a)
```

Output :
```
<a title="Livre Python avancé">Livre Python avancé</a>

print(livre.h3.a.text)
```

Output :
```
Livre Python avancé
```
D - Extraction complète
```
livres = soup.find_all("article", class_="product_pod")

for livre in livres:
    titre = livre.h3.a["title"]
    prix = livre.find("p", class_="price_color").text
    print(titre, prix)
```

Output :
```
Livre Python avancé £45.00
Data Science Pro £39.99
Machine Learning £51.77
```

## V - Nettoyer et formater les données

Les données extraites sont toujours des chaînes de caractères (str). Il faut les nettoyer avant l'analyse ou le stockage.

Convertir les nombres en int ou float

complete ici

Supprimer les espaces et symboles

complete ici

Les  pages web changent souvent, on peut donc avoir des  :

- éléments manquants
- structures différentes
- valeusr vides
 
On peut utiliser try/except pour éviter que une erreur casse le scraping

Sans protection :
```
prix = livre.find("p", class_="price_color").text
```

Avec protection :
```
try:
    prix = livre.find("p", class_="price_color").text
except AttributeError:
    prix = None
```
## VI - Naviguer entre plusieurs pages
Les sites ont souvent pagination (page-1.html, page-2.html)

Identifier le lien vers la page suivante dans le HTML :

```
<li class="next"><a href="page-2.html">Next</a></li>
```

En Python :

```
next_link = soup.find("li", class_="next")
if next_link:
    url_suivante = next_link.a["href"]
```
Construire une boucle pour scraper toutes les pages

## VII - Sauvegarder les données
JSON pour vérifier rapidement :

```
import json
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
```
SQLite pour stockage durable (voir autres ressources)
