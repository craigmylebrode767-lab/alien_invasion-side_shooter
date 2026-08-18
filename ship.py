import pygame
from pathlib import Path

class Ship():
    def __init__(self,sssgame):
        base_dir = Path(__file__).resolve().parent
        self.image = pygame.image.load(base_dir / 'images' / '77.bmp')
        self.rect = self.image.get_rect()
        self.rect.midleft = sssgame.screen_rect.midleft

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update_position(self,sssgame):
        if self.moving_up == True and self.rect.top > 0:
            self.rect.y -= 2
        if self.moving_down == True and self.rect.bottom < sssgame.screen_rect.bottom:
            self.rect.y += 2
        if self.moving_left == True and self.rect.left > 0:
            self.rect.x -= 2
        if self.moving_right == True and self.rect.right < sssgame.screen_rect.right:
            self.rect.x += 2