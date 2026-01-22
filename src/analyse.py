import sqlite3
import pandas as pd


# Connexion et chargement
conn = sqlite3.connect('data/database.db')
df = pd.read_sql_query("SELECT * FROM produits", conn)
conn.close()

# On transforme la colonne ingredients en une liste
df['ingredients'] = df['ingredients'].str.split(',')
