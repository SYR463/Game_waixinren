import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        """ 初始化飞船， 设置其初始位置 """
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像，获取其外界矩形
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放入屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值,强制类型转化
        self.center = float(self.rect.centerx)

        # 飞船移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ 根据移动标志调整飞船位置 """
        # 更新飞船的 rect 值
            # 未触及右边缘，可以继续向右移动
        if self.moving_right and self.rect.right \
                < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
            # 未触及左边缘，可以继续向右移动
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据 self.center 控制 rect 对象
        self.rect.centerx = self.center

    def blitme(self):
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.image,self.rect)


