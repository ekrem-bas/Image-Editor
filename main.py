import tkinter as tk
from tkinter import filedialog, colorchooser
from PIL import Image, ImageTk, ImageDraw, ImageOps, ImageFilter, ImageDraw2

# Ekran
root = tk.Tk()
root.geometry("1000x600")
root.title("Image Editor")

# Varsayılan kalem rengi ve boyutu
pen_color = "Black"
pen_size = 5

# Global değişkenler
file_path = None
original_image = None
filtering_image = original_image
image_tk = None
draw = None
# ratio
ratio = 1

def resize_image(image, target_width, target_height):
    original_width, original_height = image.size
    global ratio
    ratio = min(target_width / original_width, target_height / original_height)
    new_width = int(original_width * ratio)
    new_height = int(original_height * ratio)
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
    return resized_image

def open_image():
    global original_image, image_tk, drawing_image

    file_path = filedialog.askopenfilename(filetypes=[("JPEG Files", "*.jpeg"), ("PNG Files", "*.png")])
    if not file_path:
        return

    original_image = Image.open(file_path)
    
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    resized_image = resize_image(original_image, canvas_width, canvas_height)
    image_tk = ImageTk.PhotoImage(resized_image)
    drawing_image = original_image.copy()

    canvas.delete("all")
    canvas.create_image(canvas_width // 2, canvas_height // 2, anchor="center", image=image_tk)
    canvas.image = image_tk  # Referans tutarak görüntünün kaybolmasını engelle


def save_file():
    global drawing_image
    save_file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpeg")])
    if save_file_path and drawing_image:
        drawing_image.save(save_file_path)


def draw_on_image(event):
    global drawing_image
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    
    x, y = event.x, event.y
    x1, y1 = (x - pen_size), (y - pen_size)
    x2, y2 = (x + pen_size), (y + pen_size)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline=pen_color)

    # Orijinal resimdeki koordinatları doğru şekilde ölçeklendirin
    draw = ImageDraw.Draw(drawing_image)
    original_x1 = int(x1 * original_image.width / canvas_width)
    original_y1 = int(y1 * original_image.height / canvas_height)
    original_x2 = int(x2 * original_image.width / canvas_width)
    original_y2 = int(y2 * original_image.height / canvas_height)
    
    # Çizim boyutlarını orijinal boyutlara göre ayarlayın
    original_pen_size = int(pen_size * original_image.width / canvas_width)
    
    # Çizim boyutunu doğru şekilde ölçeklendir
    draw.ellipse([original_x1, original_y1, original_x2, original_y2], fill=pen_color, outline=pen_color)

def toggle_draw():
    if canvas.bind("<B1-Motion>"):
        canvas.unbind("<B1-Motion>")
    else:
        canvas.bind("<B1-Motion>", draw_on_image)

def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title="Select Pen Color")[1]

def change_pen_size(event=None):
    global pen_size
    pen_size = int(ps_spin_box.get())

def clear_canvas():
    canvas.delete("all")
    canvas.create_image(canvas.winfo_width() // 2, canvas.winfo_height() // 2, anchor="center", image=image_tk)
    
def open_filter_menu():
        filter_menu = tk.Toplevel(root)
        filter_menu.geometry("250x350")
        filter_menu.title("Select a filter")
        filter_menu.config(bg= "white")
        
        # black and white button
        black_and_white_button = tk.Button(master= filter_menu, text= "Black and White", command= lambda : apply_filter("Black and White"), highlightbackground= "white", fg= "black")
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
        

def apply_filter(filter_):
        global filtering_image
        temp_image = original_image
        image = resize_image(original_image, canvas.winfo_width(), canvas.winfo_height())
        if filter_ == "Black and White":
                image = ImageOps.grayscale(image)
                temp_image = ImageOps.grayscale(original_image)
        elif filter_ == "Blur":
                image = image.filter(ImageFilter.BLUR)
                temp_image = temp_image.filter(ImageFilter.BLUR)
        elif filter_ == "Sharpen":
                image = image.filter(ImageFilter.SHARPEN)
                temp_image = temp_image.filter(ImageFilter.SHARPEN)
        elif filter_ == "Smooth":
                image = image.filter(ImageFilter.SMOOTH)
                temp_image = temp_image.filter(ImageFilter.SMOOTH)
        elif filter_ == "Emboss":
                image = image.filter(ImageFilter.EMBOSS)
                temp_image = temp_image.filter(ImageFilter.EMBOSS)
        else:
                image = resize_image(original_image, canvas.winfo_width(), canvas.winfo_height())
        image_tk = ImageTk.PhotoImage(image)
        canvas.delete("all")
        canvas.create_image(canvas.winfo_width() // 2, canvas.winfo_height() // 2, anchor="center", image=image_tk)
        canvas.image = image_tk
        filtering_image = temp_image

# Sol çerçeve
left_frame = tk.Frame(root, width=200, height=800, bg="white")
left_frame.pack(side="left", fill="y")

# Sağ çerçeve
right_frame = tk.Frame(root, width=1000, height=800, bg="white")
right_frame.pack(fill="both", expand=True)

# Canvas
canvas = tk.Canvas(right_frame, width=200, height=800, bg="grey", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Menü
image_button = tk.Button(master=left_frame, text="Add Image", highlightbackground="white", command=open_image)
image_button.pack(pady=15, padx=15)

color_button = tk.Button(master=left_frame, text="Change Pen Color", highlightbackground="white", command=change_color)
color_button.pack(padx=15)

pen_size_frame = tk.Frame(master=left_frame, bg="white")
pen_size_frame.pack(pady=15)

spinbox_label = tk.Label(pen_size_frame, text="Change Pen Size", bg="white", fg="black")
spinbox_label.pack()

ps_spin_box = tk.Spinbox(pen_size_frame, from_=1, to=10, command=change_pen_size, textvariable=tk.StringVar(value="5"), highlightbackground="white", background="white", foreground="black")
ps_spin_box.pack(padx=15)
ps_spin_box.bind("<Return>", change_pen_size)

draw_button = tk.Button(master=pen_size_frame, text="Toggle Draw", highlightbackground="white", command=toggle_draw)
draw_button.pack()

clear_canvas_button = tk.Button(master=left_frame, text="Clear", highlightbackground="white", command=clear_canvas)
clear_canvas_button.pack()

save_button = tk.Button(master=left_frame, text="Save", highlightbackground="white", command=save_file)
save_button.pack()

# filter menu
filter_button = tk.Button(left_frame, text= "Select a filter", highlightbackground= "white", command= open_filter_menu)
filter_button.pack()

root.mainloop()