from tkinter import Tk, Label, Frame, Button, Entry, W, PhotoImage

class IphoneScreen:
    """Creates a GUI allowing for account system with login and registration capabilities!"""
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('Iphone screen')
        self.root.geometry('315x650')
        self.root.config(bg='light blue')
        self.font = ('Times New Roman', 14)
        self.iphone_pic = PhotoImage(file='VisualAssets/iphone_screen.png')
        self.iphone_frame = Frame(self.root, bd=2, bg='light gray', padx=12, pady=10)
        Label(self.iphone_frame, image=self.iphone_pic, borderwidth=0).grid()
        self.iphone_frame.place(x=-85, y=0, width=4000, height=650)
    
    def clear_root(self) -> None:
        for widget in self.root.winfo_children():
            widget.destroy()
        

if __name__ == "__main__":
    phone = IphoneScreen()
    phone.root.mainloop()