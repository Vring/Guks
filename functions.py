import pygame
import sys
import os
import itertools
from locals import *
import random


def draw_interface(window, wind_num, fps, cur_team_name, cur_gook_name):
    font = pygame.font.Font(None, 50)
    wind_text = font.render(str(wind_num), True, pygame.Color('white'))
    fps_text = font.render(str(fps), True, pygame.Color('white'))
    cur_team_text = font.render(str(cur_team_name), True, pygame.Color('white'))
    cur_gook_text = font.render(str(cur_gook_name), True, pygame.Color('white'))
    window.blit(wind_text, [10, 10])
    window.blit(fps_text, [910, 10])
    window.blit(cur_team_text, [1700, 10])
    window.blit(cur_gook_text, [1700, 40])


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image