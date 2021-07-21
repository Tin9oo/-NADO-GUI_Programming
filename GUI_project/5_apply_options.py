import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog # __all__에 정의되어있지 않은 submodule입니다.
from PIL import Image

root =Tk()
root.title("My GUI") # Title

# Add file
def add_file():
    files = filedialog.askopenfilenames(title="Select image file", \
        filetypes=(("PNG File", "*.png"), ("All File", "*.*")), \
            initialdir=r"D:\OneDrive - 영남대학교\대학교\Programing Study\NADOCODING\GUI Programming")
            # initialdir= : 최초에 사용자가 지정한경로를 보여줌
            # Row string : 탈출문자건 뭐건 그대로 쓰겠다.

    # User select file list
    for file in files:
        list_file.insert(END, file)

# Delete file
# 삭제시 인덱스가 당겨지는 것을 주의해야 한다.
# 따라서 뒤에서부터 지운다.
def del_file():
    # print(list_file.curselection())
    for index in reversed(list_file.curselection()): # .reverse() : Reverse list with no return
                                                     # reversed() : Return reversed list with no change
        list_file.delete(index)

# Storage path (Folder)
def browse_dest_path():
    folder_selected = filedialog.askdirectory() # 최초 폴더 지정 안하나?
    if folder_selected == '': # is None 이 아닌 이유?
        return
    # print(folder_selected)
    txt_dest_path.delete(0, END) # enntry 가 아닌 text 였다면 ("1.0", END)
    txt_dest_path.insert(0, folder_selected)

# Merge image
def merge_image():
    # print("Width :", cmb_width.get())
    # print("Interval :", cmb_interval.get())
    # print("Format :", cmb_format.get())

    # Width
    img_width = cmb_width.get()
    if img_width == "Keep original":
        img_width = -1
    else:
        img_width = int(img_width)

    # Interval
    img_interval = cmb_interval.get()
    if img_interval == "Narrow":
        img_interval = 30
    elif img_interval == "Standard":
        img_interval = 60
    elif img_interval == "Wide":
        img_interval = 90
    else:
        img_interval = 0

    # Format
    img_format = cmb_format.get().lower()
    
    ###############################################################################

    images = [Image.open(x) for x in list_file.get(0, END)] # Save as list

    # 이미지 사이즈 리스트에 넣어서 하나씩 처리
    image_sizes = [] # [(w1, h1), (w2, h2), ...]
    if img_width > -1:
        # Change width
        image_sizes = [(int(img_width), int(img_width*x.size[1]/x.size[0])) \
            for x in images] # int의 범위를 왜 전부로 해주냐
                             # 해당 변수를 사용할 때 정수로 받아야 해서
    else:
        # Keep original
        image_sizes = [(x.size[0], x.size[1]) for x in images]

    # Claculate logic
    # 100 * 60 -> 80 * ??
    # (origin w) : (origin h) = (changed w) : (changed h)
    #    100     :     60     =     80      :     ??
    #     x      :      y     =     x'      :     y'
    # x*y' = x'*y
    # y'   = (x'*y)/x
    # ??   = 48

    # x  = width     = size[0]
    # y  = height    = size[1]
    # x' = img_width
    # y' = (img_width*size[1])/size[0]

    widths, heights = zip(*(image_sizes)) # Make list

    # Calculate max width and total height
    max_width, total_height = max(widths), sum(heights)

    # Prepare sketchbook
    if img_interval > 0:
        total_height += (img_interval*(len(images) - 1))

    result_image = Image.new("RGB", (max_width, total_height), (255, 255, 255))
    y_offset = 0

    for idx, img in enumerate(images):
        # 가로가 원본이 아닌 경우에는 크기 조정 필요
        if img_width > -1:
            img = img.resize(image_sizes[idx])

        result_image.paste(img, (0, y_offset))
        y_offset += (img.size[1] + img_interval)

        progress = (idx + 1) / len(images) * 100
        p_var.set(progress)
        progress_bar.update()

    # Format option processing
    file_name = "Tng photo." + img_format
    dest_path = os.path.join(txt_dest_path.get(), file_name)
    result_image.save(dest_path)
    msgbox.showinfo("Notice", "Process is done")

# Start
def start():
    # Check each options
    # print("Width :", cmb_width.get())
    # print("Interval :", cmb_interval.get())
    # print("Format :", cmb_format.get())

    # Check file list
    if list_file.size() == 0:
        msgbox.showwarning("Warning", "Add image files")
        return

    # Check Storage path
    # 실제 프로젝트에서는 유효한 저장경로인지도 판단해야 한다.
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("Warning", "Add storage path")
        return

    # Merge image process
    merge_image()

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

btn_dest_path = Button(path_frame, text="Search", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# Option frame
frame_option = LabelFrame(root, text="Option")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. Width option
lbl_width = Label(frame_option, text="Width", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

opt_width = ["Keep original", "1024", "800", "640"]
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

btn_start = Button(frame_run, padx=5, pady=5, text="Start", width = 12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False)    # x(width), y(length) value cannot be changed (window size cannot be changed)

root.mainloop()