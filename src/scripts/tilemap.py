import pygame

class TileMap:
    def __init__(self, tile_size):
        self.tile_size = tile_size
        self.tile_sprite = None
        self.collidable_tiles = []

    def set_tile_sprite(self, sprite_path):
        self.tile_sprite = pygame.image.load(sprite_path).convert_alpha()

    def generate_colliders(self, level_map):
        self.collidable_tiles = []
        for y, row in enumerate(level_map):
            for x, tile in enumerate(row):
                if tile == 1:
                    tile_rect = pygame.Rect(x * self.tile_size, y * self.tile_size,
                                            self.tile_size, self.tile_size)
                    self.collidable_tiles.append(tile_rect)

    def render(self, surface, level_map):
        for y, row in enumerate(level_map):
            for x, tile in enumerate(row):
                if tile == 1:
                    pos = (x * self.tile_size, y * self.tile_size)
                    if self.tile_sprite:
                        surface.blit(self.tile_sprite, pos)
                    else:
                        pygame.draw.rect(surface, (255, 255, 255), (*pos, self.tile_size, self.tile_size))
