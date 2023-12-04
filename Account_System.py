"""Account system with login and registration capabiities"""

from tkinter import Tk, Label, Frame, Button, Entry, CENTER, messagebox
from os import name as os_name
from Clarkes_tkinter import Window, ResizableWindow

class AccountSystem(ResizableWindow):
    """Creates a GUI allowing for account system with login and registration capabilities!"""
    def __init__(self, home, name: str = "Account System", screenwidth: int = 400, screenhieght: int = 650) -> None:
        super().__init__(name, screenwidth, screenhieght)
        self.current = self.account_manager_window
        self.home = home
        self.populate_window()
    
    def populate_window(self) -> None:
        self.current()
    
    def window_exit(self) -> None:
        self.root.destroy()
        self.home.root.deiconify()
        
    def account_manager_window(self) -> None:
        self.current = self.account_manager_window
        title_label = Label(self.root, text="Account Manager", bg="Light gray", font=('Times New Roman', int(self.screenheight/12)))
        title_label.place(x=0, y=0, width=self.screenwidth, height=self.screenheight/10)
        available_frame = Frame(self.root, bg='Turquoise')
        available_frame.place(x=0, y=self.screenheight/10, width=self.screenwidth, height=(9*self.screenheight/10)-25)
        options_frame = Frame(available_frame, bg='Turquoise')
        
        # buttons
        Button(options_frame, text='Login', font=('Times New Roman', int(self.screenheight/6)), bg="Turquoise", command=self.login_window).grid(row=0, column=0)
        Button(options_frame, text='Register', font=('Times New Roman', int(self.screenheight/6)), bg="Turquoise", command=self.register_window).grid(row=1, column=0)
        
        options_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.place_control_bar()

    def login_window(self):
        self.current = self.login_window
        self.clear_root()
        login_font = ('Times New Roman', int(self.screenheight/29))
        title_label = Label(self.root, text="Enter login details", bg='Light gray', font=('Times New Roman', int(self.screenheight/12)))
        title_label.place(x=0, y=0, width=self.screenwidth, height=self.screenheight/10)
        login_frame = Frame(self.root, bg='light gray')
        Label(login_frame, text="Enter Name", bg='light gray', font=login_font).grid(row=0, column=0)
        Label(login_frame, text="Enter Password", bg='light gray', font=login_font).grid(row=1, column=0)
        self.name_entry = Entry(login_frame, font=login_font)
        self.name_entry.grid(row=0, column=1)
        self.password_entry = Entry(login_frame, font=login_font, show='*')
        self.password_entry.grid(row=1, column=1)
        Button(login_frame, text='Login', bg="Turquoise", font=self.font, command=self.login).grid(row=3, column=1)
        Button(login_frame, text='Return', font=login_font, bg="Turquoise", command=lambda:[self.clear_root(), self.account_manager_window()]).grid(row=4, column=0)
        login_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.place_control_bar()

    def register_window(self):
        self.current = self.register_window
        self.clear_root()
        register_font = ('Times New Roman', int(self.screenheight/29))
        title_label = Label(self.root, text="Enter Register details", bg='Light gray', font=('Times New Roman', int(self.screenheight/14)))
        title_label.place(x=0, y=0, width=self.screenwidth, height=self.screenheight/10)
        register_frame = Frame(self.root, bd=2, bg='light gray', padx=10, pady=10)
        Label(register_frame, text="Enter Email", bg='light gray', font=register_font).grid(row=0, column=0)
        Label(register_frame, text="Enter Username", bg='light gray', font=register_font).grid(row=1, column=0)
        Label(register_frame, text="Enter Password", bg='light gray', font=register_font).grid(row=2, column=0)
        Label(register_frame, text="Re-Enter Password", bg='light gray', font=register_font).grid(row=3, column=0)
        self.reg_email_entry = Entry(register_frame, font=register_font)
        self.reg_username_entry = Entry(register_frame, font=register_font)
        self.reg_password_entry = Entry(register_frame, font=register_font, show='*')
        self.reg_password_reentry = Entry(register_frame, font=register_font, show='*')
        self.reg_email_entry.grid(row=0, column=1)
        self.reg_username_entry.grid(row=1, column=1)
        self.reg_password_entry.grid(row=2, column=1)
        self.reg_password_reentry.grid(row=3, column=1)
        Button(register_frame, text='Register', bg="Turquoise", font=register_font, command=self.register).grid(row=4, column=1)
        Button(register_frame, text='Return', font=register_font, bg="Turquoise", command=lambda:[self.clear_root(), self.account_manager_window()]).grid(row=4, column=0)
        register_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.place_control_bar()

    def login(self) -> None:
        print(f"name: {self.name_entry.get()}, password: {self.password_entry.get()}")
        
    def register(self) -> None:
        print(f"password: {self.reg_password_entry.get()}, repassword: {self.reg_password_reentry.get()}")
        if self.email_check() and self.name_check() and self.password_check():
            print("welcome")
            
    def email_check(self) -> bool:
        if "@" not in self.reg_email_entry.get():
            messagebox.showerror('Error', "Email must be a valid email address!")
            return False
        splitted_email = self.reg_email_entry.get().split("@")
        user, domain = splitted_email[0], splitted_email[1]
        if domain != "marlboroughcollege.org":
            messagebox.showerror('Error', "Email must be a valid marlborough college student email address!")
            return False
        if not user.isdigit():
            print("whatup")
            messagebox.showerror('Error', "Email must be a valid marlborough college student email address!")
            return False
        if len(user) < 4 or len(user) > 5:
            print("hi")
            messagebox.showerror('Error', "Email must be a valid marlborough college student email address!")
            return False
        return True

    def name_check(self) -> bool:
        if len(self.reg_username_entry.get()) < 2:
            messagebox.showerror('Error', "Username too short!")
            return False
        if len(self.reg_username_entry.get()) > 24:
            messagebox.showerror('Error', "Username too long!")
            return False
        return True
        
    def password_check(self) -> bool:
        special_characters = "!@#$%^&*()-+?_=,<>/"
        if self.reg_password_entry.get() != self.reg_password_reentry.get():
            messagebox.showerror('Error', "Passwords don't match!")
            return
        if len(self.reg_password_entry.get()) < 8:
            messagebox.showerror('Error', 'Password too short!')
            return False
        if not any(c.isupper() for c in self.reg_password_entry.get()):
            messagebox.showerror('Error', 'Requires an upper case letter!')
            return False
        if not any(c.isdigit() for c in self.reg_password_entry.get()):
            messagebox.showerror('Error', 'Requires a digit!')
            return False
        if not any(c in special_characters for c in self.reg_password_entry.get()):
            messagebox.showerror('Error', 'Requires a special character!')
            return False
        return True
    
if __name__ == "__main__":
    account_system = AccountSystem()
    account_system.root.mainloop()
