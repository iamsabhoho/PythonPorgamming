import pygame as pg
import sys
import myLib

#initialize the pygame lib
pg.init()
#sets the size of the window
winSize = (800, 700)
window = pg.display.set_mode(winSize)
#title
pg.display.set_caption('State Machine')
#the clock will be used to control how fast the screen updates
clock = pg.time.Clock()

#read the game images: sprites
waitingLink = pg.image.load('Wakerlink.jpg')
jumpingLink = pg.image.load('Jumplink.jpg')

#dictionary for characters
character = {'name':'link',
             'life':100,
             'walk_sprite': waitingLink,
             'pos_x': 100,
             'pos_y':100}

while True:

    ch = myLib.getkey()
    print(ch + ' pressed')
    if ord(ch) is 27:
        pg.quit()
        sys.exit()

    window.fill((255,255,255))
    pg.draw.line(window, (0, 0, 0), (0, 200), (200, 200))
    chr_rect = pg.Rect(character['pos_x'], character['pos_y'], 50, 50)
    #replace rect by image
    window.blit(character['walk_sprite'], chr_rect)

    # --- update the screen
    pg.display.flip()

    # --- limit to 60 frames per second
    clock.tick(10)


pygame.quit()
