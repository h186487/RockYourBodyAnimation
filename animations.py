import colorsys
import math
from random import random
from tkinter import font
import pygame
import effects
import fonts

#font = pygame.font.Font(None, 100)

def temp1(screen, y_offset=0):
    #font = pygame.font.Font(None, 74)
    text = fonts.FONT_106.render("TEMP", True, (255, 255, 255))
    rect = text.get_rect(center=(700, 200 + y_offset))
    screen.blit(text, rect)

def temp2(screen, y_offset=0):
    #font = pygame.font.Font(None, 74)
    text = fonts.FONT_108.render("TEMP", True, (255, 255, 255))
    rect = text.get_rect(center=(700, 400 + y_offset))
    screen.blit(text, rect)

def temp3(screen, y_offset=0):
    #font = pygame.font.Font(None, 74)
    text = fonts.FONT_107.render("TEMP", True, (255, 255, 255))
    rect = text.get_rect(center=(700, 800 + y_offset))
    screen.blit(text, rect)

"""seksjon 1"""

def i_wanna_rock_right_now(screen, y_offset=0):
    text = fonts.FONT_100.render("I WANNA ROCK RIGHT NOW!", True, (255, 192, 203))
    rect = text.get_rect(topleft=(100, 100 + y_offset))
    screen.blit(text, rect)

"""seksjon 2"""
def i_wanna(screen, y_offset=0):
    text = fonts.FONT_107.render("I WANNA", True, (255, 182, 193))
    rect = text.get_rect(topleft=(100, 100 + y_offset))
    screen.blit(text, rect)

def i_wanna_rock_right_now2(screen, y_offset=0):
    text1 = fonts.FONT_100.render("I WANNA ROCK RIGHT NOW!", True, (255, 105, 180))
    rect1 = text1.get_rect(topleft=(100, 100 + y_offset))
    screen.blit(text1, rect1)

"""seksjon 3"""
def i_wanna2(screen, y_offset=0):
    text = fonts.FONT_107.render("I WANNA", True, (199, 21, 133))
    rect = text.get_rect(topleft=(100, 100 + y_offset))
    screen.blit(text, rect)

def i_wanna_rock_right_now3(screen, y_offset=0):
    text = fonts.FONT_100.render("I WANNA ROCK RIGHT NOW!", True, (219, 112, 147))
    rect = text.get_rect(topleft=(100, 100 + y_offset))
    screen.blit(text, rect)

"""seksjon 4"""
#wobble
def now1(screen, elapsed_time, y_offset=0):
    text, rect = effects.font_sizeUp(
                "now",
                elapsed_time,
                (186, 85, 211),
                (700, 200)
            )
    screen.blit(text, rect)
#700,200. 700,500
#wobble
def now2(screen, elapsed_time, y_offset=0):
    text, rect = effects.font_sizeUp(
                "now",
                elapsed_time,
                (186, 85, 211),
                (700, 500)
            )
    screen.blit(text, rect)

def rock_right_now1(screen, y_offset=0):
    text = fonts.FONT_107.render("Rock Right Now", True, (102, 51, 153))
    rect = text.get_rect(center=(700, 800 + y_offset))
    screen.blit(text, rect)

"""seksjon 5"""
def i(screen, y_offset=0):
    text = fonts.FONT_106.render("I", True, (255, 140, 0))
    rect = text.get_rect(center=(700, 500 + y_offset))
    screen.blit(text, rect)    

def wanna(screen, y_offset=0):
    text = fonts.FONT_107.render("WANNA", True, (255, 165, 0))
    rect = text.get_rect(center=(700, 500 + y_offset))
    screen.blit(text, rect) 

def rock_right_now2(screen, y_offset=0):
    text = fonts.FONT_108.render("ROCK RIGHT NOW", True, (255, 127, 80))
    rect = text.get_rect(center=(700, 500 + y_offset))
    screen.blit(text, rect) 

"""seksjon 6/7"""

def i_wanna1_1(screen, y_offset=0):
    text = fonts.FONT_107.render("I WANNA", True, (240, 177, 41))
    rect = text.get_rect(center=(700, 500 + y_offset))
    screen.blit(text, rect)

def i_wanna1_2(screen, y_offset=0):
    text = fonts.FONT_107.render("I WANNA", True, (235, 235, 59))
    rect = text.get_rect(center=(700, 500 + y_offset))
    screen.blit(text, rect)

    #seksjon 7
def rock(screen, y_offset=0):
    text = fonts.FONT_105.render("ROCK", True, (255, 127, 80))
    rect = text.get_rect(center=(700, 500 + y_offset))
    screen.blit(text, rect)


"""seksjon 8"""

def right(screen, elapsed_time, y_offset=0):
    text, rect = effects.font_cycle(
        "right",
        elapsed_time,
        (186, 85, 211),
        (700, 300)
    )
    screen.blit(text, rect)

#trail/ghost effect
trail_positions = []

def nowwww(screen, elapsed_time, y_offset=0):
    global trail_positions

    font = pygame.font.Font(None, 200)
    text = font.render("NOW", True, (255, 160, 122))
    section_start = 29.9
    x = 700 + (elapsed_time - section_start) * 200
    y = 500 + y_offset
    trail_positions.append((x, y))

    if len(trail_positions) > 10:
        trail_positions.pop(0)
    
    for i, (tx, ty) in enumerate(trail_positions):
        alpha = int(255 * (i+1) / len(trail_positions))
        text_copy = text.copy()
        text_copy.set_alpha(alpha)
        rect = text_copy.get_rect(center=(tx, ty))
        screen.blit(text_copy, rect)

"""seksjon 9"""

def i_wanna_da(screen, elapsed_time, y_offset=0, gap=20):
    font = pygame.font.Font(None, 74)
    text1 = font.render("I WANNA", True, (255, 255, 255))
    text2 = font.render("DA", True, effects.rainbow(elapsed_time, speed = 3))

    total_width = text1.get_width() + gap + text2.get_width()
    start_x = 700 - total_width // 2
    y = 100

    rect1 = text1.get_rect(topleft=(start_x, y))
    rect2 = text2.get_rect(topleft=(start_x + text1.get_width() + gap, y + y_offset))

    screen.blit(text1, rect1) 
    screen.blit(text2, rect2)

def i_wanna_dance(screen, elapsed_time, y_offset=0, gap=20):
    font = pygame.font.Font(None, 74)
    text1 = font.render("I WANNA", True, (255, 255, 255))
    text2 = font.render("DANCE", True, effects.rainbow(elapsed_time, speed = 3))

    total_width = text1.get_width() + gap + text2.get_width()
    start_x = 700 - total_width // 2
    y = 100

    x_dance = start_x + text1.get_width() + gap
    x_vib, y_vib = effects.vibrate(x_dance, y + y_offset, intensity=5)

    rect1 = text1.get_rect(topleft=(start_x, y))
    rect2 = text2.get_rect(topleft=(x_vib, y_vib))

    screen.blit(text1, rect1) 
    screen.blit(text2, rect2)

def in_the(screen, y_offset=0):
    font = pygame.font.Font(None, 74)
    text = font.render("IN THE", True, (255, 255, 255))
    rect = text.get_rect(center=(700, 800 + y_offset))
    screen.blit(text, rect)

def lights(screen, y_offset=0):
    font = pygame.font.Font(None, 74)
    text = font.render("I WANNA", True, (255, 255, 255))
    rect = text.get_rect(center=(400, 300 + y_offset))
    screen.blit(text, rect)

def lights_lamp_left(screen,x, y, y_offset=0):
    # Lamp body (black)
    pygame.draw.rect(screen, (0, 0, 0), (x - 15, y + y_offset, 30, 20))  
    
    # Lamp bulb left
    bulb_surf = pygame.Surface((40, 20), pygame.SRCALPHA) 
    pygame.draw.ellipse(bulb_surf, (255, 255, 255), (0, 0, 40, 20))
    bulb_surf = pygame.transform.rotate(bulb_surf, 20) 
    screen.blit(bulb_surf, (x - 20, y + y_offset - 5))

    # Light cone left
    light_color = (255, 255, 150, 100)  # RGBA
    light_cone_left = pygame.Surface((500, 400), pygame.SRCALPHA)  
    pygame.draw.polygon(light_cone_left, light_color, [(100,0), (500,500), (0,500)])
    screen.blit(light_cone_left, (x - 100, y + y_offset))
    
def ro(screen, y_offset=0):
    text = fonts.FONT_100.render("RO-", True, (232, 148, 30))
    rect = text.get_rect(center=(700, 500 + y_offset))
    screen.blit(text, rect)

def rock10_1(screen, y_offset=0):
    text1 = fonts.FONT_100.render("ROCK", True, (232, 148, 30))
    rect1 = text1.get_rect(center=(700, 400 + y_offset))
    screen.blit(text1, rect1)

    
def your10_2(screen, y_offset=0):
    text2 = fonts.FONT_100.render("YOUR", True, (232, 148, 30))
    rect2 = text2.get_rect(center=(700, 500 + y_offset))
    screen.blit(text2, rect2)

def body10_3(screen, y_offset=0):
    text3 = fonts.FONT_100.render("BODY", True, (232, 148, 30))
    rect3 = text3.get_rect(center=(700, 600 + y_offset))
    screen.blit(text3, rect3)


    # Blit the cone from lamp position

def lights_lamp_right(screen,x, y, y_offset=0):
    pygame.draw.rect(screen, (0, 0, 0), (x - 15, y + y_offset, 30, 20))

    # Lamp bulb right
    bulb_surf = pygame.Surface((40, 20), pygame.SRCALPHA) 
    pygame.draw.ellipse(bulb_surf, (255, 255, 255), (0, 0, 40, 20))
    bulb_surf = pygame.transform.rotate(bulb_surf, -20)
    screen.blit(bulb_surf, (x - 20, y + y_offset - 5))

    # lgiht cone right
    light_color = (255, 255, 150, 100)
    light_cone_right = pygame.Surface((500, 400), pygame.SRCALPHA)
    pygame.draw.polygon(light_cone_right, light_color, [(400,0), (0,500), (500,500)])
    screen.blit(light_cone_right, (x - 400, y + y_offset))

#slide
def go (screen, y_offset=0):
    text = fonts.FONT_100.render("GO", True, (232, 148, 30))
    rect = text.get_rect(center=(700, 500 + y_offset))
    screen.blit(text, rect)

def go_for_a(screen, y_offset=0):
    text = fonts.FONT_100.render("GO FOR A", True, (232, 148, 30))
    rect = text.get_rect(center=(700, 800 + y_offset))
    screen.blit(text, rect)

def banner(screen, x, y, elapsed_time):
    rect_width = 400
    rect_height = 150
    rect_color = (255, 215, 0)
    wave_amplitude = 8       
    wave_frequency = 3

    wave_offset = math.sin(elapsed_time * wave_frequency) * wave_amplitude

    num_points = 6
    top_points = []
    bottom_points = []
    for i in range(num_points + 1):
        px = x - rect_width // 2 + i * rect_width / num_points
        offset = math.sin(elapsed_time * wave_frequency + i) * wave_amplitude
        top_points.append((px, y - rect_height // 2 + offset))
        bottom_points.append((px, y + rect_height // 2 + offset))

    points = top_points + bottom_points[::-1]
    pygame.draw.polygon(screen, rect_color, points, 4)


    text = fonts.FONT_100.render("RIDE", True, rect_color)
    text_rect = text.get_rect(center=(x,y))
    screen.blit(text, text_rect)

def ride_stick_figure(screen, x, y, phase):
    color = (255, 255, 255)

    # Head
    pygame.draw.circle(screen, color, (int(x), y - 35), 10, 2)

    # Body
    pygame.draw.line(screen, color, (x, y - 25), (x, y + 20), 2)

    # Arms (slight counter swing)
    arm_swing = math.sin(phase) * 10
    pygame.draw.line(screen, color, (x, y - 10), (x - 20, y + arm_swing), 2)
    pygame.draw.line(screen, color, (x, y - 10), (x + 20, y - arm_swing), 2)

    # Legs (walking)
    leg_swing = math.sin(phase) * 20

    # Left leg
    pygame.draw.line(
        screen,
        color,
        (x, y + 20),
        (x - 10 + leg_swing, y + 50),
        2
    )

    # Right leg (opposite phase)
    pygame.draw.line(
        screen,
        color,
        (x, y + 20),
        (x + 10 - leg_swing, y + 50),
        2
    )

def ride_scene(screen, elapsed_time, y_offset=0):
    speed = 6
    BANNER_DISTANCE = 350  # distance behind the stick figure

    if not hasattr(ride_scene, "stick_x"):
        # Stick starts offscreen right
        ride_scene.stick_x = 1400 + 50
        # Banner starts even further right
        ride_scene.banner_x = ride_scene.stick_x + BANNER_DISTANCE
        ride_scene.walk_phase = 0

    # Move everything left
    ride_scene.stick_x -= speed
    ride_scene.walk_phase += speed * 0.15

    # Banner follows the stick figure, lagging behind
    target_banner_x = ride_scene.stick_x + BANNER_DISTANCE
    drag = 0.08
    ride_scene.banner_x += (target_banner_x - ride_scene.banner_x) * drag

    y = 500

    # Draw stick figure
    ride_stick_figure(screen, ride_scene.stick_x, y, ride_scene.walk_phase)

    # Draw rope (stick hand → banner left edge)
    pygame.draw.line(
        screen,
        (180, 180, 180),
        (ride_scene.stick_x + 15, y + 5),      # stick’s right hand
        (ride_scene.banner_x - 200, y),        # banner left edge
        3
    )

    # Draw banner
    banner(screen, ride_scene.banner_x, y, elapsed_time)

def the(screen, y_offset=0):   
    text = fonts.FONT_100.render("THE", True, (255, 20, 147))
    rect = text.get_rect(center=(600, 350 + y_offset))
    screen.blit(text, rect)

def music(screen, y_offset=0):   
    text = fonts.FONT_100.render("MUSIC", True, (255, 20, 147))
    rect = text.get_rect(center=(800, 350 + y_offset))
    screen.blit(text, rect)

def hopin(screen, elapsed_time):
    text_str = "HOPIN"
    color = (255, 20, 147)

    center_x = 700
    center_y = 500
    radius = 100

    num_letters = len(text_str)
    time_per_letter = 0.1  

    letters_to_show = min(num_letters, int(elapsed_time / time_per_letter))
    letters_to_show = max(1, letters_to_show)  

    for i in range(letters_to_show):
        angle = math.pi * (i / (num_letters - 1))
        x = center_x + radius * math.sin(angle - math.pi / 2)
        y = center_y + radius * math.cos(angle - math.pi / 2)

        letter_surf = fonts.FONT_100.render(text_str[i], True, color)
        letter_rect = letter_surf.get_rect(center=(x, y))
        screen.blit(letter_surf, letter_rect)


def and_(screen, y_offset=0):   
    text = fonts.FONT_100.render("AND", True, (255, 20, 147))
    rect = text.get_rect(center=(700, 500 + y_offset))
    screen.blit(text, rect)

def right2(screen, elapsed_time, y_offset=0):
    text, rect = effects.font_cycle(
        "right",
        elapsed_time,
        (186, 85, 211),
        (700, 500)
    )
    screen.blit(text, rect)


def rock14_1(screen, y_offset=0):   
    text = fonts.FONT_101.render("ROCK", True, (255, 20, 147))
    rect = text.get_rect(center=(200, 400 + y_offset))
    screen.blit(text, rect)

def that14_1(screen, y_offset=0):   
    text = fonts.FONT_102.render("THAT", True, (255, 20, 147))
    rect = text.get_rect(center=(200, 500 + y_offset))
    screen.blit(text, rect)

def body14_1(screen, y_offset=0):   
    text = fonts.FONT_103.render("BODY", True, (255, 20, 147))
    rect = text.get_rect(center=(200, 600 + y_offset))
    screen.blit(text, rect)

def cmon_cmon14_1(screen, y_offset=0):   
    text = fonts.FONT_100.render("C'MON C'MON", True, (255, 20, 147))
    rect = text.get_rect(center=(700, 500 + y_offset))
    screen.blit(text, rect)

def rock14_2(screen, y_offset=0):   
    text = fonts.FONT_103.render("ROCK", True, (255, 20, 147))
    rect = text.get_rect(center=(1200, 400 + y_offset))
    screen.blit(text, rect)

def that14_2(screen, y_offset=0):   
    text = fonts.FONT_104.render("THAT", True, (255, 20, 147))
    rect = text.get_rect(center=(1200, 500 + y_offset))
    screen.blit(text, rect)

def body14_2(screen, y_offset=0):   
    text = fonts.FONT_105.render("BODY", True, (255, 20, 147))
    rect = text.get_rect(center=(1200, 600 + y_offset))
    screen.blit(text, rect)

def rock_your_body(screen, y_offset=0):   
    text = fonts.FONT_100.render("ROCK YOUR BODY", True, (255, 20, 147))
    rect = text.get_rect(center=(700, 500 + y_offset))
    screen.blit(text, rect)

def rock14_3(screen, y_offset=0):   
    text = fonts.FONT_102.render("ROCK", True, (255, 20, 147))
    rect = text.get_rect(center=(200, 400 + y_offset))
    screen.blit(text, rect)

def that14_3(screen, y_offset=0):   
    text = fonts.FONT_103.render("THAT", True, (255, 20, 147))
    rect = text.get_rect(center=(1200, 400 + y_offset))
    screen.blit(text, rect)

def body14_3(screen, y_offset=0):   
    text = fonts.FONT_104.render("BODY", True, (255, 20, 147))
    rect = text.get_rect(center=(200, 600 + y_offset))
    screen.blit(text, rect)

def cmon_cmon14_3(screen, y_offset=0):   
    text = fonts.FONT_100.render("C'MON C'MON", True, (255, 20, 147))
    rect = text.get_rect(center=(1200, 600 + y_offset))
    screen.blit(text, rect)

def rock14_4(screen, elapsed_time, y_offset=0):   
    text = fonts.FONT_103.render("ROCK", True, (255, 20, 147))
    section_start = 52.883
    x = 550 - ((elapsed_time - section_start) * 250)
    rect = text.get_rect(center=(x, 500 + y_offset))
    screen.blit(text, rect)

def that14_4(screen, elapsed_time, y_offset=0):   
    text = fonts.FONT_104.render("THAT", True, (255, 20, 147))
    section_start = 53.352
    x = 850 + ((elapsed_time - section_start) * 250)
    rect = text.get_rect(center=(x, 500 + y_offset))
    screen.blit(text, rect)

def bo14_4(screen, elapsed_time, y_offset=0):   
    text = fonts.FONT_105.render("BO", True, (255, 20, 147))
    section_start = 53.831
    x = 550 - ((elapsed_time - section_start) * 250)
    rect = text.get_rect(center=(x, 500 + y_offset))
    screen.blit(text, rect)

def dy14_4(screen, elapsed_time, y_offset=0):   
    text = fonts.FONT_105.render("DY", True, (255, 20, 147))
    section_start = 54.315
    x = 850 + ((elapsed_time - section_start) * 250)
    rect = text.get_rect(center=(x, 500 + y_offset))
    screen.blit(text, rect)
 


