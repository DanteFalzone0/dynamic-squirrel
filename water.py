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

score = 0

gravity = 1

drops_x = []
drops_y = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.set_caption("Water by Dante Falzone")
    
    
    instructions = myfont.render("Click to make a droplet of water", 1, (0, 255, 80))
    if pygame.mouse.get_pressed()[0] == 1:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        for q in range (-16, 16):
            drops_x.append(x + q)
            drops_x.append(x - q)
            drops_y.append(y + q)
            drops_y.append(y - q)

    if gravity == 1:
        string = "ON"
    else:
        string = "OFF"
    
    gravity_status = myfont.render("Gravity is " + string, 1, (0, 255, 80))

    SURF.fill((0, 0, 0)) # Clear the screen
    
        
    for x in range (0, len(drops_x)):
        pygame.draw.rect(SURF, (20, 20, 255), (drops_x[x], drops_y[x], 1, 1))
            
    for y in range (0, len(drops_y)):
        if drops_y[y] < 590:
            drops_y[y] += 16
        if drops_y[y] >= 590:
            drops_y[y] = 589
            
    for x in range (0, len(drops_x)):
        x_change = random.randint(-1, 1)
        drops_x[x] += x_change
        
    for x in range (0, len(drops_x)):
        if drops_x[x] in drops_x[0:(x - 1)] and drops_y[x] in drops_y[0:(x - 1)]:
            drops_y[x] -= 1

    pygame.display.update()
    fpsClock.tick(15)
