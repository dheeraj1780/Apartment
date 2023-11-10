from essential import *
from tkinter import *
from PIL import Image, ImageTk
from user import User
from database import *



class Login:
    def __init__(self,root):
        self.root = root
        menu1(root, ["HOME", "COMMUNITY", "LOGIN"], [LEFT, LEFT, RIGHT], [self.goto_home_page,self.goto_community_page, self.goto_login_page])
        self.root.frame1.pack(side=TOP, anchor="n", fill=X)

        self.conn = get_connection()
        self.cursor = self.conn.cursor()

        #self.user_page = User(self.root)

        #self.root = Frame(root, bg="#666666")

        self.f2 = Frame(self.root,bg = "black", height = 300 , width = 440)
        self.f2.place(relx=0.35, rely=0.35)

        self.heading= Label(self.root, text="Log In", font=("Roboto", 32, "bold"),fg="#FFD700",bg="#666666")
        self.heading.place(relx=0.45,rely=0.20)

        self.user = Label(self.f2, text="Username", font=("Verdana",16 ,"bold"),fg="#FFD700",bg="black")    #user label
        self.password = Label(self.f2, text="Password", font=("Verdana",16 ,"bold"),fg="#FFD700",bg="black")    #password label
        self.user.place(relx=0.05,rely=0.05,width=140,height=30)     #relative positioning of label wrt self.f2
        self.password.place(relx=0.05,rely=0.35,width=140,height=30)

        self.username_val=StringVar()    #variable assigning for storing entries
        self.password_val=StringVar()

        self.userentry = Entry(self.f2, textvariable = self.username_val, borderwidth=2, relief="sunken", bg="grey", fg="#FFD700")     #entry box
        self.userentry.configure(font="-family Verdana -size 16")
        self.passentry = Entry(self.f2, textvariable = self.password_val, borderwidth=2, relief="sunken", bg="grey", fg="#FFD700")     #grid pack place are geometry manager must use only one   
        self.userentry.configure(font="-family Verdana -size 16")
        self.userentry.place(relx=0.05,rely=0.2,width=400,height=40)     #relative positioning of label wrt self.f2
        self.passentry.place(relx=0.05,rely=0.5,width=400,height=40)     #relative positioning of label wrt self.f2


        submit=Button(self.f2)      #submit-button 
        submit.configure(relief="flat")
        submit.configure(overrelief="raised")
        submit.configure(activebackground="grey")
        submit.configure(cursor="hand2")
        submit.configure(foreground="#FFD700")
        submit.configure(background="black")
        submit.configure(font="-family Verdana -size 16")
        submit.configure(borderwidth="0")
        submit.configure(text="SUBMIT")
        submit.configure(command=self.goto_user_page)
        submit.place(relx=0.05,rely=0.8,width=90,height=40)


    def goto_user_page(self):
        user = self.userentry.get()
        psd = self.passentry.get()
        self.cursor.execute('Select Name FROM resident WHERE Username = %s AND Password = %s',(user,psd))
        name = self.cursor.fetchall()
        self.conn.commit()
        from Controller import present_Userpage_gui_frame
        self.root.destroy()
        present_Userpage_gui_frame(name[0][0],user)
        #self.root.frame1.pack_forget()
        # menu2(self.root, ["HOME", "COMMUNITY", "LOGOUT"], [LEFT, LEFT, RIGHT], [a,b,c])
        # self.root.frame2.pack(side=TOP, anchor="n", fill=X)
        # self.user_page.root.pack(side=TOP, expand = True, fill="both")

    def goto_home_page(self):
        from Controller import present_Homepage_gui_frame
        self.root.destroy()
        present_Homepage_gui_frame()

    def goto_community_page(self):
        from Controller import present_Communitypage_gui_frame
        self.root.destroy()
        present_Communitypage_gui_frame()

    def goto_login_page(self):
        pass



        





        
    

        


