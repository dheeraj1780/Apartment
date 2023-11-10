from essential import *
from tkinter import *
from PIL import Image, ImageTk
from joinus import JoinUs
#import mysql.connector
from database import *




class Community:
    def __init__(self,root):
        self.root = root

        menu1(root, ["HOME", "COMMUNITY", "LOGIN"], [LEFT, LEFT, RIGHT], [self.goto_home_page,self.goto_community_page, self.goto_login_page])
        self.root.frame1.pack(side=TOP, anchor="n", fill=X)

        #connection estabhlishing
        self.conn = get_connection()
        #cursor object
        self.cursor = self.conn.cursor()
        #operations
        self.cursor.execute("SELECT Availability FROM block")
        self.availability= self.cursor.fetchall()
        #releasing connection
        release_connection(self.conn)
        
        #community frame
        #self.root = Frame(self.root , bg="#222222")

        #object for joinus page
        #self.joinus_page = JoinUs(self.root)

        b1 = Button(self.root,text="JOIN US",command=self.goto_joinus_page)
        b1.place(relx=0.7,rely=0.1,height=40,width=75)
        b1.configure(bg="gold",fg="black")
        b1.configure(activebackground="gold")
        b1.configure(cursor="hand2")

        l1 = Label(self.root,text = "Choose the Block" ,font=("Roboto", 16, "bold"))
        l1.place(relx=0.2 , rely=0.1,height=40,width=200)
        l1.configure(bg="#222222",fg="gold")

        f2 = Frame(self.root)
        f2.place(relx= 0.2,rely=0.2,height=240,width=240)
        
        self.f3 = Frame(self.root , bg = "#222222")
        self.f3.place(relx=0.5,rely=0.3,height=300,width=300)

        #BLOCK A BUTTON
        b2 = Button(f2,text="Block A",bg="#111111",fg="gold")
        b2.configure(command=lambda: self.block_buttons(0))
        b2.place(relx=0,rely=0,height=80,width=120)
        b2.configure(activebackground="gold")
        b2.configure(cursor="hand2")

        #BLOCK B BUTTON
        b3 = Button(f2,text="Block B",bg="#111111",fg="gold")
        b3.configure(command=lambda: self.block_buttons(1))
        b3.place(relx=0.5,rely=0,height=80,width=120)
        b3.configure(activebackground="gold")
        b3.configure(cursor="hand2")

        #BLOCK C BUTTON
        b4 = Button(f2,text="Block C",bg="#111111",fg="gold")
        b4.configure(command=lambda: self.block_buttons(2))
        b4.place(relx=0,rely=0.333,height=80,width=120)
        b4.configure(activebackground="gold")
        b4.configure(cursor="hand2")

        #BLOCK D BUTTON
        b5 = Button(f2,text="Block D",bg="#111111",fg="gold")
        b5.configure(command=lambda: self.block_buttons(3))
        b5.place(relx=0.5,rely=0.333,height=80,width=120)
        b5.configure(activebackground="gold")
        b5.configure(cursor="hand2")

        #BLOCK E BUTTON
        b6 = Button(f2,text="Block E",bg="#111111",fg="gold")
        b6.configure(command=lambda: self.block_buttons(4))
        b6.place(relx=0,rely=0.666,height=80,width=120)
        b6.configure(activebackground="gold")
        b6.configure(cursor="hand2")

        #BLOCK F BUTTON
        b7 = Button(f2,text="Block F",bg="#111111",fg="gold")
        b7.configure(command=lambda: self.block_buttons(5))
        b7.place(relx=0.5,rely=0.666,height=80,width=120)
        b7.configure(activebackground="gold")
        b7.configure(cursor="hand2")


        color1 = Label(self.root,height=1,width=5)
        color1.place(relx=0.2,rely=0.65)
        color1.configure(bg="green")

        color2 = Label(self.root,height=1,width=5)
        color2.place(relx=0.2,rely=0.72)
        color2.configure(bg="red")

        text1 = Label(self.root,text="Unoccupied")
        text1.place(relx=0.25,rely=0.65)
        text1.configure(bg="gold")

        text2 = Label(self.root,text="Occupied")
        text2.place(relx=0.25,rely=0.72)
        text2.configure(bg="gold")

    def goto_joinus_page(self):
        from Controller import present_Joinuspage_gui_frame
        self.root.destroy()
        present_Joinuspage_gui_frame()
        
    def block_buttons(self,block):
        #print(block)
        l1 = Label(self.f3,text = "G1")
        self.color(0,l1,block)
        l1.place(relx=0,rely=0.666,height=100,width=100)
        l2 = Label(self.f3,text = "G2")
        self.color(1,l2,block)
        l2.place(relx=0.333,rely=0.666,height=100,width=100)
        l3 = Label(self.f3,text = "G3")
        self.color(2,l3,block)
        l3.place(relx=0.666,rely=0.666,height=100,width=100)
        l4 = Label(self.f3,text = "F1")
        self.color(3,l4,block)
        l4.place(relx=0,rely=0.333,height=100,width=100)
        l5 = Label(self.f3,text = "F2")
        self.color(4,l5,block)
        l5.place(relx=0.333,rely=0.333,height=100,width=100)
        l6 = Label(self.f3,text = "F3")
        self.color(5,l6,block)
        l6.place(relx=0.666,rely=0.333,height=100,width=100)
        l7 = Label(self.f3,text = "S1")
        self.color(6,l7,block)
        l7.place(relx=0,rely=0,height=100,width=100)
        l8 = Label(self.f3,text = "S2")
        self.color(7,l8,block)
        l8.place(relx=0.333,rely=0,height=100,width=100)
        l9 = Label(self.f3,text = "S3")
        self.color(8,l9,block)
        l9.place(relx=0.666,rely=0,height=100,width=100)

    def color(self,i,label,block):
        i = (block*9)+i 
        #print(i)
        if self.availability[i] == (0,):
            label.configure(bg="green")
        else:
            label.configure(bg="red")

    def goto_home_page(self):
        from Controller import present_Homepage_gui_frame
        self.root.destroy()
        present_Homepage_gui_frame()

    def goto_community_page(self):
        pass

    def goto_login_page(self):
        from Controller import present_Loginpage_gui_frame
        self.root.destroy()
        present_Loginpage_gui_frame()








        
