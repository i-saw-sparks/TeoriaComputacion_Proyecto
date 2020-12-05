import pygame
from pygame_widgets import ButtonArray, TextBox

pygame.init()

screen = pygame.display.set_mode((1260, 720))
screen.fill((255, 255, 255))
pygame.display.update() 

pygame.display.set_caption("I5915")
pygame.display.set_icon(pygame.image.load('assests/planta.png'))

buttonArray = ButtonArray(screen, 400, 600, 500, 100, (4, 1),
                          border=20, texts=('Regar', 'Asolear', 'Nutrir', 'Quitar plaga'),
                            colour=(200, 200, 0)
                         )

textbox = TextBox(screen, 100, 100, 800, 80, fontSize=50,
                  borderColour=(255, 0, 0), textColour=(0, 200, 0),
                  radius=10, borderThickness=5)

running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            quit()
    
    buttonArray.listen(events)
    buttonArray.draw()
    pygame.display.update()

