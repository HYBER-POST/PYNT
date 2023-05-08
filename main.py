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
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    if brush_shape == 'round':
        cv.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color)
        draw.ellipse((x1, y1, x2, y2), fill=current_color, outline=current_color)
    elif brush_shape == 'square':
        cv.create_rectangle(x1, y1, x2, y2, fill=current_color, outline=current_color)
        draw.rectangle((x1, y1, x2, y2), fill=current_color, outline=current_color)

def clear(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    cv.create_rectangle(x1, y1, x2, y2, fill='white', outline='white')
    draw.rectangle((x1, y1, x2, y2), fill='white', outline='white')

def change_color(color):
    global current_color
    current_color = color

def change_brush_shape(shape):
    global brush_shape
    brush_shape = shape

def change_brush_size(size):
    global brush_size
    brush_size = size

root = Tk()
root.title("Pynt")
root.resizable(width=False, height=False)

colors = ['red', 'green', 'orange', 'black', 'cyan', 'yellow', 'purple']
current_color = 'black'

brush_shapes = ['round', 'square']
brush_shape = 'round'

brush_sizes = [5, 10, 15, 20, 25]
brush_size = 5

frame_colors = Frame(root)
frame_colors.pack(pady=10)
for color in colors:
    btn_color = Button(frame_colors, text=color, bg=color, command=lambda color=color: change_color(color))
    btn_color.pack(side=LEFT, padx=5)

frame_brush_shapes = Frame(root)
frame_brush_shapes.pack(pady=10)
for shape in brush_shapes:
    btn_shape = Button(frame_brush_shapes, text=shape, command=lambda shape=shape: change_brush_shape(shape))
    btn_shape.pack(side=LEFT, padx=5)

frame_brush_sizes = Frame(root)
frame_brush_sizes.pack(pady=10)
for size in brush_sizes:
    btn_size = Button(frame_brush_sizes, text=size, command=lambda size=size: change_brush_size(size))
    btn_size.pack(side=LEFT, padx=5)

cv = Canvas(root, width=1280, height=720, bg='white')

image1 = PIL.Image.new('RGB', (1280, 720), 'white')
draw = ImageDraw.Draw(image1)

cv.bind('<B1-Motion>', paint)
cv.bind('<B3-Motion>', clear)
cv.pack(expand=1, fill=BOTH)

btn_save = Button(text="Download my\nmasterpiece", command=save, bg='black', fg='white', font=('Century Gothic', 9), width=17,height=4)
btn_save.place(relx=1.0, x=-10, y=10, anchor=NE)
root.resizable(True, True)
root.mainloop()
