import pygame

class Ship():
    def __init__(self,sssgame):
        self.image = pygame.image.load('images/77.bmp')
        self.rect = self.image.get_rect()
        self.rect.midleft = sssgame.screen_rect.midleft

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update_position(self):
        if self.moving_up == True:
            self.rect.y -= 2
        if self.moving_down == True:
            self.rect.y += 2
        if self.moving_left == True:
            self.rect.x -= 2
        if self.moving_right == True:
            self.rect.x += 2