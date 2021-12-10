from tkinter import *
import os

from PIL import Image, ImageDraw, ImageFont


def open():
    im = Image.open('images/logo.png')
    width, height = im.size

    gtext = watermark_label.get()
    draw = ImageDraw.Draw(im)
    text = f"©{gtext}"

    font = ImageFont.truetype('arial.ttf', 10)
    textwidth, textheight = draw.textsize(text, font)

    # calculate the x,y coordinates of the text
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font)
    # im.show()
    im.save('images/watermark.jpg.png')

# WINDOW

window = Tk()
window.title("Create Personal Watermarker")
window.minsize(width=100, height=100)
window.config(background="#548CA8")



# LABEL

watermark_label = Label(text="ADD WATERMARK TEXT HERE: ").pack()
watermark_label = Entry(window)
watermark_label.pack()


# BUTTON
Button(window, text="Click Here", command=open).pack()


window.mainloop()




