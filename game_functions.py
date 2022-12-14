import sys
import pygame
# from settings import Settings

def check_keydown_events(event, ship):
    """ 响应按键 """
    # 向左、右移动
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """ 松开按键 """
    # 停止向左、右移动
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """ 响应键盘和鼠标事件 """
    for event in pygame.event.get():
        # 退出
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings,screen,ship):
    """ 更新屏幕上的图像，并切换到新屏幕 """

    # 每次循环时重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

