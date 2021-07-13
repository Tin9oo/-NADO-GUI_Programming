from tkinter import *

root =Tk()
root.title("My GUI")    # Title
root.geometry("640x480")

def create_new_file():
    print("Create new file")

menu = Menu(root)

# File menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)    # create inner menu
menu_file.add_command(label="New Window")
menu_file.add_separator()   # separator
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File",  menu=menu_file) # create menu in window

# Edit menu (Empty)
menu.add_cascade(label="Edit")

# Insert Language menu (Choose one by radio button)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# View menu
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)

root.mainloop()