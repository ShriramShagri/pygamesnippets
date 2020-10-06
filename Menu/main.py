import pygame
import os
from gridcard import Card
from random import randint

WIDTH = 750
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('Test')

menu = pygame.image.load('menu.png')
close = pygame.image.load('back.png')
os.environ['SDL_VIDEO_CENTERED'] = '1'

MENU_VEL = 10

def gradientRect( left_colour, right_colour, target_rect ):
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface( ( 2, 2 ) )                                   # tiny! 2x2 bitmap
    pygame.draw.line( colour_rect, left_colour,  ( 0,0 ), ( 0,1 ) )            # left colour line
    pygame.draw.line( colour_rect, right_colour, ( 1,0 ), ( 1,1 ) )            # right colour line
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )  # stretch!
    WIN.blit( colour_rect, target_rect )  

def isOver(pos, x, y, width, height):
    if pos[0] > x and pos[0] < x + width:
        if pos[1] > y and pos[1] < y + height:
            return True
    return False

def drawmenu(a, color, menupos):
    s = pygame.Surface((WIDTH,WIDTH), pygame.SRCALPHA)
    s.fill((0,0,0,a))
    WIN.fill(color)
    WIN.blit(s, (0,0))

    gradientRect((0x03, 0x11, 0x63), (0x19, 0x78, 0xa5), pygame.Rect( menupos,0, WIDTH, WIDTH ) )

def openMenu(a, color, menupos):
    drawmenu(a, color, menupos)
    x = lambda pos : pos + MENU_VEL
    y = lambda k : k+2 if k<=60 else k

    if menupos < -WIDTH//2:
        return 0, y(a), x(menupos)
    return 1, y(a), menupos

def closeMenu(a, color, menupos):
    drawmenu(a, color, menupos)
    x = lambda pos : pos - MENU_VEL
    y = lambda k : k-2 if k>0 else k

    if menupos > -WIDTH:
        return 2, y(a), x(menupos)
    return 3, y(a), menupos

def maintainMenu(card, a1, a, color, menupos, clickpos):
    y = lambda k : k-5 if k>0 else k
    ph = 1
    drawmenu(a1, color, menupos)
    WIN.blit(close, (15, 20))
    card.draw(WIN, y(a))
    if clickpos:
        if isOver(clickpos, 15, 20, 24, 24):
            ph = 2
    return ph, y(a), menupos

def menuManager(color):
    card = Card('none', 1)
    run = True
    a = 0
    a2 = 150
    menupos = -WIDTH
    phase = 0 # 0- opening, 1-opened, 2-closing
    clickpos = None

    while run:
        # a, menupos = drawmenu(a, color, menupos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clickpos = pygame.mouse.get_pos()
        
        if phase == 0:
            phase, a, menupos = openMenu(a, color, menupos)
        elif phase == 1:
            phase, a2, menupos = maintainMenu(card, a, a2, color, menupos, clickpos)
            clickpos = None
        elif phase == 2:
            phase, a, menupos = closeMenu(a, color, menupos)
        else:
            break

        pygame.display.update()
    return run

def main():
    run = True
    pygame.init()
    color = (0x1f, 0xbf, 0xb8)

    while run:
        WIN.fill(color)
        WIN.blit(menu, (10, 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if isOver(pos, 10, 20, 24, 24):
                        run = menuManager(color)

        
        pygame.display.update()



if __name__ == "__main__":
    main()