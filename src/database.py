import sqlite3            # pour travailler avec SQLite # pour enregistrer la date du scraping

class DatabaseManager:
    def __init__(self, db_path="database.db"):
        # Connexion à la base SQLite (une seule fois)
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        # On crée la table si elle n'existait pas avant
        self.creer_table()

    # database.py
    def recup_prod(self):
        self.cursor.execute("SELECT * FROM produits") # avec self.cursor.execute : on parle en SQL
        return self.cursor.fetchall()


    def creer_table(self):
        # on crée la table ( 1ère utilisation avec les colonnes nom, nutri-score, ingrédients, date)
        
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS produits (
            nom TEXT NOT NULL,
            nutriscore TEXT,
            ingredients TEXT
        )
        """)

        self.conn.commit()  # on sauvegarde la création de la table

    def insert_produit(self, nom, nutriscore, ingredients):
        # Insertion immédiate d'un produit
        try:
            self.cursor.execute("""
                INSERT INTO produits (
                     nom, nutriscore, ingredients
                ) VALUES (?, ?, ?)
            """, (
                nom,                        
                nutriscore,                
                ingredients))                 
            self.conn.commit()  # on sauvegarde l'ajout du noveau produit
        except sqlite3.IntegrityError:
            # pour éviter les doublons
            pass

    def close(self):
        #Fermeture propre de la base
        self.conn.close()
