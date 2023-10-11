import sqlite3

class Database:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("NEA_database.db")
        self.c = self.conn.cursor()
    
    def create_users_table(self) -> None:
        self.c.execute('''CREATE TABLE IF NOT EXISTS Users(
                UserID INT NOT NULL PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL,
                Password TEXT NOT NULL,
                Email Text NOT NULL
            )
        ''')
        self.conn.commit()
    
    def create_recipes_table(self) -> None:
        self.c.execute('''CREATE TABLE IF NOT EXISTS Recipes(
                RecipeID INT NOT NULL PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Calories INT NOT NULL
            )
        ''')
        self.conn.commit()
    
    def create_pantry_table(self) -> None:
        self.c.execute('''CREATE TABLE IF NOT EXISTS Pantry(
                IngredientID INT NOT NULL PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                
            )
        ''')
        self.conn.commit()
    
    def create_User_Recipes_table(self) -> None:
        self.c.execute('''CREATE TABLE IF NOT EXISTS User-Recipes(
                FOREIGN KEY(UserID) REFERENCES Users(UserID)
                FOREIGN KEY(RecipeID) REFERENCES Recipes(RecipeID)
                PRIMARY KEY (UserID, RecipeID)
            )   
        ''')
        self.conn.commit()
        
    def create_User_Pantry_table(self) -> None:
        self.c.execute('''CREATE TABLE IF NOT EXISTS User-Pantry(
                FOREIGN KEY(UserID) REFERENCES Users(UserID)
                FOREIGN KEY(IngredientID) REFERENCES Pantry(IngredientID)
                PRIMARY KEY (UserID, IngredientID)
            )   
        ''')
        self.conn.commit()
        
