import pygame
from pathlib import Path

class Ship():
    def __init__(self,sssgame):
        self.game = sssgame
        self.screen = sssgame.screen
        self.screen_rect = sssgame.screen_rect
        base_dir = Path(__file__).resolve().parent
        self.image = pygame.image.load(base_dir / 'images' / '77.bmp')
        self.rect = self.image.get_rect()
        self.rect.midleft = sssgame.screen_rect.midleft

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        self.speed = sssgame.settings.ship_speed

    def update_position(self):
        if self.moving_up == True and self.rect.top > 0:
            self.rect.y -= self.speed
        if self.moving_down == True and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.speed
        if self.moving_left == True and self.rect.left > 0:
            self.rect.x -= self.speed
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed
"""感觉可以重构，目前在ship类的各个方法里为了避免传入入sssgame，需要在init里给ship增加属性，
使得ship的属性变得臃肿，考虑保留ship类的本地属性，其他属性直接打包在self.game = sssgame里,这样ship的其他
方法里就可以直接用self.game.screen/self.game.settings等来访问了"""