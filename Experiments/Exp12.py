#Vaibhav Bhaliya   seitb-b3   68
from tkinter import *
import sqlite3
def login():
    uname=username.get()
    pwd=password.get()
    if uname=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
      conn = sqlite3.connect('student.db')
      cursor = conn.execute('SELECT * from ADMIN where USERNAME="%s" and PASSWORD="%s"'%(uname,pwd))
      if cursor.fetchone():
        message.set("Login success")
      else:
        message.set("Wrong username or password!!!")

def Loginform():
    global login_screen
    login_screen = Tk()
    login_screen.title("Vaibhav")
    login_screen.geometry("450x150")
    login_screen["bg"]="#1A2833"
    global  message
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()

    Label(login_screen,width="300",text="Login From", bg="#0A6655",fg="white",font=("Arial",12,"bold")).pack()
    Label(login_screen, text="Username",bg="#1F2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=40)
    Entry(login_screen,textvariable=username,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=42)
    Label(login_screen, text="Password",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=90)
    Entry(login_screen, textvariable=password,show="*",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=92)
    Label(login_screen, text="",textvariable=message,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=95,y=120)
    Button(login_screen, text="Login", width=10, height=1, command=login, bg="#0E6655",fg="white",font=("Arial",12,"bold")).place(x=325,y=65)
    login_screen.mainloop()
Loginform()




# from tkinter import *
# Vaibhav BHaliya  68  seitb-b3
# class Shape:
#     def __init__(self, master=None):
#         self.master = master
#         self.create()
#     def create(self):
#         self.canvas = Canvas(self.master)
#         self.canvas.create_oval(10, 10, 80, 80,outline="black", fill="white", width=2)
#         self.canvas.create_oval(110, 10, 210, 80,outline="red", fill="green", width=2)
#         self.canvas.create_rectangle(230, 10, 290, 60,outline="black", fill="blue", width=2)
#         self.canvas.create_arc(30, 200, 90, 100, start=0, extent=210, outline="green",fill="red", width=2)
#         points = [150, 100, 200, 120, 240, 180, 210, 200, 150, 150, 100, 200]
#         self.canvas.create_polygon(points, outline="blue", fill="orange", width=2)
#         self.canvas.pack(fill=BOTH, expand=1)
#
# if __name__ == "__main__":
#     master = Tk()
#     shape = Shape(master)
#     master.title("Shapes")
#     master.geometry("330x220")
#     mainloop()




# Vaibhav BHaliya  68  seitb-b3
# from tkinter import *
# root = Tk()
# root.geometry('150x150')
# btn = Button(root, text='Destroy!!', bd='5', command=root.destroy)
# btn.pack(side='top')
# btn1 = Button(root, text='Destroy!', bd='5', command=root.destroy)
# btn1.pack(side='top')
# btn2 = Button(root, text='Destroy!!', bd='5', command=root.destroy)
# btn2.pack(side='top')
# root.mainloop()




# Vaibhav BHaliya  68  seitb-b3
# from tkinter import *
#
# def sel():
#     selection = "The option Selected is " + str(var.get())
#     label.config(text=selection)
# root = Tk()
# var = IntVar()
# R1 = Radiobutton(root, text="female", variable=var, value=1, command=sel)
# R1.pack(anchor=W)
# R2 = Radiobutton(root, text="male", variable=var, value=2, command=sel)
# R2.pack(anchor=W)
# label = Label(root)
# label.pack()
# root.mainloop()


# Vaibhav BHaliya  68  seitb-b3
# from tkinter import *
#
# root = Tk()
# root.geometry("150x150")
# def show():
#     label.config(text=clicked.get())
# options = [
# 'science', 'commerce', 'arts'
# ]
# clicked = StringVar()
# clicked.set( "subjects" )
# drop = OptionMenu(root, clicked, *options)
# drop.pack()
# button = Button(root, text="Add", command=show).pack()
# label = Label(root, text=" ")
# label.pack()
# root.mainloop()

