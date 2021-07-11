import time
import tkinter.ttk as ttk
from tkinter import *

root =Tk()
root.title("My GUI")    # Title
root.geometry("640x480")

# # indeterminate : 끝날 시간이 결정되지 않음
# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# # indeterminate : 끝날 시간이 결정되지 않음
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10)   # 10 ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop()

# btn = Button(root, text="Interrupt", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)    # 0.01 sec wait

        p_var2.set(i)   # set progress bar value
        progressbar2.update()   # GUI update
        print(p_var2.get())

btn2 = Button(root, text="Start", command=btncmd2)
btn2.pack()

root.mainloop()