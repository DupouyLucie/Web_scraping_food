import requests
from bs4 import BeautifulSoup

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
#EAU
#URL = "https://world.openfoodfacts.org/product/6111035002175/sidi-ali"
#MAYO
#URL="https://world.openfoodfacts.org/product/6111184004129/mayonnaise-original-recipe-star"
#princes
URL="https://world.openfoodfacts.org/product/7622210449283/prince-gout-chocolat-lu"

def scraper(url):
    response = requests.get(url)   # Python va sur le site, récupère la page HTML, stocke dans response
    soup = BeautifulSoup(response.text, "html.parser") # transforme le HTML brut en objet BeautifulSoup lisible par python

    nom= soup.find("h1")
    nom_produit = nom.get_text(strip=True)  if nom else None # nécéssaire sinon retourne la balise HTML et pas le texte 

    nutri = soup.find("strong", text=lambda t: t and "Nutri-Score" in t) # on cherche avec inspecter
    nutriscore = nutri.text.replace("Nutri-Score:", "").strip() if nutri_tag else None

    ingr = soup.find("h3", id="panel_group_ingredients").find_next("div", class_="panel_text") # pareil, necessaire car pas assez précis juste "ingrédients"
    ingredients = ingr.get_text(" ", strip=True) if ingredients_tag else "Sans ingrédients"

    return {"nom": nom_produit, "nutriscore": nutriscore, "ingredients": ingredients }


if __name__ == "__main__":
    product = scraper(URL)
    print(product)





































# #test

# url_prod="https://world.openfoodfacts.org/product/6111035000430/"
# rep=requests.get(url)
# if response.status_code != 200:
#      print("Erreur :", response.status_code)
# soup = BeautifulSoup(response.text, "html.parser")
# nom=soup.find("h1", property="food:name")
# ingredient=soup.find("div", property='content panel_content expand-for-large active')
# nutriscore=soup.find("h4", property="Nutri-Score")
# print(nom)
# print(ingredient)
# print(nutriscore)

# # url = "https://world.openfoodfacts.org/"
# # response = requests.get(url)
# # html = response.text

# # if response.status_code != 200:
# #     print("Erreur :", response.status_code)

# # print(type(html))
# # soup = BeautifulSoup(html, "html.parser")
# # type(soup)

# # livre = soup.find("v", class_="viewport")
# # print(livre)
# # #print(html[:2000]) 


# # Test 

# # url_2 = "https://world.openfoodfacts.org/product/737628064502/coca-cola"
# # response = requests.get(url_2)
# # html = response.text
# # soup = BeautifulSoup(response.text, "html.parser")
# # nom=soup.find("h1", property="food:name")
# # ingredient=soup.find("  ")
# # # print(nom)
# # print(html[:2000]) 

