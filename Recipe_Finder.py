"""recipe searching for Foodie Findz app"""

from tkinter import Label, Frame, Button, Entry, CENTER
from requests import get
from pprint import pprint
from json import dumps, load
from PIL import ImageTk, Image
from io import BytesIO
from Clarkes_tkinter import SecondaryWindow

class APIError(Exception):
    pass 

class RecipeFinder:
    def __init__(self, home) -> None:
        self.API = API(self)
        self.home = home
    
    def create_page(self) -> None:
        self.page = RecipeFinderPage(self)

class RecipeFinderPage(SecondaryWindow):
    """Creates a GUI that connects to a Spoonacular API to recieve recipes and information."""
    def __init__(self, recipe_finder, name: str = "Recipe Page", screenwidth: int = 400, screenhieght: int = 650) -> None:
        super().__init__(name, screenwidth, screenhieght)
        self.recipe_finder = recipe_finder
        self.populate_window()
        
    def populate_window(self) -> None:
        """Creates all widgets for the recipe page GUI"""
        search_frame = Frame(self.root, bd=2, bg='light blue', padx=0, pady=0)
        self.query_entry = Entry(search_frame, font=self.font)
        self.cuisine_entry = Entry(search_frame, font=self.font)
        self.ingredients_entry = Entry(search_frame, font=self.font)
        self.query_entry.grid(row=0, column=1, pady=5, padx=10)
        self.cuisine_entry.grid(row=1, column=1, pady=5, padx=10)
        self.ingredients_entry.grid(row=2, column=1, pady=5, padx=10)
        enter_btn = Button(search_frame, text='search', bg="Turquoise", font=self.font, command=self.recipe_finder.API.search)
        enter_btn.grid(row=3, column=1, pady=10, padx=10)
        search_frame.place(x=0, y=150, width=500, height=225)
        self.place_control_bar()   

    def visualise(self, data) -> None:
        """Visualizes results returned from a Spoonacular API request"""
        self.clear_root()
        parsed_image = Image.open(BytesIO(data[1].content)).resize((400,225))
        self.image = ImageTk.PhotoImage(parsed_image)
        image_frame = Frame(self.root, bg='light blue')
        Label(image_frame, image=self.image).pack()
        image_frame.place(x=-2.5, y=-2.5, width=400, height=225)
        steps_frame = Frame(self.root, bg='light blue')
        text_label = Label(steps_frame, text=f"Ingredients: {data[2]}\nInstructions:\n{data[0]}\nServes: {data[3]}", font=self.font, wraplength=380, bg='white')
        text_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        steps_frame.place(x=0, y=225, width=400, height=425)  

class API:
    """connects to the Spoonacular API to search for and parse data on recipes."""
    def __init__(self, recipe_finder) -> None:
        self.API_KEY = "c5d172e74d5e4f40a01fc6f6e824969c"
        self.recipe_finder = recipe_finder
    
    # searches:
    def search(self) -> None:
       response = self.query_search()
       response_id = self.recipe_parse(response)
       data = self.ID_parse(self.ID_search(response_id))
       self.recipe_finder.page.visualise(data)
    
    def get_random_recipes_data(self) -> list:
        return(self.random_parse(self.random(2)))
        
    # API calls:
    def query_search(self) -> dict:
        """Returns a dictionary containing multiple results from a query of search criteria retrieved from the recipe page's entry boxes"""
        url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={self.API_KEY}&query={self.recipe_finder.page.query_entry.get()}&cuisine={self.recipe_finder.page.cuisine_entry.get()}&includeIngredients={self.recipe_finder.page.ingredients_entry.get()}"
        return(get(url).json())
    
    def ID_search(self, ID) -> dict:
        """Returns a dictionary containing the recipe data of the recipe who's ID has been passed in"""
        url = f"https://api.spoonacular.com/recipes/{ID}/information?apiKey={self.API_KEY}"
        return(get(url).json())
    
    def random(self, number) -> dict:
        """returns a dictionary containing multiple randoms recipes"""
        url = f"https://api.spoonacular.com/recipes/random?apiKey={self.API_KEY}&number={number}"
        return(get(url).json())
        
    # parses:
    def recipe_parse(self, r) -> int:
        recipes = r["results"]
        for i, recipe in enumerate(recipes):
            if i == 1:
                return(recipe["id"])
    
    def ID_parse(self, r) -> list:
        steps = r["analyzedInstructions"][0]["steps"]
        steps_string = ""
        for i, step in enumerate(steps):
            steps_string += f"{i+1}){step['step']} \n"
        image = get(r['image'])
        ingredients = [[ingredient["name"], ingredient["measures"]["metric"]["amount"], ingredient["measures"]["metric"]["unitShort"]] for ingredient in r["extendedIngredients"]]
        ingredients = set([f"{ingredient[0]}: {round(ingredient[1], 1)}{ingredient[2]}" for ingredient in ingredients])
        ingredients_string = ""
        for i, ingredient in enumerate(ingredients):
            if i == len(ingredients) - 1:
                ingredients_string += f"{ingredient}.\n"
            else:
                ingredients_string += f"{ingredient}, "
        servings = r["servings"]
        data = [steps_string, image, ingredients_string, servings]
        return data
        
    def random_parse(self, r) -> list:
        data = []
        for i in range(2):
            name = r['recipes'][i]['title']
            ID = r['recipes'][i]['id']
            image_url = get(r['recipes'][i]['image'])
            data.append([name, ID, image_url])
        return data

    def status_check(self,r) -> bool:
        if r['status'] == 'failure':
            raise APIError("ran out of API points!")

    
        
if __name__ == "__main__":
    recipe_finder = RecipeFinder()
    recipe_finder.create_page()
    recipe_finder.page.root.mainloop()