from essential import *
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from database import *

class Community_strength:
    def __init__(self,root,name,username):
        self.root = root
        self.name = name
        self.username = username

        #container frame
        f1= Frame(self.root)
        f1.pack(side=TOP, expand = True, fill="both")

        #create a canvas
        my_canvas= Canvas(f1)
        my_canvas.pack(side=LEFT, fill="both", expand= True)

        #main frame
        f2= Frame()
        f2.configure(bg="#222222")

        # Create a vertical scrollbar
        scrollbar = Scrollbar(f2,orient="vertical", command=my_canvas.yview)
        my_canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(relx=0.995, rely=0 , relheight=1, anchor='ne')


        self.conn = get_connection()
        
        self.cursor = self.conn.cursor()

        #get details of resident
        self.cursor.execute("SELECT Name, BlockNo, Houseno, Phone, Join_Date FROM resident")
        resident_details = self.cursor.fetchall()
        print(resident_details)

        #adding main frame to canvas window
        my_canvas.create_window((0,0), window=f2, anchor='nw', width=root.winfo_screenwidth(), height=250+ ((len(resident_details)+1)*240))
        menu2(f2, ["HOME", "COMMUNITY", "LOGOUT"], [LEFT, LEFT, RIGHT], [self.goto_user_page , self.goto_community_page , self.goto_login_page])
        f2.frame2.pack(fill='x')

        #title
        title= Label(f2)
        title.configure(text="COMMUNITY STRENGTH", font=("Roboto", 24, "bold"),fg="#FFD700",bg="#222222")
        title.pack(pady=100, padx=10)


        for i in range(len(resident_details)):
            frames = "f"+str(i+3)
            print(frames)
            frames = Frame(f2)
            frames.configure(bg="#333333", height=200, width=1200)
            frames.pack(pady=20)

            #content under name frame
            name = Label(frames)
            name.configure(text="Name :  "+resident_details[i][0], font=("Roboto", 16, "bold"),fg="#FFD700",bg="#333333")
            name.place(relx=0.1, rely=0.1)

            #content under house frame
            house_no = Label(frames)
            house_no.configure(text="House no. :  "+resident_details[i][1]+"-"+resident_details[i][2], font=("Roboto", 16, "bold"),fg="#FFD700",bg="#333333")
            house_no.place(relx=0.1, rely=0.3)

            #content under phone frame
            house_no = Label(frames)
            house_no.configure(text="Phone no. :  "+resident_details[i][3], font=("Roboto", 16, "bold"),fg="#FFD700",bg="#333333")
            house_no.place(relx=0.1, rely=0.5)

            #content under date of joining frame
            date_join = Label(frames)
            str_date = resident_details[i][4].strftime("%Y-%m-%d")
            date_join.configure(text="Date of Joining :  "+str_date, font=("Roboto", 16, "bold"),fg="#FFD700",bg="#333333")
            date_join.place(relx=0.1, rely=0.7)      

        # Update the scroll region of the canvas
        my_canvas.update_idletasks()
        my_canvas.config(scrollregion=my_canvas.bbox("all"))

        # Close the cursor and connection
        release_connection(self.conn)

    
    def goto_user_page(self):
        from Controller import present_Userpage_gui_frame
        self.root.destroy()
        present_Userpage_gui_frame(self.name, self.username)

    def goto_community_page(self):
        pass

    def goto_login_page(self):
        from Controller import present_Loginpage_gui_frame
        self.root.destroy()
        present_Loginpage_gui_frame()






