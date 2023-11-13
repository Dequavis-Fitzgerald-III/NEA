from tkinter import Tk, Label, Frame, Button, CENTER
from pprint import pprint
from os import name as os_name
from PIL import ImageTk, Image
from Recipe_Finder import RecipeFinder
from Account_System import AccountSystem
try:
    from messagebox import askyesno
except ImportError:
    print("due to being on Mac OS, not all features are supported")

print(os_name)


class HomePage:
    """Creates a GUI system for the Foodie Findz APP (prototype)"""
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('Home Page')
        self.screenwidth: int = 400
        self.screenheight: int = 650
        self.root.geometry(f'{self.screenwidth}x{self.screenheight}')
        self.root.config(bg='light blue')
        self.font = ('Times New Roman', 14)
        self.home_pic = ImageTk.PhotoImage(Image.open('VisualAssets/home_picture.png').resize((self.screenwidth,int(5*self.screenheight/13))))
        self.menu_icon = ImageTk.PhotoImage(Image.open('VisualAssets/menu_icon.png').resize((int(self.screenwidth/8),int(self.screenwidth/8))))
        self.search_icon = ImageTk.PhotoImage(Image.open('VisualAssets/search_icon.png').resize((int(self.screenwidth/8),int(self.screenwidth/8))))
        if os_name == "nt":
            self.serial_check = 13
        else: 
            self.serial_check = 273
        self.root.bind("<Configure>", self.resized)
        self.root.protocol("WM_DELETE_WINDOW", self.window_exit)
        self.home_page_creation()
        
    def home_page_creation(self) -> None:
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
        
    def clear_root(self) -> None:
        """Clears all widgets"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def place_exit_btn(self) -> None:
        """Places an exit button"""
        exit_btn = Button(self.root, text='X', font=self.font, bg="Turquoise", command=self.window_exit)
        exit_btn.place(x=self.screenwidth - 25, y=self.screenheight-25, width=25, height=25)
    
    def window_exit(self) -> None:
        """Closes the window if user confirms the pop up"""
        try:
            close = askyesno("Exit?", "Are you sure you want to exit?")
            if close:
                self.root.destroy()
        except NameError:
            self.root.destroy()
    
    def resized(self, event) -> None:
        """maintians proportions of widget placements when screen is resized"""
        if event.widget == self.root and event.serial != self.serial_check:
            self.screenwidth = self.root.winfo_width()
            self.screenheight = self.root.winfo_height()
            self.clear_root()
            self.home_page_creation()
        
if __name__ == "__main__":
    home_page = HomePage()
    home_page.root.mainloop()
