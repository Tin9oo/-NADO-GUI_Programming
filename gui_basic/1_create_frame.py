from tkinter import *

root =Tk()
root.title("My GUI")    # Title
root.geometry("640x480")    # Size & Position
                            # width * length + x pos + y pos

root.resizable(False, False)    # x(width), y(length) value cannot be changed (window size cannot be changed)

root.mainloop()