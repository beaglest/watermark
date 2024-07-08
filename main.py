#from PIL import Image
import PIL.Image
from tkinter import *
import tkinter as tk

from pathlib import Path
from tkinter import filedialog

def button_clicked():
    filename = filedialog.askopenfilename()
    if filename:
        # Read and print the content (in bytes) of the file.

        fp = open(filename, "rb")
        img = PIL.Image.open(fp)

        print(img.format, img.size, img.mode)

        fp2 = open("tcmb.png", "rb")
        wm = PIL.Image.open(fp2)

        size = (302, 61)
        wm.thumbnail(size)


        # add watermark
        copied_image = img.copy()
        copied_image.paste(wm, (600, 500), wm)

        copied_image.show()

        #print(filename)
        #print(Path(filename).read_bytes())
    else:
        print("No file selected.")

root = Tk()

root.title("WATERMARK")
canvas = Canvas(root, bg="white",height=450, width=700)

canvas.create_text(325, 150, text="Please upload your image", fill="black", font='Helvetica 15 bold')

canvas.pack()
button = tk.Button(root,
                   text="Open File",
                   command=button_clicked,
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button.pack(padx=20, pady=20)
mainloop()
