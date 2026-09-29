import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
running = True

while running:
    pygame.event.pump()  # Add this line
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

