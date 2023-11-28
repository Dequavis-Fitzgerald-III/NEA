from tkinter import Tk, Label, Frame, Button, Entry, W, PhotoImage, S, CENTER
from requests import get
from pprint import pprint
from json import dumps, load
from PIL import ImageTk, Image
from io import BytesIO
from Clarkes_tkinter import Window

class RecipeFinder(Window):
    """Creates a GUI that connects to a Spoonacular API to recieve recipes and information."""
    def __init__(self, name: str = "Recipe Page", screenwidth: int = 400, screenhieght: int = 650) -> None:
        super().__init__(name, screenwidth, screenhieght)
        self.API = API(self)
        self.populate_window()
        
    def populate_window(self) -> None:
        """Creates all widgets for the reciope page GUI"""
        search_frame = Frame(self.root, bd=2, bg='light blue', padx=0, pady=0)
        self.query_entry = Entry(search_frame, font=self.font)
        self.cuisine_entry = Entry(search_frame, font=self.font)
        self.ingredients_entry = Entry(search_frame, font=self.font)
        self.query_entry.grid(row=0, column=1, pady=5, padx=10)
        self.cuisine_entry.grid(row=1, column=1, pady=5, padx=10)
        self.ingredients_entry.grid(row=2, column=1, pady=5, padx=10)
        enter_btn = Button(search_frame, text='search', bg="Turquoise", font=self.font, command=self.API.query_search)
        enter_btn.grid(row=3, column=1, pady=10, padx=10)
        search_frame.place(x=0, y=150, width=500, height=225)
        self.place_exit_btn()   
    
    def visualise(self, url, steps_string) -> None:
        """Visualizes results returned from a Spoonacular API request"""
        self.clear_root()
        parsed_image = Image.open(BytesIO(url.content)).resize((400,225))
        self.image = ImageTk.PhotoImage(parsed_image)
        image_frame = Frame(self.root, bg='light blue')
        Label(image_frame, image=self.image).pack()
        image_frame.place(x=-2.5, y=-2.5, width=400, height=225)
        steps_frame = Frame(self.root, bg='light blue')
        text_label = Label(steps_frame, text=steps_string, font=self.font, wraplength=380, bg='white')
        text_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        steps_frame.place(x=0, y=225, width=400, height=425)

class API:
    """connects to the Spoonacular API to search for and parse data on recipes."""
    def __init__(self, recipe_page) -> None:
        self.API_KEY = "c5d172e74d5e4f40a01fc6f6e824969c"
        self.recipe_page = recipe_page
    
    # searches:
    def query_search(self) -> None:
        url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={self.API_KEY}&query={self.recipe_page.query_entry.get()}&cuisine={self.recipe_page.cuisine_entry.get()}&includeIngredients={self.recipe_page.ingredients_entry.get()}"
        r = get(url)
        self.recipe_parse(r.json())
    
    def ID_search(self, ID) -> None:
        url = f"https://api.spoonacular.com/recipes/{ID}/information?apiKey={self.API_KEY}"
        r = get(url)
        self.ID_parse(r.json())
        
    # parses:
    def recipe_parse(self, r) -> None:
        recipes = r["results"]
        for i, recipe in enumerate(recipes):
            if i == 1:
                self.ID_search(recipe["id"])
    
    def ID_parse(self, r) -> None:
        print(f"{r['title']}:")
        steps = r["analyzedInstructions"][0]["steps"]
        steps_string = ""
        for i, step in enumerate(steps):
            steps_string += f"{i+1}){step['step']} \n"
        print(r['image'])
        url = get(r['image'])
        self.recipe_page.visualise(url, steps_string)
    
        
if __name__ == "__main__":
    recipe_page = RecipeFinder()
    recipe_page.root.mainloop()