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
        # uses a try and except block - users who are not logged into an account are sent back to the home screen with a prompt that they need to log in
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
        """Creates all widgets for the pantry page GUI."""
        # resizes the image to place on top of the screen
        self.pantry_pic = ImageTk.PhotoImage(Image.open('VisualAssets/pantry_picture.png').resize((395,250)))
        pantry_font = ('Times New Roman', int(650/29))
        # places a title at the top of the screen
        title_label = Label(self.root, text="Pantry", bg='Light gray', font=('Times New Roman', 50))
        title_label.place(x=0, y=0, width=400, height=65)
        Label(self.root, image=self.pantry_pic).place(x=0, y=65)
        # Frames:
        # stores the entry box that allows the user to find ingredients to add to their pantry
        search_frame = Frame(self.root, bd=2, bg='light gray', padx=0, pady=0)
        # stores the pantry ingredients - displaying to the user what ingredients they have and allowing them to be removed
        pantry_frame = Frame(self.root, bd=2, bg='light gray', padx=0, pady=0)
        
        # Entries:
        self.ingredient_entry = Entry(search_frame, font=pantry_font)
        self.ingredient_entry.grid(row=0, column=0, pady=5, padx=10)
        
        # buttons:
        enter_btn = Button(search_frame, text='search', bg="Turquoise", font=pantry_font, command=self.add_ingredient)
        enter_btn.grid(row=0, column=1, pady=10, padx=10)
        
        # searches the database for what is in the pantry of the current user
        # iterates through the results creating buttons to place on the screen
        num_of_ingredients = 0
        for i, row in enumerate(self.c.execute("SELECT Pantry.Name, Pantry.IngredientID FROM Pantry INNER JOIN UserPantry, Users ON Pantry.IngredientID = UserPantry.IngredientID AND UserPantry.UserID = Users.UserID WHERE Users.UserID = ?", [self.current_user[0]])):
            # uses the name to create a label and grids it onto the screen
            Label(pantry_frame, text=f"{row[0]}", bg='light gray', font=pantry_font).grid(row=i, column=0)
            # creates a button to remove the ingredient and grids it to the screen.
            # this button calls the remove_ingredient method which takes in an ingredient ID and removes it from the current user's pantry
            new_button = Button(pantry_frame, text=f'Remove', font=pantry_font, bg="red", width = 10, command=lambda:self.remove_ingredient(row[1]))
            new_button.grid(row=i, column=1)
            num_of_ingredients += 1
            
        #Place:
        search_frame.place(x=0, y=340, width=400, height=50)
        pantry_frame.place(x=0, y=390, width=400, height=num_of_ingredients * 35)
        self.place_control_bar()
    
    def add_ingredient(self) -> None:
        """Adds an ingredient to the current user's pantry"""
        # finds ingredients that match the user's search
        # uses the SQL LIKE operater to get items that are similair to the search
        for row in self.c.execute("SELECT * FROM Pantry WHERE Name LIKE ?;", [str("%" + self.ingredient_entry.get() + "%")]):
            # uses a yes or no message box to assetain whether the ingredient that the user was using for has been found
            correct = messagebox.askyesno('Error', f"Is this the ingredient you were looking for:\n{row[1]}")
            if correct:
                # if the correct ingredient is found it is added to the user's pantry
                self.c.execute("INSERT INTO UserPantry (UserID, IngredientID) VALUES (:UserID,:IngredientID)",
                  {
                    'UserID': self.current_user[0],
                    'IngredientID': row[0]
                    })
                self.conn.commit()
                # window is updated to show the change
                self.clear_root()
                self.populate_window()
        print("none found")
        
    def remove_ingredient(self, ingredientID) -> None:
        """Removes an ingredient from the current user's pantry.

        Args:
            ingredientID (str): the ID of the ingredient to be deleted
        """
        # deletes the ingredient (given by the ID paramater) from the current user's pantry
        self.c.execute("DELETE FROM UserPantry WHERE IngredientID = ? AND UserID = ?", [ingredientID, self.current_user[0]])
        self.conn.commit()
        # updates the window to show the change
        self.clear_root()
        self.populate_window()
