import pygame

FIRSTCARD_X = 25
FIRSTCARD_Y = 100

class Card():
    def __init__(self, name, no):
        self.name = name
        self.x = FIRSTCARD_X
        self.y = FIRSTCARD_Y * no
        self.height = 50
        self.width = 325
        self.left_color = (0x1f, 0xbf, 0xb8)
        self.right_color = (0x05, 0x71, 0x6c)
    
    def draw(self, win, a):
        # pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        if a<5:
            pygame.draw.rect(win, (0, 0, 220), (self.x-2,self.y-2,self.width+4,self.height+4),0)
        self.gradientRect(win, pygame.Rect( self.x, self.y, self.width, self.height ))
        if a>5:
            s = pygame.Surface((self.width,self.height), pygame.SRCALPHA)
            s.fill((0,0,0,a))
            win.blit(s, (self.x,self.y))
    
    def gradientRect(self, win, target_rect ):
        """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
        colour_rect = pygame.Surface( ( 2, 2 ) )                                   # tiny! 2x2 bitmap
        pygame.draw.line( colour_rect, self.left_color,  ( 0,0 ), ( 0,1 ) )            # left colour line
        pygame.draw.line( colour_rect, self.right_color, ( 1,0 ), ( 1,1 ) )            # right colour line
        colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )  # stretch!
        win.blit( colour_rect, target_rect )  