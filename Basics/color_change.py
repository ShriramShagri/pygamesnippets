import pygame
import os
from random import randint

WIDTH, HEIGHT = 400, 400

class ChangeColor:

    def __init__(self):
        '''
        Just some vars
        '''
        os.environ["SDL_VIDEO_CENTERED"] = '1'
        self.WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Click to change color!')
        self.background = (255, 255, 255)
    
    def change_color(self):
        '''
        The color magician
        '''
        self.background = tuple([randint(0, 255) for _ in range(3)])
    
    def main(self):
        '''
        I'm the mainloop
        '''
        run = True

        while run:
            self.WINDOW.fill(self.background)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                
                # Below lines is for change of 1 color per click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.change_color()
            
            # Following lines keeps on changing color per frame if mouse button pressed
            # if pygame.mouse.get_pressed()[0]:
            #     self.change_color()
            
            pygame.display.update()


if __name__ == "__main__":
    ChangeColor().main()
        