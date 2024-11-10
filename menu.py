#games
import pygame 
import shooter_game
Windows = pygame.display.set_mode((700,500))

FPS = pygame.time.Clock()
button_rect = pygame.Rect(200, 200, 200, 50)       
button_exit = pygame.Rect(200, 270, 200, 50)
result2 = f'Выход:{str()}'
result3 = f'Начать:{str()}'
bed = pygame.font.Font(None, 35).render(result3 , True , (255, 255, 255))
exit_b = pygame.font.Font(None, 35).render(result2, True, (255, 255, 255))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                shooter_game.game()
                running = False

            if button_exit.collidepoint(event.pos):
                running = False

    pygame.draw.rect(Windows, (22, 66, 168), button_rect)
    pygame.draw.rect(Windows, (22, 66, 168), button_exit)
    Windows.blit(bed,(250,200))
    Windows.blit(exit_b,(250,270))







    pygame.display.update()
    FPS.tick(100)
