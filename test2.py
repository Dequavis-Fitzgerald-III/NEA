from Test import Window

class home_page(Window):
    def __init__(self, name: str, screenwidth: int = 400, screenhieght: int = 650) -> None:
        super().__init__(name, screenwidth, screenhieght)
        
if __name__ == "__main__":
    home_page = home_page("home page")
    home_page.root.mainloop()
