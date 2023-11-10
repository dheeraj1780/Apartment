from essential import *
from home import Home
from community import Community
from login import Login
from joinus import JoinUs
from payment import Payment
from create_profile import Profile
from user import User
from pay_maintenance import Pay_maintenance
from make_announcement import Make_announcement
from maintenance_records import Maintenance_records
from community_strength import Community_strength
from update_profile import Update_profile

#Homepage
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
    window['background'] = '#222222'

    window.mainloop()

#Communitypage
def present_Communitypage_gui_frame():
    window = Tk()
    Community(window)

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Set the window title
    window.title('Apartment Management System')

    # Set the window dimensions to fill the screen
    window.geometry("{}x{}+0+0".format(screen_width, screen_height))

    # Set the background color
    window['background'] = '#222222'

    window.mainloop()

#Loginpage
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
    window['background'] = '#222222'

    window.mainloop()

#Joinuspage
def present_Joinuspage_gui_frame():
    window = Tk()
    JoinUs(window)

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Set the window title
    window.title('Apartment Management System')

    # Set the window dimensions to fill the screen
    window.geometry("{}x{}+0+0".format(screen_width, screen_height))

    # Set the background color
    window['background'] = '#222222'

    window.mainloop()

#Paymentpage
def present_Paymentpage_gui_frame(block,house):
    window = Tk()
    Payment(window,block,house)

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Set the window title
    window.title('Apartment Management System')

    # Set the window dimensions to fill the screen
    window.geometry("{}x{}+0+0".format(screen_width, screen_height))

    # Set the background color
    window['background'] = '#222222'

    window.mainloop()

#Profilepage
def present_Profilepage_gui_frame(block,house):
    window = Tk()
    Profile(window,block,house)

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Set the window title
    window.title('Apartment Management System')

    # Set the window dimensions to fill the screen
    window.geometry("{}x{}+0+0".format(screen_width, screen_height))

    # Set the background color
    window['background'] = '#222222'

    window.mainloop()

#Userpage
def present_Userpage_gui_frame(name,username):
    window = Tk()
    User(window,name,username)

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Set the window title
    window.title('Apartment Management System')

    # Set the window dimensions to fill the screen
    window.geometry("{}x{}+0+0".format(screen_width, screen_height))

    # Set the background color
    window['background'] = '#222222'

    window.mainloop()

#Maintenance Records
def present_Maintenance_Records_gui_frame(name,username):
    window = Tk()
    Maintenance_records(window,name,username)

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Set the window title
    window.title('Apartment Management System')

    # Set the window dimensions to fill the screen
    window.geometry("{}x{}+0+0".format(screen_width, screen_height))

    # Set the background color
    window['background'] = '#222222'

    window.mainloop()

#Pay Maintenance
def present_Pay_Maintenance_gui_frame(name,username):
    window = Tk()
    Pay_maintenance(window,name,username)

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Set the window title
    window.title('Apartment Management System')

    # Set the window dimensions to fill the screen
    window.geometry("{}x{}+0+0".format(screen_width, screen_height))

    # Set the background color
    window['background'] = '#222222'

    window.mainloop()

#update profile
def present_Update_Profile_gui_frame(name,username):
    window = Tk()
    Update_profile(window,name,username)

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Set the window title
    window.title('Apartment Management System')

    # Set the window dimensions to fill the screen
    window.geometry("{}x{}+0+0".format(screen_width, screen_height))

    # Set the background color
    window['background'] = '#222222'

    window.mainloop()

#Make Announcement
def present_Make_Announcement_gui_frame(name,username):
    window = Tk()
    Make_announcement(window,name,username)

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Set the window title
    window.title('Apartment Management System')

    # Set the window dimensions to fill the screen
    window.geometry("{}x{}+0+0".format(screen_width, screen_height))

    # Set the background color
    window['background'] = '#222222'

    window.mainloop()


#COMMUNITY STRENGTH
def present_Community_Strength_gui_frame(name,username):
    window = Tk()
    Community_strength(window,name,username)

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Set the window title
    window.title('Apartment Management System')

    # Set the window dimensions to fill the screen
    window.geometry("{}x{}+0+0".format(screen_width, screen_height))

    # Set the background color
    window['background'] = '#222222'

    window.mainloop()



