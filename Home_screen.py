"""Home screen for Foodie Findz app"""

from tkinter import Label, Frame, Button, CENTER
from PIL import ImageTk, Image
from io import BytesIO
from Recipe_Finder import RecipeFinder, APIError
from Account_System import AccountSystem
from Pantry import Pantry
from Clarkes_tkinter import ResizableWindow

class HomePage(ResizableWindow):
    """Creates a GUI system for the Foodie Findz APP (prototype)"""
    def __init__(self, name: str = "Home Page", screenwidth: int = 400, screenhieght: int = 650) -> None:
        super().__init__(name, screenwidth, screenhieght)
        # creates a recipe finder class so that the API can be used to get random recipes.
        self.recipe_finder = RecipeFinder(self)
        self.API = self.recipe_finder.API
        # stores the random recipe data collected from calling the get_random_recipes_data() method into a list attribute
        self.random_recipes_data = self.API.get_random_recipes_data()
        
    def populate_window(self) -> None:
            """Creates all widgets for the home page GUI"""
            # images:
            # creates tkinter photoimages. All are resized to proportional size compared to the window:
            self.home_pic = ImageTk.PhotoImage(Image.open('VisualAssets/home_picture.png').resize((self.screenwidth,int(5*self.screenheight/13))))
            self.menu_icon = ImageTk.PhotoImage(Image.open('VisualAssets/menu_icon.png').resize((int(self.screenwidth/8),int(self.screenwidth/8))))
            self.search_icon = ImageTk.PhotoImage(Image.open('VisualAssets/search_icon.png').resize((int(self.screenwidth/8),int(self.screenwidth/8))))
            self.random_recipe1_img = Image.open(BytesIO(self.random_recipes_data[0][2].content)).resize(((int(7*self.screenwidth/20)),int((2*((7*self.screenheight/13)-25)/6))))
            self.random_recipe1_img = ImageTk.PhotoImage(self.random_recipe1_img)
            self.random_recipe2_img = Image.open(BytesIO(self.random_recipes_data[1][2].content)).resize(((int(7*self.screenwidth/20)),int((2*((7*self.screenheight/13)-25)/6))))
            self.random_recipe2_img = ImageTk.PhotoImage(self.random_recipe2_img)
            
            #Frames:
            # holds image and the menu/search buttons
            home_frame = Frame(self.root, bg='light blue')
            home_frame.place(x=0, y=0, width=self.screenwidth, height=(5*self.screenheight/13))
            
            # holds all home screen buttons
            functions_frame = Frame(self.root, bg='purple')
            functions_frame.place(x=0, y=(5*self.screenheight/13), width=self.screenwidth, height=(self.screenheight/13))
            
            # holds the random recipe pictures and descriptions
            random_recipes_frame = Frame(self.root, bg='Turquoise')
            random_recipes_frame.place(x=0, y=(6*self.screenheight/13), width=self.screenwidth, height=((7*self.screenheight/13)-25))

            #pictures:
            Label(home_frame, image=self.home_pic).pack()

            # Text for random recipes section:
            title = Label(random_recipes_frame, text="Why Not Try!:", font=self.font, bg="light blue")
            title.place(relx=0.5, rely=0.05, anchor=CENTER)
            
            random_recipe1_text = Label(random_recipes_frame, text=f"{self.random_recipes_data[0][0]} TRY IT!", font=self.font, wraplength=((7*self.screenwidth/20)-20), bg="light blue")
            random_recipe1_text.place(relx=5/8, rely=3/10, anchor=CENTER, width=(7*self.screenwidth/20), height=(2*((7*self.screenheight/13)-25)/6))
            
            random_recipe2_text = Label(random_recipes_frame, text=f"{self.random_recipes_data[1][0]} TRY IT!", font=self.font, wraplength=((7*self.screenwidth/20)-20), bg="light blue")
            random_recipe2_text.place(relx=3/8, rely=7/10, anchor=CENTER, width=(7*self.screenwidth/20), height=(2*((7*self.screenheight/13)-25)/6))
            
            # buttons:
            menu_btn = Button(self.root, image=self.menu_icon, command=self.menu)
            menu_btn.place(x=0, y=0, width=(self.screenwidth/8), height=(self.screenwidth/8))
            
            search_btn = Button(self.root, image=self.search_icon, command=self.search)
            search_btn.place(x=(self.screenwidth-self.screenwidth/8), y=0, width=(self.screenwidth/8), height=(self.screenwidth/8))
            
            acounts_btn = Button(functions_frame, text='accounts', font=('Verdana', int(self.screenheight/24)), bg="Turquoise", command=self.account)
            acounts_btn.place(relx=1/6, rely=0.5, anchor=CENTER)
            
            recipe_btn = Button(functions_frame, text='recipe', font=('Verdana', int(self.screenheight/24)), bg="Turquoise", command=self.recipe)
            recipe_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
        
            pantry_btn = Button(functions_frame, text='Pantry', font=('Verdana', int(self.screenheight/24)), bg="Turquoise", command=self.pantry)
            pantry_btn.place(relx=5/6, rely=0.5, anchor=CENTER)
            
            random_recipe1_btn= Button(random_recipes_frame, image=self.random_recipe1_img, command=lambda:self.random(0))
            random_recipe1_btn.place(relx=2/8, rely=3/10, anchor=CENTER, width=(7*self.screenwidth/20), height=(2*((7*self.screenheight/13)-25)/6))
            
            random_recipe2_btn= Button(random_recipes_frame, image=self.random_recipe2_img, command=lambda:self.random(1))
            random_recipe2_btn.place(relx=6/8, rely=7/10, anchor=CENTER, width=(7*self.screenwidth/20), height=(2*((7*self.screenheight/13)-25)/6))
        
            self.place_control_bar()
            
    def menu(self) -> None:
        """opens the menu bar at the top left of the home page"""
        # creates a menu frame
        menu_frame = Frame(self.root, bg='magenta')
        menu_frame.place(x=0, y=0, width=(2*self.screenwidth/6), height=(7*self.screenheight/15))
        
        # place the title frame to add a title and exit button to close the menu
        title_frame = Frame(menu_frame, bg= 'pink')
        title_frame.place(x=0, y=0, width=(2*self.screenwidth/6), height=(self.screenheight/15))
        title_label = Label(title_frame, text="Menu", bg='pink', font=('Verdana', int(self.screenheight/30)))
        title_label.place(relx=0.6, rely=0.5, anchor=CENTER)
        exit_btn = Button(title_frame, text='X', font=('Verdana', int(self.screenheight/30)), bg="pink", command=menu_frame.destroy)
        exit_btn.place(relx=0.2, rely=0.5, anchor=CENTER, width=self.screenheight/20, height=self.screenheight/20)
        
        # places all the buttons for fucntionality in the menu frame
        recipes_button = Button(menu_frame, text='Find recipes', font=self.font, bg="magenta", command=self.recipe)
        recipes_button.place(x=0, y=(self.screenheight/15), width=(2*self.screenwidth/6), height=(2*self.screenheight/15))
        recipes_button = Button(menu_frame, text='more options', font=self.font, bg="magenta", command=lambda: print("more options"))
        recipes_button.place(x=0, y=(self.screenheight/5), width=(2*self.screenwidth/6), height=(2*self.screenheight/15))
        accounts_button = Button(menu_frame, text='Account', font=self.font, bg="magenta", command=self.account)
        accounts_button.place(x=0, y=(self.screenheight/3), width=(2*self.screenwidth/6), height=(self.screenheight/15))
        settings_button = Button(menu_frame, text='Settings', font=self.font, bg="magenta", command=lambda: print("settings"))
        settings_button.place(x=0, y=(2*self.screenheight/5), width=(2*self.screenwidth/6), height=(self.screenheight/15))
        
    def search(self) -> None:
        """Opens the search bar at the top of the home page"""
        print("open search bar")
        
    def account(self) -> None:
        """Opens the accounts system"""
        # Uses .withdraw() to hide the home page window instead of deleting it, allowing it to be reopened
        self.root.withdraw()
        self.account_page = AccountSystem(self)
        
    def recipe(self) -> None:
        """Opens the recipe system"""
        # Uses .withdraw() to hide the home page window instead of deleting it, allowing it to be reopened
        self.root.withdraw()
        self.recipe_finder.create_page()
    
    def pantry(self) -> None:
        # Uses .withdraw() to hide the home page window instead of deleting it, allowing it to be reopened
        self.root.withdraw()
        self.pantry = Pantry(self)
            
    def random(self, num) -> None:
        """Opens the recipe system onto the visualisation of the selected random recipe"""
        # Uses .withdraw() to hide the home page window instead of deleting it, allowing it to be reopened
        self.root.withdraw()
        self.recipe_finder.create_page()
        # Searches and parses the ID of the random recipe (collected from the random_recipes_data list)
        # the num variable holds a integer value donoting whether the 1st or 2nd random recipe was pressed
        data = self.API.ID_parse(self.API.ID_search(self.random_recipes_data[num][1]))
        # visualises this data on the rcipe page
        self.recipe_finder.page.visualise(data)

if __name__ == "__main__":
    home_page = HomePage()
    home_page.root.mainloop()