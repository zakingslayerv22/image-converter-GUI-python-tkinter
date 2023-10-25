from tkinter import *
from tkinter import filedialog as fd
import os
from PIL import Image

root=Tk()
root.geometry("400x400")
root.title("FIN and TXT converter")

def jpg_to_png():
    filename=fd.askopenfilename()
    if filename.endswith(".jpg"):
        Image.open(filename).save("sample1.png")
        Label_2=Label(root,text="Success!", width=20,fg="green", font=("bold",15))
        Label_2.place(x=40,y=280)
    else:
        Label_2=Label(root,text="Error!", width=20,fg="red", font=("bold",15))
        Label_2.place(x=40,y=280)

def jpg_to_pdf():
    filename=fd.askopenfilename()
    if filename.endswith(".jpg"):
        Image.open(filename).save("sample1.pdf", resolution=100.0)
        Label_2=Label(root,text="Success!", width=20,fg="green", font=("bold",15))
        Label_2.place(x=40,y=280)
    else:
        Label_2=Label(root,text="Error!", width=20,fg="red", font=("bold",15))
        Label_2.place(x=40,y=280)

Label_1=Label(root,text="Browse A File", width=20, font=("bold",15))
Label_1.place(x=40,y=80)


# the buttons
Button(root,text="JPG_to_PNG", width=20, height=2, bg="brown",fg="white",command=jpg_to_png).place(x=80,y=120)
Button(root,text="JPG_to_PDF", width=20, height=2, bg="brown",fg="white", command=jpg_to_pdf).place(x=80,y=220)

root.mainloop()