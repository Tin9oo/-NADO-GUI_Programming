from tkinter import *

root =Tk()
root.title("My GUI")    # Title
root.geometry("640x480")

txt = Text(root, width=30, height=5)    # 우리가 아는 평범한 텍스트 상자
txt.pack()
txt.insert(END, "Input text")

e = Entry(root, width=30)   # 한줄 입력
e.pack()
e.insert(0, "Input a line") # 현재는 값이 비어있으므로 END를 써도 무방합니다.

def btncmd():
    print(txt.get("1.0", END))  # 첫번째 줄 첫 글자부터 마지막까지 가져와라
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()