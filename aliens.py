import pygame
from pathlib import Path
from random import choice


class Alien():
    def __init__(self,sssgame):
        self.game = sssgame
        self.screen = sssgame.screen
        base_dir = Path(__file__).resolve().parent
        self.image = pygame.image.load(base_dir / 'images' / 'alien.bmp')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        #还有初始位置
        self.rect.right = sssgame.screen_rect.right
        self.rect.y = self.rect.height

        # alien速度
        self.xspeed = sssgame.alien_xspeed
        self.yspeed = sssgame.settings.alien_yspeed

    def update_position(self):
        #横向移动
        self.rect.x -= self.xspeed

        #纵向移动
        '''方案一：移动方向随机，移动的幅度为yspeed'''
        '''方案二：位置随机'''
        '''还要考虑是否每一帧都要移动纵向，还是每一帧都有一定概率移动纵向'''
        # if self.rect.top >= 0 and self.rect.bottom <= self.screen.get_rect().bottom:
        #     self.rect.y += choice([-1, 0, 1]) * self.yspeed




    