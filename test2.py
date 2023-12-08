from Clarkes_tkinter import Window
from tkinter import Frame, Label, CENTER

class home_page(Window):
    def __init__(self, name: str, screenwidth: int = 400, screenhieght: int = 650) -> None:
        super().__init__(name, screenwidth, screenhieght)
        self.clear_root()
        steps_frame = Frame(self.root, bg='light blue')
        text_label = Label(steps_frame, text="1)Preheat oven to 350F degrees.In a large bowl, mix together apples, oil, sugar, eggs and walnuts by hand. 2)Mix well then set aside.In a separate bowl, mix flour, baking soda, salt, vanilla and cinnamon 3)Mix well then add to the apple mixture. The batter will be thick. 4)Pour into ungreased 13x9 baking pan, and bake for one hour or until done. ", wraplength=380, font=self.font, bg='white')
        text_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        steps_frame.place(x=0, y=225, width=400, height=425)
        
if __name__ == "__main__":
    home_page = home_page("home page")
    home_page.root.mainloop()
