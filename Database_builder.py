import sqlite3

class Database:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("NEA_database.db")
        self.c = self.conn.cursor()
    
    def create_users_table(self) -> None:
        self.c.execute('''CREATE TABLE IF NOT EXISTS Users(
                UserID INT NOT NULL PRIMARY KEY,
                Username TEXT NOT NULL,
                Password TEXT NOT NULL,
                Email Text NOT NULL
            )
        ''')
        self.conn.commit()
    
    def create_recipes_table(self) -> None:
        self.c.execute('''CREATE TABLE IF NOT EXISTS Recipes(
                RecipeID INT NOT NULL PRIMARY KEY,
                Name TEXT NOT NULL,
                Calories INT NOT NULL
            )
        ''')
        self.conn.commit()
    
    def create_pantry_table(self) -> None:
        self.c.execute('''CREATE TABLE IF NOT EXISTS Pantry(
                
            )
        ''')
        