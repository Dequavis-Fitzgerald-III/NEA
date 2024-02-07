"""Pantry system for Foodie Findz app"""
from tkinter import Frame, Button, Entry, messagebox, Label
from sqlite3 import connect
from Clarkes_tkinter import SecondaryWindow
from PIL import ImageTk, Image
    
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
        except AttributeError or TypeError:
            messagebox.showerror('Error', "You must be logged in to use this feature")
            self.window_exit()
        
    def window_exit(self) -> None:
        self.root.destroy()
        self.home.root.deiconify()
        
    def populate_window(self):
        self.home_pic = ImageTk.PhotoImage(Image.open('VisualAssets/pantry_picture.png').resize((395,250)))
        pantry_font = ('Times New Roman', int(650/29))
        title_label = Label(self.root, text="Pantry", bg='Light gray', font=('Times New Roman', 50))
        title_label.place(x=0, y=0, width=400, height=65)
        Label(self.root, image=self.home_pic).place(x=0, y=65)
        # Frames:
        search_frame = Frame(self.root, bd=2, bg='light gray', padx=0, pady=0)
        pantry_frame = Frame(self.root, bd=2, bg='light blue', padx=0, pady=0)
        
        # Entries:
        self.ingredient_entry = Entry(search_frame, font=pantry_font)
        self.ingredient_entry.grid(row=0, column=0, pady=5, padx=10)
        
        # buttons:
        enter_btn = Button(search_frame, text='search', bg="Turquoise", font=pantry_font, command=self.ingredient_search)
        enter_btn.grid(row=0, column=1, pady=10, padx=10)
        for i, row in enumerate(self.c.execute("SELECT Pantry.Name, Pantry.IngredientID FROM Pantry INNER JOIN UserPantry, Users ON Pantry.IngredientID = UserPantry.IngredientID AND UserPantry.UserID = Users.UserID WHERE Users.UserID = ?", [self.current_user[0]])):
            Label(pantry_frame, text=f"{row[0]}", bg='Turquoise', font=pantry_font).grid(row=i, column=0)
            new_button = Button(pantry_frame, text=f'Remove {row[0]}', font=pantry_font, bg="red", command=lambda:self.remove_ingredient(row[1]))
            new_button.grid(row=i, column=1)
            
        #Place:
        search_frame.place(x=0, y=315, width=400, height=50)
        pantry_frame.place(x=0, y=365, width=400, height=285)
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
        
    def remove_ingredient(self, ingredientID) -> None:
        self.c.execute("DELETE FROM UserPantry WHERE IngredientID = ? AND UserID = ?", [ingredientID, self.current_user[0]])
        self.conn.commit()
        self.clear_root()
        self.populate_window()
