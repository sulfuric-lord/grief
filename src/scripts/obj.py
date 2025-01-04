import pygame
from cfg import *


class PhysicalObject:
    def __init__(self, x, y, width, height, speed, sprite=None):
        self.gravity = 1
        self.rect = pygame.Rect(x, y, width, height)
        self.sprite = sprite
        if sprite:
            sprite_width, sprite_height = sprite.get_size()
            self.sprite = sprite
            self.sprite_pos = (self.rect.x, self.rect.bottom - sprite_height)
        else:
            self.sprite_pos = (self.rect.x, self.rect.y)
        self.speed = speed
        self.dy = 0 
        self.on_ground = False
        self.state = 'idle'

    def move(self, dx, dy, collidable_tiles):
        self.rect.x += dx
        for tile in collidable_tiles:
            if self.rect.colliderect(tile):
                if dx > 0: 
                    self.rect.right = tile.left
                elif dx < 0: 
                    self.rect.left = tile.right

        self.rect.y += dy
        self.on_ground = False 
        for tile in collidable_tiles:
            if self.rect.colliderect(tile):
                if dy > 0: 
                    self.rect.bottom = tile.top
                    self.on_ground = True 
                    self.dy = 0 
                elif dy < 0: 
                    self.rect.top = tile.bottom
                    self.dy = 0  

        if self.sprite:
            self.sprite_pos = (self.rect.x, self.rect.bottom - self.sprite.get_height())

    def apply_gravity(self):
        if not self.on_ground:
            self.dy += int(self.gravity)
            if self.gravity < 9:
                self.gravity += 0.1
        else:
            self.gravity = 0
            if self.state != 'jump':
                self.dy = 0

    def jump(self):
        self.state = 'jump'
        if self.on_ground:
            self.dy = -10

    def change_state(self, state):
        self.state = state

    def render(self, surface):
        if self.sprite:
            surface.blit(self.sprite, self.sprite_pos)
