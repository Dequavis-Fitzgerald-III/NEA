"""Account system with login and registration capabiities"""

from tkinter import Label, Frame, Button, Entry, CENTER, messagebox
from os import name as os_name
from Clarkes_tkinter import SecondaryResizableWindow
from PIL import ImageTk, Image
from sqlite3 import connect
from hashlib import sha256

class AccountSystem(SecondaryResizableWindow):
    """Creates a GUI allowing for account system with login and registration capabilities!"""
    def __init__(self, home, name: str = "Account System", screenwidth: int = 400, screenhieght: int = 650) -> None:
        super().__init__(name, screenwidth, screenhieght)
        self.current = self.login_window
        self.home = home
        self.current_user = None
        self.conn = connect("FoodieFindz_database.db")
        self.c = self.conn.cursor()
        self.populate_window()
    
    def populate_window(self) -> None:
        self.current()
    
    def window_exit(self) -> None:
        self.root.destroy()
        self.home.root.deiconify()

    def login_window(self):
        """Creates all widgets for the login page GUI."""
        self.current = self.login_window
        self.clear_root()
        # resizes the image to place on top of the screen
        self.home_pic = ImageTk.PhotoImage(Image.open('VisualAssets/account_picture.png').resize((self.screenwidth-5,int(5*self.screenheight/13))))
        login_font = ('Times New Roman', int(self.screenheight/29))
        # places a title at the top of the screen
        title_label = Label(self.root, text="Enter login details", bg='Light gray', font=('Times New Roman', int(self.screenheight/12)))
        title_label.place(x=0, y=0, width=self.screenwidth, height=self.screenheight/10)
        Label(self.root, image=self.home_pic).place(x=0, y=self.screenheight/10)
        # creates a frame to store all the buttons, labels and entries
        login_frame = Frame(self.root, bg='light gray')
        # adds entries for the users' name and password and grids them
        Label(login_frame, text="Enter Name", bg='light gray', font=login_font).grid(row=0, column=0)
        Label(login_frame, text="Enter Password", bg='light gray', font=login_font).grid(row=1, column=0)
        self.name_entry = Entry(login_frame, font=login_font)
        self.name_entry.grid(row=0, column=1)
        self.password_entry = Entry(login_frame, font=login_font, show='*')
        self.password_entry.grid(row=1, column=1)
        # adds an entry button that calls the login method
        Button(login_frame, text='Login', bg="Turquoise", font=login_font, command=self.login).grid(row=3, column=1)
        # adds a button for the user to press if they do not have an account and want to register
        Button(login_frame, text="Don't have an account?\n click to register", font=login_font, bg="Turquoise", command=self.register_window).grid(row=4, column=1)
        login_frame.place(relx=0.5, rely=0.65, anchor=CENTER)
        self.place_control_bar()

    def register_window(self):
        """Creates all widgets for the register page GUI."""
        self.current = self.register_window
        self.clear_root()
        register_font = ('Times New Roman', int(self.screenheight/29))
        # places a title at the top of the screen
        title_label = Label(self.root, text="Enter Register details", bg='Light gray', font=('Times New Roman', int(self.screenheight/14)))
        title_label.place(x=0, y=0, width=self.screenwidth, height=self.screenheight/10)
        # creates a frame to store all the buttons, labels and entries
        register_frame = Frame(self.root, bd=2, bg='light gray', padx=10, pady=10)
        # adds entries for the users' intended email, username, password and grids them
        # (also has a password re-entry to ensure that the user knows the password they enter)
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
        # adds buttons to call the register function or return to the login page
        Button(register_frame, text='Register', bg="Turquoise", font=register_font, command=self.register).grid(row=4, column=1)
        Button(register_frame, text='Return', font=register_font, bg="Turquoise", command=lambda:[self.clear_root(), self.login_window()]).grid(row=4, column=0)
        register_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.place_control_bar()

    def login(self) -> None:
        """Logs users into their accounts"""
        # checks if there is a user in the database with the correct matching username and password
        for ID in self.c.execute("SELECT UserID FROM Users WHERE Username = ? AND Password = ?;", [self.name_entry.get(), sha256(self.password_entry.get().encode()).hexdigest()]):
            # if it is is correct the current user is stored and the window is closed after telling the user they are logged in
            self.current_user = ID
            messagebox.showinfo('confirmation', 'Logged in!')
            self.window_exit()
            break
        else:
            # if no account is found the user is prompted to try again as their details are incorrect
            messagebox.showerror('Error', "Details are incorrect, please try again!")
        
    def register(self) -> None:
        """Registers new accounts"""
        # if all checks are correct and details entered pass validation
        if self.email_check() and self.name_check() and self.password_check():
            # user is entered into the database
            self.c.execute("INSERT INTO Users (Username, Password, Email) VALUES (:Username,:Password,:Email)",
                  {
                    'Username': self.reg_username_entry.get(),
                    'Password': sha256(self.reg_password_entry.get().encode()).hexdigest(),
                    'Email': self.reg_email_entry.get()
                    })
            self.conn.commit()
            messagebox.showinfo('confirmation', 'Record Saved')
            # user is sent back to the login screen after being told that they have been added to the database
            self.clear_root()
            self.account_manager_window()
            
    def email_check(self) -> bool:
        """Validates that the users entered email fits the criteria"""
        # ensures that the email adress isn't already used by a different user
        for _ in self.c.execute("SELECT UserID FROM Users WHERE Email = ?;", [self.reg_email_entry.get()]):
            messagebox.showerror('Error', "Email address is taken!")
            return False
        # ensures that the user has entered an email adress
        if "@" not in self.reg_email_entry.get():
            messagebox.showerror('Error', "Email must be a valid email address!")
            return False
        # splits the email into its different parts to be validated seperately
        splitted_email = self.reg_email_entry.get().split("@")
        user, domain = splitted_email[0], splitted_email[1]
        # ensures that the email is a marlborough college email adress by checking the domain
        if domain != "marlboroughcollege.org":
            messagebox.showerror('Error', "Email must be a valid marlborough college student email address!")
            return False
        # ensures that the user has entered an email of digits (marlboroughc college student)
        if not user.isdigit():
            print("whatup")
            messagebox.showerror('Error', "Email must be a valid marlborough college student email address!")
            return False
        # checks the length of the email adress
        if len(user) < 4 or len(user) > 5:
            print("hi")
            messagebox.showerror('Error', "Email must be a valid marlborough college student email address!")
            return False
        return True

    def name_check(self) -> bool:
        """Validates that the user's entered username fits the criteria"""
        # ensures that the username isn't already used by a different user
        for _ in self.c.execute("SELECT UserID FROM Users WHERE Username = ?;", [self.reg_username_entry.get()]):
            messagebox.showerror('Error', "Username is taken!")
            return False
        # checks that teh suername is within the lengths required by the database
        if len(self.reg_username_entry.get()) < 2:
            messagebox.showerror('Error', "Username must be between 2 and 24 characters!")
            return False
        if len(self.reg_username_entry.get()) > 24:
            messagebox.showerror('Error', "sername must be between 2 and 24 characters!")
            return False
        return True
        
    def password_check(self) -> bool:
        """Validates that the users inputted password fits the criteria"""
        special_characters = "!@#$%^&*()-+?_=,<>/"
        # ensures that the password matches the password re-entry
        if self.reg_password_entry.get() != self.reg_password_reentry.get():
            messagebox.showerror('Error', "Passwords don't match!")
            return
        # ensures that the password is long enough
        if len(self.reg_password_entry.get()) < 8:
            messagebox.showerror('Error', 'Password must be greater than 8 characters!')
            return False
        # ensures that the password contains an upper case letter 
        if not any(c.isupper() for c in self.reg_password_entry.get()):
            messagebox.showerror('Error', 'Requires an upper case letter!')
            return False
        # ensures that the password contains a number
        if not any(c.isdigit() for c in self.reg_password_entry.get()):
            messagebox.showerror('Error', 'Requires a digit!')
            return False
        # ensures that the password contains a special character
        if not any(c in special_characters for c in self.reg_password_entry.get()):
            messagebox.showerror('Error', 'Requires a special character!')
            return False
        return True
