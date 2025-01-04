import pygame
from src.scripts.obj import PhysicalObject

from src.scripts.tilemap import TileMap

tilemap = TileMap(64) 

level_map = [
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
]
tilemap.generate_colliders(level_map)

f_sprite = pygame.image.load("src/data/sprites/character/f_idle.png")
player = PhysicalObject(0, 0, 32, 64, pygame.transform.scale(f_sprite, (32, 64)))



class Level1:
    def __init__(self):
        self.gravity = True

    def render(self, surface, events):
        surface.fill((0, 0, 0))

        keys = pygame.key.get_pressed()
        dx = 0
        if keys[pygame.K_d]:
            dx = 2
        elif keys[pygame.K_a]:
            dx = -2
        if keys[pygame.K_SPACE]:
            player.jump()
        if keys[pygame.K_c]:
            self.gravity = not self.gravity
            player.dy = 0

        if self.gravity:
            player.apply_gravity()  
        player.move(dx, player.dy, tilemap.collidable_tiles)

        player.render(surface)
        tilemap.render(surface, level_map)
