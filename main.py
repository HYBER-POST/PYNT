from tkinter import *
import PIL
from PIL import Image, ImageDraw
from tkinter import messagebox
import datetime
from datetime import datetime

def save():
    c = datetime.now()
    filename = f'pynt_{c.year}_{c.month}_{c.day}_{c.minute}.{c.second}.png'
    image1.save(f'images/{filename}')
    messagebox.showinfo('Saving', f'Saved under the name {filename}')


def paint(event):
    x1, y1 = (event.x - 5), (event.y - 5)
    x2, y2 = (event.x + 5), (event.y + 5)
    cv.create_line(x1, y1, x2, y2, fill='black', width=5)
    draw.line((x1, y1, x2, y2), fill='black', width=5)

def clear(event):
    x1, y1 = (event.x - 5), (event.y - 5)
    x2, y2 = (event.x + 5), (event.y + 5)
    cv.create_line(x1, y1, x2, y2, fill='white', width=5)
    draw.line((x1, y1, x2, y2), fill='white', width=5)


root = Tk()
root.title("Pynt")
root.resizable(width=False, height=False)

cv = Canvas(root, width=1280, height=720, bg='white')

image1 = PIL.Image.new('RGB', (1280, 720), 'white')
draw = ImageDraw.Draw(image1)

cv.bind('<B1-Motion>', paint)
cv.bind('<B3-Motion>', clear)
cv.pack(expand=1, fill=BOTH)

btn_save = Button(text="Download my masterpiece", command=save, bg='black', fg='white', font=('Century Gothic', 30))
btn_save.pack()

root.mainloop()
