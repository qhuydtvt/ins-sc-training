import pygame

WHITE = (255, 0, 0)

#1. Init pygame
pygame.init()

#2. Setup screen
size = (600, 800)
canvas = pygame.display.set_mode(size)

#3. Clock
clock = pygame.time.Clock()

loop = True
while loop:
    # Game loop 1: Event processing
    events = pygame.event.get() # Mouse & Keyboards
    for event in events:
        if event.type == pygame.QUIT:
           loop = False

    # Game loop 2: Draw
    canvas.fill(WHITE)
    pygame.display.set_caption("Micro-war")

    # Game loop 3: Flip
    clock.tick(60)
    pygame.display.flip() # second buffer