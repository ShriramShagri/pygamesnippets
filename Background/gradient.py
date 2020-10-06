# An example of changing color in the background with gradient of two color

# Both static and changing colors are implemented

import pygame
import random

WIDTH, HEIGHT = 750, 750

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Gradient')

class Grid:
    '''
    Remove this class if u don't need changing background
    '''
    def __init__(self, left, right):
        self.leftcolor = left
        self.left = [True, True, True]
        self.rightcolor = right
        self.right = [True, True, True]
        self.timer = 20
    
    def getcolor(self):
        '''
        Just For fun :)
        '''
        left = list(self.leftcolor)
        right = list(self.rightcolor)
        if self.timer > 0:
            self.timer -=1
        else:
            self.timer = 20
            c1 = random.choice(left)
            c2 = random.choice(right)
            if c1 < 255 and self.left[left.index(c1)]:
                left[left.index(c1)] = c1+1
            elif c1 == 255 and self.left[left.index(c1)]:
                self.left[left.index(c1)] = False
            elif c1 > 0 and not self.left[left.index(c1)]:
                left[left.index(c1)] = c1-1
            elif c1 == 0 and not self.left[left.index(c1)]:
                self.left[left.index(c1)] = True
            if c2 < 255 and self.right[right.index(c2)]:
                right[right.index(c2)] = c2+1
            elif c2 == 255 and self.right[right.index(c2)]:
                self.right[right.index(c2)] = False
            elif c2 > 0 and not self.right[right.index(c2)]:
                right[right.index(c2)] = c2-1
            elif c2 == 0 and not self.right[right.index(c2)]:
                self.right[right.index(c2)] = True
        self.leftcolor = left
        self.rightcolor = right

def gradientRect(left_colour, right_colour, target_rect):
    colour_rect = pygame.Surface(( 2, 2 ))
    pygame.draw.line(colour_rect, left_colour, (0, 0), (0, 1))
    pygame.draw.line(colour_rect, right_colour, (1, 0), (1, 1))
    colour_rect = pygame.transform.smoothscale(colour_rect, (target_rect.width, target_rect.height))
    WINDOW.blit(colour_rect, target_rect) 

def main():
    run = True
    # Comment this line to disable changing color
    background = Grid((random.randint(0, 255) for _ in range(3)), (random.randint(0, 255) for _ in range(3)))
    
    while run:
        # Comment the below 2 lines and uncomment the third to stop changing color
        color = background.getcolor()
        gradientRect(background.leftcolor, background.rightcolor, pygame.Rect(0, 0, WIDTH, HEIGHT ))
        # gradientRect((255, 0, 0), (255, 255, 0), pygame.Rect(0, 0, WIDTH, HEIGHT ))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()
    

if __name__ == "__main__":
    main()