import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ 对飞船发射子弹进行管理的类 """
    def __init__(self,ai_settings,screen,ship):
        """ 在飞船所处位置创建子弹 """

        # super() 继承 Sprite
        super(Bullet,self).__init__()
        self.screen = screen

        # 在（0，0）处创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

