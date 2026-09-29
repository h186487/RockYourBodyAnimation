import pygame

FONT_000 = None
FONT_100 = None
FONT_101 = None
FONT_102 = None
FONT_103 = None
FONT_104 = None
FONT_105 = None

def init():
    global FONT_000, FONT_100, FONT_101, FONT_102, FONT_103, FONT_104, FONT_105

    FONT_000 = pygame.font.Font(None, 74)
    FONT_100 = pygame.font.SysFont("arial", 74)
    FONT_101 = pygame.font.SysFont("timesnewroman", 74)
    FONT_102 = pygame.font.SysFont("comicsansms", 74)
    FONT_103 = pygame.font.SysFont("couriernew", 74)
    FONT_104 = pygame.font.SysFont("impact", 74)
    FONT_105 = pygame.font.SysFont("verdana", 74)