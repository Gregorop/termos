#типо греет
from pygame import *

def shoot(_surface):
    surface_array = surfarray.array2d(_surface)
    for x in range(len(surface_array)):
        for y in range(len(surface_array[x])):
            
            if sum(_surface.unmap_rgb(surface_array[x][y])[:-1]) > 100:
                _surface.set_at((x,y), (255,0,0))
   

if __name__ == "__main__":
    img = image.load('2.jpg')
    
    shoot(img)

    image.save(img, 'test.jpg')