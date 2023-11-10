from essential import *
from tkinter import *
from PIL import Image, ImageTk
from database import *
from io import BytesIO
from maintenance_records import Maintenance_records
from make_announcement import Make_announcement
from community_strength import Community_strength
from update_profile import Update_profile


class User:
    def __init__(self,root,name,username):
        self.root = root
        self.name = name 
        self.username = username

        menu2(self.root, ["HOME", "COMMUNITY", "LOGOUT"], [LEFT, LEFT, RIGHT], [self.goto_user_page , self.goto_community_page , self.goto_login_page])
        self.root.frame2.pack(side=TOP, anchor="n", fill=X)

        #main frame
        # self.root= Frame(self.root)
        # self.f1.configure(bg="#222222")

        self.conn = get_connection()
        
        self.cursor = self.conn.cursor()

        # self.maintenance_records_page = Maintenance_records(self.root)
        # self.make_announcement_page = Make_announcement(self.root)
        # self.community_strength_page = Community_strength(self.root)

        #annoucement frame
        f2= Frame(self.root)
        f2.configure(bg="gold")
        f2.pack(side=RIGHT, fill=Y)
        f2.configure(width=390)


        heading1 = Label(self.root,text=f"WELCOME {self.name}", font=("Roboto", 32, "bold"),fg="gold",bg="#222222")
        heading1.place(relx=0.35,rely=0.20,anchor='center')


        #various operations


        def Edit_Your_Profile():
            from Controller import present_Update_Profile_gui_frame
            self.root.destroy()
            present_Update_Profile_gui_frame(self.name, self.username)

        def Pay_Maintanence():
            from Controller import present_Maintenance_Records_gui_frame
            self.root.destroy()
            present_Maintenance_Records_gui_frame(self.name, self.username)
            #self.maintenance_records_page.root.pack(side=TOP, expand = True, fill="both")

        def Announcement_To_Community():
            from Controller import present_Make_Announcement_gui_frame
            self.root.destroy()
            present_Make_Announcement_gui_frame(self.name, self.username)
            #self.make_announcement_page.root.pack(side=TOP, expand = True, fill="both")

        def View_Our_Community_Strength():
            from Controller import present_Community_Strength_gui_frame
            self.root.destroy()
            present_Community_Strength_gui_frame(self.name, self.username)
            #self.community_strength_page.root.pack(side=TOP, expand = True, fill="both")

###################################################################################################
        def Images_for_announcements(current_id):
            f4 = Frame(self.root)
            f4.configure(bg="#111111")
            f4.place(relx=0.1,rely=0.1,relheight=0.8,relwidth=0.8)
            
            print("this is the id of that respective annuoncement for displaying images",current_id)

            self.cursor.execute("SELECT image1,image2,image3 from announcement WHERE id = "+str(current_id))
            image_data = self.cursor.fetchall()

            image_data = [tuple(x for x in sub_tuple if x != b'') for sub_tuple in image_data]

            def exit():
                f4.destroy()
            Close_button = Button(f4)
            Close_button.configure(text="X")
            Close_button.configure(bg="red")
            Close_button.configure(activebackground="blue")
            Close_button.configure(command=exit)
            Close_button.place(relx=0.983,rely=0)

            if image_data==[]:
                msg=Label(f4)
                msg.configure(text="no images uploaded")
                msg.configure(bg="#111111")
                msg.configure(font=("Roboto", 24, "bold"))
                msg.place(relx=0.35,rely=0.4)
            elif image_data==[(b'', b'', b'')]:
                msg=Label(f4)
                msg.configure(text="no images uploaded")
                msg.configure(bg="#111111")
                msg.configure(font=("Roboto", 24, "bold"))
                msg.place(relx=0.35,rely=0.4)
            elif image_data==[()]:
                msg=Label(f4)
                msg.configure(text="no images uploaded")
                msg.configure(bg="#111111")
                msg.configure(font=("Roboto", 24, "bold"))
                msg.place(relx=0.35,rely=0.4)
            else:
                #opening the image in the carousel
                image_obj = Image.open(BytesIO(image_data[0][0]))
                resize_image = image_obj.resize((250,250))
                img= ImageTk.PhotoImage(resize_image)

                #creating label to show the pic
                gallery = Label(f4)
                gallery.image = img
                gallery['image'] = img
                gallery.place(relx=0.1,rely=0.1, relheight=0.8, relwidth=0.8)

            if image_data!=[] and image_data!=[(b'', b'', b'')] and image_data!=[()]:
                self.i=0
                def Right_carousel():
                    self.i+=1
                    index= self.i%len(image_data[0])
                    image_obj = Image.open(BytesIO(image_data[0][index]))
                    resize_image = image_obj.resize((250,250))
                    img= ImageTk.PhotoImage(resize_image)
                    print(self.i%len(image_data[0]))
                    #creating a label to display the profile picture.
                    self.gallery = Label(f4)
                    self.gallery.image = img
                    self.gallery['image']=img
                    self.gallery.place(relx=0.1,rely=0.1, relheight=0.8, relwidth=0.8)

                def Left_carousel():
                    self.i-=1
                    index= self.i%len(image_data[0])
                    image_obj = Image.open(BytesIO(image_data[0][index]))
                    resize_image = image_obj.resize((250,250))
                    img= ImageTk.PhotoImage(resize_image)
                    print(self.i%len(image_data[0]))
                    #creating a label to display the profile picture.
                    self.gallery = Label(f4)
                    self.gallery.image = img
                    self.gallery['image']=img
                    self.gallery.place(relx=0.1,rely=0.1, relheight=0.8, relwidth=0.8)

                #to move the carousel towards right
                Right = Button(f4)
                Right.place(relx= 0.96 , rely= 0.4)
                Right.configure(text=">",height=3,width=1,bg="#111111")
                Right.configure(command=Right_carousel)
                Right.configure(activebackground="#555555")
                Right.configure(cursor="hand2")

                #to move the carousel towards left
                Left = Button(f4)
                Left.place(relx= 0.0 , rely= 0.4)
                Left.configure(text="<",height=3,width=1,bg="#111111")
                Left.configure(command=Left_carousel)
                Left.configure(activebackground="#555555")
                Left.configure(cursor="hand2")

###################################################################################################

        #buttons for various operations
        button1 = Button(self.root)
        button1.configure(text="=> Edit Your Profile")
        button1.configure(font=("Roboto", 24, "bold"))
        button1.configure(fg="gold",bg="#111111")
        button1.configure(activebackground="gold")
        button1.configure(command=Edit_Your_Profile)
        button1.place(relx=0.1,rely=0.3)

        button2 = Button(self.root)
        button2.configure(text="=> Pay Maintanance")
        button2.configure(font=("Roboto", 24, "bold"))
        button2.configure(fg="gold",bg="#111111")
        button2 .configure(activebackground="gold")
        button2.configure(command=Pay_Maintanence)
        button2.place(relx=0.1,rely=0.4)

        button3 = Button(self.root)
        button3.configure(text="=> Announcement To Community")
        button3.configure(font=("Roboto", 24, "bold"))
        button3.configure(fg="gold",bg="#111111")
        button3 .configure(activebackground="gold")
        button3.configure(command=Announcement_To_Community)
        button3.place(relx=0.1,rely=0.5)

        button4 = Button(self.root)
        button4.configure(text="=> View Our Community Strength")
        button4.configure(font=("Roboto", 24, "bold"))
        button4.configure(fg="gold",bg="#111111")
        button4 .configure(activebackground="gold")
        button4.configure(command=View_Our_Community_Strength)
        button4.place(relx=0.1,rely=0.6)

        #content in annoucement frame
        heading2 = Label(f2,text="Announcement", font=("Roboto", 16, "bold"),fg="gold",bg="#222222")
        heading2.place(relx=0.25,rely=0.2,anchor='center')


        def carousel(announcements):
            print(announcements)
            f3= Frame(f2)
            content = Text(f3)
            content.pack()
            announcement=announcements
            scrollbar = Scrollbar(f3, command=content.yview)
            content.config(yscrollcommand=scrollbar.set)
            scrollbar.pack(side="right", fill="y")
            detail = Label(f3)
            detail.place(relx=0.01,rely=0.9, relheight=0.05, relwidth=0.95)
            v=announcement[0][1]
            n=announcement[0][2]
            d=announcement[0][3]
            format_d = d.strftime("%Y-%m-%d %H:%M:%S")
            content.insert("1.0",v)
            detail.configure(bg="red" , text="from : "+n+" on : "+format_d)
            
            i=0
            current_id=0
            def right():
                nonlocal i
                nonlocal current_id
                content.configure(state="normal")
                content.delete("1.0","end")
                i=(i+1)%(len(announcement))
                text=announcement[i][1]
                n=announcement[i][2]
                d=announcement[i][3]
                current_id=announcement[i][0]
                print(current_id)
                content.insert("1.0",text)
                content.configure(state="disabled")
                detail.configure(bg="red" , text="from : "+n+" on : "+format_d)
                return current_id

            def left():
                nonlocal i
                nonlocal current_id
                content.configure(state="normal")
                content.delete("1.0","end")
                i=(i-1)%(len(announcement))
                text=announcement[i][1]
                n=announcement[i][2]
                d=announcement[i][3]
                current_id=announcement[i][0]
                print(current_id)
                content.insert("1.0",text)
                content.configure(state="disabled")
                detail.configure(bg="red" , text="from : "+n+" on : "+format_d)
                return current_id
            
            # content.insert("1.0",[0])
            

        #left button
            right_but = Button(f2, text=">")
            right_but.configure(fg="#222222",bg="gold")
            right_but.configure(command=right)
            right_but.place(relx=0.9 ,rely=0.5)

        #right button
            left_but = Button(f2, text="<")
            left_but.configure(fg="#222222",bg="gold")
            left_but.configure(command=left)
            left_but.place(relx=0.05 ,rely=0.5)
            
            content.config(state=DISABLED)
            
            f3.place(relx=0.1, rely=0.27, relheight=0.5, relwidth=0.8)
###################################################################################################
            button5 = Button(f3)
            button5.configure(text="Images attached")
            button5.configure(font=("Roboto", 10, "bold"))
            button5.configure(fg="gold",bg="#111111")
            button5 .configure(activebackground="gold")
            button5.configure(command=lambda:Images_for_announcements(current_id))
            button5.place(relx=0.35,rely=0.7)
####################################################################################################
        self.cursor.execute(f"SELECT id,announcement_text,Name,announcement_datetime FROM announcement")
        results = self.cursor.fetchall()
        carousel(results)


        # Close the cursor and connection
        release_connection(self.conn)

    
    # def user_hide_all(self):
    #         self.root.pack_forget()
    #         self.maintenance_records_page.root.pack_forget()
    #         self.make_announcement_page.root.pack_forget()
    #         self.community_strength_page.root.pack_forget()

    def goto_user_page(self):
        pass

    def goto_community_page(self):
        pass

    def goto_login_page(self):
        from Controller import present_Loginpage_gui_frame
        self.root.destroy()
        present_Loginpage_gui_frame()
       





