import pygame
from src.scenes import level1, level2
from cfg import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
clock = pygame.time.Clock()


scenes = [level1.Level1(), level2.Level2()]
current_scene = 0

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

    scenes[current_scene].render(game_surface, events)
    scaled_surface = pygame.transform.scale(game_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
