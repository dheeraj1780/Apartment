from essential import *
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tmsg
import mysql.connector
import io
from database import *

class Make_announcement:
    def __init__(self,root,name,username):
        self.root = root
        self.name = name
        self.username = username

        menu2(self.root, ["HOME", "LOGOUT"], [LEFT, RIGHT], [self.goto_user_page , self.goto_login_page])
        self.root.frame2.pack(side=TOP, anchor="n", fill=X)

        def repack_frame():
            self.root.pack_forget()  # Remove the frame     
            self.root.pack(side=TOP, expand = True, fill="both")
            self.conn = get_connection()
            self.cursor = self.conn.cursor()
        def clear_content():
            self.text_content = content.delete("1.0","end")
            self.list_path = []
            self.gallery.destroy()
            self.gallery = Label(f2)

        #main frame
        # self.root= Frame(self.root)
        # self.root.configure(bg="#222222")
        

        self.conn = get_connection()
        
        self.cursor = self.conn.cursor()

        #image carousel frame
        f2 = Frame(self.root)
        f2.configure(bg="#333333")
        f2.place(relx=0.62,rely=0.4,relheight=0.35,relwidth=0.35)

        #content under due payment frame
        maintenance = Label(self.root)
        maintenance.configure(text="YOUR ANNOUNCEMENT", font=("Roboto", 24, "bold"),fg="#FFD700",bg="#222222")
        maintenance.place(relx=0.40, rely=0.25)

        content = Text(self.root)
        content.place(relx=0.1,rely=0.4, relheight=0.4, relwidth=0.5)

        self.list_path = []
        self.text_content = ""
        self.gallery = Label(f2)

        #carousel picture changing variable
        self.i=0


        def Pass():
            self.text_content = content.get("1.0", "end")      # Get text from line 1, character 0 to end
            if len(self.list_path)==3:
                image_data1=self.list_path[0]
                image_data2=self.list_path[1]
                image_data3=self.list_path[2]
            elif len(self.list_path)==2:
                image_data1=self.list_path[0]
                image_data2=self.list_path[1]
                image_data3=""
            elif len(self.list_path)==1:
                image_data1=self.list_path[0]
                image_data2=""
                image_data3=""
            else:
                image_data1=""
                image_data2=""
                image_data3=""

            if self.text_content=='''
''':
                tmsg.showwarning("EMPTY","Your announcement is empty")
            else:
            #print(f"INSERT INTO announcement(announcer_name, announcement_datetime, announcement_text, image1, image2, image3)VALUES ('John Doe', NOW(), '{self.text_content}', {image_data1}, {image_data2}, {image_data3});")
                self.cursor.execute(f"INSERT INTO announcement(Name, announcement_datetime, announcement_text, announcer_name, image1, image2, image3) VALUES (%s,NOW(),%s,%s,%s,%s)",(self.name,self.text_content,image_data1,image_data2,image_data3))
                self.conn.commit()

                release_connection(self.conn)
                # self.text_content = content.delete("1.0","end")
                # self.list_path.clear()
                repack_frame()
                clear_content()


        def Pics():
            self.i= len(self.list_path)
            if (self.i < 3) :
                file_path = filedialog.askopenfilename(filetypes=[('Image files', '*.png')])
                #opening the image in LBOB
                with open(file_path,'rb') as file:
                    image_data = file.read()
                #appending the LBOB in a list
                self.list_path.append(image_data)

                #opening the image in the carousel
                image_obj = Image.open(file_path)
                resize_image = image_obj.resize((250,250))
                img= ImageTk.PhotoImage(resize_image)

                #creating label to show the pic
                self.gallery.image = img
                self.gallery['image'] = img
                self.gallery.place(relx=0.1,rely=0.0, relheight=1, relwidth=0.8)
            else:
                tmsg.showinfo("Alert","You can't upload more than 3 images!")
            return self.list_path

        def Right_carousel():
            self.i+=1
            index= self.i%len(self.list_path)
            image_obj = Image.open(io.BytesIO(self.list_path[index]))
            resize_image = image_obj.resize((250,250))
            img= ImageTk.PhotoImage(resize_image)

            #creating a label to display the profile picture.
            self.gallery = Label(f2)
            self.gallery.image = img
            self.gallery['image']=img
            self.gallery.place(relx=0.1,rely=0.0, relheight=1, relwidth=0.8)

        def Left_carousel():
            self.i-=1
            index= self.i%len(self.list_path)
            image_obj = Image.open(io.BytesIO(self.list_path[index]))
            resize_image = image_obj.resize((250,250))
            img= ImageTk.PhotoImage(resize_image)

            #creating a label to display the profile picture.
            self.gallery = Label(f2)
            self.gallery.image = img
            self.gallery['image']=img
            self.gallery.place(relx=0.1,rely=0.0, relheight=1, relwidth=0.8)

        #to move the carousel towards right
        Right = Button(f2)
        Right.place(relx= 0.96 , rely= 0.4)
        Right.configure(text=">",height=3,width=1,bg="#111111")
        Right.configure(command=Right_carousel)
        Right.configure(activebackground="#555555")
        Right.configure(cursor="hand2")

        #to move the carousel towards left
        Left = Button(f2)
        Left.place(relx= 0.0 , rely= 0.4)
        Left.configure(text="<",height=3,width=1,bg="#111111")
        Left.configure(command=Left_carousel)
        Left.configure(activebackground="#555555")
        Left.configure(cursor="hand2")

        #submit button
        Submit = Button(self.root)
        Submit.pack()
        Submit.place(relx= 0.60, rely=0.85)
        Submit.configure(text="Submit",height=3, width=10, bg="gold", fg="black")
        Submit.configure(command=Pass)
        Submit.configure(activebackground="#333333")
        Submit.configure(cursor="hand2")

        Upload = Button(self.root)
        Upload.pack()
        Upload.place(relx=0.75, rely=0.76)
        Upload.configure(text="Upload pictures",height=2, width=12, bg="#111111", fg="black")
        Upload.configure(command=Pics)
        Upload.configure(activebackground="#333333")
        Upload.configure(cursor="hand2")


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





