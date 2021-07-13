from tkinter import *
from typing import List

root =Tk()
root.title("My GUI")    # Title
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set이 없으면 스크롤을 내려도 다시 올라온다.
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32):
    listbox.insert(END, str(i))
listbox.pack(side="left")

# 리스트 박스의 스크롤을 매핑
scrollbar.config(command=listbox.yview)

root.mainloop()