import sys
import pygame

def sky():
    pygame.init()

    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("BIUE SKY")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((116,162,219))

        pygame.display.flip()

sky()