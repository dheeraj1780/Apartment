from essential import *
from tkinter import *
from PIL import Image, ImageTk
from database import *




class Home():
    def __init__(self,root):
        self.root = root
        menu1(root, ["HOME", "COMMUNITY", "LOGIN"], [LEFT, LEFT, RIGHT], [self.goto_home_page,self.goto_community_page, self.goto_login_page])
        self.root.frame1.pack(side=TOP, anchor="n", fill=X)

        self.heading = Label(self.root, text="ABC\nApartments", font=("Roboto", 45, "bold"),fg="#FFD700",bg="#111111")
        self.heading.place(relx=0.39,rely=0.37)

    def goto_home_page(self):
        pass

    def goto_community_page(self):
        from Controller import present_Communitypage_gui_frame
        self.root.destroy()
        present_Communitypage_gui_frame()

    def goto_login_page(self):
        from Controller import present_Loginpage_gui_frame
        self.root.destroy()
        present_Loginpage_gui_frame()
