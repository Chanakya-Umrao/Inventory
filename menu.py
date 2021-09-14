from tkinter import filedialog
from tkinter import *
import os

def AddSubject():
    root.destroy()
    os.system('stockadd.py')
    
def ModifySubject():
    root.destroy()
    os.system('stockupdate.py')

def SubjectIssue():
    print ("Subject ISSUE")
def SubjectReceipt():
    print ("Subject RECEIPT")

def ReportAllItems():
    root.destroy()
    os.system('allitemreport.py')

def ReportAllIssue():
    print ("Report All Issue")

def ReportAllReceipt():
    print ("Report All Receipt")


    
root = Tk()
root.attributes("-fullscreen",True)
root.title("Main Menu")

menu = Menu(root)
root.config(menu=menu)
stockmenu = Menu(menu)
transactionmenu = Menu(menu)
reportmenu = Menu(menu)
exitmenu = Menu(menu)

menu.add_cascade(label="Stock", menu=stockmenu)
menu.add_cascade(label="Transaction", menu=transactionmenu)
menu.add_cascade(label="Reports", menu=reportmenu)
menu.add_cascade(label="Exit", menu=exitmenu)

stockmenu.add_command(label="Add Item", command=StockAddItem)
stockmenu.add_separator()
stockmenu.add_command(label="Modify Item", command=StockModifyItem)

transactionmenu.add_command(label="Item Issue", command=StockIssue)
transactionmenu.add_separator()
transactionmenu.add_command(label="Item Receipt", command=StockReceipt)

reportmenu.add_command(label="All Items Details", command=ReportAllItems)
reportmenu.add_command(label="All Issue Details", command=ReportAllIssue)
reportmenu.add_command(label="All Receipts Details", command=ReportAllReceipt)
reportmenu.add_command(label="Single Item Details")

exitmenu.add_command(label="Quit App",command=root.destroy)

mainloop()
