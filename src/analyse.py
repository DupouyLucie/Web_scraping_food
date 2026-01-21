import sqlite3
import pandas as pd
from database import Database


db = Database("data/database.db")  # ouvre la base
List=db.get_all_produits() # On récupère toutes les infos
db.close()  # fermeture propre

if __name__ == "__main__":
    print(List)

