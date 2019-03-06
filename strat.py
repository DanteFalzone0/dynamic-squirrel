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

fpsClock = pygame.time.Clock() # This line is necessary so that the framerate can be easily set.

SURF = pygame.display.set_mode((1000, 600))  # Set the surface


def hex(x, y):
    pygame.draw.line(SURF, (100, 100, 100), ( x,         y),       ((x + 8),   y),       1) # Top edge of hex
    pygame.draw.line(SURF, (100, 100, 100), ((x + 8),    y),       ((x + 12), (y + 8)),  1) # Top-right edge of hex
    pygame.draw.line(SURF, (100, 100, 100), ((x + 12),  (y + 8)),  ((x + 8),  (y + 16)), 1) # Bottom-right edge of hex
    pygame.draw.line(SURF, (100, 100, 100), ( x,        (y + 16)), ((x + 8),  (y + 16)), 1) # Bottom edge of hex
    pygame.draw.line(SURF, (100, 100, 100), ( x,         y),       ((x - 4),  (y + 8)),  1) # Top-left edge of hex
    pygame.draw.line(SURF, (100, 100, 100), ( x,        (y + 16)), ((x - 4),  (y + 8)),  1) # Bottom-left edge of hex


def highlight(fakex, fakey): # Highlights selected hexagon when placing something on the board
    x = (fakex * 12) + 32 # Decides where to put the hex on the screen relative to actual screen location
    if fakex / 2 != fakex // 2:
        y = (fakey * 16) + 36
    else:
        y = (fakey * 16) + 44
    pygame.draw.line(SURF, (255, 255, 255), ( x,         y),       ((x + 8),   y),       5) # Top edge of hex
    pygame.draw.line(SURF, (255, 255, 255), ((x + 8),    y),       ((x + 12), (y + 8)),  5) # Top-right edge of hex
    pygame.draw.line(SURF, (255, 255, 255), ((x + 12),  (y + 8)),  ((x + 8),  (y + 16)), 5) # Bottom-right edge of hex
    pygame.draw.line(SURF, (255, 255, 255), ( x,        (y + 16)), ((x + 8),  (y + 16)), 5) # Bottom edge of hex
    pygame.draw.line(SURF, (255, 255, 255), ( x,         y),       ((x - 4),  (y + 8)),  5) # Top-left edge of hex
    pygame.draw.line(SURF, (255, 255, 255), ( x,        (y + 16)), ((x - 4),  (y + 8)),  5) # Bottom-left edge of hex


def blue(fakex, fakey): # Highlights blue territory
    x = (fakex * 12) + 32
    if fakex / 2 != fakex // 2:
        y = (fakey * 16) + 36
    else:
        y = (fakey * 16) + 44
    pygame.draw.line(SURF, (0, 70, 255), ( x,         y),       ((x + 8),   y),       2) # Top edge of hexagon
    pygame.draw.line(SURF, (0, 70, 255), ((x + 8),    y),       ((x + 12), (y + 8)),  2) # Top-right edge of hexagon
    pygame.draw.line(SURF, (0, 70, 255), ((x + 12),  (y + 8)),  ((x + 8),  (y + 16)), 2) # Bottom-right edge of hexagon
    pygame.draw.line(SURF, (0, 70, 255), ( x,        (y + 16)), ((x + 8),  (y + 16)), 2) # Bottom edge of hexagon
    pygame.draw.line(SURF, (0, 70, 255), ( x,         y),       ((x - 4),  (y + 8)),  2) # Top-left edge of hexagon
    pygame.draw.line(SURF, (0, 70, 255), ( x,        (y + 16)), ((x - 4),  (y + 8)),  2) # Bottom-left edge of hexagon


def red(fakex, fakey): # Highlights red territory
    x = (fakex * 12) + 32
    if fakex / 2 != fakex // 2:
        y = (fakey * 16) + 36
    else:
        y = (fakey * 16) + 44
    pygame.draw.line(SURF, (255, 10, 10), ( x,         y),       ((x + 8),   y),       2) # Top edge of hexagon
    pygame.draw.line(SURF, (255, 10, 10), ((x + 8),    y),       ((x + 12), (y + 8)),  2) # Top-right edge of hexagon
    pygame.draw.line(SURF, (255, 10, 10), ((x + 12),  (y + 8)),  ((x + 8),  (y + 16)), 2) # Bottom-right edge of hexagon
    pygame.draw.line(SURF, (255, 10, 10), ( x,        (y + 16)), ((x + 8),  (y + 16)), 2) # Bottom edge of hexagon
    pygame.draw.line(SURF, (255, 10, 10), ( x,         y),       ((x - 4),  (y + 8)),  2) # Top-left edge of hexagon
    pygame.draw.line(SURF, (255, 10, 10), ( x,        (y + 16)), ((x - 4),  (y + 8)),  2) # Bottom-left edge of hexagon


def cross(x, y):
    realx = (x * 12) + 36 # Decides where to put the cross on the screen relative to actual screen location
    if x / 2 != x // 2:
        realy = (y * 16) + 44
    else:
        realy = (y * 16) + 52
    pygame.draw.line(SURF, (255, 255, 255), (realx, (realy - 4)), (realx, (realy + 4)), 1)
    pygame.draw.line(SURF, (255, 255, 255), ((realx - 4), realy), ((realx + 4), realy), 1)


def farm(x, y):
    realx = (x * 12) + 36
    if x / 2 != x // 2:
        realy = (y * 16) + 44
    else:
        realy = (y * 16) + 52
    pygame.draw.line(SURF, (240, 255, 10), ((realx - 4), (realy - 4)), ((realx + 4), (realy - 4)), 1)
    pygame.draw.line(SURF, (240, 255, 10), ((realx - 4), (realy - 0)), ((realx + 4), (realy - 0)), 1)
    pygame.draw.line(SURF, (240, 255, 10), ((realx - 4), (realy + 4)), ((realx + 4), (realy + 4)), 1)


def draw_grid(width, height):
    xwidth = width * 24
    xheight = height * 16
    xvalues = []
    yvalues = []
    for x in range (20, (20 + xwidth)):
        if (x - 20) / 24 == (x - 20) // 24: # In English, "if x - 20 is evenly divisible by 24". I bet there's a way to
            xvalues.append(x)               # do this through an inbuilt function or the math module, but this just seemed
    for y in range (20, (20 + xheight)):    # so elegant to me.
        if (y - 20) / 16 == (y - 20) // 16:
            yvalues.append(y)
    for x in xvalues:
        for y in yvalues:
            hex(x, y)
            hex((x + 12), (y + 8))


def have_adjacents(checksum, list_of_other_checksums): # Return a list of all adjacent checksums.
    adjacency_list = []
    adjacency_list.append(checksum + 1)
    adjacency_list.append(checksum - 1)
    adjacency_list.append(checksum + 1000)
    adjacency_list.append(checksum - 1000)
    adjacency_list.append(checksum + 1001)
    adjacency_list.append(checksum - 1001)

    if set(adjacency_list).intersection(list_of_other_checksums):
        return True
    else:
        return False


pygame.font.init()
myfont = pygame.font.SysFont("$HACKERMAN", 24)  # Initialize the font (dependency: $HACKERMAN font; available as FOSS on FontStruct)

width = 30
height = 34

blue_cities = 0
blue_city_x_vals = []
blue_city_y_vals = []

blue_farms = 0
blue_farm_x_vals = []
blue_farm_y_vals = []


blues = 7
blue_x_vals = [1,  1,  1,  2,  2,  0,  0]
blue_y_vals = [0,  2,  1,  0,  1,  0,  1]


red_cities = 0
red_city_x_vals = []
red_city_y_vals = []

red_farms = 0
red_farm_x_vals = []
red_farm_y_vals = []


reds = 7
red_x_vals = [56, 56, 56, 57, 57, 55, 55]
red_y_vals = [30, 29, 31, 30, 31, 30, 31]


blue_food = 20.0
blue_money = 20.0
red_food = 20.0
red_money = 20.0

mode = 0 # The game modes are as follows:
         # 0 - main game
         # 1 - place a city
         # 2 - place a farm
         # 3 - claim territory


blue_checksums = []
red_checksums  = []
blue_farm_checksums = []
blue_city_checksums = []
red_farm_checksums  = []
red_city_checksums  = []


turn = 0 # 0 for blue, 1 for red


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if blues != 0:
        for x in range (0, blues):
            blue_checksums.append((blue_x_vals[x]) + (1000 * (7 + (blue_y_vals[x]))))


    if reds != 0:
        for x in range (0, reds):
            red_checksums.append((red_x_vals[x]) + (1000 * (7 + red_y_vals[x])))


    if blue_farms != 0:
         for x in range (0, blue_farms):
            blue_farm_checksums.append((blue_farm_x_vals[x]) + (1000 * (7 + (blue_farm_y_vals[x]))))

    if blue_cities != 0:
        for x in range (0, (blue_cities - 1)):
            blue_city_checksums.append((blue_city_x_vals[x]) + (1000 * (7 + (blue_city_y_vals[x]))))

    if red_farms != 0:
         for x in range (0, (red_farms - 1)):
            red_farm_checksums.append((red_farm_x_vals[x]) + (1000 * (7 + (red_farm_y_vals[x]))))

    if red_cities != 0:
        for x in range (0, (red_cities - 1)):
            red_city_checksums.append((red_city_x_vals[x]) + (1000 * (7 + (red_city_y_vals[x]))))

    """
    Checksums are used here as a way of deciding whether or not a certain
    thing can be placed somewhere. For example, suppose the player tries to
    put a farm in a hex where there's already a city. The program will see
    that the checksum of the hex where they want to put their city is already
    in the list of city checksums, and on that basis will not allow them to
    put their farm there.

    By multiplying the y-values of each coordinate pair by 1000, the program
    ensures that there is exactly one and only one possible checksum for every
    hex on the board. For example, the coordinates (32, 7) have a checksum
    of 14032, whereas the coordinates (7, 32) have a checksum of 39007. If the
    program didn't multiply either of the values, then both coordinate pairs
    would have a checksum of 39, which would lead to bugs; if, for example, the
    hex at (7, 32) was occupied, and the player wanted to put a city or farm
    at hex (32, 7), they wouldn't be able to due to both hexes having the same
    checksum.

    By adding 7 to the values, the program ensures that it doesn't trip up on hexes
    with a coordinate of zero. If it didn't, then the coordinates (5, 0) would have
    a checksum of 5, and that would choke the `are_adjacent()` function.
    """
 
    SURF.fill((0, 0, 0)) # Clear the screen

    draw_grid(width, height)

    keys = pygame.key.get_pressed()  # Callback for ingame keypresses
    if mode == 0: # Default/gameplay mode
        pygame.display.set_caption('To place a city, press 1. To place a farm, press 2. To claim a territory, press 3.')

        blue_food -= (0.1 * blue_cities) # Each city consumes 0.1 food.

        blue_food += (0.03 * blue_farms) # Each farm produces 0.03 food.

        blue_money += (0.02 * blue_cities) # Each city produces 0.02 money.

        red_food -= (0.1 * red_cities) # Each city consumes 0.1 food.

        red_food += (0.03 * red_farms) # Each farm produces 0.03 food.

        red_money += (0.02 * red_cities) # Each city produces 0.02 money.

        if turn / 2 == turn // 2:
           if keys[K_1]:
                if blue_money >= 5.00:
                    blue_city_x_vals.append(0)
                    blue_city_y_vals.append(0)
                    blue_money -= 5 # Each city costs 5 money to build.
                    turn += 1
                    mode = 1
                else:
                    pass
           if keys[K_2]:
                if blue_money >= 1.00:
                    blue_farm_x_vals.append(0)
                    blue_farm_y_vals.append(0)
                    blue_money -= 1 # Each farm costs 1 money to build.
                    turn += 1
                    mode = 2
                else:
                    pass
           if keys[K_3]:
                if blue_money >= 1.00 and blue_food >= 0.50:
                    blue_x_vals.append(0)
                    blue_y_vals.append(0)
                    blue_money -= 1  # Each hex costs 1 money and
                    blue_food -= 0.5 # 0.5 food to conquer.
                    turn += 1
                    mode = 3
                else:
                    pass
        elif turn / 2 != turn // 2:
            if keys[K_1]:
                if red_money >= 5.00:
                    red_city_x_vals.append(56)
                    red_city_y_vals.append(30)
                    red_money -= 5 # Each city costs 5 money to build.
                    turn += 1
                    mode = 1
                else:
                    pass
            if keys[K_2]:
                if red_money >= 1.00:
                    red_farm_x_vals.append(56)
                    red_farm_y_vals.append(30)
                    red_money -= 1 # Each farm costs 1 money to build.
                    turn += 1
                    mode = 2
                else:
                    pass
            if keys[K_3]:
                if red_money >= 1.00 and red_food >= 0.50:
                    red_x_vals.append(56)
                    red_y_vals.append(30)
                    red_money -= 1  # Each hex costs 1 money and
                    red_food -= 0.5 # 0.5 food to conquer.
                    turn += 1
                    mode = 3
                else:
                    pass
 
    # ----------- #
    if mode == 1: # Mode for placing cities
        w = 2 * width
        h = 2 * height
        pygame.display.set_caption('Use the keys 7, Y, H, N, J, U to move. Press the spacebar to place your city.')
        if turn / 2 == turn // 2:
            highlight(blue_city_x_vals[blue_cities], blue_city_y_vals[blue_cities])
            if keys[K_y]:
                if blue_city_x_vals[blue_cities] / 2 != blue_city_x_vals[blue_cities] // 2:
                    blue_city_x_vals[blue_cities] -= 1
                    blue_city_y_vals[blue_cities] -= 1
                else:
                    blue_city_x_vals[blue_cities] -= 1
            if keys[K_u]:
                if blue_city_x_vals[blue_cities] / 2 != blue_city_x_vals[blue_cities] // 2:
                    blue_city_x_vals[blue_cities] += 1
                    blue_city_y_vals[blue_cities] -= 1
                else:
                    blue_city_x_vals[blue_cities] += 1
            if keys[K_h]:
                if blue_city_x_vals[blue_cities] / 2 != blue_city_x_vals[blue_cities] // 2:
                    blue_city_x_vals[blue_cities] -= 1
                else:
                    blue_city_x_vals[blue_cities] -= 1
                    blue_city_y_vals[blue_cities] += 1
            if keys[K_j]:
                if blue_city_x_vals[blue_cities] / 2 != blue_city_x_vals[blue_cities]  // 2:
                    blue_city_x_vals[blue_cities] += 1
                else:
                    blue_city_x_vals[blue_cities] += 1
                    blue_city_y_vals[blue_cities] += 1
            if keys[K_7]:
                blue_city_y_vals[blue_cities] -= 1
            if keys[K_n]:
                blue_city_y_vals[blue_cities] += 1
            else:
                pass

            if keys[K_SPACE]:
                temp_checksum = (blue_city_x_vals[blue_cities] + (1000 * (7 + (blue_city_y_vals[blue_cities]))))
                if temp_checksum not in blue_city_checksums:
                    if temp_checksum not in blue_farm_checksums:
                        if temp_checksum in blue_checksums:
                            if temp_checksum not in red_checksums:
                                blue_cities += 1
                                red_city_x_vals.append(56)
                                red_city_y_vals.append(30)
                                mode = 0


        if turn / 2 != turn // 2:
            highlight(red_city_x_vals[red_cities], red_city_y_vals[red_cities])
            if keys[K_y]:
                if red_city_x_vals[red_cities] / 2 != red_city_x_vals[red_cities] // 2:
                    red_city_x_vals[red_cities] -= 1
                    red_city_y_vals[red_cities] -= 1
                else:
                    red_city_x_vals[red_cities] -= 1
            if keys[K_u]:
                if red_city_x_vals[red_cities] / 2 != red_city_x_vals[red_cities] // 2:
                    red_city_x_vals[red_cities] += 1
                    red_city_y_vals[red_cities] -= 1
                else:
                    red_city_x_vals[red_cities] += 1
            if keys[K_h]:
                if red_city_x_vals[red_cities] / 2 != red_city_x_vals[red_cities] // 2:
                    red_city_x_vals[red_cities] -= 1
                else:
                    red_city_x_vals[red_cities] -= 1
                    red_city_y_vals[red_cities] += 1
            if keys[K_j]:
                if red_city_x_vals[red_cities] / 2 != red_city_x_vals[red_cities]  // 2:
                    red_city_x_vals[red_cities] += 1
                else:
                    red_city_x_vals[red_cities] += 1
                    red_city_y_vals[red_cities] += 1
            if keys[K_7]:
                red_city_y_vals[red_cities] -= 1
            if keys[K_n]:
                red_city_y_vals[red_cities] += 1
            else:
                pass

            if keys[K_SPACE]:
                temp_checksum = (red_city_x_vals[red_cities] + (1000 * (7 + (red_city_y_vals[cities]))))
                if temp_checksum not in red_city_checksums:
                    if temp_checksum not in red_farm_checksums:
                        if temp_checksum in red_checksums:
                            if temp_checksum not in blue_checksums:
                                red_cities += 1
                                mode = 0

   # ----------- #
    if mode == 2: # Mode for placing farms
        w = 2 * width
        h = 2 * height
        pygame.display.set_caption('Use the keys 7, Y, H, N, J, U to move. Press the spacebar to place your farm.')
        if turn / 2 == turn // 2:
            highlight(blue_farm_x_vals[blue_farms], blue_farm_y_vals[blue_farms])
            if keys[K_y]:
                if blue_farm_x_vals[blue_farms] / 2 != blue_farm_x_vals[blue_farms] // 2:
                    blue_farm_x_vals[blue_farms] -= 1
                    blue_farm_y_vals[blue_farms] -= 1
                else:
                    blue_farm_x_vals[blue_farms] -= 1
            if keys[K_u]:
                if blue_farm_x_vals[blue_farms] / 2 != blue_farm_x_vals[blue_farms] // 2:
                    blue_farm_x_vals[blue_farms] += 1
                    blue_farm_y_vals[blue_farms] -= 1
                else:
                    blue_farm_x_vals[blue_farms] += 1
            if keys[K_h]:
                if blue_farm_x_vals[blue_farms] / 2 != blue_farm_x_vals[blue_farms] // 2:
                    blue_farm_x_vals[blue_farms] -= 1
                else:
                    blue_farm_x_vals[blue_farms] -= 1
                    blue_farm_y_vals[blue_farms] += 1
            if keys[K_j]:
                if blue_farm_x_vals[blue_farms] / 2 != blue_farm_x_vals[blue_farms]  // 2:
                    blue_farm_x_vals[blue_farms] += 1
                else:
                    blue_farm_x_vals[blue_farms] += 1
                    blue_farm_y_vals[blue_farms] += 1
            if keys[K_7]:
                blue_farm_y_vals[blue_farms] -= 1
            if keys[K_n]:
                blue_farm_y_vals[blue_farms] += 1
            else:
                pass
    
            if keys[K_SPACE]:
                temp_checksum = (blue_farm_x_vals[blue_farms] + (1000 * (7 + (blue_farm_y_vals[blue_farms]))))
                if temp_checksum not in blue_farm_checksums:
                    if temp_checksum not in blue_city_checksums:
                        if temp_checksum in blue_checksums:
                            if temp_checksum not in red_checksums:
                                blue_farms += 1
                                red_farm_x_vals.append(56)
                                red_farm_y_vals.append(30)
                                mode = 0
        if turn / 2 != turn // 2:
            highlight(red_farm_x_vals[len(red_farm_x_vals)], red_farm_y_vals[len(red_farm_y_vals)])
            if keys[K_y]:
                if red_farm_x_vals[red_farms] / 2 != red_farm_x_vals[red_farms] // 2:
                    red_farm_x_vals[red_farms] -= 1
                    red_farm_y_vals[red_farms] -= 1
                else:
                    red_farm_x_vals[red_farms] -= 1
            if keys[K_u]:
                if red_farm_x_vals[red_farms] / 2 != red_farm_x_vals[red_farms] // 2:
                    red_farm_x_vals[red_farms] += 1
                    red_farm_y_vals[red_farms] -= 1
                else:
                    red_farm_x_vals[red_farms] += 1
            if keys[K_h]:
                if red_farm_x_vals[red_farms] / 2 != red_farm_x_vals[red_farms] // 2:
                    red_farm_x_vals[red_farms] -= 1
                else:
                    red_farm_x_vals[red_farms] -= 1
                    red_farm_y_vals[red_farms] += 1
            if keys[K_j]:
                if red_farm_x_vals[red_farms] / 2 != red_farm_x_vals[red_farms]  // 2:
                    red_farm_x_vals[red_farms] += 1
                else:
                    red_farm_x_vals[red_farms] += 1
                    red_farm_y_vals[red_farms] += 1
            if keys[K_7]:
                red_farm_y_vals[red_farms] -= 1
            if keys[K_n]:
                red_farm_y_vals[red_farms] += 1
            else:
                pass
    
            if keys[K_SPACE]:
                temp_checksum = (red_farm_x_vals[red_farms] + (1000 * (7 + (red_farm_y_vals[red_farms]))))
                if temp_checksum not in red_farm_checksums:
                    if temp_checksum not in red_city_checksums:
                        if temp_checksum in red_checksums:
                            if temp_checksum not in blue_checksums:
                                red_farms += 1
                                mode = 0
    # ----------- #
    if mode == 3: # Mode for conquering territory
        w = width
        h = height
        pygame.display.set_caption('Use the keys 7, Y, H, N, J, U to move. Press the spacebar to claim territory.')
        if turn / 2 == turn // 2:
            if blue_x_vals[blues] > -2 and blue_x_vals[blues] <= w and blue_y_vals[blues] > -2 and blue_y_vals[blues] <= h:
                highlight(blue_x_vals[blues], blue_y_vals[blues])
            if keys[K_y]:
                if blue_x_vals[blues] / 2 != blue_x_vals[blues] // 2:
                    blue_x_vals[blues] -= 1
                    blue_y_vals[blues] -= 1
                else:
                    blue_x_vals[blues] -= 1
            if keys[K_u]:
                if blue_x_vals[blues] / 2 != blue_x_vals[blues] // 2:
                    blue_x_vals[blues] += 1
                    blue_y_vals[blues] -= 1
                else:
                    blue_x_vals[blues] += 1
            if keys[K_h]:
                if blue_x_vals[blues] / 2 != blue_x_vals[blues] // 2:
                    blue_x_vals[blues] -= 1
                else:
                    blue_x_vals[blues] -= 1
                    blue_y_vals[blues] += 1
            if keys[K_j]:
                if blue_x_vals[blues] / 2 != blue_x_vals[blues]  // 2:
                    blue_x_vals[blues] += 1
                else:
                    blue_x_vals[blues] += 1
                    blue_y_vals[blues] += 1
            if keys[K_7]:
                blue_y_vals[blues] -= 1
            if keys[K_n]:
                blue_y_vals[blues] += 1
            else:
                pass
    
            if keys[K_SPACE]:
                temp_checksum = (blue_x_vals[blues] + (1000 * (7 + (blue_y_vals[blues]))))
                if temp_checksum not in blue_checksums:
                    if have_adjacents(temp_checksum, blue_checksums):
                        blues += 1
                        if temp_checksum in red_checksums:
                            if blue_money >= 60 and blue_food >= 60:
                                blue_money -= 60.0
                                blue_food -= 60.0
                        mode = 0
                    else:
                        pass
                else:
                    pass
        if turn / 2 != turn // 2:
            if red_x_vals[reds] > -2 and red_x_vals[reds] <= w and red_y_vals[reds] > -2 and red_y_vals[reds] <= h:
                highlight(red_x_vals[reds], red_y_vals[reds])
            if keys[K_y]:
                if red_x_vals[reds] / 2 != red_x_vals[reds] // 2:
                    red_x_vals[reds] -= 1
                    red_y_vals[reds] -= 1
                else:
                    red_x_vals[reds] -= 1
            if keys[K_u]:
                if red_x_vals[reds] / 2 != red_x_vals[reds] // 2:
                    red_x_vals[reds] += 1
                    red_y_vals[reds] -= 1
                else:
                    red_x_vals[reds] += 1
            if keys[K_h]:
                if red_x_vals[reds] / 2 != red_x_vals[reds] // 2:
                    red_x_vals[reds] -= 1
                else:
                    red_x_vals[reds] -= 1
                    red_y_vals[reds] += 1
            if keys[K_j]:
                if red_x_vals[reds] / 2 != red_x_vals[reds]  // 2:
                    red_x_vals[reds] += 1
                else:
                    red_x_vals[reds] += 1
                    red_y_vals[reds] += 1
            if keys[K_7]:
                red_y_vals[reds] -= 1
            if keys[K_n]:
                red_y_vals[reds] += 1
            else:
                pass
    
            if keys[K_SPACE]:
                temp_checksum = (red_x_vals[reds] + (1000 * (7 + (red_y_vals[reds]))))
                if temp_checksum not in red_checksums:
                    if have_adjacents(temp_checksum, red_checksums):
                        reds += 1
                        if temp_checksum in blue_checksums:
                            if red_food >= 60 and red_money >= 60:
                                red_food -= 60.0
                                red_money -= 60.0
                        mode = 0
                    else:
                        pass
                else:
                    pass
    # ----------- #

#    if keys[K_LEFT]: # This block describes the adjustment of the board dimensions. (Not an option in this version)
#        if height <= 0:
#            pass
#        else:
#            width -= 1
#    if keys[K_RIGHT]:
#        if width >= 40:
#            pass
#        else:
#            width += 1
#    if keys[K_UP]:
#        if height <= 0:
#            pass
#        else:
#            height -= 1
#    if keys[K_DOWN]:
#        if height >= 34:
#             pass
#        else:
#            height += 1

    # -------- #

    for n in range (0, blue_cities):
        cross(blue_city_x_vals[n], blue_city_y_vals[n])

    for n in range(1, red_cities):
        cross(red_city_x_vals[n], red_city_y_vals[n])
        
    for n in range (0, blue_farms):
        farm(blue_farm_x_vals[n], blue_farm_y_vals[n])

    for n in range (1, red_farms):
        farm(red_farm_x_vals[n], red_farm_y_vals[n])

    for n in range (0, blues):
        blue(blue_x_vals[n], blue_y_vals[n])
        
    for n in range (0, reds):
        red(red_x_vals[n], red_y_vals[n])


    blue_food_string  = myfont.render(str("{0:.2f}".format(blue_food)), 1, (0, 70, 255))
    blue_money_string = myfont.render("$ " + str("{0:.2f}".format(blue_money)), 1, (0, 70, 255))
    red_food_string   = myfont.render(str("{0:.2f}".format(red_food)), 1, (255, 10, 10))
    red_money_string  = myfont.render("$ " + str("{0:.2f}".format(red_money)), 1, (255, 10, 10))

    blue_food_announcement = myfont.render("Food: ", 1, (0, 70, 255))
    blue_money_announcement = myfont.render("Wealth: ", 1, (0, 70, 255))
    red_food_announcement = myfont.render("Food: ", 1, (255, 10, 10))
    red_money_announcement = myfont.render("Wealth: ", 1, (255, 10, 10))
    divider = myfont.render("~~~~~~~~~~~~", 1, (0, 255, 45))

    SURF.blit(blue_food_announcement, (750, 70))
    SURF.blit(blue_food_string, (750, 100))
    SURF.blit(divider, (750, 130))
    SURF.blit(blue_money_announcement, (750, 160))
    SURF.blit(blue_money_string, (750, 190))
    SURF.blit(divider, (750, 220))
    SURF.blit(red_food_announcement, (750, 250))
    SURF.blit(red_food_string, (750, 280))
    SURF.blit(divider, (750, 310))
    SURF.blit(red_money_announcement, (750, 340))
    SURF.blit(red_money_string, (750, 370))

    blue_checksums.clear() # Reset the checksums each frame since they're global lists and would get filled up otherwise
    blue_farm_checksums.clear()
    blue_city_checksums.clear()
    red_checksums.clear()
    red_farm_checksums.clear()
    red_city_checksums.clear()

    pygame.display.update()
    fpsClock.tick(5)
