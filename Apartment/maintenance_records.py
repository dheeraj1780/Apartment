from essential import *
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from database import *
from pay_maintenance import Pay_maintenance

class Maintenance_records:
    def __init__(self,root,name,username):
        self.root = root
        self.name = name
        self.username = username

        menu2(self.root, ["HOME", "COMMUNITY", "LOGOUT"], [LEFT, LEFT, RIGHT], [self.goto_user_page , self.goto_community_page , self.goto_login_page])
        self.root.frame2.pack(side=TOP, anchor="n", fill=X)
        
        self.conn = get_connection()
        
        self.cursor = self.conn.cursor()

        #main frame
        # self.root= Frame(root)
        # self.root.configure(bg="#222222")
        
        self.pay_maintenance_page = Pay_maintenance(self.root,self.name,self.username)

        #due payment frame
        f2 = Frame(self.root)
        f2.configure(bg="#333333")
        f2.place(relx=0.0, rely=0.2, relwidth=0.5, relheight=1)

        #paid payment frame
        f3 = Frame(self.root)
        f3.configure(bg="#111111")
        f3.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=1)

        
            # self.root.pack_forget()
            # self.pay_maintenance_page.root.pack(side=TOP, expand = True, fill="both")

        #pay button
        button1 = Button(f2)
        button1.configure(text="Pay")
        button1.configure(font=("Roboto", 24, "bold"))
        button1.configure(fg="gold",bg="#111111")
        button1.configure(activebackground="gold")
        button1.configure(command=self.goto_pay_maintenance_page)
        button1.place(relx=0.1,rely=0.3)

        #content under due payment frame
        due = Label(f2)
        due.configure(text="DUE", font=("Roboto", 24, "bold"),fg="#FFD700",bg="#333333")
        due.place(relx=0.4, rely=0.05)


        #content under paid payment frame
        paid = Label(f3)
        paid.configure(text="PAID", font=("Roboto", 24, "bold"),fg="#FFD700",bg="#111111")
        paid.place(relx=0.45, rely=0.05)

        # Close the cursor and connection
        release_connection(self.conn)

    def goto_pay_maintenance_page(self):
            from Controller import present_Pay_Maintenance_gui_frame
            self.root.destroy()
            present_Pay_Maintenance_gui_frame(self.name,self.username)

    def goto_user_page(self):
        from Controller import present_Userpage_gui_frame
        self.root.destroy()
        present_Userpage_gui_frame(self.name,self.username)

    def goto_community_page(self):
        pass

    def goto_login_page(self):
        from Controller import present_Loginpage_gui_frame
        self.root.destroy()
        present_Loginpage_gui_frame()