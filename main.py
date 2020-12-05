import pygame
import pygame_gui

pygame.init()

screen = pygame.display.set_mode((1260, 720))
manager = pygame_gui.UIManager((1260, 720))

background = pygame.Surface((1260, 720))
background.fill(pygame.Color('#FFFFFF'))

pygame.display.set_caption("I5915")
pygame.display.set_icon(pygame.image.load('assests/planta.png'))

clock = pygame.time.Clock()

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 600), (100, 50)),
                                            text='Regar',
                                            manager=manager)

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
                if event.ui_element == hello_button:
                    print('Hello World!')

        manager.process_events(event)

    manager.update(time_delta)

    screen.blit(background, (0, 0))
    manager.draw_ui(screen)
    pygame.display.update()
