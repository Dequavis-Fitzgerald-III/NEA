"""recipe searching for Foodie Findz app"""

from tkinter import Label, Frame, Button, Entry, CENTER, scrolledtext, END, WORD, messagebox
from requests import get
from json import JSONDecodeError
from PIL import ImageTk, Image
from io import BytesIO
from Clarkes_tkinter import SecondaryWindow

class APIError(Exception):
    pass 

class RecipeFinder:
    def __init__(self, home) -> None:
        # creates a virtual class
        self.API = API(self)
        self.home = home
    
    def create_page(self) -> None:
        """Creates a recipe page window."""
        self.page = RecipeFinderPage(self)

class RecipeFinderPage(SecondaryWindow):
    """Creates a GUI that connects to a Spoonacular API to recieve recipes and information."""
    def __init__(self, recipe_finder: RecipeFinder, name: str = "Recipe Page", screenwidth: int = 400, screenhieght: int = 650) -> None:
        super().__init__(name, screenwidth, screenhieght)
        self.recipe_finder = recipe_finder
        self.populate_window()
        
    def populate_window(self) -> None:
        """Creates all widgets for the recipe page GUI."""
        self.home_pic = ImageTk.PhotoImage(Image.open('VisualAssets/home_picture.png').resize((395,250)))
        recipe_font = ('Times New Roman', int(650/29))
        title_label = Label(self.root, text="Enter search criteria", bg='Light gray', font=('Times New Roman', 50))
        title_label.place(x=0, y=0, width=400, height=65)
        Label(self.root, image=self.home_pic).place(x=0, y=65)
        search_frame = Frame(self.root, bg='light gray')
        Label(search_frame, text="Enter query", bg='light gray', font=recipe_font).grid(row=0, column=0)
        Label(search_frame, text="Enter cuisine", bg='light gray', font=recipe_font).grid(row=1, column=0)
        Label(search_frame, text="Enter ingredients", bg='light gray', font=recipe_font).grid(row=2, column=0)
        self.query_entry = Entry(search_frame, font=recipe_font)
        self.query_entry.grid(row=0, column=1)
        self.cuisine_entry = Entry(search_frame, font=recipe_font)
        self.cuisine_entry.grid(row=1, column=1)
        self.ingredients_entry = Entry(search_frame, font=recipe_font)
        self.ingredients_entry.grid(row=2, column=1)
        Button(search_frame, text='enter', bg="Turquoise", font=recipe_font, command=self.recipe_finder.API.search).grid(row=3, column=1)
        search_frame.place(x=0, y=340, width=400, height=160)
        self.place_control_bar()

    def visualise(self, data) -> None:
        """Visualizes results returned from a Spoonacular API request."""
        self.clear_root()
        recipe_info_text = f"Ingredients:\n{data[2]}\nInstructions:\n{data[0]}\nServes: {data[3]}"
        # resizes image and makes it a type usable by tkinter
        parsed_image = Image.open(BytesIO(data[1].content)).resize((400,225))
        self.image = ImageTk.PhotoImage(parsed_image)
        # creates and populates frames and labels
        image_frame = Frame(self.root, bg='light blue')
        Label(image_frame, image=self.image).pack()
        image_frame.place(x=-2.5, y=-2.5, width=400, height=225)
        steps_frame = Frame(self.root, bg='light blue')
        # formats text onto the page
        text_label = scrolledtext.ScrolledText(steps_frame, font=self.font, wrap=WORD, bg='white')
        text_label.insert(END, recipe_info_text)
        text_label.place(relx=0.5, rely=0.5, anchor=CENTER, width = 380)
        steps_frame.place(x=0, y=225, width=400, height=425)  

class API:
    """connects to the Spoonacular API to search for and parse data on recipes."""
    def __init__(self, recipe_finder: RecipeFinder) -> None:
        self.API_KEY = "c5d172e74d5e4f40a01fc6f6e824969c"
        self.recipe_finder = recipe_finder
    
    # searches:
    def search(self) -> None:
        """Makes a Spoonacular API search using given search criteria (from recipe page inputs) and visualises them on the recipe page."""
        try:
            response = self.query_search()
            response_id = self.recipe_parse(response)
            data = self.ID_parse(self.ID_search(response_id))
            self.recipe_finder.page.visualise(data)
        except JSONDecodeError:
            messagebox.showerror('Error', "NO RESULTS FOUND")
            self.recipe_finder.page.clear_root()
            self.recipe_finder.page.populate_window()
            
    
    def get_random_recipes_data(self) -> list:
        """Finds and parses 2 random recipes from the spoonacular API.

        Returns:
            list: The parsed data (includes: name, ID and image for each recipe).
        """
        return(self.random_parse(self.random(2)))
        
    # API calls:
    def query_search(self) -> dict:
        """Performs a query of search criteria retrieved from the recipe page's entry boxes.

        Returns:
            dict: a json dictionary containing the responses from the search.
        """
        url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={self.API_KEY}&query={self.recipe_finder.page.query_entry.get()}&cuisine={self.recipe_finder.page.cuisine_entry.get()}&includeIngredients={self.recipe_finder.page.ingredients_entry.get()}"
        return(get(url).json())
    
    def ID_search(self, ID: int) -> dict:
        """API call to ellaborate on a given recipe, retrieving more information.

        Args:
            ID (int): the ID of the recipe to be searched.

        Returns:
            dict: a json dictionary containing the response from the search.
        """
        url = f"https://api.spoonacular.com/recipes/{ID}/information?apiKey={self.API_KEY}"
        return(get(url).json())
    
    def random(self, number: int) -> dict:
        """Performs a an API call to retrive data on random recipes.

        Args:
            number (int): the amount of random recipes the users wants returned.

        Returns:
            dict: a json dictionary containing the responses from the search.
        """
        url = f"https://api.spoonacular.com/recipes/random?apiKey={self.API_KEY}&number={number}"
        return(get(url).json())
        
    # parses:
    def recipe_parse(self, r: dict) -> int:
        """Parses the results from a query search to retrieve the ID.

        Args:
            r (dict): a json dictionary containing the responses from a query search.

        Returns:
            int: the IDs of the recipes. 
        """
        recipes = r["results"]
        for i, recipe in enumerate(recipes):
            if i == 1:
                return(recipe["id"])
    
    def ID_parse(self, r: dict) -> list:
        """Condenses the response from an ID search to a simplified list.

        Args:
            r (dict): a json dictionary containing the response from an ID search.

        Returns:
            list: a simplified list of the data from the recipe.
        """
        # Steps:
        steps_list = r["analyzedInstructions"][0]["steps"]
        steps: str = ""
        # iterates through the list of steps formatting them into a string that can be visualised.
        for i, step in enumerate(steps_list):
            steps += f"{i+1}){step['step']} \n"
        # Image (returned as a response to be parsed later):
        image = get(r['image'])
        # Ingredients:
        # creates a 2 dimensional list of ingredients including the name of the ingredient as well as both the amount and metric used for the amount.
        ingredients_list = [[ingredient["name"], ingredient["measures"]["metric"]["amount"], ingredient["measures"]["metric"]["unitShort"]] for ingredient in r["extendedIngredients"]]
        # creats a set to remove duplicates, also rounds the amount to remove unnecasarely long numbers.
        ingredients_list = set([f"{ingredient[0]}: {round(ingredient[1], 1)}{ingredient[2]}" for ingredient in ingredients_list])
        ingredients: str = ""
        # iterates through the ingredients set formating them into a string that can be visualised.
        for i, ingredient in enumerate(ingredients_list):
            if i == len(ingredients_list) - 1:
                ingredients += f"{ingredient}.\n"
            else:
                ingredients += f"{ingredient}, "
        # Servings:
        servings: int = r["servings"]
        data = [steps, image, ingredients, servings]
        return data
        
    def random_parse(self, r:dict) -> list:
        """Iterates through random recipes getting out important information.

        Args:
            r (dict): a json dictionary containing the responses from a random search.

        Returns:
            list: a simplified list of the data from the recipe.
        """
        data = []
        for i in range(2):
            name: str = r['recipes'][i]['title']
            ID: int = r['recipes'][i]['id']
            image_url = get(r['recipes'][i]['image'])
            data.append([name, ID, image_url])
        return data

    def status_check(self,r:dict) -> bool:
        if r['status'] == 'failure':
            raise APIError("ran out of API points!")