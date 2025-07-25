#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
import pygame as pg

from pygame import Surface, Rect
from pygame.font import Font

from code.enemy import Enemy
from code.entityMediator import EntityMediator
from code.const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode  # Modo de jogo
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name))
        player = (EntityFactory.get_entity('player1'))
        player.score = player_score[0]
        self.entity_list.append(player)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = (EntityFactory.get_entity('player2'))
            player.score = player_score[1]
            self.entity_list.append(player)
            self.entity_list.append(EntityFactory.get_entity('player2'))
        pg.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pg.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
        pg.mixer_music.load(f'./assets/{self.name}.wav')
        pg.mixer_music.play(-1)
        clock = pg.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'player1':
                    self.level_text(14, f'player1: - Health: {ent.health} | Score: {ent.score}',
                                    C_GREEN, (10, 25))
                if ent.name == 'player2':
                    self.level_text(14, f'player2: - Health: {ent.health} | Score: {ent.score}',
                                    C_CYAN, (10, 45))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('enemy1', 'enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'player2':
                                player_score[1] = ent.score
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_WHITE,
                            (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE,
                            (10, WIN_HEIGHT - 20))
            pg.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
        # pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pg.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
