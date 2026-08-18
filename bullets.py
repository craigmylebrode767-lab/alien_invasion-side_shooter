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
        self.rect.x += 100

    """子弹类已经设置，接下来考虑一个问题：第一次循环时先update_position()，然后再绘制子弹图像，
    导致第一帧子弹图像在初始位置偏右，通过设置帧率不大于1和移动速度100发现了这个问题
    但还没有设置按下空格键才发射，如果设置了按下空格键才发射，使得第一次循环时update_position()不会执行，
    子弹图像会在初始位置绘制，这点尚不确定"""
    """但万一以后遇到自动发射的图像呢？从通用性的角度说这个问题也值得解决。初步的方案是在循环前加一次初始化屏幕
    ，即第一帧屏幕单独写一套逻辑"""
    '''目前先考虑按下空格键才发射的情况，首先Update_screen里blit 子弹没有问题，但按下空格键控制的是bullets的创建
    但这样flip_screen时子弹的位置仍然不是初始位置'''
    """子弹有多个，为了感受sprite_group的作用，先不使用sprite_group，先用列表bullets来存储和管理子弹对象"""

    