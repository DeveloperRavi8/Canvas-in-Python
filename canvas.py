from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Canvas Desktop Application")
root.geometry("600x600")

# Global Variables #
direction = ""
newx = 50
newy = 50
oldx = 50
oldy = 50

# Defining Canvas 
canvas = Canvas(root, width="590", height="510", background="white")
canvas.pack()

label = Label(root, text="Enter color name : ")
label.place(relx=0.6, rely=0.9, anchor=CENTER)

# An Input Box to Get the fill Color
color_entry = Entry(root)
color_entry.insert(0, "black")
color_entry.place(relx=0.8, rely=0.9, anchor=CENTER)

# Getting Image of Artist and displaying it on Canvas
img = ImageTk.PhotoImage(Image.open("start_point1.png"))
image_artist = canvas.create_image(50,50, image=img)

def draw(direction, oldx, oldy, newx, newy):
    fill_color = color_entry.get()
    print(oldx, oldy, newx, newy, direction,fill_color)
    # if(direction == "right") :
    canvas.create_line(oldx, oldy, newx, newy, fill=fill_color, width=3)

def right_dir(event):
    print("right")
    print(event)
    global direction
    global oldx
    global oldy
    global newx 
    global newy
    oldx = newx
    oldy = newy
    newx = newx + 5
    direction = "right"
    draw(direction, oldx, oldy, newx, newy)
    
def left_dir(event):
    print("left")
    print(event)
    global direction
    global oldx
    global oldy
    global newx 
    global newy
    oldx = newx
    oldy = newy
    newx = newx - 5
    direction = "left"
    draw(direction, oldx, oldy, newx, newy)

    
def up_dir(event):
    print("up")
    print(event)
    global direction
    global oldx
    global oldy
    global newx 
    global newy
    oldx = newx
    oldy = newy
    newy = newy - 5
    direction = "up"
    draw(direction, oldx, oldy, newx, newy)

def down_dir(event):
    print("down")
    print(event)
    global direction
    global oldx
    global oldy
    global newx 
    global newy
    oldx = newx
    oldy = newy
    newy = newy + 5
    direction = "down"
    draw(direction, oldx, oldy, newx, newy)
    
root.bind("<Right>", right_dir)
root.bind("<Left>", left_dir)
root.bind("<Up>", up_dir)
root.bind("<Down>", down_dir)

root.mainloop()
