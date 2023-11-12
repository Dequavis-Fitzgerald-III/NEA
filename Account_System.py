from tkinter import Tk, Label, Frame, Button, Entry, W

class AccountSystem:
    """Creates a GUI allowing for account system with login and registration capabilities!"""
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('Account System')
        self.root.geometry('500x450')
        self.root.config(bg='Gray')
        self.font = ('Times New Roman', 14)
        self.account_management_window()

    def close(self):
        self.root.destroy()
        self.super()
    
    def clear_root(self) -> None:
        for widget in self.root.winfo_children():
            widget.destroy()

    def place_exit_btn(self) -> None:
        exit_btn = Button(self.root, text='EXIT', font=self.font, bg="Turquoise", command=self.close)
        exit_btn.place(x=300, y=400, width=200, height=50)
    
    def place_return_btn(self, frame_input) -> None:
        return_btn = Button(frame_input, text='Return', font=self.font, bg="Turquoise", command=lambda:[self.clear_root(), self.account_management_window()])
        return_btn.place(x=0, y=125, width=150, height=75)
    
    def account_management_window(self) -> None:
        title_label =Label(self.root, text="Account Manager", bg="Turquoise", font=('Times New Roman', 50))
        title_label.place(x=45, y=50, width=390, height=100)

        # buttons
        login_btn = Button(self.root, text='Login', font=self.font, bg="Turquoise", command=self.login_window)
        login_btn.place(x=60, y=175, width=360, height=100)

        register_btn = Button(self.root, text='Register', font=self.font, bg="Turquoise", command=self.register_window)
        register_btn.place(x=60, y=275, width=360, height=100)
        self.place_exit_btn()       

    def login_window(self):
        self.clear_root()
        login_frame = Frame(self.root, bd=2, bg='light gray', padx=12, pady=10)
        Label(login_frame, text="Enter login details", bg='light gray', font=('Times New Roman', 50)).grid(padx=10,
                                                                                        pady=10)
        login_frame.place(x=0, y=0, width=500, height=100)
        Login_frame = Frame(self.root, bd=2, bg='light gray', padx=10, pady=10)
        Label(Login_frame, text="Enter Name", bg='light gray', font=self.font).grid(row=0, column=0,
                                                                            sticky=W, pady=10)
        Label(Login_frame, text="Enter Password", bg='light gray', font=self.font).grid(row=1, column=0,
                                                                                sticky=W,
                                                                                pady=10)
        Entry(Login_frame, font=self.font).grid(row=0, column=1, pady=5, padx=10)
        Entry(Login_frame, font=self.font, show='*').grid(row=1, column=1, pady=5, padx=10)
        enter_btn = Button(Login_frame, text='Login', bg="Turquoise", font=self.font)
        enter_btn.grid(row=3, column=1, pady=10, padx=10)
        Login_frame.place(x=0, y=150, width=500, height=225)
        self.place_return_btn(Login_frame)
        self.place_exit_btn()

    def register_window(self):
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
        self.place_return_btn(register_frame)
        self.place_exit_btn()

if __name__ == "__main__":
    account_system = AccountSystem()
    account_system.root.mainloop()
