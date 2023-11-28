"""Home screen for Foodie Findz app"""

from tkinter import Label, Frame, Button, CENTER
from PIL import ImageTk, Image
from Recipe_Finder import RecipeFinder
from Account_System import AccountSystem
from Clarkes_tkinter import Window

class HomePage(Window):
    """Creates a GUI system for the Foodie Findz APP (prototype)"""
    def __init__(self, name: str = "Home Page", screenwidth: int = 400, screenhieght: int = 650) -> None:
        super().__init__(name, screenwidth, screenhieght)
        self.home_pic = ImageTk.PhotoImage(Image.open('VisualAssets/home_picture.png').resize((self.screenwidth,int(5*self.screenheight/13))))
        self.menu_icon = ImageTk.PhotoImage(Image.open('VisualAssets/menu_icon.png').resize((int(self.screenwidth/8),int(self.screenwidth/8))))
        self.search_icon = ImageTk.PhotoImage(Image.open('VisualAssets/search_icon.png').resize((int(self.screenwidth/8),int(self.screenwidth/8))))
        self.populate_window()
        
    def populate_window(self) -> None:
            """Creates all widgets for the home page GUI"""
            #Frames:
            home_frame = Frame(self.root, bg='light blue')
            home_frame.place(x=0, y=0, width=self.screenwidth, height=(5*self.screenheight/13))
            
            functions_frame = Frame(self.root, bg='purple')
            functions_frame.place(x=0, y=(5*self.screenheight/13), width=self.screenwidth, height=(self.screenheight/13))
            
            random_recipes_frame = Frame(self.root, bg='light blue')
            random_recipes_frame.place(x=0, y=(6*self.screenheight/13), width=self.screenwidth, height=((7*self.screenheight/13)-25))

            control_bar_frame = Frame(self.root, bg='red')
            control_bar_frame.place(x=0, y=self.screenheight-25, width=self.screenwidth, height=25)

            #pictures:
            Label(home_frame, image=self.home_pic).pack()

            # Text:
            title = Label(random_recipes_frame, text="Why Not Try!:", font=self.font, bg="light blue")
            title.place(relx=0.5, rely=0.05, anchor=CENTER)
            # buttons:
            menu_btn = Button(self.root, image=self.menu_icon, command=self.menu)
            menu_btn.place(x=0, y=0, width=(self.screenwidth/8), height=(self.screenwidth/8))
            
            search_btn = Button(self.root, image=self.search_icon, command=self.search)
            search_btn.place(x=(self.screenwidth-self.screenwidth/8), y=0, width=(self.screenwidth/8), height=(self.screenwidth/8))
            
            acounts_btn = Button(functions_frame, text='accounts', font=self.font, bg="Turquoise", command=self.account)
            acounts_btn.place(relx=1/6, rely=0.5, anchor=CENTER)
            
            recipe_btn = Button(functions_frame, text='recipe', font=self.font, bg="Turquoise", command=self.recipe)
            recipe_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
        
            unknown_btn = Button(functions_frame, text='?', font=self.font, bg="Turquoise", command=self.recipe)
            unknown_btn.place(relx=5/6, rely=0.5, anchor=CENTER)
            
            self.place_exit_btn()      
    
    def menu(self) -> None:
        """opens the menu bar at the top left of the home page"""
        print("open menu")
        
    def search(self) -> None:
        """Opens the search bar at the top of the home page"""
        print("open search bar")
        
    def account(self) -> None:
        """Opens the accounts system"""
        self.root.destroy()
        account_page = AccountSystem()
        account_page.root.mainloop()
        
    def recipe(self) -> None:
        """Opens the recipe system"""
        self.root.destroy()
        recipe_page = RecipeFinder()
        recipe_page.root.mainloop()
        
        
if __name__ == "__main__":
    home_page = HomePage()
    home_page.root.mainloop()
