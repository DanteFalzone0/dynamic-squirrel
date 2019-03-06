"""
Copyright (C) 2019 Dante Falzone

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import pygame
import os
import sys
import random
import re
from pygame.locals import *

fpsClock = pygame.time.Clock()

SURF = pygame.display.set_mode((1000, 600))  # Set the surface

def beep(freq, time):  # Make a beeping noise.
    os.system('play -n synth %s sin %s' % (time / 1000, freq))

pygame.font.init()
myfont = pygame.font.SysFont("$HACKERMAN", 24)  # Initialize the font (dependency: $HACKERMAN font; available as FOSS on FontStruct)

ball = pygame.image.load('ballpix')
trail = pygame.image.load('trail')
bg0 = pygame.image.load('stars0')
bg0 = pygame.transform.scale(bg0, (1000, 600))
bg1 = pygame.image.load('stars1')
bg1 = pygame.transform.scale(bg1, (1000, 600))

ball_x = 430
ball_y = 230
ball_down_momentum = 0
ball_left_momentum = 0

# gravity_val = (1 / 6)

bounciness = 1

score = 0

gravity = 0
trailbool = 1
ballbool = 1
cycle = 0

previous_y_positions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
previous_x_positions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.set_caption("Gravity Ball by Dante Falzone")
    
    
    instructions = myfont.render("Arrow keys to move, G to toggle gravity, T to toggle trail, B to toggle ball", 1, (0, 255, 80))

    if gravity == 1:
        string = "ON"
    else:
        string = "OFF"
    
    gravity_status = myfont.render("Gravity is " + string, 1, (0, 255, 80))

    SURF.fill((0, 0, 0)) # Clear the screen
    if cycle in range (0, 30):
        SURF.blit(bg0, (0, 0))
    else:
        SURF.blit(bg1, (0, 0))
    
    previous_x_positions.append(ball_x + 7.5)
    previous_y_positions.append(ball_y + 7.5)
    if len(previous_x_positions) > 10:
        del previous_x_positions[0]
    if len(previous_y_positions) > 10:
        del previous_y_positions[0]
    
    SURF.blit(instructions, (70, 10))
    SURF.blit(gravity_status, (430, 40))

    if trailbool == 1:
        SURF.blit(trail, (previous_x_positions[0], previous_y_positions[0]))
        SURF.blit(trail, (previous_x_positions[2], previous_y_positions[2]))
        SURF.blit(trail, (previous_x_positions[4], previous_y_positions[4]))
        SURF.blit(trail, (previous_x_positions[6], previous_y_positions[6]))
        SURF.blit(trail, (previous_x_positions[8], previous_y_positions[8]))

    if ballbool == 1:
        SURF.blit(ball, (ball_x, ball_y))
    else:
        SURF.blit(trail, (ball_x + 7.5, ball_y + 7.5))
    
    
    ball_y += ball_down_momentum # The ball falls
    ball_x -= ball_left_momentum # The ball drifts according to its sideways momentum
    
    if gravity == 1:
        ball_down_momentum += 0.5
    
    if ball_y >= 530: # In other words, if the ball touches the bottom
    #    beep(200, 50) # got annoying
        ball_down_momentum = ((ball_down_momentum - bounciness) * -1) + 1
        # the ball bounces upwards and goes a little lower
    if ball_y <= 0:
        ball_down_momentum = ((ball_down_momentum - bounciness) * -1)
    if ball_y > 530:
        ball_y = 530 # The ball will never fall through the ground...
    if ball_y < 0:
        ball_y = 0 # ...or break through the ceiling
        
    if ball_x <= -71: # Screen wrapping
        ball_x = 1070
    if ball_x >= 1071:
        ball_x = -70

    keys = pygame.key.get_pressed()  # Callback for ingame keypresses
    
    if keys[K_LEFT]: # Move the ball side to side
        ball_left_momentum += 1
    if keys[K_RIGHT]:
        ball_left_momentum -= 1
        
    if ball_y in range(529, 531): # while touching the ground
        ball_left_momentum = (255 * ball_left_momentum) / 256 # the ball's motion averages towards zero while on ground
        
    if keys[K_UP]: # Increase the ball's energy
        ball_down_momentum -= 1.5
    if keys[K_DOWN]:
        ball_down_momentum += 1.5
    
    if keys[K_g]:
        if gravity == 1:
            gravity = 0
        else:
            gravity = 1
            
    if keys[K_t]:
        if trailbool == 1:
            trailbool = 0
        else:
            trailbool = 1
            
    if keys[K_b]:
        if ballbool == 1:
            ballbool = 0
        else:
            ballbool = 1
       
    """
    if keys[K_w]:
        gravity_val += 0.01
        bounciness += 0.01
        print(str(bounciness))
    if keys[K_s]:
        if gravity >= 0:
            gravity_val -= 0.01
            bounciness -= 0.01
        print(str(bounciness))
    """
    
    cycle += 1
    if cycle >= 60:
        cycle = 0

    pygame.display.update()
    fpsClock.tick(60)
