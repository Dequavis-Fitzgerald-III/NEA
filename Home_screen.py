from tkinter import Tk, Label, Frame, Button, CENTER
from PIL import ImageTk, Image


class HomePage:
    """Creates a GUI system for the Foodie Findz APP (prototype)"""
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('Home Page')
        self.SCREENWIDTH: int = 400
        self.SCREENHEIGHT: int = 600
        self.root.geometry(f'{self.SCREENWIDTH}x{self.SCREENHEIGHT}')
        self.root.config(bg='light blue')
        self.font = ('Times New Roman', 14)
        self.home_pic = ImageTk.PhotoImage(Image.open('VisualAssets/home_picture.png').resize((self.SCREENWIDTH,int(5 * self.SCREENHEIGHT / 13))))
        self.menu_icon = ImageTk.PhotoImage(Image.open('VisualAssets/menu_icon.png').resize((int(self.SCREENWIDTH / 8),int(self.SCREENWIDTH / 8))))
        self.search_icon = ImageTk.PhotoImage(Image.open('VisualAssets/search_icon.png').resize((int(self.SCREENWIDTH / 8),int(self.SCREENWIDTH / 8))))
        self.home_page_creation()
        
    def home_page_creation(self) -> None:
            """Creates all widgets for the home page GUI"""
            #Frames:
            home_frame = Frame(self.root, bd=2, bg='light blue', padx=0, pady=0)
            home_frame.place(x=-2.5, y=-2.5, width=self.SCREENWIDTH, height=(5 * self.SCREENHEIGHT /13))
            
            accounts_frame = Frame(self.root, bd=2, bg='light blue', padx=0, pady=0)
            accounts_frame.place(x=0, y=(5 * self.SCREENHEIGHT / 13), width=(self.SCREENWIDTH / 3), height=(self.SCREENHEIGHT /13))
            
            recipe_frame = Frame(self.root, bd=2, bg='light blue', padx=0, pady=0)
            recipe_frame.place(x=(self.SCREENWIDTH / 3), y=(5 * self.SCREENHEIGHT / 13), width=(self.SCREENWIDTH / 3), height=(self.SCREENHEIGHT /13))
            
            unknown_frame = Frame(self.root, bd=2, bg='light blue', padx=0, pady=0)
            unknown_frame.place(x=(2 * self.SCREENWIDTH / 3), y=(5 * self.SCREENHEIGHT / 13), width=(self.SCREENWIDTH / 3), height=(self.SCREENHEIGHT /13))
            
            #pictures:
            Label(home_frame, image=self.home_pic).grid(padx=0, pady=0)
            Label(home_frame, text="Foodie Findz", font=self.font, bg='purple').grid(padx=100, pady=112.5)
    
            # buttons:
            menu_btn = Button(self.root, image=self.menu_icon, command=self.menu)
            menu_btn.place(x=0, y=0, width=(self.SCREENWIDTH / 8), height=(self.SCREENWIDTH / 8))
            
            search_btn = Button(self.root, image=self.search_icon, command=self.search)
            search_btn.place(x=(self.SCREENWIDTH - self.SCREENWIDTH / 8), y=0, width=(self.SCREENWIDTH / 8), height=(self.SCREENWIDTH / 8))
            
            acounts_btn = Button(accounts_frame, text='accounts', font=self.font, bg="Turquoise", command=self.account)
            acounts_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
            
            recipe_btn = Button(recipe_frame, text='recipe', font=self.font, bg="Turquoise", command=self.recipe)
            recipe_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
        
            unknown_btn = Button(unknown_frame, text='?', font=self.font, bg="Turquoise", command=self.recipe)
            unknown_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
            
            self.place_exit_btn()      
    
    def menu(self) -> None:
        """opens the menu bar at the top left of the home page"""
        print("open menu")
        
    def search(self) -> None:
        """Opens the search bar at the top of the home page"""
        print("open search bar")
        
    def account(self) -> None:
        """Opens the accounts system"""
        print("open account system")
        
    def recipe(self) -> None:
        """Opens the recipe finder system"""
        print("open recipe finder system")
        
    def clear_root(self) -> None:
        """Clears all widgets"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def place_exit_btn(self) -> None:
        """Places an exit button"""
        exit_btn = Button(self.root, text='EXIT', font=('Times New Roman', 50), bg="Turquoise", command=self.root.destroy)
        exit_btn.place(x=200, y=600, width=200, height=50)
        
if __name__ == "__main__":
    home_page = HomePage()
    home_page.root.mainloop()