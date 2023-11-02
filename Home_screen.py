from tkinter import Tk, Label, Frame, Button, Entry, W, PhotoImage
from tkmacosx import Button as BUTTON

class HomePage:
    """Creates a GUI system for the Foodie Findz APP (prototype)"""
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('Home Page')
        self.root.geometry('400x650')
        self.root.config(bg='light blue')
        self.font = ('Times New Roman', 14)
        self.home_pic = PhotoImage(file='VisualAssets/home_picture.png')
        self.home_page_creation()
        
    def home_page_creation(self) -> None:
            home_frame = Frame(self.root, bd=2, bg='light blue', padx=0, pady=0)
            #pictures:
            Label(home_frame, image=self.home_pic).grid(padx=0, pady=0)
            Label(home_frame, text="Foodie Findz", font=self.font, bg='purple').grid(padx=100, pady=112.5)
            home_frame.place(x=-2.5, y=-2.5, width=400, height=225)
            
            # buttons:
            menu_btn = BUTTON(self.root, text='menu', font=self.font, bg="Turquoise", command=self.menu)
            menu_btn.place(x=0, y=0, width=50, height=50)

            search_btn = BUTTON(self.root, text='search', font=self.font, bg="Turquoise", command=self.search)
            search_btn.place(x=350, y=0, width=50, height=50)
            
            acounts_btn = BUTTON(self.root, text='accounts', font=self.font, bg="Turquoise", command=self.account)
            acounts_btn.place(x=0, y=0, width=50, height=50)
            
            recipe_btn = BUTTON(self.root, text='recipe', font=self.font, bg="Turquoise", command=self.recipe)
            recipe_btn.place(x=0, y=0, width=50, height=50)
        
            
            self.place_exit_btn()      
    
    def menu(self) -> None:
        print("open menu")
        
    def search(self) -> None:
        print("open search bar")
        
    def account(self) -> None:
        print("open account system")
        
    def recipe(self) -> None:
        print("open recipe system")
        
    def clear_root(self) -> None:
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def place_exit_btn(self) -> None:
        exit_btn = BUTTON(self.root, text='EXIT', font=('Times New Roman', 50), bg="Turquoise", command=self.root.destroy)
        exit_btn.place(x=200, y=600, width=200, height=50)
        
if __name__ == "__main__":
    home_page = HomePage()
    home_page.root.mainloop()