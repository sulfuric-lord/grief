import pygame
from src.scenes import level1, level2, main_menu
import cfg

pygame.init()

clock = pygame.time.Clock()

scenes = [level1.Level1(), main_menu.Main_menu()]
current_scene = 1

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                current_scene = (current_scene + 1) % len(scenes)
            if event.key == pygame.K_ESCAPE:
                running = False

    scenes[current_scene].render(cfg.game_surface, events)
    scaled_surface = pygame.transform.scale(cfg.game_surface, (cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))
    cfg.screen.blit(scaled_surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
