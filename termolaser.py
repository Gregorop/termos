#типо греет
from pygame import *

def shoot(_surface):
    surface_array = surfarray.array2d(_surface)
    for x in range(len(surface_array)):
        for y in range(len(surface_array[x])):
            value = sum(_surface.unmap_rgb(surface_array[x][y])[:-1])
            kef = value/3
            if value > 130:
                _surface.set_at((x,y), (kef,kef/5,0))
            elif value < 80:
                _surface.set_at((x,y), (0,0,255))
            else:
                _surface.set_at((x,y), (kef/10,kef,0))
    

if __name__ == "__main__":
    img = image.load('2.jpg')
    
    shoot(img)

    image.save(img, 'test.jpg')