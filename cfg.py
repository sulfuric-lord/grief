import pygame

pygame.init()

INFO = pygame.display.Info()
SCREEN_WIDTH = INFO.current_w
SCREEN_HEIGHT = int(SCREEN_WIDTH / (16 / 9))
GAME_WIDTH = 1280
GAME_HEIGHT = 720
SCALE_X = SCREEN_WIDTH / GAME_WIDTH
SCALE_Y = SCREEN_HEIGHT / GAME_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))