from pygame import *
from termolaser import *

from PyQt5 import QtWidgets

from PIL import Image

def field_move_border():
    if field.left < 0: field.left = 0
    if field.right > w: field.right = w
    if field.bottom > h: field.bottom = h
    if field.top < 0: field.top = 0


app = QtWidgets.QApplication([])
wb_patch = QtWidgets.QFileDialog.getOpenFileName()[0]

print(wb_patch)
w,h = Image.open(wb_patch).size

win = display.set_mode([w,h])
img = image.load(wb_patch)
field = Rect(0,0,w//2,h//2)

while True:
    
    for e in event.get():
        if e.type == QUIT: exit()

        if e.type == MOUSEMOTION:
            field.center = e.pos
            field_move_border()

        if e.type == MOUSEBUTTONDOWN:
            area = img.subsurface(field)
            shoot(area)
            
            image.save(img, 'final'+wb_patch.split("/")[-1])
            
    win.blit(img,(0,0))
    draw.rect(win,(0,0,0),field,3)
    display.update()