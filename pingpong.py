# coding: utf-8
import sys
import pygame
from config import Settings


def run_game():
    pygame.init()
    pp_settings = Settings()
    screen = pygame.display.set_mode((pp_settings.window_width, pp_settings.window_height))
    pygame.display.set_caption("Ping Pong")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(pp_settings.bg_color)
        pygame.display.flip()


run_game()