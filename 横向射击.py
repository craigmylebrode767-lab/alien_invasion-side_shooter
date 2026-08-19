import pygame
import sys

from ship import Ship
from bullets import Bullet
from aliens import Alien    
from settings import Settings


class Sidescrollingshooter:
    def __init__(self):
        #别忘了初始化
        pygame.init()

        #游戏设置
        self.settings = Settings()
        
        #创建屏幕
        self.screen =pygame.display.set_mode((800,600))
        self.screen_rect = self.screen.get_rect()

        #控制帧率的时钟
        self.clock = pygame.time.Clock()

        #初始化创建飞船
        self.ship = Ship(self)

        #子弹
        self.bullets = []

        #初始化创建外星人
        self.aliens = []
        self._create_fleets()

       

    def run_game(self):


        while True:

            '''while循环的次数是即为FPS，需要clock来设置
            然后思考每个循环即每一帧需要做什么：获取键鼠事件、执行动作（本来就要执行的比如子弹的 ）
            的移动，以及键鼠事件控制执行的）、把后端改变的数据绘制到屏幕
            暂时先添加按Q退出的功能，安全起见，也添加鼠标点击退出的功能'''

            self._check_events()

            '''对屏幕进行更改：每一帧都：绘制背景色，绘制飞船图像。
            现在考虑通过键鼠事件移动飞船
            宏观逻辑：
            check_events--keydown/keyup--K_left/right/up/down--
            self.ship.image_rect.x/y改变--update_screen时飞船位置
            参数self.ship.image_rect改变'''

            #改变飞船的位置等参数
            self._update_ship()

            #改变子弹的位置等参数，清除飞出屏幕的子弹
            self._update_bullets()

            #改变外星人的位置等参数
            self._update_aliens()

            #涂背景色，绘制飞船图像,子弹图像
            self._update_screen()

            #显示屏幕
            pygame.display.flip()

            #控制帧率
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
                elif event.key == pygame.K_SPACE:
                    self.bullets.append(Bullet(self))



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

        # 绘制子弹图案
        for bullet in self.bullets:
            self.screen.blit(bullet.image, bullet.rect)

        # 绘制外星人图案
        for alien in self.aliens:
            self.screen.blit(alien.image, alien.rect)

    def _update_ship(self):
        #改变飞船位置
        self.ship.update_position()
        #改变数量等等功能

    def _update_bullets(self): 
        for bullet in self.bullets.copy():
            #改变子弹位置
            bullet.update_position()

            #清除飞出屏幕的子弹
            if bullet.rect.left > self.screen_rect.right:
                self.bullets.remove(bullet)

            #其他功能
            pass


    ###外星人设置：
    #_update_aliens

    def _update_aliens(self):
        for alien in self.aliens:
            #改变外星人位置
            alien.update_position()

        #检测外星人与子弹碰撞
        i,j = 0,0
        if self.bullets and self.aliens:
            for bullet in self.bullets.copy():
                i += 1
                for alien in self.aliens.copy():
                    j+=1
                    #检测俩个surface有重叠
                    if not (
                        bullet.rect.right <= alien.rect.left or
                        bullet.rect.bottom <= alien.rect.top or
                        bullet.rect.top >= alien.rect.bottom or
                        bullet.rect.left >= alien.rect.right
                    ):
                        try:
                            self.bullets.remove(bullet)
                            print(bullet,bullet.rect)
                            self.aliens.remove(alien)
                            print(alien,alien.rect)
                            print(i,j)

                        except ValueError:
                            print(self.bullets)
                            print("出错的子弹:",bullet)
                            print("出错的外星人:",alien)
                            print(alien.rect,bullet.rect)
                            print("子弹列表长度:", len(self.bullets))
                            print(i,j)

        #清除飞出屏幕的外星人
        for alien in self.aliens:
            if alien.rect.right <self.screen_rect.left:
                self.aliens.remove(alien)

            #其他功能
            pass

    def _create_fleets(self):
        #创建外星人群
        alien = Alien(self)
        self.aliens.append(alien)
        alien_width, alien_height = alien.rect.size
        current_x = alien.rect.x
        current_y = alien.rect.y+2*alien.rect.height
        for i in range(3):
            #纵向创建new_alien,在y处创建
            while current_y < self.screen_rect.bottom - alien_height:
                self._create_alien(current_x, current_y)
                current_y += 2 * alien_height
            current_y = alien.rect.y
            current_x += 2 * alien.rect.width

    def _create_alien(self, x_position='', y_position=''):
        """创建一个外星人并将其放在当前行中"""
        new_alien = Alien(self)

        new_alien.rect.x = x_position
        new_alien.rect.y = y_position

        self.aliens.append(new_alien)


if __name__ == '__main__':
    sss = Sidescrollingshooter()
    sss.run_game()