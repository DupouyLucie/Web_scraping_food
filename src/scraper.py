import requests
from bs4 import BeautifulSoup
from database import Database


# avec Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
import time






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
# URL="https://world.openfoodfacts.org/"
URL="https://world.openfoodfacts.org/cgi/search.pl?action=process&page_size=20"

def scraper_produit(url):
    response = requests.get(url)   # Python va sur le site, récupère la page HTML, stocke dans response
    soup = BeautifulSoup(response.text, "html.parser") # transforme le HTML brut en objet BeautifulSoup lisible par python

    nom= soup.find("h1")
    nom_produit = nom.get_text(strip=True)  if nom else None # nécéssaire sinon retourne la balise HTML et pas le texte 

    nutri = soup.find("strong", text=lambda t: t and "Nutri-Score" in t) # on cherche avec inspecter
    nutriscore = nutri.text.replace("Nutri-Score:", "").strip() if nutri else None

    ingr = soup.find("h3", id="panel_group_ingredients").find_next("div", class_="panel_text") # pareil, necessaire car pas assez précis juste "ingrédients"
    ingredients = ingr.get_text(" ", strip=True) if ingr else "Sans ingrédients"
    #print ("nom", nom_produit, "nutriscore:", nutriscore, "ingredients", ingredients )

    return {"nom": nom_produit, "nutriscore": nutriscore, "ingredients": ingredients }


def scraper_lien():
    # "donne une liste de lien"
    # response = requests.get(URL) #ici il faut que ce soit l'URL du site
    # if response.status_code != 200:
    #     print("Erreur :", response.status_code)
    # soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())
    # liens = []
    # balises=soup.find_all("a", class_="list_product_a")
    # #balises=soup.find_all("a", href=True)
    # #<a href="https://world.openfoodfacts.org/product/6111242100992/perly" class="list_product_a" title="Perly – 100&nbsp;g"><div class="list_product_content"><div class="list_product_img_div"><img src="https://images.openfoodfacts.org/images/products/611/124/210/0992/front_fr.172.200.jpg" class="list_product_img" alt="Perly – 100&nbsp;g" loading="lazy"></div><div class="list_product_name">Perly – 100&nbsp;g</div><div class="list_product_sc"><img class="list_product_icons" src="https://static.openfoodfacts.org/images/attributes/dist/nutriscore-unknown-new-en.svg" title="Nutri-Score unknown - Missing data to compute the Nutri-Score" alt="Nutri-Score unknown" loading="lazy"><img class="list_product_icons" src="https://static.openfoodfacts.org/images/attributes/dist/nova-group-3.svg" title="Processed foods" alt="Processed foods" loading="lazy"><img class="list_product_icons" src="https://static.openfoodfacts.org/images/attributes/dist/green-score-b.svg" title="Green-Score B - Low environmental impact" alt="Green-Score B" loading="lazy"></div></div></a>
    # print(balises)
    # #ici, on a un liste de balise. Nous, on veut récupérer que le lien 
    # for balise in balises :
    #     lien_produit = balise["href"]
    #     if "/product/" in lien_produit:
    #         url = "https://world.openfoodfacts.org" + lien_produit
    #         if url not in liens:
    #             print(url)
    #             liens.append(url)
    #     if len(liens) == n:
    #         break 
    # return liens
    liens=[]
    for i in range(1,5):
        print(i)
        URL="https://world.openfoodfacts.org/"+str(i)
        driver = webdriver.Chrome()   # ouvre Chrome
        driver.get(URL)  # page d'accueil
        time.sleep(5)  # attendre que le JS charge
        produits = driver.find_elements(By.CLASS_NAME, "list_product_a")

        for p in produits:
            lien = p.get_attribute("href")
            liens.append(lien)
    return liens


def boucle_scrap():
    liste_liens=scraper_lien()
    for lien in liste_liens:
        exporter_database(lien)

def exporter_database(url):    
    # On exporte les données sur le fichier SQL
    db = Database("data/database.db")  # ouvre la base
    product = scraper_produit(url) # On récupère toutes les infos
    db.insert_produit(nom=product["nom"], nutriscore=product["nutriscore"], ingredients=product["ingredients"]
    )
    db.close()  # fermeture propre



if __name__ == "__main__":
    boucle_scrap()



