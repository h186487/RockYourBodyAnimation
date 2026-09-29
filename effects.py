import colorsys
import random

import pygame

import fonts


def rainbow(elapsed_time, speed):
    hue = (elapsed_time * speed) % 1.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    return int(r * 255), int(g * 255), int(b *255)

def vibrate(x, y, intensity):
    offset_x = random.randint(-intensity, intensity)
    offset_y = random.randint(-intensity, intensity)
    return x + offset_x, y + offset_y

def font_cycle(text, elapsed_time, colour, position):
    font_cycle = [
        fonts.FONT_100,
        fonts.FONT_101,
        fonts.FONT_102,
        fonts.FONT_103,
        fonts.FONT_104,
        fonts.FONT_105
    ]
    font_index = int(elapsed_time * 5) % len(font_cycle)
    current_font = font_cycle[font_index]

    rendered_text = current_font.render(text, True, colour)
    rect = rendered_text.get_rect(center=position)
    return rendered_text, rect

def font_sizeUp(text, elapsed_time, colour, position):
    font_size = int(50 + elapsed_time * 100)
    font_size = min(font_size, 200)

    current_font = pygame.font.Font(None, font_size)

    rendered_text = current_font.render(text, True, colour)
    rect = rendered_text.get_rect(center=position)

    return rendered_text, rect