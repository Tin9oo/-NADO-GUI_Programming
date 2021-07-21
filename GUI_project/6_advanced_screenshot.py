import time
import keyboard
from PIL import ImageGrab

def screenshot():
    # 2020년 6월 1일 10시 20분 30초 -> _20200601_102030
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time)) # ex) image_20200601_102030.png

keyboard.add_hotkey("F9", screenshot) # Save
                                      # ctrl+shift+s 와 같이 복합적으로도 사용 가능하다.

keyboard.wait("esc") # Exit