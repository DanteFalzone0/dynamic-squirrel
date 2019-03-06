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
import sys
import os
import random
import re
import math
from pygame.locals import *

fpsClock = pygame.time.Clock()

p = 1 # Global for the line thickness. Yes, I know that globals are bad.


class Line:
    def __init__(self, x0, y0, z0, x1, y1, z1):
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1


def shift(point, towards, depth):
     return (point + (towards * depth)) / (depth + 1)



def draw(linea, perspective):
    shiftedx0 = shift(linea.x0, linea.z0, perspective)
    shiftedy0 = shift(linea.y0, linea.z0, perspective)
    shiftedx1 = shift(linea.x1, linea.z1, perspective)
    shiftedy1 = shift(linea.y1, linea.z1, perspective)
    pygame.draw.line(SURF, (0, 255, 35), (shiftedx0, shiftedy0), (shiftedx1, shiftedy1), p)


def vertrect(x, y, z, width, height, depth):  # Where x, y, and z are the coordinates of the top left vertex of a rectangle paralell to screen
    top = Line(x, y, z, (x + width), y, z)
    left = Line(x, y, z, x, (y + height), z)
    right = Line((x + width), y, z, (x + width), (y + height), z)
    bottom = Line(x, (y + height), z, (x + width), (y + height), z)
    draw(top, depth)
    draw(left, depth)
    draw(bottom, depth)
    draw(right, depth)


def equilateral_tetrahedron(x, z, height, perspective, angle): # Coordinates of top vertex
    b = math.sqrt(1 / 12) # Distance from the center of an equilateral triangle to the midpoint of any edge, given edge length of 1.
    c = (1 / math.sqrt(3)) # Distance from the center of an equilateral triangle to any vertex, given edge length of 1.



    def rotate(point_x, point_y, angle, val):
        rotated_point_x = (point_x * math.cos(angle)) - (point_y * math.sin(angle))
        rotated_point_y = (point_y * math.cos(angle)) + (point_x * math.sin(angle))
        if val == "x":
            return rotated_point_x
        if val == "y":
            return rotated_point_y

    edge0 = Line(rotate(x, z, angle, "x"), rotate(x, z, angle, "y"), z, rotate((x - ((1 / 2) * height)), (z + height), angle, "x"), rotate((x - ((1 / 2) * height)), (z + height), angle, "y"),  (z - (b * height))) # Edges from apex to base
    edge1 = Line(rotate(x, z, angle, "x"), rotate(x, z, angle, "y"), z, rotate((x + ((1 / 2) * height)), (z + height), angle, "x"), rotate((x + ((1 / 2) * height)), (z + height), angle, "y"), (z - (b * height)))
    edge2 = Line(rotate(x, z, angle, "x"), rotate(x, z, angle, "y"), z, rotate(x, (z + height), angle, "x"), rotate(x, (z + height), angle, "y"),  (z + (c * height)))
    draw(edge0, (perspective / 10))
    draw(edge1, (perspective / 10))
    draw(edge2, (perspective / 10))

    edge3 = Line(rotate((x - ((1 / 2) * height)), (z + height), angle, "x"), rotate((x - ((1 / 2) * height)), (z + height), angle, "y"), (z - (b * height)), rotate((x + ((1 / 2) * height)), (z + height), angle, "x"), rotate((x + ((1 / 2) * height)), (z + height), angle, "y"), (z - (b * height)))
    edge4 = Line(rotate((x - ((1 / 2) * height)), (z + height), angle, "x"), rotate((x - ((1 / 2) * height)), (z + height), angle, "y"), (z - (b * height)), rotate(x, (z + height), angle, "x"), rotate(x, (z + height), angle, "y"), (z + (c * height)))
    edge5 = Line(rotate((x + ((1 / 2) * height)), (z + height), angle, "x"), rotate((x + ((1 / 2) * height)), (z + height), angle, "y"),(z - (b * height)), rotate(x, (z + height), angle, "x"), rotate(x, (z + height), angle, "y"), (z + (c * height)))
    draw(edge3, (perspective / 10))
    draw(edge4, (perspective / 10))
    draw(edge5, (perspective / 10))


#def rectprism(x, y, z, width, height, frontdepth, backdepth):  # Where x, y, and z are the top left front vertex.
#    vertrect(x, y, z, width, height, (frontdepth / 10)) # Face closest to the viewer.
#    vertrect((x - backdepth), (y - backdepth), z, width, height, (backdepth / 10)) # Face farther back.
#    top_left_edge = Line(x, y, z, (x - backdepth), (y - backdepth), z)
#    top_right_edge = Line((x + width), y, z, (x + width), y, z)
#    bottom_left_edge = Line(x, (y + height), z, (x - backdepth), ((y + height) - backdepth), z)
#    bottom_right_edge = Line((x + width), (y + height), z, ((x + width) - backdepth), ((y + height) - backdepth), z)
#    draw(top_left_edge, (backdepth / 10))
#    draw(top_right_edge, (backdepth / 10))
#    draw(bottom_left_edge, (backdepth / 10))
#    draw(bottom_right_edge, (backdepth / 10))  # TODO: Either fix this, or delete it


SURF = pygame.display.set_mode((1000, 600))  # Set the surface

pygame.font.init()
myfont = pygame.font.SysFont("$HACKERMAN", 24)  # Initialize the font (dependency: $HACKERMAN font; available as FOSS on FontStruct)

x = 100
y = 100
z = 100
realh = 100
apparenth = 100
theta = 1
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.set_caption('Polyhedron World by Dante Falzone')

    SURF.fill((0, 0, 0)) # Clear the screen

    keys = pygame.key.get_pressed()  # Callback for ingame keypresses

    if realh <= 0:
        apparenth = 1
    else:
        apparenth = realh

    if keys[K_d]:
        x += 2
    if keys[K_a]:
        x -= 2
    if keys[K_w]:
        y -= 2
    if keys[K_s]:
        y += 2
    if keys[K_q]:
        z -= 10
        realh -= 1
    if keys[K_e]:
        z += 10
        realh += 1
    if keys[K_h]:
        if theta >= 4:
            pass
        else:
            x += 1
            y += 1
            realh += 1
            theta += 0.1
    if keys[K_t]:
        if theta <= -4:
            pass
        else:
            if theta == 0.1: # Avoid divide by zero errors
                x -= 1
                y -= 1
                realh -= 1.1
                theta -= 0.11
            else:
                x -= 1
                y -= 1
                realh -= 1
                theta -= 0.1
    if keys[K_LEFT]:
        angle += 0.1
    if keys[K_RIGHT]:
        angle -= 0.1

    equilateral_tetrahedron(x, z, apparenth, theta, angle)

    control_instructions_title = myfont.render("Instructions:", 1, (0, 255, 35))
    control_instruction_0 = myfont.render("[W - S] move up and down", 1, (0, 255, 35))
    control_instruction_1 = myfont.render("[A - D] move left and right", 1, (0, 255, 35))
    control_instruction_2 = myfont.render("[Q - E] move forwards and backwards", 1, (0, 255, 35))
    control_instruction_3 = myfont.render("[T - H] shift perspective", 1, (0, 255, 35))
    SURF.blit(control_instructions_title, (30, 430))
    SURF.blit(control_instruction_0, (30, 460))
    SURF.blit(control_instruction_1, (30, 490))
    SURF.blit(control_instruction_2, (30, 520))
    SURF.blit(control_instruction_3, (30, 550))



    pygame.display.update()
    fpsClock.tick(60)
