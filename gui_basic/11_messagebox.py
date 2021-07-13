import tkinter.messagebox as msgbox
from tkinter import *

root =Tk()
root.title("My GUI")    # Title
root.geometry("640x480")

def info():
    msgbox.showinfo("Alert", "Book is successed.")
    
def warn():
    msgbox.showwarning("Warning", "Sold out.")

def error():
    msgbox.showerror("Error", "Error is occured")


def okcancle():
    msgbox.askokcancel("Okay / Cancle", \
        "This seat is not recommended for you. Are you okay?")

def retrycancle():
    response = msgbox.askretrycancel("Retry / Cancle", \
        "Temporary error in the field. Do you want to try again?")
    if response == 1:
        print("Retry")
    elif response == 0:
        print("Cancel")

def yesno():
    msgbox.askyesno("Yes / No", \
        "This seat is reversed. Do you wnat to book?")

def yesnocancle():
    response = msgbox.askyesnocancel(title=None, \
        message="Book list is not saved.\nAre you quit after save?")
    # Yes : Save and Quit
    # No : Unsave and Quit
    # Cancel : Continue
    print("Response :", response)   # True, False, None -> Yes : 1, No : 0, Canscel : Other
    if response == 1:
        print("Yes")
    elif response == 0:
        print("No")
    else:
        print("Cancel")

Button(root, command=info, text="Alert").pack()
Button(root, command=warn, text="Warning").pack()
Button(root, command=error, text="Error").pack()

Button(root, command=okcancle, text="Ok Cancle").pack()
Button(root, command=retrycancle, text="Retry Cancle").pack()
Button(root, command=yesno, text="Yes No").pack()
Button(root, command=yesnocancle, text="Yes No Cancle").pack()

root.mainloop()