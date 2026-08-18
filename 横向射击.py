import pygame
import sys
from ship import Ship


class Sidescrollingshooter:
    def __init__(self):
        #别忘了初始化
        pygame.init()

        #创建屏幕
        self.screen =pygame.display.set_mode((800,600))
        self.screen_rect = self.screen.get_rect()

        #控制帧率的时钟
        self.clock = pygame.time.Clock()

        #飞船
        self.ship = Ship(self)

    def run_game(self):

        while True:

            #while循环的次数是即为FPS，需要clock来设置
            #然后思考每个循环即每一帧需要做什么：获取键鼠事件、执行动作（本来就要执行的比如子弹的 ）
            #的移动，以及键鼠事件控制执行的）、把后端改变的数据绘制到屏幕
            #暂时先添加按Q退出的功能，安全起见，也添加鼠标点击退出的功能



            self._check_events()

            #对屏幕进行更改：每一帧都：绘制背景色，绘制飞船图像。
            # 现在考虑通过键鼠事件移动飞船
            #宏观逻辑：
            #check_events--keydown/keyup--K_left/right/up/down--
            # self.ship.image_rect.x/y改变--update_screen时飞船位置
            # 参数self.ship.image_rect改变

            #改变飞船的位置等参数
            self._update_ship()

            # 注意到绘制飞船时提供的position在_init_
            #里被固定了
            self._update_screen()



            pygame.display.flip()

            self.clock.tick(60)


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    #退出
                    sys.exit()

                elif event.key == pygame.K_UP:
                    #开始向上移动
                    self.ship.moving_up =True

                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down =True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

            elif event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        # 虽然背景色始终不变，但最好放到循环内部，这样每一帧都是独立的不容易残留
        self.screen.fill((255, 255, 255))

        # 绘制飞船图案，需要读取bmp文件--添加到screen上
        self.screen.blit(self.ship.image, self.ship.rect)

    def _update_ship(self):
        #改变飞船位置
        self.ship.update_position()
        #改变数量等等功能

if __name__ == '__main__':
    sss = Sidescrollingshooter()
    sss.run_game()

