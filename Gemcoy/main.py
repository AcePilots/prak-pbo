import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # Set run to False to exit the loop

    screen.fill((255, 255, 255))  # Set the background color to white

    pygame.draw.circle(screen, (255, 0, 0), (320, 240), 50)

    pygame.display.update()

pygame.quit()  # Quit pygame properly after the loop ends
