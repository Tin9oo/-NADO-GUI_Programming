from tkinter import *

root =Tk()
root.title("My GUI")    # Title
root.geometry("640x480")

Label(root, text="Select menu").pack()  # 변경할 것이 아니기 때문에 바로 팩

burger_var = IntVar()   # int형으로 값을 저장
btn_burger1 = Radiobutton(root, text="Hamburger", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="Cheeseburger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="Chickenburger", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="Select drink").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="Coke", value="Coke", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="Sprite", value="Sprite", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get()) # return selected value
    print(drink_var.get())

btn = Button(root, text="Order", command=btncmd)
btn.pack()

root.mainloop()