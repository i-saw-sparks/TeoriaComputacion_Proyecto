import pygame
import pygame_gui
from automatum import Automatum

pygame.init()

screen = pygame.display.set_mode((1260, 720))
manager = pygame_gui.UIManager((1260, 720))

background = pygame.Surface((1260, 720))
background.fill(pygame.Color('#F6F6F6'))

pygame.display.set_caption("I5915")
pygame.display.set_icon(pygame.image.load('assets/planta.png'))

state_m = Automatum()
image_route = state_m.get_image()
image_route_new = image_route
image = pygame.image.load(image_route)
background.blit(image, (370, 0))

clock = pygame.time.Clock()

buttons = []
i = 0
while i < 4:
    buttons.append(pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300 + (200 * i), 550), (100, 50)),
                                                text=" ",
                                            manager=manager))
    i = i+1

buttons[0].set_text(text="Regar")
buttons[1].set_text(text="Asolear")
buttons[2].set_text(text="Nutrir")
buttons[3].set_text(text="Fumigar")


htmlText = "<b>Fernanda Noemi Aguayo Carmona<br>Jesus Emmanuel Garza Flores<br>Andres Manuel Molina Aceves</b>";
pygame_gui.elements.UITextBox(html_text=htmlText, relative_rect=pygame.Rect((970, 640), (300, 300)), manager=manager)

running = True

while running:
    time_delta = clock.tick(60) / 1000.0
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            quit()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == buttons[0]:
                    image_route_new = state_m.get_next_state_image(0)
                if event.ui_element == buttons[1]:
                    image_route_new = state_m.get_next_state_image(1)
                if event.ui_element == buttons[2]:
                    image_route_new = state_m.get_next_state_image(2)
                if event.ui_element == buttons[3]:
                    image_route_new = state_m.get_next_state_image(3)
        manager.process_events(event)
    manager.update(time_delta)

    if image_route != image_route_new:
        image_route = image_route_new
        image = pygame.image.load(image_route)
        background.blit(image, (370, 0))

    screen.blit(background, (0, 0))
    manager.draw_ui(screen)
    pygame.display.update()
