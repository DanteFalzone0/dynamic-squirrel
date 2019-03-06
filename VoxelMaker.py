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

# Tool for creating vector voxel graphics with the illusion of perspective.
import turtle
import sys


class Voxel:
    def __init__(self, x, y, z, vanishx, vanishy):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.vanishx = int(vanishx)
        self.vanishy = int(vanishy)


def draw(x, y, z, vanishx, vanishy):
    voxel = Voxel((x * 10), (y * 10), z, vanishx, vanishy)
    if turtle.isvisible():
        turtle.hideturtle()

    def shift(point, towards, depth):
        return point - (towards * depth)

    x0 = shift(voxel.x, vanishx, voxel.z)
    y0 = shift(voxel.y, vanishy, voxel.z)

    x1 = shift(voxel.x, vanishx, (voxel.z + 1))
    y1 = shift(voxel.y, vanishy, (voxel.z + 1))

    turtle.penup()
    turtle.goto(x0, y0)
    turtle.pencolor("#00FF47")
    turtle.pendown()
    turtle.goto((x0 + 10), y0)
    turtle.goto((x0 + 10), (y0 + 10))
    turtle.goto(x0, (y0 + 10))
    turtle.goto(x0, y0)
    turtle.goto(x1, y1)
    turtle.goto(x1, (y1 + 10))
    turtle.goto(x0, (y0 + 10))
    turtle.goto(x1, (y1 + 10))
    turtle.goto((x1 + 10), (y1 + 10))
    turtle.goto((x0 + 10), (y0 + 10))
    turtle.goto((x1 + 10), (y1 + 10))
    turtle.goto((x1 + 10), y1)
    turtle.goto((x0 + 10), y0)
    turtle.goto((x1 + 10), y1)
    turtle.goto(x1, y1)
    turtle.penup()


def main_program():
    turtle.bgcolor("black")
    k = turtle.numinput("Vanishing Point X-coordinate", "Input the x-coordinate for t"
                                                        "he vanishing point and press ENTER.", -5)
    b = turtle.numinput("Vanishing Point Y-coordinate", "Input the y-coordinate for t"
                                                        "he vanishing point and press ENTER.", 5)
    turtle.hideturtle()
    turtle.clearscreen()
    turtle.bgcolor("black")
    draw(-10, 0, 0, k, b)  # Starting point.
    draw(12, 5, 6, k, b)
    main_program()
    turtle.mainloop()


main_program()
