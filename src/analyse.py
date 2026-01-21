import sqlite3
import pandas as pd
from database import Database


# db = Database("data/database.db")  # ouvre la base
# List=db.get_all_produits() # On récupère toutes les infos
# db.close()  # fermeture propre

df = pd.read_sql_query('''SELECT * FROM produit''', con=sqlite3)



#analyse 1 
# for el in 

if __name__ == "__main__":
    print(df.head(10))