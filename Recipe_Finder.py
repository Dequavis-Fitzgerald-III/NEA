from tkinter import Tk, Label, Frame, Button, Entry, W, PhotoImage
from tkmacosx import Button as BUTTON
from requests import get
from pprint import pprint
import json

class RecipeFinder:
    """Creates a GUI allowing for account system with login and registration capabilities!"""
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('Recipe Finder')
        self.root.geometry('400x650')
        self.root.config(bg='light blue')
        self.font = ('Times New Roman', 14)
        self.recipe_page_creation()
        
    def recipe_page_creation(self) -> None:
            search_frame = Frame(self.root, bd=2, bg='light blue', padx=0, pady=0)
            self.query_entry = Entry(search_frame, font=self.font)
            self.cuisine_entry = Entry(search_frame, font=self.font)
            self.query_entry.grid(row=0, column=1, pady=5, padx=10)
            self.cuisine_entry.grid(row=1, column=1, pady=5, padx=10)
            enter_btn = BUTTON(search_frame, text='search', bg="Turquoise", font=self.font, command=self.api_call)
            enter_btn.grid(row=3, column=1, pady=10, padx=10)
            search_frame.place(x=0, y=150, width=500, height=225)
            self.place_exit_btn()      

    def api_call(self) -> None:
        url = ("https://api.spoonacular.com/recipes/complexSearch?apiKey=c5d172e74d5e4f40a01fc6f6e824969c") + (f"&query={self.query_entry.get()}") +(f"&cuisine={self.cuisine_entry.get()}")
        r = get(url)
        pprint(r.json())
        
    def clear_root(self) -> None:
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def place_exit_btn(self) -> None:
        exit_btn = BUTTON(self.root, text='EXIT', font=('Times New Roman', 50), bg="Turquoise", command=self.root.destroy)
        exit_btn.place(x=200, y=600, width=200, height=50)
        
if __name__ == "__main__":
    recipe_page = RecipeFinder()
    recipe_page.root.mainloop()