import time
from PIL import ImageGrab

time.sleep(5) # Wait 5 sec

for i in range(1, 11): # 2 sec interval 10 image save
    img = ImageGrab.grab() # Screenshot
    img.save("image{}.png".format(i)) # Save in png file
    time. sleep(2) # Sleep 2 sec