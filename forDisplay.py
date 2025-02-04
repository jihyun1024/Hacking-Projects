from tkinter import *
from tkinter import messagebox
import time


def Call():
    msg = Label(Window, text = "Keylogging stoped")
    msg.place(x = 240, y = 115)
    button["bg"] = 'red'
    button['fg'] = 'white'
    messagebox.showinfo('Alarm', 'The window closed!')
    Window.destroy()


def Call2():
    msg = Label(Window, text = "Keylogging started")
    msg.place(x = 240, y = 35)
    button2["bg"] = 'green'
    button2['fg'] = 'black'
    hello()


def hello():
    print('hello world')


Window = Tk()
Window.title('KeyLoggerJH')
Window.geometry('400x200')
button = Button(text = 'Stop Keylogging', command = Call)
button2 = Button(text = 'Start Keylogging', command = Call2)

button.place(x = 90, y = 100, width = 120, height = 50)
button2.place(x = 90, y = 20, width = 120, height = 50)
Window.mainloop()