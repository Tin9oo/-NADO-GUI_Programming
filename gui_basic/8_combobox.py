import tkinter.ttk as ttk
from tkinter import *

root =Tk()
root.title("My GUI")    # Title
root.geometry("640x480")

values = [str(i) for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("Card payment date")   # 최초 목록 제목 설정 & 버튼 클릭을 통한 값 설정 가능


ro_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") # 읽기 전용
ro_combobox.current(0) # 0번째 인덱스 값 선택
ro_combobox.pack()


def btncmd():
    print(combobox.get())
    print(ro_combobox.get())

btn = Button(root, text="Select", command=btncmd)
btn.pack()

root.mainloop()