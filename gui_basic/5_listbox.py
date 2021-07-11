from tkinter import *

root =Tk()
root.title("My GUI")    # Title
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)    # selectmode : extended, single
                                                            # height : 보여주는 개수
listbox.insert(0, "Apple")
listbox.insert(1, "Strawberry")
listbox.insert(2, "Banana")
listbox.insert(END, "Watermellon")
listbox.insert(END, "Graph")
listbox.pack()

def btncmd():
    # delete (position)
    # listbox.delete(0)
    
    # 갯수 확인 ()
    # print("List size is", listbox.size())

    # 항목 확인 (start, end)
    # print("1st to 3rd :", listbox.get(0, 2))
    
    # 선택된 항목 확인 ()
    print("Selected listbox :", listbox.curselection())

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()