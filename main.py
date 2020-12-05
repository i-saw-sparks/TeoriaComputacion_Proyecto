import pygame
import pygame_widgets

pygame.init()

screen = pygame.display.set_mode((1260, 720))
screen.fill((255, 255, 255));
pygame.display.update()

pygame.display.set_caption("I5915")
pygame.display.set_icon(pygame.image.load('assests/planta.png'))



button = pygame_widgets.Button(
        screen, 100, 100, 300, 150
     )

running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    button.listen(events)
    button.draw()
    pygame.display.update()