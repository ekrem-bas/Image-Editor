import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageFilter, ImageTk, Image, ImageDraw

# screen
root = tk.Tk()
root.geometry("1000x600")
root.title("Image Editor")


# default pen color
pen_color = "Black"
# default pen size
pen_size = 5
# file path
file_path = None

# open image function
def open_image():
        global file_path
        file_path = filedialog.askopenfilename(filetypes=[("JPEG Files" , ".jpeg") , ("PNG Files", ".png")])
        image = Image.open(file_path)
        width, height = int(image.width // 2), int(image.height // 2)
        if width > canvas.winfo_width() or height > canvas.winfo_height():
                canvas.config(width= image.width, height= image.height)
                image = image.resize(size= (canvas.winfo_width(), canvas.winfo_height()), resample= Image.Resampling.LANCZOS)
                
        else:
                image = image.resize(size= (width, height), resample= Image.Resampling.LANCZOS) # antialias
                canvas.config(width= image.width, height= image.height)        
        
        # adjust the root screen with the height and width of the image
        root.geometry(f"{image.width + 237}x{image.height}")
        image = ImageTk.PhotoImage(image)
        canvas.image = image
        canvas.create_image(0, 0, image = image, anchor = "nw")

# draw function
def draw(event):
        x1 = (event.x - pen_size)
        y1 = (event.y - pen_size)
        x2 = (event.x + pen_size)
        y2 = (event.y + pen_size)
        canvas.create_oval(x1, y1, x2, y2, fill= pen_color, outline= "")
# change color function        
def change_color():
        global pen_color
        pen_color = colorchooser.askcolor(title= "Select Pen Color")[1]

# change pen size function
def change_pen_size(event = None):
        global pen_size
        pen_size = int (ps_spin_box.get())

# clear canvas function
def clear_canvas():
        canvas.delete("all")
        canvas.create_image(0, 0, image = canvas.image, anchor = "nw")     

# filter window
def open_filter_menu():
        filter_menu = tk.Toplevel(root)
        filter_menu.geometry("250x350")
        filter_menu.title("Select a filter")
        filter_menu.config(bg= "white")

        # black and white button
        black_and_white_button = tk.Button(master= filter_menu, text= "Sharpen", command= lambda : apply_filter("Black and White"), highlightbackground= "white", fg= "black")
        black_and_white_button.pack(pady= 15)
        # blur button
        blur_button = tk.Button(master= filter_menu, text= "Blur", command= lambda : apply_filter("Blur"), highlightbackground= "white", fg= "black")
        blur_button.pack(after= black_and_white_button)
        # sharpen button
        sharpen_button = tk.Button(master= filter_menu, text= "Sharpen", command= lambda : apply_filter("Sharpen"), highlightbackground= "white", fg= "black")
        sharpen_button.pack(pady= 15)
        # smooth button
        smooth_button = tk.Button(master= filter_menu, text= "Smooth", command= lambda : apply_filter("Smooth"), highlightbackground= "white", fg= "black")
        smooth_button.pack()
        # emboss button
        emboss_button = tk.Button(master= filter_menu, text= "Emboss", command= lambda : apply_filter("Emboss"), highlightbackground="white", fg= "black")
        emboss_button.pack(pady= 15)
        # clear filter button
        clear_button = tk.Button(master= filter_menu, text= "Clear", command= lambda : apply_filter("Clear"), highlightbackground= "white", fg= "black")
        clear_button.pack()

# TODO : Add filters  (clear button is completed) / continue to video from 39:11
# TODO : look at imageOps contain function (something about resizing, it can be used for the crop operation)
# apply filter function
def apply_filter(filter_):
        image = Image.open(file_path)
        width, height = int(image.width / 2), int(image.height / 2)
        image = image.resize(size= (width, height), resample= Image.Resampling.LANCZOS) # antialias
        if filter_ == "Black and White":
                image = ImageOps.grayscale(image)
        elif filter_ == "Blur":
                image = image.filter(ImageFilter.BLUR)
        elif filter_ == "Sharpen":
                image = image.filter(ImageFilter.SHARPEN)
        elif filter_ == "Smooth":
                image = image.filter(ImageFilter.SMOOTH)
        elif filter_ == "Emboss":
                image = image.filter(ImageFilter.EMBOSS)
        else:
                image = image
        image2 = ImageTk.PhotoImage(image)
        canvas.image = image2
        canvas.create_image(0, 0, image = image2, anchor = "nw")  


# left part of the screen - left frame
left_frame = tk.Frame(root, width=200, height=800, bg="white")
left_frame.pack(side="left", fill= "y")

# right part of the screen - right frame
right_frame = tk.Frame(root, width= 1000, height= 800, bg= "white")
right_frame.pack(fill= "both", expand= True)

# canvas
canvas = tk.Canvas(right_frame, width= 200, height= 800, bg= "white")
canvas.pack(fill= "both", expand= True)

# image button
image_button = tk.Button(master= left_frame, text= "Add Image", highlightbackground="white", command= open_image)
image_button.pack(pady= 15, padx= 15)

# color button
color_button = tk.Button(master= left_frame, text= "Change Pen Color", highlightbackground= "white", command= change_color)
color_button.pack(padx= 15)

# pen size 
pen_size_frame = tk.Frame(master=left_frame, bg="white")
pen_size_frame.pack(pady=15)

spinbox_label = tk.Label(pen_size_frame, text="Change Pen Size", bg="white", fg="black")
spinbox_label.pack()

ps_spin_box = tk.Spinbox(pen_size_frame, from_=1, to=10, command=change_pen_size, textvariable=tk.StringVar(value="5"), highlightbackground= "white", background= "white", foreground="black")
ps_spin_box.pack(padx= 15)
# when user press enter on spinbox it will change the pen size
ps_spin_box.bind("<Return>", change_pen_size)

# clear button
clear_canvas_button = tk.Button(master= left_frame, text= "Clear", highlightbackground= "white", command= clear_canvas)
clear_canvas_button.pack()

# drawing
# TODO: add button to draw on picture
canvas.bind("<B1-Motion>", draw)

# filter menu
filter_button = tk.Button(left_frame, text= "Select a filter", highlightbackground= "white", command= open_filter_menu)
filter_button.pack(pady= 15)


root.mainloop()