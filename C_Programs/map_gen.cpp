/*
map_gen.cpp - a program for creating randomly generated maps.
Copyright (C) 2019, Dante Falzone.
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
 
************************************************************************

It is recommended that you compile this program in the following manner:
    g++ map_gen.cpp -o mapmaker $(pkg-config --libs --cflags cairo)
and then run it with the following command:
    ./mapmaker

For that, you'll need to have used the following commands:
    sudo apt install libcairo2-dev
    sudo apt install pkg-config
...or whatever is appropriate for you if your distro doesn't use apt.

I will NOT port this to Microsloth Losedoze.
 */

#include <cairo.h>
#include <stdio.h>
#include <random>

using namespace std;

cairo_surface_t *surface = cairo_image_surface_create(CAIRO_FORMAT_ARGB32, 500, 500);
cairo_t *cr = cairo_create(surface);

void draw_green_line(float x0, float y0, float x1, float y1) {
    cairo_set_source_rgb(cr, 0.0, 5.0, 0.2);
    cairo_move_to(cr, x0, y0);
    cairo_line_to(cr, x1, y1);
    cairo_set_line_width(cr, 1);
    cairo_stroke(cr);
}


// Help determine where the line should start.
int set_pos() {
    random_device rd;
    uniform_int_distribution<int> dist(0, 500);
    return dist(rd);
}


// Pick a new value by which to move when drawing line.
int change() {
    random_device rd;
    uniform_int_distribution<int> dist(-3, 4);
    return dist(rd);
}


// Choose which side to start drawing from.
int which_side() {
    random_device rd;
    uniform_int_distribution<int> dist(0, 3); // 0 for top, 1 for left, 2 for bottom, 3 for right
    return dist(rd);
}


int main(void) {
    cairo_set_source_rgb(cr, 0.01, 0.01, 0.01);
    cairo_paint(cr);

    // Draw a border around the map.
    draw_green_line(0, 0, 500, 0);
    draw_green_line(500, 0, 500, 500);
    draw_green_line(500, 500, 0, 500);
    draw_green_line(0, 500, 0, 0);
    
    int side = which_side();
    
    if (side == 0) {
        int xpos = set_pos();
        int ypos = 0;
        
        while (ypos < 500) {
            int new_xpos = xpos + change();
            int new_ypos = ypos + change();
            draw_green_line(xpos, ypos, new_xpos, new_ypos);
            xpos = new_xpos;
            ypos = new_ypos;
        }
    } else if (side == 1) {
        int xpos = 0;
        int ypos = set_pos();
        
        while (xpos < 500) {
            int new_xpos = xpos + change();
            int new_ypos = ypos + change();
            draw_green_line(xpos, ypos, new_xpos, new_ypos);
            xpos = new_xpos;
            ypos = new_ypos;
        }        
    } else if (side == 2) {
        int xpos = set_pos();
        int ypos = 500;
        
        while (ypos > 0) {
            int new_xpos = xpos + change();
            int new_ypos = ypos - change();
            draw_green_line(xpos, ypos, new_xpos, new_ypos);
            xpos = new_xpos;
            ypos = new_ypos;
        }        
    } else if (side == 3) {
        int xpos = 500;
        int ypos = set_pos();
        
        while (xpos > 0) {
            int new_xpos = xpos - change();
            int new_ypos = ypos + change();
            draw_green_line(xpos, ypos, new_xpos, new_ypos);
            xpos = new_xpos;
            ypos = new_ypos;
        }        
    }

    cairo_destroy(cr);
    cairo_surface_write_to_png(surface, "map.png");
    printf("Your randomly generated map has been saved as `map.png`.\n");
    cairo_surface_destroy(surface);
    return 0;
}
