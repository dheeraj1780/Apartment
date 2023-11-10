from essential import *
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from database import *

class Pay_maintenance:
    def __init__(self,root,name,username):
        self.root = root
        self.name = name
        self.username = username

        #main frame
        #self.root= Frame(self.root)
        #self.f1.configure(bg="#222222")

        self.conn = get_connection()
        
        self.cursor = self.conn.cursor()

        #content under due payment frame
        maintenance = Label(self.root)
        maintenance.configure(text="PAYMENT", font=("Roboto", 24, "bold"),fg="#FFD700",bg="#222222")
        maintenance.place(relx=0.45, rely=0.25)

        text1 = Label(self.root,text="Accept to pay maintenance", font=("Roboto", 12, "bold"),fg="#FFD700",bg="#222222")
        text1.place(relx=0.65,rely=0.64)

        text2 = Label(self.root,text="Decline to go back to \nmaintenance payment page", font=("Roboto", 12, "bold"),fg="#FFD700",bg="#222222")
        text2.place(relx=0.20,rely=0.64)
            

        Decline = Button(self.root)
        Decline.pack()
        Decline.place(relx= 0.25, rely=0.7)
        Decline.configure(text="Decline",height=3, width=10, bg="gold", fg="black")
        Decline.configure(command=self.decline)
        Decline.configure(activebackground="gold")
        Decline.configure(cursor="hand2")

        Accept = Button(self.root)
        Accept.pack()
        Accept.place(relx=0.70, rely=0.7)
        Accept.configure(text="Accept",height=3, width=10, bg="gold", fg="black")
        Accept.configure(command=self.accept)
        Accept.configure(activebackground="gold")
        Accept.configure(cursor="hand2")

    def decline(self):
        from Controller import present_Maintenance_Records_gui_frame
        self.root.destroy()
        present_Maintenance_Records_gui_frame(self.name,self.username)

    def accept(self):
        self.cursor.execute(f'UPDATE resident SET Maintainence_fee = 1 WHERE Username = %s AND Name = %s',(self.username , self.name))
        self.conn.commit()
        from Controller import present_Maintenance_Records_gui_frame
        self.root.destroy()
        present_Maintenance_Records_gui_frame(self.name,self.username)

        




