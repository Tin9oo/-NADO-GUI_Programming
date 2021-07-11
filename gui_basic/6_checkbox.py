from tkinter import *

root =Tk()
root.title("My GUI")    # Title
root.geometry("640x480")

chkvar = IntVar()   # chkvar에 int형으로 값을 저장
chkbox = Checkbutton(root, text="Don't see today", variable=chkvar)
# chkbox.select() # 자동 선택 처리
# chkbox.deselect()   # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="Don't see anymore", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0: uncheck, 1 : check
    print(chkvar2.get())

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()