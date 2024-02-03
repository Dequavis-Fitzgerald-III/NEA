"""Pantry system for Foodie Findz app"""
from tkinter import Frame, Button, Entry, messagebox, Label
from sqlite3 import connect
from Clarkes_tkinter import SecondaryWindow
    
class Pantry(SecondaryWindow):
    """Creates a Pantry GUI for the Foodie Findz app!"""
    def __init__(self, home, name: str = "Pantry", screenwidth: int = 400, screenhieght: int = 650) -> None:
        super().__init__(name, screenwidth, screenhieght)
        self.home = home
        try:
            self.current_user = home.account_page.current_user
            self.conn = connect("FoodieFindz_database.db")
            self.c = self.conn.cursor()
            self.populate_window()
        except AttributeError:
            messagebox.showerror('Error', "You must be logged in to use this feature")
            self.window_exit()
        
    def window_exit(self) -> None:
        self.root.destroy()
        self.home.root.deiconify()
        
    def populate_window(self):
        # Frames:
        search_frame = Frame(self.root, bd=2, bg='light blue', padx=0, pady=0)
        pantry_frame = Frame(self.root, bd=2, bg='light blue', padx=0, pady=0)
        
        # Entries:
        self.ingredient_entry = Entry(search_frame, font=self.font)
        self.ingredient_entry.grid(row=0, column=1, pady=5, padx=10)
        
        # buttons:
        enter_btn = Button(search_frame, text='search', bg="Turquoise", font=self.font, command=self.ingredient_search)
        enter_btn.grid(row=1, column=1, pady=10, padx=10)
        for i, row in enumerate(self.c.execute("SELECT Pantry.Name, Pantry.IngredientID FROM Pantry INNER JOIN UserPantry, Users ON Pantry.IngredientID = UserPantry.IngredientID AND UserPantry.UserID = Users.UserID WHERE Users.UserID = ?", [self.current_user[0]])):
            Label(pantry_frame, text=f"{row[0]}", bg='Turquoise', font=self.font).grid(row=i, column=0)
            newbutton = Button(pantry_frame, text='Remove', font=self.font, bg="red", command=lambda:self.remove_ingredient(row[1], row[0]))
            newbutton.grid(row=i, column=1)
        
        #Place:
        search_frame.place(x=0, y=0, width=400, height=325)
        pantry_frame.place(x=0, y=325, width=400, height=325)
        self.place_control_bar()
    
    def ingredient_search(self) -> None:
        for row in self.c.execute("SELECT * FROM Pantry WHERE Name LIKE ? LIMIT 5;", [str("%" + self.ingredient_entry.get() + "%")]):
            correct = messagebox.askyesno('Error', f"Is this the ingredient you were looking for:\n{row[1]}")
            if correct:
                self.c.execute("INSERT INTO UserPantry (UserID, IngredientID) VALUES (:UserID,:IngredientID)",
                  {
                    'UserID': self.current_user[0],
                    'IngredientID': row[0]
                    })
                self.conn.commit()
                self.clear_root()
                self.populate_window()
            else:
                print("no")
        print("none found")
        
    def remove_ingredient(self, ingredientID, name) -> None:
        print(ingredientID, name)
        # self.c.execute("DELETE FROM UserPantry WHERE IngredientID = ? AND UserID = ?", [ingredientID, self.current_user[0]])
        # self.conn.commit()
        self.clear_root()
        self.populate_window()
