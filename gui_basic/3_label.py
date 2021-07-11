from tkinter import *

root =Tk()  # main window
root.title("My GUI")    # Title
root.geometry("640x480")

# label : Show text and image
label1 = Label(root, text="Hi")
label1.pack()

photo = PhotoImage(file="gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="See you again")

    # Garbage Collection : 불필요한 메모리 공간 해제
    # 전역변수로 만들어야 해제를 안함
    # 함수 내에서의 이미지 변경은 전역변수 설정이 필요
    global photo2
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)

btn = Button(root, text="Click", command=change)
btn.pack()

root.mainloop()