#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg

from code.level import Level
from code.const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from code.menu import Menu


class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                player_score = [0, 0]  # [Player1, Player2]
                level = Level(self.window, 'level1Bg', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'level2Bg', menu_return, player_score)
                    level_return = level.run(player_score)

            elif menu_return == MENU_OPTION[3]:
                pg.quit()  # Close Window
                quit()  # End pygame
            else:
                pass
