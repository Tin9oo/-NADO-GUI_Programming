import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog # __all__에 정의되어있지 않은 submodule입니다.

root =Tk()
root.title("My GUI") # Title

# Add file
def add_file():
    files = filedialog.askopenfilenames(title="Select image file", \
        filetypes=(("PNG File", "*.png"), ("All File", "*.*")), \
            initialdir=r"D:\OneDrive - 영남대학교\대학교\Programing Study\NADOCODING\pygame_project\images")
            # initialdir= : 최초에 사용자가 지정한경로를 보여줌
            # Row string : 탈출문자건 뭐건 그대로 쓰겠다.

    # User select file list
    for file in files:
        list_file.insert(END, file)

# Delete file
# 삭제시 인덱스가 당겨지는 것을 주의해야 한다.
# 따라서 뒤에서부터 지운다.
def del_file():
    print(list_file.curselection())

    for index 

# File frame(add file, delete selected file)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="Add File", command=add_file)
# The reason of Using both padx and width
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="Delete File", command=del_file)
btn_del_file.pack(side="right")

# List frame
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# Storage path frame
path_frame = LabelFrame(root, text="Storage Path")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

btn_dest_path = Button(path_frame, text="Search", width=10)
btn_dest_path.pack(side="right", padx=5, pady=5)

# Option frame
frame_option = LabelFrame(root, text="Option")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. Width option
lbl_width = Label(frame_option, text="Width", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

opt_width = ["Keep original text", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. Interval option
lbl_interval = Label(frame_option, text="Interval", width=8)
lbl_interval.pack(side="left", padx=5, pady=5)

opt_interval = ["None", "Narrow", "Standard", "Wide"]
cmb_interval = ttk.Combobox(frame_option, state="readonly", values=opt_interval, width=10)
cmb_interval.current(0)
cmb_interval.pack(side="left", padx=5, pady=5)

# 3. File format option
lbl_format = Label(frame_option, text="Format", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# Progress bar
frame_progress = LabelFrame(root, text="Progress")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# Run
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="Close", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="Start", width = 12)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False)    # x(width), y(length) value cannot be changed (window size cannot be changed)

root.mainloop()