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
    print("Hey..Dino game is about to start in 3 seconds")
    time.sleep(2)

    while True:
        #This line below is used to convert coloured image into greyscale image
        image=ImageGrab.grab().convert("L")
        data=image.load()
        # print(asarray(image)) #This as array makes the program run slow so it is removed
        isCollide(data)

    # This 2 for loops is used for hit and trial method for placing the rectangle
        ##Draw a rectangle for cactus
        # for i in range(385,480):
        #     for j in range(595,720):
        #         data[i,j]=0 #This detects a black rectangle on the grey screen

        # # #Draw a rectangle for birds
        # for i in range(385,480):
        #     for j in range(500,595):
        #         data[i,j]=171

        # image.show()
        # break