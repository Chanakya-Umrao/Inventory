from tkinter import *
import time

root=Tk()
root.title("Splash Screen")
root.geometry("700x650")
root.grid_columnconfigure(0, weight=1)
root.config(bg='white')
titleLabel0=Label(root,text=" ",font=("Stencil",50),bg='white')
titleLabel0.grid(row=0,column=0)
titleLabel1=Label(root,text="WELCOME TO",font=("Stencil",50),fg='black')
titleLabel1.grid(row=1,column=0)
titleLabel2=Label(root,text="CHANAKYA",font=("Stencil",50),fg='black')
titleLabel2.grid(row=3,column=0)
titleLabel3=Label(root,text="ACADEMY",font=("Stencil",50),fg='black')
titleLabel3.grid(row=4,column=0)
titleLabel3=Label(root,text="",font=("Stencil",50),bg='white')
titleLabel3.grid(row=5,column=0)
nameLabel3=Label(root,text="Submitted by: CHANAKYA UMRAO",font=("Stencil",25),fg='black')
nameLabel3.grid(row=6,column=0)
import os
def waitfn():
    time.sleep(1)
    root.destroy()
    os.system("loginscreen.py")

root.after(2000,waitfn)
root.mainloop()
