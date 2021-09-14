from tkinter import *
from tkinter import messagebox
import os
import sqlite3


root=Tk()
root.title("Stock Entry Screen")
root.attributes("-fullscreen",True)

varicode=StringVar()
variname=StringVar()
varrate=StringVar()
varqoh=StringVar()


def getautoicode():
    print("here")
    sqlite_file = 'inventorydb.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute("select icode from tblstock")
    data=c.fetchall()
    if(len(data)==0):
        varicode.set("1001")
    else:
        lastrow=data[-1]
        ic=int(lastrow[0])
        ic=ic+1
        print(ic)
        varicode.set(str(ic))
    conn.close()
    
def clear_clicked():
    varicode.set("")
    variname.set("")
    varrate.set("")
    varqoh.set("")
    


def insertitem_clicked():
    sqlite_file = 'inventorydb.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    vic=varicode.get()
    vin=variname.get()
    vr=varrate.get()
    vqoh=varqoh.get()
    c.execute("insert into tblstock(icode,iname,rate,qoh) values (?,?,?,?)",(vic,vin,vr,vqoh))
    messagebox.showinfo("Great","Item Inserted...")
    conn.commit()
    conn.close()
    clear_clicked()
    getautoicode()
    txtiname.focus()


def cancel_clicked():
    root.destroy()


titleLabel=Label(root,text="Stock Entry Screen",font=("Stencil",30),bg='khaki').place(x=600,y=100);

lblicode=Label(root,text="ITEM CODE",font=("Stencil",20),bg='khaki').place(x=520,y=250);
lbliname=Label(root,text="ITEM NAME",font=("Stencil",20),bg='khaki').place(x=520,y=350);
lblrate=Label(root,text="RATE",font=("Stencil",20),bg='khaki').place(x=520,y=450);
lblqoh=Label(root,text="QOH",font=("Stencil",20),bg='khaki').place(x=520,y=550);

txticode=Entry(root,font=("Arial",20),state='disabled',bg='khaki',textvariable=varicode)
txticode.place(x=850,y=250);
txtiname=Entry(root,font=("Arial",20),bg='khaki',textvariable=variname)
txtiname.place(x=850,y=350);
txtrate=Entry(root,font=("Arial",20),bg='khaki',textvariable=varrate)
txtrate.place(x=850,y=450);
txtqoh=Entry(root,font=("Arial",20),bg='khaki',textvariable=varqoh)
txtqoh.place(x=850,y=550);


btnlogin=Button(root,text="INSERT",font=("Stencil",20),bg='khaki',command=insertitem_clicked).place(x=600,y=700);
btncreate=Button(root,text="CLEAR",font=("Stencil",20),bg='khaki',command=clear_clicked).place(x=800,y=700);
btncancel=Button(root,text="CANCEL",font=("Stencil",20),bg='khaki',command=cancel_clicked).place(x=1000,y=700);

getautoicode()
root.mainloop()

