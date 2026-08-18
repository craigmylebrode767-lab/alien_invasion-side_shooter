class Settings():
    """存储游戏的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #速度设置
        self.ship_speed = 5
        self.bullet_speed = 5
        self.alien_xspeed = 3
        self.alien_yspeed = 2