
from tkinter import *
from PIL import Image, ImageTk


class Home():
    def __init__(self,root):
        self.root = root
        self.name = "Navya"
        self.gender = "Female"

        heading = Label(self.root, text="HOME", font=("Roboto", 45, "bold"),fg="#FFD700",bg="#111111")
        heading.place(relx=0.39,rely=0.37)

        community_button = Button(root, text="Community Page", bg="#ADECDF", command=self.goto_community_page)
        community_button.place(x=400, y=20)

        login_button = Button(root, text="Login Page", bg="#ADECDF", command=self.goto_login_page)
        login_button.place(x=700, y=20)

    def goto_community_page(self):
        self.root.destroy()
        present_Communitypage_gui_frame(self.name,self.gender)

    def goto_login_page(self):
        self.root.destroy()
        present_Loginpage_gui_frame()


class Community():
    def __init__(self,root,name,gender):
        self.root = root
        heading = Label(self.root, text="COMMUNITY", font=("Roboto", 45, "bold"),fg="#FFD700",bg="#111111")
        heading.place(relx=0.39,rely=0.37)

        home_button = Button(root, text="Home Page", bg="#ADECDF", command=self.goto_home_page)
        home_button.place(x=400, y=20)

        login_button = Button(root, text="Login Page", bg="#ADECDF", command=self.goto_login_page)
        login_button.place(x=700, y=20)

        print("Community")
        print(name)
        print(gender)

    def goto_home_page(self):
        self.root.destroy()
        present_Homepage_gui_frame()

    def goto_login_page(self):
        self.root.destroy()
        present_Loginpage_gui_frame()

class Login():
    def __init__(self,root):
        self.root = root
        heading = Label(self.root, text="LOGIN", font=("Roboto", 45, "bold"),fg="#FFD700",bg="#111111")
        heading.place(relx=0.39,rely=0.37)

        home_button = Button(root, text="Home Page", bg="#ADECDF", command=self.goto_home_page)
        home_button.place(x=400, y=20)

        community_button = Button(root, text="Community Page", bg="#ADECDF", command=self.goto_community_page)
        community_button.place(x=600, y=20)
        

    def goto_community_page(self):
        self.root.destroy()
        present_Communitypage_gui_frame()

    def goto_home_page(self):
        self.root.destroy()
        present_Homepage_gui_frame()


def present_Homepage_gui_frame():
    window = Tk()
    Home(window)

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Set the window title
    window.title('Apartment Management System')

    # Set the window dimensions to fill the screen
    window.geometry("{}x{}+0+0".format(screen_width, screen_height))

    # Set the background color
    window['background'] = '#CAE9F5'

    window.mainloop()



def present_Communitypage_gui_frame(name,gender):
    window = Tk()
    Community(window,name,gender)

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Set the window title
    window.title('Apartment Management System')

    # Set the window dimensions to fill the screen
    window.geometry("{}x{}+0+0".format(screen_width, screen_height))

    # Set the background color
    window['background'] = '#CAE9F5'

    window.mainloop()


def present_Loginpage_gui_frame():
    window = Tk()
    Login(window)

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Set the window title
    window.title('Apartment Management System')

    # Set the window dimensions to fill the screen
    window.geometry("{}x{}+0+0".format(screen_width, screen_height))

    # Set the background color
    window['background'] = '#CAE9F5'

    window.mainloop()


present_Homepage_gui_frame()

