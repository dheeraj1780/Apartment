from tkinter import *
from PIL import Image, ImageTk



# def background_img(root,path):
#         #background images for respective windows
#         root.ogimage = Image.open(path)
#         root.rsimage = root.ogimage.resize((900,900))
#         root.bgimg = ImageTk.PhotoImage(root.rsimage)
#         root.img = Label(image=root.bgimg)
#         #root.img.place(relx=0,rely=0)
#         root.img.pack(fill='both')

def title_bar(root, title):
        #frame to hold title
        root.f1 = Frame(root)
        root.f1.configure(bg='#111111')
        root.f1.configure(borderwidth=10)
        root.f1.pack(side=TOP, fill='x')
        #title name
        root.title = Label(root.f1)
        root.title.configure(text=title)
        root.title.configure(font='-family {Poppins SemiBold} -size 26')
        root.title.configure(bg='#111111')
        root.title.configure(fg='gold')
        root.title.pack(padx=50)

def button(root,text,side):
        #buttons
        root.button = Button(root)
        root.button.configure(relief="flat")
        root.button.configure(overrelief="raised")
        root.button.configure(activebackground="#D2463E")
        root.button.configure(cursor="hand2")
        root.button.configure(foreground="#ffffff")
        root.button.configure(background="#D2463E")
        root.button.configure(font="-family {Poppins SemiBold} -size 16")
        root.button.configure(borderwidth="0")
        root.button.configure(text=text)
        root.button.pack(side=side)

def menu1(root,text,side,command):
        #frame for menubar
        root.frame1 = Frame(root)
        root.frame1.configure(relief=RAISED)
        root.frame1.configure(background="#111111")
        #root.frame1.pack(side=TOP, anchor="n", fill=X)
        #menues for menubar
        for i in range(len(text)):
            root.button = Button(root.frame1)
            root.button.configure(relief="flat")
            root.button.configure(overrelief="raised")
            root.button.configure(activebackground="#222222")
            root.button.configure(cursor="hand2")
            root.button.configure(foreground="gold")
            root.button.configure(background="#111111")
            root.button.configure(font="-family {Poppins SemiBold} -size 16")
            root.button.configure(borderwidth="0")
            root.button.configure(text=text[i])
            root.button.configure(command=command[i])
            root.button.pack(side=side[i],fill=X)

def menu2(root,text,side,command):
        #frame for menubar
        root.frame2 = Frame(root)
        root.frame2.configure(relief=RAISED)
        root.frame2.configure(background="#111111")
        #root.frame2.pack(side=TOP, anchor="n", fill=X)
        #menues for menubar
        for i in range(len(text)):
            root.button = Button(root.frame2)
            root.button.configure(relief="flat")
            root.button.configure(overrelief="raised")
            root.button.configure(activebackground="#222222")
            root.button.configure(cursor="hand2")
            root.button.configure(foreground="gold")
            root.button.configure(background="#111111")
            root.button.configure(font="-family {Poppins SemiBold} -size 16")
            root.button.configure(borderwidth="0")
            root.button.configure(text=text[i])
            root.button.configure(command=command[i])
            root.button.pack(side=side[i],fill=X)
        
def imageshow(root, path, width, height):
        #to show images
        root.ogimage = Image.open(path)
        root.rsimage = root.ogimage.resize((width, height))
        root.photo = ImageTk.PhotoImage(root.rsimage)
        root.images = Label(image=root.photo)
        root.images.pack()

