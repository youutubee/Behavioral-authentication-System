from pynput import keyboard
import time


def start_time():
    start=time.time()
    return start

def end_time():
    end=time.time()
    return end
def on_press(key):
    try:
        start = time.time()
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        start=time.time();
        print('special key {0} pressed'.format(key))



def on_release(key):
    start=start_time()
    end=end_time()
    print('{0} released'.format(key),"time",(end-start)*1000)

    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()





