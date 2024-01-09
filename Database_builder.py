from sqlite3 import connect

class Database:
    def __init__(self) -> None:
        self.conn = connect("FoodieFindz_database.db")
        self.c = self.conn.cursor()
    
    def create_users_table(self) -> None:
        self.c.execute('''CREATE TABLE IF NOT EXISTS Users(
                UserID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL,
                Password TEXT NOT NULL,
                Email Text NOT NULL
            )
        ''')
        self.conn.commit()
    
    def create_cookbook_table(self) -> None:
        self.c.execute('''CREATE TABLE IF NOT EXISTS Cookbook(
                RecipeID INT NOT NULL PRIMARY KEY,
                Name TEXT NOT NULL
            )
        ''')
        self.conn.commit()
    
    def create_pantry_table(self) -> None:
        self.c.execute('''CREATE TABLE IF NOT EXISTS Pantry(
                IngredientID INT NOT NULL PRIMARY KEY,
                Name TEXT NOT NULL
            )
        ''')
        self.conn.commit()
    
    def create_User_Cookbook_table(self) -> None:
        self.c.execute('''CREATE TABLE IF NOT EXISTS UserCookbook(
                UserID int,
                RecipeID int,
                FOREIGN KEY (UserID) REFERENCES Users(UserID)
                FOREIGN KEY (RecipeID) REFERENCES Cookbook(RecipeID)
                PRIMARY KEY (UserID, RecipeID)
            )   
        ''')
        self.conn.commit()
        
    def create_User_Pantry_table(self) -> None:
        self.c.execute('''CREATE TABLE IF NOT EXISTS UserPantry(
                UserID int,
                IngredientID int,
                FOREIGN KEY (UserID) REFERENCES Users(UserID)
                FOREIGN KEY (IngredientID) REFERENCES Pantry(IngredientID)
                PRIMARY KEY (UserID, IngredientID)
            )   
        ''')
        self.conn.commit()
        
if __name__ == "__main__":
    database = Database()
    database.create_User_Cookbook_table()
    database.create_User_Pantry_table()
    