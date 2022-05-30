from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os

class GUI:
    def selected():
        global img_path, img
        img_path = filedialog.askopenfilename(initialdir=os.getcwd()) 
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        img1 = ImageTk.PhotoImage(img)
        canvas2.create_image(300, 210, image=img1)
        canvas2.image=img1                                                                                                                                                                                                                
    def blur(event):
        global img_path, img1, imgg
        for m in range(0, v1.get()+1):
                img = Image.open(img_path)
                img.thumbnail((350, 350))
                imgg = img.filter(ImageFilter.BoxBlur(m))
                img1 = ImageTk.PhotoImage(imgg) 
                canvas2.create_image(300, 210, image=img1)
                canvas2.image=img1
    def brightness(event):
        global img_path, img2, img3
        for m in range(0, v2.get()+1):
                img = Image.open(img_path)
                img.thumbnail((350, 350))
                imgg = ImageEnhance.Brightness(img)
                img2 = imgg.enhance(m)
                img3 = ImageTk.PhotoImage(img2)
                canvas2.create_image(300, 210, image=img3)
                canvas2.image=img3
    def contrast(event):
        global img_path, img4, img5
        for m in range(0, v3.get()+1):
                img = Image.open(img_path)
                img.thumbnail((350, 350))
                imgg = ImageEnhance.Contrast(img)
                img4 = imgg.enhance(m)
                img5 = ImageTk.PhotoImage(img4)
                canvas2.create_image(300, 210, image=img5)
                canvas2.image=img5
    def rotate_image(event):
            global img_path, img6, img7
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            img6 = img.rotate(int(rotate_combo.get()))
            img7 = ImageTk.PhotoImage(img6)
            canvas2.create_image(300, 210, image=img7)
            canvas2.image=img7
            
    def flip_image(event):
            global img_path, img8, img9
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            if flip_combo.get() == "FLIP LEFT TO RIGHT":
                img8 = img.transpose(Image.FLIP_LEFT_RIGHT)
            elif flip_combo.get() == "FLIP TOP TO BOTTOM":
                img8 = img.transpose(Image.FLIP_TOP_BOTTOM)
            img9 = ImageTk.PhotoImage(img8)
            canvas2.create_image(300, 210, image=img9)
            canvas2.image=img9   
    def image_border(event):
        global img_path, img10, img11
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        img10 = ImageOps.expand(img, border=int(border_combo.get()), fill=95)
        img11 = ImageTk.PhotoImage(img10)
        canvas2.create_image(300, 210, image=img11)
        canvas2.image=img11    
    img1 = None
    img3 = None
    img5 = None
    img7 = None
    img9 = None
    img11 = None
    def save():
        global img_path, imgg, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11
        ext = img_path.split(".")[-1]
        file=asksaveasfilename(defaultextension =f".{ext}",filetypes=[("All Files","*.*"),("PNG file","*.png"),("jpg file","*.jpg")])
        if file: 
                if canvas2.image==img1:
                    imgg.save(file)
                elif canvas2.image==img3:
                    img2.save(file)
                elif canvas2.image==img5:
                    img4.save(file)
                elif canvas2.image==img7:
                    img6.save(file)
                elif canvas2.image==img9:
                    img8.save(file)
                elif canvas2.image==img11:
                    img10.save(file)        

root = Tk()
root.title("Aizhamal")
root.geometry("640x640")

rotate = Label(root, text="Rotate:", font=("ariel 17 bold"))
rotate.place(x=370, y=8)
values = [0, 90, 180, 270, 360]
rotate_combo = ttk.Combobox(root, values=values, font=('ariel 10 bold'))
rotate_combo.place(x=460, y=15)
rotate_combo.bind("<<ComboboxSelected>>", GUI.rotate_image)
flip = Label(root, text="Flip:", font=("ariel 17 bold"))
flip.place(x=400, y=50)
values1 = ["FLIP LEFT TO RIGHT", "FLIP TOP TO BOTTOM"]
flip_combo = ttk.Combobox(root, values=values1, font=('ariel 10 bold'))
flip_combo.place(x=460, y=57)
flip_combo.bind("<<ComboboxSelected>>", GUI.flip_image)
blurr = Label(root, text="Blur:", font=("ariel 17 bold"), width=9, anchor='e')
blurr.place(x=323, y=92)
v1 = IntVar()
scale1 = ttk.Scale(root, from_=0, to=10, variable=v1, orient=HORIZONTAL, command=GUI.blur) 
scale1.place(x=460, y=99)

canvas2 = Canvas(root, width="600", height="420", relief=RIDGE, bd=2)
canvas2.place(x=15, y=150)

btn1 = Button(root, text="Select Image", bg='black', fg='gold', font=('ariel 17 bold'), relief=GROOVE, command=GUI.selected)
btn1.place(x=120, y=590)
btn2 = Button(root, text="Save", width=12, bg='black', fg='gold', font=('ariel 17 bold'), relief=GROOVE, command=GUI.save)
btn2.place(x=300, y=590)

image1 = ImageTk.PhotoImage(Image.open("image/logo.jpg"))
logo = Label(root, image=image1)
logo.place(x=0, y=0)
root.mainloop()