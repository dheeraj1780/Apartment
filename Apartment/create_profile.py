from tkinter import *
import os
#import mysql.connector
from tkinter import filedialog
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk
from database import *
from tkcalendar import Calendar
from datetime import datetime


class Profile:
    def __init__(self,root,block,house):
        self.root = root

        self.block = block
        self.house = house

        self.conn = get_connection()
        self.cursor = self.conn.cursor()

        heading = Label(self.root,text="Your Profile", font=("Roboto", 32, "bold"),fg="#FFD700",bg="#222222")
        heading.place(relx=0.42,rely=0.05)

        #frame containing the labels and entry widgets
        f2 = Frame(self.root,height=550,width=1010)
        f2.place(relx=0.1,rely=0.13,relheight=0.6,relwidth=0.8)
        f2.configure(bg="#111111")

        #frame for containing profile pic
        f3 = Frame(f2)
        f3.place(relx=0.05,rely=0.05,relheight=0.5, relwidth=0.2)
        f3.configure(bg="#222222")

        #creating labels for profile details
        name = Label(f2,text="Name :", font=("Roboto", 16, "bold"),fg="#FFD700",bg="#222222")
        name.place(relx=0.4,rely=0.05)
        houseno = Label(f2,text="House no. :", font=("Roboto", 16, "bold"),fg="#FFD700",bg="#222222")
        houseno.place(relx=0.4,rely=0.15)
        blockno = Label(f2,text="Block no. :", font=("Roboto", 16, "bold"),fg="#FFD700",bg="#222222")
        blockno.place(relx=0.4,rely=0.25)
        username = Label(f2,text="Username :", font=("Roboto", 16, "bold"),fg="#FFD700",bg="#222222")
        username.place(relx=0.4,rely=0.35)
        password = Label(f2,text="Password :", font=("Roboto", 16, "bold"),fg="#FFD700",bg="#222222")
        password.place(relx=0.4,rely=0.45)
        phone = Label(f2,text="Phone no. :", font=("Roboto", 16, "bold"),fg="#FFD700",bg="#222222")
        phone.place(relx=0.4,rely=0.55)
        join_date = Label(f2,text="Date of Joining :", font=("Roboto", 16, "bold"),fg="#FFD700",bg="#222222")
        join_date.place(relx=0.4,rely=0.65)
        profile = Label(f2,text="Profile Photo", font=("Roboto", 16, "bold"),fg="#FFD700",bg="#222222")
        profile.place(relx=0.075,rely=0.7)


        #creating a label to display the profile picture.
        profile_picture_label = Label(f3)
        profile_picture_label.place(relx=0.0,rely=0.0, relheight=1, relwidth=1)

        #function to upload profile pic
        def upload_profile_picture():
            # Open a dialog box that allows the user to select a file from their computer.
            file_path = filedialog.askopenfilename(filetypes=[('Image files', '*.png')])

            # If the user selected a file, load the image and display it in the label.
            if file_path:
                image_obj = Image.open(file_path)
                resize_image = image_obj.resize((250,250))
                img= ImageTk.PhotoImage(resize_image)
            #creating a label to display the profile picture.
                profile_picture_label = Label(f3)
                profile_picture_label.image = img
                profile_picture_label['image']=img
            #profile_picture_label.config()
                profile_picture_label.place(relx=0.0,rely=0.0, relheight=1, relwidth=1)


        #creating upload button to upload profile pic
        upload_button1 = Button(f3, text="+", command=upload_profile_picture)
        upload_button1.place(relx=0.45,rely=0.45)
        upload_button1.configure(fg="gold",bg="#111111")


        #creating the variables to store the values
        name_var = StringVar()
        username_var = StringVar()
        password_var = StringVar()
        phone_var = IntVar()

        #calender frame and contents
        cal_frame = Frame(self.root)
        cal_frame.place_forget()  # Initially hide the calendar frame

        self.cal = Calendar(cal_frame)
        self.cal.pack(pady=10)

        def get_selected_date():
            selected_date = self.cal.get_date()
            formatted_date = datetime.strptime(selected_date, '%m/%d/%y').strftime('%Y-%m-%d')
            self.date_entry.delete(0, END)
            self.date_entry.insert(0, formatted_date)
            cal_frame.place_forget()  # Hide the calendar frame
        def open_calendar():
            cal_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        #creating entry widgets
        self.name_entry = Entry(f2,textvariable=name_var,font=("Verdana",12 ,"bold"),fg="#FFD700",bg="#111111")
        self.name_entry.place(relx=0.6,rely=0.05,height=30,width=350)
        self.house_label = Label(f2,text=self.house,font=("Verdana",12 ,"bold"),fg="#FFD700",bg="#111111")
        self.house_label.place(relx=0.6,rely=0.15,height=30,width=350)
        self.block_label = Label(f2,text=self.block,font=("Verdana",12 ,"bold"),fg="#FFD700",bg="#111111")
        self.block_label.place(relx=0.6,rely=0.25,height=30,width=350)
        # self.houseno_entry = Entry(f2,textvariable=houseno_var,font=("Verdana",12 ,"bold"),fg="#FFD700",bg="#111111")
        # self.houseno_entry.place(relx=0.6,rely=0.15,height=30,width=350)
        # self.blockno_entry = Entry(f2,textvariable=blockno_var,font=("Verdana",12 ,"bold"),fg="#FFD700",bg="#111111")
        # self.blockno_entry.place(relx=0.6,rely=0.25,height=30,width=350)
        self.username_entry = Entry(f2,textvariable=username_var,font=("Verdana",12 ,"bold"),fg="#FFD700",bg="#111111")
        self.username_entry.place(relx=0.6,rely=0.35,height=30,width=350)
        self.password_entry = Entry(f2,textvariable=password_var,font=("Verdana",12 ,"bold"),fg="#FFD700",bg="#111111")
        self.password_entry.place(relx=0.6,rely=0.45,height=30,width=350)
        self.phone_entry = Entry(f2,textvariable=phone_var,font=("Verdana",12 ,"bold"),fg="#FFD700",bg="#111111")
        self.phone_entry.place(relx=0.6,rely=0.55,height=30,width=350)
        self.date_entry = Entry(f2,font=("Verdana",12 ,"bold"),fg="#FFD700",bg="#111111")
        self.date_entry.place(relx=0.6,rely=0.65,height=30,width=270)
        btn_select_date = Button(f2, text="Select Date", command=open_calendar)
        btn_select_date.place(relx= 0.80, rely=0.65 , height=30, width=70)
        btn_select_date.configure(fg="gold",bg="#111111")
        btn_done = Button(cal_frame, text="Done", command=get_selected_date)
        btn_done.pack()
        upload_button2 = Button(f2, text="UPLOAD", command=upload_profile_picture)
        upload_button2.place(relx=0.115,rely=0.61)
        upload_button2.configure(fg="gold",bg="#111111")

    
        #updating records

        #button to entry these records
        Submit = Button(f2,text="SUBMIT", command = self.update_records,font=("Verdana",12 ,"bold"))
        Submit.configure(activebackground="gold")
        Submit.configure(cursor="hand2")
        Submit.place(relx=0.85,rely=0.75,relheight=0.1,relwidth=0.1)
        Submit.configure(fg="gold",bg="#111111")


    def update_records(self):
        name = self.name_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        phone = self.phone_entry.get()
        date = self.date_entry.get()
        if name=="" and username =="" and password=="" and phone=="0" and date=="":
            tmsg.showerror("EMPTY ENTRY","Please fill the entries")
        else:
            self.cursor.execute(f"INSERT INTO resident (Name,Username,Password,Phone,BlockNo,HouseNo,Join_Date) VALUES (%s,%s,%s,%s,%s,%s,%s)",(name,username,password,phone,self.block,self.house,date))
            self.conn.commit()
            release_connection(self.conn)
            self.root.destroy()
            from Controller import present_Userpage_gui_frame
            present_Userpage_gui_frame(name,username)

        
        
        #self.conn.close_connection()

        # self.conn.commit()
        # self.cursor.close()
        # self.conn.close()
