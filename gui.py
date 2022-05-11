from ast import arg
from email.mime import base
from http.client import REQUEST_TIMEOUT
import time
from tkinter import *
from tkinter.ttk import Progressbar
from backend import RunScript, OpenFolder, GetLinksNumber
import threading
import platform

WIDTH = 600
HEIGHT = 350
BACKGROUND_COLOR = '#535353'
TITLE = "Web Crawler"

class InputBox:
    def __init__(self, Window, x_coordinate, y_coordinate, width, height, bg_color, fg_color, border, font=('Calibri', 12)):
        self.Window = Window
        self.Box = Text(self.Window, width = width, height=height, border=border, bg=bg_color, fg = fg_color, font = font)
        self.Box.place(x = x_coordinate, y = y_coordinate)
    def GetText(self):
        return self.Box.get('1.0', END).rstrip()

class LabelBox:
    def __init__(self, Window, text, bg, fg, x_coordinate, y_coordinate, font = ('Calibri', 12)):
        self.Box = Label(Window, text=text, bg = bg, fg = fg, font = font)
        self.Box.place(x = x_coordinate, y = y_coordinate)
    def SetText(self, text):
        self.Box.config(text=text)

class ButtonBox:
    def __init__(self, Window, text, bg, fg, activeforeground, activebackground, x_coordinate, y_coordinate, command, *args):
        self.Button = Button(Window, text= text, bg = bg, fg = fg, activebackground=activebackground, activeforeground=activeforeground, command=lambda:command(*args))
        self.Button.place(x = x_coordinate, y = y_coordinate)

class ProgressBox:
    def __init__(self, Window, orient, lenght, mode, x_coordinate, y_coordinate) -> None:
        self.Window = Window
        self.Bar = Progressbar(Window, orient=orient, length=lenght, mode=mode)
        self.Bar.place(x=x_coordinate, y=y_coordinate)
    def Step(self, timeout):
        self.Bar['value'] = 0
        self.Bar['maximum'] = timeout
        speed = timeout/100
        progress = 0
        MaxProgress = timeout
        while progress < MaxProgress:
            time.sleep(speed)
            self.Bar['value'] += speed
            progress += speed
            self.Window.update_idletasks()

def ChangeLabel(timeout, LinksNumberLabel):
    time.sleep(timeout+3)
    LinksNumberLabel.SetText(('Succesfully extracted ' + str(GetLinksNumber()) + ' urls'))
        
def Run(BaseLinkBox, TimeoutBox, ProgressWidget, LinksNumberLabel):
    base_link = BaseLinkBox.GetText()
    timeout = TimeoutBox.GetText()
    if timeout == '':
        timeout = '60'
    thread1 = threading.Thread(target=RunScript, args=[base_link, timeout])
    thread1.start()
    thread2 = threading.Thread(target=ProgressWidget.Step, args=[int(timeout)])
    thread2.start()
    thread3 = threading.Thread(target=ChangeLabel, args=[int(timeout), LinksNumberLabel])
    thread3.start()


def OpenFile():
    thread1 = threading.Thread(target=OpenFolder)
    thread1.start()
    

if __name__ == '__main__':
    Window = Tk()
    Window.geometry(str(WIDTH) + 'x' + str(HEIGHT))
    Window.title(TITLE)
    Window.configure(bg = BACKGROUND_COLOR)
    BaseLinkLabel = LabelBox(Window, "Root Link:", BACKGROUND_COLOR, '#a9a9a9', 260, 50)
    BaseLinkBox = InputBox(Window, 100, 75, 50, 1, '#5c5c5c', '#a9a9a9', 1)
    TimeoutLabel = LabelBox(Window, "Timeout(default=60s):", BACKGROUND_COLOR, '#a9a9a9', 220, 120)
    TimeoutBox = InputBox(Window, 100, 150, 50, 1, '#5c5c5c', '#a9a9a9', 1)
    LinksNumberLabel = LabelBox(Window, '', BACKGROUND_COLOR, '#a9a9a9', 190, 300)
    ProgressWidget = ProgressBox(Window, HORIZONTAL, 350, 'determinate', 130, 240) 
    StartButton = ButtonBox(Window, "Start Crawling", '#5c5c5c', '#a9a9a9', '#5c5c5c', '#a9a9a9', 160, 190, Run, BaseLinkBox, TimeoutBox, ProgressWidget, LinksNumberLabel)
    SpreadSheetButton = ButtonBox(Window, "Open links file", '#5c5c5c', '#a9a9a9', '#5c5c5c', '#a9a9a9', 330, 190, OpenFile)
    Window.mainloop()
    