from essential import *
from tkinter import *
from PIL import Image, ImageTk
from payment import Payment
# import mysql.connector
from database import *



class JoinUs:
    def __init__(self,root):
        self.root = root

        menu1(root, ["HOME", "COMMUNITY", "LOGIN"], [LEFT, LEFT, RIGHT], [self.goto_home_page,self.goto_community_page, self.goto_login_page])
        self.root.frame1.pack(side=TOP, anchor="n", fill=X)

        #self.root = Frame(root, bg="#222222")

        #self.payment_page = Payment(self.root,'A','1')

        heading = Label(self.root,text="Join Us", font=("Roboto", 32, "bold"),fg="#FFD700",bg="#222222")
        heading.place(relx=0.45,rely=0.10)

        #estabhlishing connection
        self.conn = get_connection()
        self.cursor = self.conn.cursor()
        text1 = Label(self.root,text="All Paper Works are free of cost\n free movers and packers\nfriendly community", font=("Roboto", 24, "bold"),fg="#111111",bg="#222222")
        text1.place(relx=0.35,rely=0.2)

        text2 = Label(self.root,text="SELECT YOUR SWEET HOME", font=("Roboto", 24, "bold"),fg="#FFD700",bg="#222222")
        text2.place(relx=0.35,rely=0.4)

        self.cursor.execute("SELECT * FROM block WHERE Availability = 0")
        results = self.cursor.fetchall()

        release_connection(self.conn)

        f2=Frame(self.root)
        scrollbar = Scrollbar(f2)
        self.lbx = Listbox(f2, yscrollcommand=scrollbar.set)
        self.lbx.configure(bg="#111111",width=72,fg="gold")
        scrollbar.config(command=self.lbx.yview, orient=VERTICAL)
        f2.pack()
        f2.configure(bg="#111111")
        f2.place(relx=0.32, rely= 0.47)
        scrollbar.pack(side=RIGHT, fill=Y)
        # scrollbar.configure(bg="#111111",fg="gold")
        self.lbx.pack()

        #inserting the unoccupied house details in the list box
        for i in range(len(results)):
            block = results[i][0]
            house = results[i][1]
            bhk = results[i][3]
            self.lbx.insert(END, f"Block no. - {block} House no. - {house} BHK - {bhk}")
            self.lbx.configure(font=("Roboto", 10, "bold"))


        #proceed button to provide the details of the selected house
        Proceed = Button(f2)
        Proceed.pack(anchor='s')
        Proceed.configure(text="Proceed")
        Proceed.configure(command=self.goto_Payment_page)
        Proceed.configure(bg="gold", fg="#111111")
        Proceed.configure(activebackground="gold")
        Proceed.configure(cursor="hand2")


    def goto_Payment_page(self):
        # self.root.pack_forget()
        # self.root.frame.pack_forget()
        #self.payment_page.root.pack(side=TOP, expand = True, fill="both")
        from Controller import present_Paymentpage_gui_frame
        detail=self.lbx.get(self.lbx.curselection())
        block=detail[12]
        house=detail[26:28]
        self.root.destroy()
        present_Paymentpage_gui_frame(block,house)

        #self.payment_page = Payment(self.root, block, house)
        # self.payment_page.root.pack(side=TOP, expand=True, fill="both")
        # self.conn.close_connection()
        # self.conn.commit()
        # self.cursor.close()
        # self.conn.close()

    def goto_home_page(self):
        from Controller import present_Homepage_gui_frame
        self.root.destroy()
        present_Homepage_gui_frame()

    def goto_community_page(self):
        from Controller import present_Communitypage_gui_frame
        self.root.destroy()
        present_Communitypage_gui_frame()

    def goto_login_page(self):
        from Controller import present_Loginpage_gui_frame
        self.root.destroy()
        present_Loginpage_gui_frame()




