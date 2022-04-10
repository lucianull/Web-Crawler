from tkinter import *
from turtle import st
import request_module

WIDTH = 600
HEIGHT = 600
BACKGROUND_COLOR = '#535353'
TITLE = "Web Crawler"

def Run():
    pass

class InputBox:
    def __init__(self, Window, x_coordinate, y_coordinate, width, height, bg_color, fg_color, border, font=('Calibri', 12)):
        self.Window = Window
        self.Box = Text(self.Window, width = width, height=height, border=border, bg=bg_color, fg = fg_color, font = font)
        self.Box.place(x = x_coordinate, y = y_coordinate)

class LabelBox:
    def __init__(self, Window, text, bg, fg, x_coordinate, y_coordinate, font = ('Calibri', 12)):
        self.Box = Label(Window, text=text, bg = bg, fg = fg, font = font)
        self.Box.place(x = x_coordinate, y = y_coordinate)
class ButtonBox:
    def __init__(self, Window, text, bg, fg, activeforeground, activebackground, command, x_coordinate, y_coordinate):
        self.Button = Button(Window, text= text, bg = bg, fg = fg, activebackground=activebackground, activeforeground=activeforeground, command=command)
        self.Button.place(x = x_coordinate, y = y_coordinate)



if __name__ == '__main__':
    Window = Tk()
    Window.geometry(str(WIDTH) + 'x' + str(HEIGHT))
    Window.title(TITLE)
    Window.configure(bg = BACKGROUND_COLOR)
    BaseLinkLabel = LabelBox(Window, "Root Link:", BACKGROUND_COLOR, '#a9a9a9', 260, 50)
    BaseLinkBox = InputBox(Window, 100, 75, 50, 1, '#5c5c5c', '#a9a9a9', 1)
    StartButton = ButtonBox(Window, "Start Crawling", '#5c5c5c', '#a9a9a9', '#5c5c5c', '#a9a9a9', Run, 255, 130)
    Window.mainloop()