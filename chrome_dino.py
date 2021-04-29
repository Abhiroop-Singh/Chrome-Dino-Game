import pyautogui #pip install pyautogui
from PIL import Image,ImageGrab #pip install pillow
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    #Draw a rectangle for birds
    for i in range(385,480):
        for j in range(500,595):
            if data[i,j]<100:
                hit("down")
                return
    
    #Draw a rectangle for cactus
    for i in range(385,480):
            for j in range(595,720):
                if data[i,j]<100:
                    hit("up")
                    return 
    return 

if __name__=="__main__":
    print("Hey...This Dino game is about to start in 2 seconds")
    time.sleep(2)

    while True:
        #These lines below is used to convert coloured image into greyscale image
        #Here grayscale image is used as processing a coloured image will take time
        
        image=ImageGrab.grab().convert("L")
        data=image.load()
        isCollide(data)

    # These 2 for loops are used for hit and trial method for positioning rectangle
        ##Draw a rectangle for cactus
        # for i in range(385,480):
        #     for j in range(595,720):
        #         data[i,j]=0 ##Here 0 denotes the pixel value for black colour
        
        # # #Draw a rectangle for birds
        # for i in range(385,480):
        #     for j in range(500,595):
        #         data[i,j]=171

        # image.show()
        # break
