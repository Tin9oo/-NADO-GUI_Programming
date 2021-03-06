from tkinter import *

root =Tk()
root.title("My GUI")    # Title
root.geometry("640x480")

Label(root, text="Select a menu").pack(side="top")

Button(root, text="Order").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="Hamburger").pack()
Button(frame_burger, text="Cheeseburger").pack()
Button(frame_burger, text="Chickenburger").pack()

frame_drink = LabelFrame(root, text="Drink")
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="Coke").pack()
Button(frame_drink, text="Sprite").pack()

root.mainloop()