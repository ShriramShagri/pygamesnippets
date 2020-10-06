import pygame

WIDTH, HEIGHT = 400, 400

pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Basic Template')


def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    

if __name__ == "__main__":
    main()