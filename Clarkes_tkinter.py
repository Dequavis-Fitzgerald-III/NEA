"""Custom tkinter library for quick and easy GUI creation"""

from tkinter import Tk, Button
from os import name as os_name
if os_name == "nt":
    from messagebox import askyesno
else:
    print("due to being on Mac OS, not all features are supported")

class Window:
    """creates a custom scalable tkinter window."""
    def __init__(self, name:str, screenwidth:int = 400, screenhieght:int = 650) -> None:
        self.root = Tk()
        self.root.title(name)
        self.screenwidth = screenwidth
        self.screenheight = screenhieght
        self.root.geometry(f'{self.screenwidth}x{self.screenheight}')
        self.root.config(bg='light blue')
        self.font = ('Times New Roman', 14)
        self.root.bind("<Configure>", self.resized)
        self.root.protocol("WM_DELETE_WINDOW", self.window_exit)
    
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
        if event.widget == self.root:
            self.screenwidth = self.root.winfo_width()
            self.screenheight = self.root.winfo_height()
            self.clear_root()
            self.populate_window()