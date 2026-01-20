import requests
from bs4 import BeautifulSoup

# en vrai c'est scrapper le projet mais c'est pour pas avoir des commit issues avec Yannis
# on doit extraire le nom, les ingrédients le nutriscore.
# 1er problème : les produits ne se trouvent pas sur la page d'accueil,
#  il faut aller voir la page de chaque produit
#Test sur une page déjà ouvert d'un ingrédient :
url_prod="https://world.openfoodfacts.org/product/6111035000430/"
rep=requests.get(url)
if response.status_code != 200:
     print("Erreur :", response.status_code)
soup = BeautifulSoup(response.text, "html.parser")
nom=soup.find("h1", property="food:name")
ingredient=soup.find("div", property='content panel_content expand-for-large active')
nutriscore=soup.find("h4", property="Nutri-Score")
print(nom)
print(ingredient)
print(nutriscore)

# url = "https://world.openfoodfacts.org/"
# response = requests.get(url)
# html = response.text

# if response.status_code != 200:
#     print("Erreur :", response.status_code)

# print(type(html))
# soup = BeautifulSoup(html, "html.parser")
# type(soup)

# livre = soup.find("v", class_="viewport")
# print(livre)
# #print(html[:2000]) 


# Test 

# url_2 = "https://world.openfoodfacts.org/product/737628064502/coca-cola"
# response = requests.get(url_2)
# html = response.text
# soup = BeautifulSoup(response.text, "html.parser")
# nom=soup.find("h1", property="food:name")
# ingredient=soup.find("  ")
# # print(nom)
# print(html[:2000]) 

