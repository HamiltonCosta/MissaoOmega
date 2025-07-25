#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.player import Player
from code.enemy import Enemy


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'level1Bg':
                list_bg = []
                for i in range(5):  # level1Bg images number
                    list_bg.append(Background(f'level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'level2Bg':
                list_bg = []
                for i in range(6):  # level2Bg images numer
                    list_bg.append(Background(f'level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'player1':
                return Player('player1', (10, WIN_HEIGHT / 2 - 30))
            case 'player2':
                return Player('player2', (10, WIN_HEIGHT / 2 + 30))
            case 'enemy1':
                return Enemy('enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'enemy2':
                return Enemy('enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
