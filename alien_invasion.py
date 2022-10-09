import pygame

import game_functions as gf
from ship import Ship
from settings import Settings

def run_game():
    pygame.init()  # 初始化游戏界面
    ai_settings = Settings()

    # 设置游戏界面的大小
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen,ship)



run_game()

