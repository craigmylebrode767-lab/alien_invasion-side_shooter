import pygame


class Bullet():
    def __init__(self,sssgame):
        self.game = sssgame

        '''子弹不需要导入图像文件，只要设置矩形，长宽度，颜色即可
        ，思考bullet_image的数据类型，应该也是surface，之前pygame.image.load()
        返回的就是surface，spygame.draw.rect()返回的也是surface,但不如直接pygame.Surface()创建
        后者可以直接设置长宽度；再考虑surface的颜色，pygame.draw.rect()可以直接设置颜色，
        pygame.Surface()创建的surface需要再用fill()方法设置颜色'''
        self.screen = sssgame.screen
        self.image = pygame.Surface((10,300))
        self.image.fill((60,60,60))
        self.rect = self.image.get_rect()

        #还有初始位置
        self.rect.midleft = sssgame.ship.rect.midright

        #子弹速度
        self.speed = sssgame.settings.bullet_speed

    def update_position(self):
        self.rect.x += self.speed

    """子弹有多个，为了感受sprite_group的作用，先不使用sprite_group，先用列表bullets来存储和管理子弹对象"""
    """下一步添加子弹的边界管理和settings控制速度"""
    