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
    turtle.tracer(0, 0)
    voxel = Voxel((x * 20), (y * 20), z, vanishx, vanishy)
    if turtle.isvisible():
        turtle.hideturtle()

    def shift(point, towards, depth):
        return point - (towards * depth)
    
    x0 = shift(voxel.x, vanishx, voxel.z + 1)
    y0 = shift(voxel.y, vanishy, voxel.z + 1)

    x1 = shift(voxel.x, vanishx, (voxel.z + 2))
    y1 = shift(voxel.y, vanishy, (voxel.z + 2))

    turtle.penup()
    turtle.goto(x0, y0)
    turtle.pencolor("#00FF47")
    turtle.pendown()
    turtle.goto((x0 + 20), y0)
    turtle.goto((x0 + 20), (y0 + 20))
    turtle.goto(x0, (y0 + 20))
    turtle.goto(x0, y0)
    turtle.goto(x1, y1)
    turtle.goto(x1, (y1 + 20))
    turtle.goto(x0, (y0 + 20))
    turtle.goto(x1, (y1 + 20))
    turtle.goto((x1 + 20), (y1 + 20))
    turtle.goto((x0 + 20), (y0 + 20))
    turtle.goto((x1 + 20), (y1 + 20))
    turtle.goto((x1 + 20), y1)
    turtle.goto((x0 + 20), y0)
    turtle.goto((x1 + 20), y1)
    turtle.goto(x1, y1)
    turtle.penup()
    turtle.update()


def main_program():
    turtle.bgcolor("black")
    k = turtle.numinput("Vanishing Point X-coordinate", "Input an x-coordinate between -20 and 20 for t"
                                                        "he vanishing point and press ENTER.", -6)
    b = turtle.numinput("Vanishing Point Y-coordinate", "Input a  y-coordinate between -20 and 20 for t"
                                                        "he vanishing point and press ENTER.", 3)
    turtle.hideturtle()
    turtle.clearscreen()
    turtle.bgcolor("black")
    turtle.tracer(0, 0)
    turtle.penup()
    c = (20 * k) - 80
    f = (20 * b) + 70
    turtle.goto(c, f)
    turtle.pendown()
    turtle.pencolor("#00FF47")
    turtle.goto(c, (f + 5))
    turtle.goto(c, f)
    turtle.goto((c + 5), f)
    turtle.goto(c, f)
    turtle.goto((c - 5), f)
    turtle.goto(c, f)
    turtle.goto(c, (f - 5))
    turtle.update()

    draw(-10, 0, 0, k, b)  # First layer of the left side of the house.
    draw(-10, 0, 1, k, b)
    draw(-10, 0, 2, k, b)  
    draw(-10, 0, 3, k, b)  
    draw(-10, 0, 4, k, b)
    draw(-10, 0, 5, k, b)  
    draw(-10, 0, 6, k, b)  
    draw(-10, 0, 7, k, b)  
    draw(-10, 0, 8, k, b)  

    draw(-9, 0, 8, k, b)  # First layer of the front and back of the house.
    draw(-9, 0, 0, k, b)   
    draw(-8, 0, 8, k, b)   
    draw(-8, 0, 0, k, b)   
    draw(-7, 0, 8, k, b)
    draw(-7, 0, 0, k, b)   
    draw(-6, 0, 8, k, b)   
    draw(-6, 0, 0, k, b)   
    draw(-5, 0, 0, k, b)   
    draw(-4, 0, 0, k, b)   
    draw(-3, 0, 8, k, b)   
    draw(-3, 0, 0, k, b)   
    draw(-2, 0, 8, k, b)   
    draw(-2, 0, 0, k, b)   
    draw(-1, 0, 8, k, b)   
    draw(-1, 0, 0, k, b)   

    draw(0, 0, 0, k, b)  # First layer of the right side of the house.
    draw(0, 0, 1, k, b)  
    draw(0, 0, 2, k, b)  
    draw(0, 0, 3, k, b)  
    draw(0, 0, 4, k, b)
    draw(0, 0, 5, k, b)  
    draw(0, 0, 6, k, b)  
    draw(0, 0, 7, k, b)  
    draw(0, 0, 8, k, b)  

    draw(-6, 1, 8, k, b)  # Doorway of the house.
    draw(-6, 2, 8, k, b)  
    draw(-6, 3, 8, k, b)  
    draw(-6, 4, 8, k, b)  
    draw(-5, 4, 8, k, b)
    draw(-4, 4, 8, k, b)  
    draw(-3, 4, 8, k, b)  
    draw(-3, 3, 8, k, b)  
    draw(-3, 2, 8, k, b)  
    draw(-3, 1, 8, k, b)  

    draw(-10, 1, 0, k, b)  # Back left corner of the house.
    draw(-10, 2, 0, k, b)   
    draw(-10, 3, 0, k, b)
    draw(-10, 4, 0, k, b)   
    draw(-10, 5, 0, k, b)   
    draw(-10, 6, 0, k, b)   

    draw(-10, 1, 8, k, b)  # Front left corner of the house.
    draw(-10, 2, 8, k, b)   
    draw(-10, 3, 8, k, b)
    draw(-10, 4, 8, k, b)   
    draw(-10, 5, 8, k, b)   
    draw(-10, 6, 8, k, b)   

    draw(0, 1, 0, k, b)  # Back right corner of the house.
    draw(0, 2, 0, k, b)   
    draw(0, 3, 0, k, b)
    draw(0, 4, 0, k, b)   
    draw(0, 5, 0, k, b)   
    draw(0, 6, 0, k, b)   

    draw(0, 1, 8, k, b)  # Front right corner of the house.
    draw(0, 2, 8, k, b)    
    draw(0, 3, 8, k, b)
    draw(0, 4, 8, k, b)    
    draw(0, 5, 8, k, b)    
    draw(0, 6, 8, k, b)    

    draw(-10, 6, 1, k, b)  # Top layer of the left side of the house.
    draw(-10, 6, 2, k, b)  
    draw(-10, 6, 3, k, b)  
    draw(-10, 6, 4, k, b)
    draw(-10, 6, 5, k, b)  
    draw(-10, 6, 6, k, b)  
    draw(-10, 6, 7, k, b)  
    
    draw(-9, 6, 8, k, b)  # Top layer of the front and back of the house.
    draw(-9, 6, 0, k, b)   
    draw(-8, 6, 8, k, b)   
    draw(-8, 6, 0, k, b)   
    draw(-7, 6, 8, k, b)    
    draw(-7, 6, 0, k, b)   
    draw(-6, 6, 8, k, b)   
    draw(-6, 6, 0, k, b)   
    draw(-5, 6, 8, k, b)   
    draw(-5, 6, 0, k, b)   
    draw(-4, 6, 8, k, b)   
    draw(-4, 6, 0, k, b)   
    draw(-3, 6, 8, k, b)   
    draw(-3, 6, 0, k, b)   
    draw(-2, 6, 8, k, b)   
    draw(-2, 6, 0, k, b)   
    draw(-1, 6, 8, k, b)   
    draw(-1, 6, 0, k, b)   

    draw(0, 6, 1, k, b)  # Top layer of the right side of the house.
    draw(0, 6, 2, k, b)
    draw(0, 6, 3, k, b)
    draw(0, 6, 4, k, b)
    draw(0, 6, 5, k, b)    
    draw(0, 6, 6, k, b)    
    draw(0, 6, 7, k, b)    

    draw(-11, 6, 0, k, b)  # Left gutter.
    draw(-11, 6, 1, k, b)  
    draw(-11, 6, 2, k, b)  
    draw(-11, 6, 3, k, b)  
    draw(-11, 6, 4, k, b)
    draw(-11, 6, 5, k, b)  
    draw(-11, 6, 6, k, b)  
    draw(-11, 6, 7, k, b)  
    draw(-11, 6, 8, k, b)  

    draw(1, 6, 0, k, b)  # Right gutter.
    draw(1, 6, 1, k, b)    
    draw(1, 6, 2, k, b)    
    draw(1, 6, 3, k, b)    
    draw(1, 6, 4, k, b)
    draw(1, 6, 5, k, b)    
    draw(1, 6, 6, k, b)    
    draw(1, 6, 7, k, b)    
    draw(1, 6, 8, k, b)    

    draw(-10, 7, 0, k, b)  # Back left part of roof.
    draw(-9, 8, 0, k, b)   
    draw(-8, 9, 0, k, b)
    draw(-7, 10, 0, k, b)  
    draw(-6, 11, 0, k, b)  
    draw(-5, 12, 0, k, b)  

    draw(-4, 11, 0, k, b)  # Back right part of roof.
    draw(-3, 10, 0, k, b)  
    draw(-2, 9, 0, k, b)
    draw(-1, 8, 0, k, b)   
    draw(0, 7, 0, k, b)    

    draw(-10, 7, 8, k, b)  # Front left part of roof.
    draw(-9, 8, 8, k, b)   
    draw(-8, 9, 8, k, b)
    draw(-7, 10, 8, k, b)  
    draw(-6, 11, 8, k, b)  
    draw(-5, 12, 8, k, b)  

    draw(-4, 11, 8, k, b)  # Front right part of roof.
    draw(-3, 10, 8, k, b)  
    draw(-2, 9, 8, k, b)
    draw(-1, 8, 8, k, b)   
    draw(0, 7, 8, k, b)    

    draw(-5, 12, 1, k, b)  # Ridge beam.
    draw(-5, 12, 2, k, b)
    draw(-5, 12, 3, k, b)
    draw(-5, 12, 4, k, b)
    draw(-5, 12, 5, k, b)
    draw(-5, 12, 6, k, b)
    draw(-5, 12, 7, k, b)
    
    main_program()
    turtle.mainloop()


main_program()
