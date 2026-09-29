import os
os.environ['SDL_VIDEODRIVER'] = 'windib'
import pygame
import math
import time
import fonts
import animations
import cv2

video_section0 = cv2.VideoCapture("introAnimation.mp4")
video_section0_fps = video_section0.get(cv2.CAP_PROP_FPS)

video_section1 = cv2.VideoCapture("danceInTheLightsAni.mp4")
video_section1_fps = video_section1.get(cv2.CAP_PROP_FPS)
    
pygame.init()
fonts.init()

# Window
WIDTH, HEIGHT = 1400, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.mixer.music.load("rockTrimmed.mp3")
pygame.mixer.music.play()

clock = pygame.time.Clock()

start_time = time.time()

running = True
while running:
    screen.fill((0, 0, 0))
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    elapsed_time = pygame.mixer.music.get_pos() / 1000.0 

#seksjon 0
    if 0.000 <= elapsed_time <= 16.387:
        target_frame = int((elapsed_time - 0) * video_section0_fps)
        video_section0.set(cv2.CAP_PROP_POS_FRAMES, target_frame)
        ret, frame_section0 = video_section0.read()
        if ret:
            frame_section0 = cv2.cvtColor(frame_section0, cv2.COLOR_BGR2RGB)
            frame_section0 = cv2.resize(frame_section0, (1400, 1000))
            surface_section0 = pygame.surfarray.make_surface(frame_section0.swapaxes(0, 1))
            screen.blit(surface_section0, (0, 0))

    if 0.000 <= elapsed_time <= 16.387:
        animations.temp1(screen) 
        animations.temp2(screen)
        animations.temp3(screen)      

#seksjon 1

    if 16.387 <= elapsed_time <= 17.807:
        # Add your animation or logic here
        animations.i_wanna_rock_right_now(screen)

#seksjon 2

    if 17.807 < elapsed_time <= 18.302:
        animations.i_wanna(screen)

    if 18.302 < elapsed_time <= 19.710:
        animations.i_wanna_rock_right_now2(screen)

#seksjon 3

    if 19.710 < elapsed_time <= 20.215:
        animations.i_wanna2(screen)

    if 20.215 < elapsed_time <= 21.638:
        animations.i_wanna_rock_right_now3(screen)

#seksjon 4

    if 21.638 < elapsed_time <= 23.554:
        animations.now1(screen, elapsed_time)

    if 22.109 < elapsed_time <= 23.554:
        animations.now2(screen, elapsed_time)

    if 22.616 < elapsed_time <= 23.554:
        animations.rock_right_now1(screen)

#seksjon 5

    if 23.557 < elapsed_time <= 23.753:
        animations.i(screen)
    
    if 23.753 < elapsed_time <= 24.052:
        animations.wanna(screen)

    if 24.052 < elapsed_time <= 24.290:
        animations.i(screen)
    
    if 24.290 < elapsed_time <= 24.535:
        animations.wanna(screen)

    if 24.535 < elapsed_time <= 25.482:
        animations.rock_right_now2(screen)

#seksjon 6

    #iwanna
    if 25.482 < elapsed_time <= 25.989:
        animations.i_wanna1_1(screen)

    #iwanna
    if 25.989 < elapsed_time <= 26.472:
        animations.i_wanna1_2(screen)

    #rock right now
    if 26.472 < elapsed_time <= 27.401:
        animations.rock_right_now2(screen)

#sekjson 7

    #iwanna
    if 27.401 < elapsed_time <= 27.902:
        animations.i_wanna1_1(screen)
    #iwanna
    if 27.902 < elapsed_time <= 28.372:
        animations.i_wanna1_2(screen)

    #rock
    if 28.372 < elapsed_time <= 28.855:
        animations.rock(screen)

#seksjon 8

    if 28.855 < elapsed_time <= 29.814:
        animations.right(screen, elapsed_time)

    #31.801
    if 29.814 < elapsed_time <= 38.801:
        animations.nowwww(screen, elapsed_time)

#seksjon 9
    #danceinTheLightsAni
    if 31.978 < elapsed_time:
        target_frame = int((elapsed_time - 31.978) * video_section1_fps)
        video_section1.set(cv2.CAP_PROP_POS_FRAMES, target_frame)
        ret, frame_section1 = video_section1.read()
        if ret:
            frame_section1 = cv2.cvtColor(frame_section1, cv2.COLOR_BGR2RGB)
            frame_section1 = cv2.resize(frame_section1, (700, 500))
            surface_section1 = pygame.surfarray.make_surface(frame_section1.swapaxes(0, 1))
            screen.blit(surface_section1, (350, 250))

    #iwannada
    if 31.978 < elapsed_time <= 32.968:
        animations.i_wanna_da(screen, elapsed_time)

    #iwannadance
    if 32.968 < elapsed_time <= 34.141:
        animations.i_wanna_dance(screen, elapsed_time)

    #inthelights
    if 34.141 < elapsed_time <= 35.827:
        animations.in_the(screen)
        
    if 34.355 < elapsed_time <= 35.827:
        #animations.lights(screen, elapsed_time)
        animations.lights_lamp_left(screen, 550, 230)
        animations.lights_lamp_right(screen, 850, 230)   
#section 10
    #iwannaro
    if 35.847 < elapsed_time <= 36.085:
        animations.i(screen, elapsed_time)

    if 36.085 < elapsed_time <= 36.340:
        animations.wanna(screen, elapsed_time)

    if 36.340 < elapsed_time <= 36.793:
        animations.ro(screen, elapsed_time)

    #iwannarockyourbody
    if 36.793 < elapsed_time <= 37.035:
        animations.i(screen, elapsed_time)
    
    if 37.035 < elapsed_time <= 37.516:
        animations.wanna(screen, elapsed_time)

    if 37.516 < elapsed_time <= 39.476:
        animations.rock10_1(screen, elapsed_time)
    
    if 38.000 < elapsed_time <= 39.476:
        animations.your10_2(screen, elapsed_time)
    
    if 38.478 < elapsed_time <= 39.476:
        animations.body10_3(screen, elapsed_time)
#section 11
    #iwannagoiwanna
    if 39.683 < elapsed_time <= 39.925:
        animations.i(screen, elapsed_time)

    if 39.925 < elapsed_time <= 40.378:
        animations.wanna(screen, elapsed_time)

    if 40.378 < elapsed_time <= 40.649:
        animations.go(screen, elapsed_time)

    if 40.649 < elapsed_time <= 40.835:
        animations.i(screen, elapsed_time)
    
    if 40.835 < elapsed_time <= 41.351:
        animations.wanna(screen, elapsed_time)

    #goforaride
    if 41.351 < elapsed_time <= 43.392:
        animations.go_for_a(screen, elapsed_time)

    if 40.000 < elapsed_time <= 45.432:
        animations.ride_scene(screen, elapsed_time)
#section 12
    #hopinthemusic
    if 43.496 < elapsed_time <= 44.708:
        animations.hopin(screen, elapsed_time)

    if 43.965 < elapsed_time <= 44.708:
        animations.the(screen, elapsed_time)

    if 44.222 < elapsed_time <= 44.708:
        animations.music(screen, elapsed_time)
#section 13
    #androckyourbodyright
    if 44.696 < elapsed_time <= 45.188:
        animations.and_(screen, elapsed_time)
    if 45.188 < elapsed_time <= 45.668:
        animations.rock10_1(screen, elapsed_time)
    if 45.668 < elapsed_time <= 46.148:
        animations.your10_2(screen, elapsed_time)
    if 46.148 < elapsed_time <= 47.080:
        animations.body10_3(screen, elapsed_time)

    if 47.080 < elapsed_time <= 47.942:
        animations.right2(screen, elapsed_time)
#section 14
    #rockthatbody
    if  47.126 < elapsed_time <= 47.988:
        animations.rock14_1(screen)

    if  47.352 < elapsed_time <= 47.988:
        animations.that14_1(screen)

    if  47.599 < elapsed_time <= 47.988:
        animations.body14_1(screen)
    #cmoncmon
    if 48.236 < elapsed_time <= 48.962:
        animations.cmon_cmon14_1(screen)
    #rockthatbody
    if 49.038 < elapsed_time <= 49.901:
        animations.rock14_2(screen)

    if 49.243 < elapsed_time <= 49.901:
        animations.that14_2(screen)

    if 49.490 < elapsed_time <= 49.901:
        animations.body14_2(screen)            
    #rockyourbody
    if 49.942 < elapsed_time <= 50.804:
        animations.rock_your_body(screen)
    #rockthatbody
    if 50.970< elapsed_time <= 52.149:
        animations.rock14_3(screen)

    if 51.151 < elapsed_time <= 52.149:
        animations.that14_3(screen)

    if 51.423 < elapsed_time <= 52.149:
        animations.body14_3(screen)
    
    #cmoncmon
    if 52.149< elapsed_time <= 52.800:
        animations.cmon_cmon14_3(screen)
    #rock-that-bo-dy
    if 52.883 < elapsed_time <= 60.000:
        animations.rock14_4(screen, elapsed_time)

    if 53.352 < elapsed_time <= 60.000:
        animations.that14_4(screen, elapsed_time)

    if 53.831  < elapsed_time <= 60.000:
        animations.bo14_4(screen, elapsed_time)

    if 54.315 < elapsed_time <= 60.000:
        animations.dy14_4(screen, elapsed_time)        
    #rockthatbody
    #cmoncmon
    #rockthatbody
    #rockyourbody
    #rockthatbody   
    #cmoncmon
    #rock-that-bo-dy

    #letmeseeyourbodyrock
    #shakinitfromthebottomtotop
    #freaktowhatthedjdrop
    #webetheonestomakeithot
    #tomakeithot
    #electricshockenergylikeabillionwatts
    #spacebeboominthespeakerspop
    #galacticcallmemrspock
    #webumpininyourparkinglot
    #whenyourecominupinthespot
    #dontbringnothinwecallpinkdot
    #causeweburningaroundtheclock
    #hitthelightsandthenturnthemof
    #ifyoubringthatdontmakeyoustop
    #likethejungleweruntheblock
    #noonerollinthewaywerock
    #waywerock

    #iwannarockrightnow
    #iwanna


    pygame.display.flip()

video_section0.release()
pygame.quit()        