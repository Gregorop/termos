from pygame import *
from termolaser import *

w,h = 640, 480

win = display.set_mode([w,h])
img = image.load('2.jpg')
area = img.subsurface(w//2-150,h//2-150,300,300)
shoot(area)

while True:
    for e in event.get():
        if e.type == QUIT: exit()

        
    win.blit(img,(0,0))
    display.update()