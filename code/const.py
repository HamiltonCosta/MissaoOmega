import pygame as pg

# C
COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_YELLOW = (255, 255, 0)

# E
EVENT_ENEMY = pg.USEREVENT + 1

ENTITY_SPEED = {
    'level1Bg0': 0,
    'level1Bg1': 1,
    'level1Bg2': 2,
    'level1Bg3': 3,
    'level1Bg4': 4,
    'player1': 3,
    'player1Shot': 4,
    'player2': 3,
    'player2Shot': 4,
    'enemy1': 1,
    'enemy1Shot': 5,
    'enemy2': 1,
    'enemy2Shot': 2,
}

ENTITY_SHOT_DELAY = {
    'player1': 10,
    'player2': 10,
    'enemy1': 100,
    'enemy2': 200,
}

# H
ENTITY_HEALTH = {
    'level1Bg0': 999,
    'level1Bg1': 999,
    'level1Bg2': 999,
    'level1Bg3': 999,
    'level1Bg4': 999,
    'player1': 300,
    'player1Shot': 1,
    'player2': 300,
    'player2Shot': 1,
    'enemy1': 50,
    'enemy1Shot': 1,
    'enemy2': 60,
    'enemy2Shot': 1,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'player1': pg.K_UP,
                 'player2': pg.K_w}
PLAYER_KEY_DOWN = {'player1': pg.K_DOWN,
                   'player2': pg.K_s}
PLAYER_KEY_LEFT = {'player1': pg.K_LEFT,
                   'player2': pg.K_a}
PLAYER_KEY_RIGHT = {'player1': pg.K_RIGHT,
                    'player2': pg.K_d}
PLAYER_KEY_SHOOT = {'player1': pg.K_RCTRL,
                    'player2': pg.K_LCTRL}

# S
SPAWN_TIME = 3000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
