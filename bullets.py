import pygame

class Bullet():
    def __init__(self,sssgame):
        '''子弹不需要导入图像文件，只要设置矩形，长宽度，颜色即可
        ，思考bullet_image的数据类型，应该也是surface，之前pygame.image.load()
        返回的就是surface，spygame.draw.rect()返回的也是surface,但不如直接pygame.Surface()创建
        后者可以直接设置长宽度；再考虑surface的颜色，pygame.draw.rect()可以直接设置颜色，
        pygame.Surface()创建的surface需要再用fill()方法设置颜色'''
        
        self.image = pygame.Surface((10,3))
        self.image.fill((60,60,60))
        self.rect = self.image.get_rect()

        #还有初始位置
        self.rect.midleft = sssgame.ship.rect.midright

    def update_position(self):
        self.rect.x += 2   

    