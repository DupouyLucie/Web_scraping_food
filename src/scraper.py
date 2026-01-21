import requests
from bs4 import BeautifulSoup
from database import Database

"""
on doit extraire le nom, les ingrédients le nutriscore.
Pour regarder ce qu'on doit extraire, on clique sur inspecter :
Nom : <h1>
Nutriscore :span avec nutriscore
Ingrédients : <div id="ingredients_text">

1er problème : les produits ne se trouvent pas sur la page d'accueil,
il faut aller voir la page de chaque produit

scraper = outil ou programme qui visite des pages web, lis le HTML,extrait des informations
"""

#URL de produits ( premiers tests)
#EAU
#URL = "https://world.openfoodfacts.org/product/6111035002175/sidi-ali"
#MAYO
#URL="https://world.openfoodfacts.org/product/6111184004129/mayonnaise-original-recipe-star"
#princes
#URL="https://world.openfoodfacts.org/product/7622210449283/prince-gout-chocolat-lu"

#URL de la page d'acceuil:
URL=https://world.openfoodfacts.org/

def scraper(url):
    response = requests.get(url)   # Python va sur le site, récupère la page HTML, stocke dans response
    soup = BeautifulSoup(response.text, "html.parser") # transforme le HTML brut en objet BeautifulSoup lisible par python

    nom= soup.find("h1")
    nom_produit = nom.get_text(strip=True)  if nom else None # nécéssaire sinon retourne la balise HTML et pas le texte 

    nutri = soup.find("strong", text=lambda t: t and "Nutri-Score" in t) # on cherche avec inspecter
    nutriscore = nutri.text.replace("Nutri-Score:", "").strip() if nutri else None

    ingr = soup.find("h3", id="panel_group_ingredients").find_next("div", class_="panel_text") # pareil, necessaire car pas assez précis juste "ingrédients"
    ingredients = ingr.get_text(" ", strip=True) if ingr else "Sans ingrédients"

    return {"nom": nom_produit, "nutriscore": nutriscore, "ingredients": ingredients }

# On exporte les données sur le fichier SQL
db = Database("data/database.db")  # ouvre la base
product = scraper(URL) # On récupère toutes les infos
db.insert_produit(nom=product["nom"], nutriscore=product["nutriscore"], ingredients=product["ingredients"]
)
print("nouvelle ligne: " , db.recup_prod())
db.close()  # fermeture propre



# if __name__ == "__main__":
#     product = scraper(URL)
#     print(product)

