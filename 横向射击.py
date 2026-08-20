import time

import pygame
import sys
from time import sleep

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

        #时间相关
        self.clock = pygame.time.Clock()

        #初始化创建飞船
        self.ship = Ship(self)

        #子弹
        self.bullets = []

        #初始化创建外星人
        self.aliens = []
        self._create_fleets()

        #状态管理
        self.status = 'not started'
        self.sta_text = pygame.font.Font('freesansbold.ttf',20)

        # self.not_start_sf = self.sta_text.render('not started', True, (0,0,60))
        # self.playing_sf = self.sta_text.render('playing', True, (0,0,60))
        # self.paused_sf = self.sta_text.render('paused', True, (0,0,60))
        # self.lose_sf = self.sta_text.render('lose', True, (0,0,60))
        # self.game_over_sf = self.sta_text.render('game over', True, (0,0,60))



    def run_game(self):
        while True:
            #结算上局结果
            self.settle_round()

            #检查键鼠事件
            self._check_events()

            if self.status == 'playing':
                #改变飞船的位置等参数
                self._update_ship()

                #改变子弹的位置等参数，清除飞出屏幕的子弹
                self._update_bullets()

                #改变外星人的位置等参数
                self._update_aliens()

                #检测是否结束单次游戏
                self._check_game_over()

            #涂背景色，绘制飞船图像,子弹图像
            self._update_screen()

            #显示屏幕
            pygame.display.flip()
            pygame.display.set_caption("横向射击")

            #控制帧率
            self.clock.tick(60)

    def settle_round(self):
        if self.status in ['win', 'lose']:
            self.ship.rect.midleft = self.screen_rect.midleft
            self.aliens.clear()
            self.bullets.clear()
            self._create_fleets()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_p:  
                    if self.status in ['not started','paused','win''lose','game over']:
                        self.status = 'playing'
                    elif self.status == 'playing':
                        self.status = 'paused'
                elif self.status == 'playing':
                    if event.key == pygame.K_UP:
                        self.ship.moving_up = True
                    elif event.key == pygame.K_DOWN:
                        self.ship.moving_down = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                    elif event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_SPACE:
                        self.bullets.append(Bullet(self))

            elif event.type == pygame.KEYUP:
                if self.status == 'playing':
                    if event.key == pygame.K_UP:
                        self.ship.moving_up = False
                    elif event.key == pygame.K_DOWN:
                        self.ship.moving_down = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                    elif event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    

                    


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

        #状态文字显示
        self.status_surf = self.sta_text.render(self.status, True, (0, 0, 60))
        self.status_surf_rect = self.status_surf.get_rect()
        self.screen.blit(self.status_surf, self.status_surf_rect)


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


    def _update_aliens(self):
        for alien in self.aliens:
            #改变外星人位置
            alien.update_position()

        # 检测外星人与子弹碰撞
        if self.bullets and self.aliens:
            for bullet in self.bullets.copy():
                bullet_hit = False
                for alien in self.aliens.copy():
                    #检测俩个surface有重叠
                    if self._rect_collision(bullet.rect,alien.rect):
                        self.aliens.remove(alien)
                        bullet_hit = True
                if bullet_hit:
                    self.bullets.remove(bullet)


    def _check_game_over(self):
        if not self.aliens:
            self.status = 'win'
        else:
            for alien in self.aliens.copy():
                #检测外星人与飞船碰撞与飞出屏幕的外星人
                if (
                    self._rect_collision(self.ship.rect,alien.rect) or
                    alien.rect.left < self.screen_rect.left
                ) :
                    self.status = 'lose'
                    break

    #检测碰撞，若俩rect有重叠则返回True
    def _rect_collision(self,rect_1,rect_2):
        if (
            rect_1.right <= rect_2.left or
            rect_1.left >= rect_2.right or
            rect_1.bottom <= rect_2.top or
            rect_1.top >= rect_2.bottom
        ):
            return False
        else :
            return True


    def _create_fleets(self):
        #创建外星人群
        alien = Alien(self)
        self.aliens.append(alien)
        current_x = alien.rect.x
        current_y = alien.rect.y+2*alien.rect.height
        for i in range(3):
            #纵向创建new_alien,在y处创建
            while current_y < self.screen_rect.bottom - alien.rect.height:
                self._create_alien(current_x, current_y)
                current_y += 2 * alien.rect.height
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