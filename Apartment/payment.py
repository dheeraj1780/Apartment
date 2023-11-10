from essential import *
from tkinter import *
from PIL import Image, ImageTk
from create_profile import Profile
#import mysql.connector
from database import *


class Payment():
    def __init__(self,root,block,house):
        self.root = root
        self.block = block
        self.house = house
        
        self.conn = get_connection()
        
        self.cursor = self.conn.cursor()

        #self.profile_page = Profile(self.root,self.block,self.house)

        # from community import Community
        # self.community_page = Community(self.root)

        #self.root = Frame(root)
        #self.f1.configure(bg="#222222")
        
        heading = Label(self.root,text="Payment Page", font=("Roboto", 32, "bold"),fg="#FFD700",bg="#222222")
        heading.place(relx=0.40,rely=0.20)

        text1 = Label(self.root,text="Accept to become a part of our community", font=("Roboto", 24, "bold"),fg="#FFD700",bg="#222222")
        text1.place(relx=0.25,rely=0.3)

        text2 = Label(self.root,text="Decline to select other sweet home", font=("Roboto", 24, "bold"),fg="#FFD700",bg="#222222")
        text2.place(relx=0.29,rely=0.5)

        Decline = Button(self.root)
        Decline.pack()
        Decline.place(relx= 0.35, rely=0.7)
        Decline.configure(text="Decline",height=3, width=10, bg="gold", fg="black")
        Decline.configure(command=self.decline)
        Decline.configure(activebackground="gold")
        Decline.configure(cursor="hand2")

        Accept = Button(self.root)
        Accept.pack()
        Accept.place(relx=0.65, rely=0.7)
        Accept.configure(text="Accept",height=3, width=10, bg="gold", fg="black")
        Accept.configure(command=self.accept)
        Accept.configure(activebackground="gold")
        Accept.configure(cursor="hand2")

    # def update_content(self, accepted):
    #         #self.content_label.config(text="")
    #     if accepted:
    #         self.root.pack_forget()
    #         self.profile_page.root.pack(side=TOP, expand = True, fill="both")

    #     else:
    #         self.root.pack_forget()
    #         from community import Community
    #         community_page = Community(self.root)
    #         community_page.root.pack(side=TOP, expand = True, fill="both")

    def decline(self):
        from Controller import present_Communitypage_gui_frame
        self.root.destroy()
        present_Communitypage_gui_frame()
        # self.conn = get_connection()
        
        # self.cursor = self.conn.cursor()
        # self.root.pack_forget()
        # from community import Community
        # self.community_page = Community(self.root)
        # self.community_page.root.pack(side=TOP, expand = True, fill="both")
        # #releasing connection
        # release_connection(self.conn)

    def accept(self):
        # self.conn = get_connection()
        
        # self.cursor = self.conn.cursor()
       
        self.cursor.execute(f'UPDATE block SET Availability = 1 WHERE BlockNo = %s AND HouseNo = %s', (self.block, self.house))
        self.root.destroy()
        #self.profile_page.root.pack(side=TOP, expand = True, fill="both")
        from Controller import present_Profilepage_gui_frame
        present_Profilepage_gui_frame(self.block,self.house)
        
        #releasing connection
        self.conn.commit()
        release_connection(self.conn)

