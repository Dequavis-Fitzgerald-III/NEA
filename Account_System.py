from tkinter import Tk, Label, Frame, Button, Entry, W, CENTER
from os import name as os_name

class AccountSystem:
    """Creates a GUI allowing for account system with login and registration capabilities!"""
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('Account System')
        self.screenwidth: int = 400
        self.screenheight: int = 650
        self.root.geometry(f'{self.screenwidth}x{self.screenheight}')
        self.root.config(bg='Gray')
        self.font = ('Times New Roman', 14)
        self.current = self.account_management_window
        if os_name == "nt":
            self.serial_check = 13
        else: 
            self.serial_check = 273
        self.root.bind("<Configure>", self.resized)
        self.account_management_window()

    def close(self):
        self.root.destroy()
        self.super()
    
    def clear_root(self) -> None:
        for widget in self.root.winfo_children():
            widget.destroy()

    def place_exit_btn(self) -> None:
        exit_btn = Button(self.root, text='EXIT', font=self.font, bg="Turquoise", command=self.close)
        exit_btn.place(x=self.screenwidth-50, y=self.screenheight - 50, width=50, height=50)
    
    
    def account_management_window(self) -> None:
        self.current = self.account_management_window
        title_label =Label(self.root, text="Account Manager", bg="Turquoise", font=('Times New Roman', 50))
        title_label.place(relx=0.5, rely=0.07, anchor=CENTER)

        options_frame = Frame(self.root, bg='light gray')
        
        # buttons
        Button(options_frame, text='Login', font=self.font, bg="Turquoise", command=self.login_window).grid(row=0, column=0)
        Button(options_frame, text='Register', font=self.font, bg="Turquoise", command=self.register_window).grid(row=1, column=0)
        
        options_frame.place(relx=0.5, rely=0.5, width=self.screenwidth/2, height=self.screenheight/6, anchor=CENTER)
        self.place_exit_btn()

    def login_window(self):
        self.current = self.login_window
        self.clear_root()
        login_label = Label(self.root, text="Enter login details", bg='light gray', font=('Times New Roman', 50))
        login_label.place(relx=0.5, rely=0.07, anchor=CENTER)
        login_frame = Frame(self.root, bg='light gray')
        Label(login_frame, text="Enter Name", bg='light gray', font=self.font).grid(row=0, column=0)
        Label(login_frame, text="Enter Password", bg='light gray', font=self.font).grid(row=1, column=0)
        Entry(login_frame, font=self.font).grid(row=0, column=1)
        Entry(login_frame, font=self.font, show='*').grid(row=1, column=1)
        Button(login_frame, text='Login', bg="Turquoise", font=self.font).grid(row=3, column=1)
        Button(login_frame, text='Return', font=self.font, bg="Turquoise", command=lambda:[self.clear_root(), self.account_management_window()]).grid(row=4, column=0)
        login_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.place_exit_btn()

    def register_window(self):
        self.current = self.register_window
        self.clear_root()
        register_frame = Frame(self.root, bd=2, bg='light gray', padx=4, pady=10)
        Label(register_frame, text="Register your details", bg='light gray', font=('Times New Roman', 50)).grid(
            padx=4, pady=10)
        register_frame.place(x=0, y=0, width=500, height=100)
        register_frame = Frame(self.root, bd=2, bg='light gray', padx=10, pady=10)
        Label(register_frame, text="Enter Name", bg='light gray', font=self.font).grid(row=0, column=0,
                                                                                sticky=W, pady=2)
        Label(register_frame, text="Enter Password", bg='light gray', font=self.font).grid(row=1,
                                                                                    column=0,
                                                                                    sticky=W,
                                                                                    pady=2)
        Label(register_frame, text="Re-Enter Password", bg='light gray', font=self.font).grid(row=2,
                                                                                        column=0,
                                                                                        sticky=W,
                                                                                        pady=2)
        register_name = Entry(register_frame, font=self.font)
        register_pwd = Entry(register_frame, font=self.font, show='*')
        pwd_again = Entry(register_frame, font=self.font, show='*')
        enter_btn = Button(register_frame, text='Register', bg="Turquoise", font=self.font)
        register_name.grid(row=0, column=1, pady=3, padx=12)
        register_pwd.grid(row=1, column=1, pady=3, padx=12)
        pwd_again.grid(row=2, column=1, pady=3, padx=12)
        enter_btn.grid(row=3, column=1, pady=5, padx=12)
        register_frame.place(x=0, y=150, width=500, height=225)
        self.place_exit_btn()
    
    def resized(self, event) -> None:
        """maintians proportions of widget placements when screen is resized"""
        if event.widget == self.root and event.serial != self.serial_check:
            self.screenwidth = self.root.winfo_width()
            self.screenheight = self.root.winfo_height()
            self.clear_root()
            self.current()

if __name__ == "__main__":
    account_system = AccountSystem()
    account_system.root.mainloop()
