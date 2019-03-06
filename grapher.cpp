// grapher.cpp - a program for making graphs out of equations.
// IMPORTANT NOTE! This program is still under construction.
#include <cairo.h>
#include <iostream>
#include <cmath>

using namespace std;

cairo_surface_t *surface =
    cairo_image_surface_create(CAIRO_FORMAT_ARGB32, 500, 500);
cairo_t *cr =
    cairo_create(surface);
    

int quadratic(long double a, long double x, long double b) {
    return (a * pow(x - 250, 2)) + 250 + b;
    /*                                               2
     * The reason why this doesn't look like f(x) = x is because
     * firstly, the graph must be transformed due to the Cairo
     * library placing the origin in the top-left corner rather
     * than the center.
     */ 
}

int linear(long double m, long double x, long double b) {
    return (m * (x - 250) + 250 + b);
}

int expo(long double a, long double x, long double b) { // TODO: fix this function
        return pow(a - 250, x) + 250 + b;
}


void draw_green_line(float x0, float y0, float x1, float y1){
    cairo_set_source_rgb(cr, 0.0, 5.0, 0.2);
    cairo_move_to(cr, x0, y0);
    cairo_line_to(cr, x1, y1);
    cairo_set_line_width(cr, 2);
    cairo_stroke(cr);
}

void draw_quadratic(long double a, long double b) {
        for (int x = 10; x < 490; x += 1) { // draws all points (x, f(x)) where said points are inside the graph
        int y = quadratic((-0.1 * a), x, (-10 * b)); // multiplication needed due to scale distortions
        int prev_x = x - 1;
        int prev_y = quadratic((-0.1 * a), prev_x, (-10 * b));
        if (prev_y >= 10 && y <= 490 && prev_y <= 490 && y >= 10) {
            draw_green_line(prev_x, prev_y, x, y);
        }
    }
}


void draw_linear(long double a, long double b) {
        for (int x = 10; x < 490; x += 1) { // draws all points (x, f(x)) where said points are inside the graph
        int y = linear((-0.1 * a), x, (-10 * b)); // multiplication needed due to scale distortions
        int prev_x = x - 1;
        int prev_y = linear((-0.1 * a), prev_x, (-10 * b));
        if (prev_y >= 10 && y <= 490 && prev_y <= 490 && y >= 10) {
            draw_green_line(prev_x, prev_y, x, y);
        }
    }
}


void draw_expo(long double a, long double b) { // TODO: fix this function
        for (int x = 10; x < 490; x += 1) { // draws all points (x, f(x)) where said points are inside the graph
        int y = expo((-0.1 * a), x, (-10 * b)); // multiplication needed due to scale distortions
        int prev_x = x - 1;
        int prev_y = expo((-0.1 * a), prev_x, (-10 * b));
        if (prev_y >= 10 && y <= 490 && prev_y <= 490 && y >= 10) {
            draw_green_line(prev_x, prev_y, x, y);
        }
    }
}


int main(int argc, char *argv[]) {
    cout << "To graph an equation, first select which type of equation you want from the list below by" << endl
         << "typing the number next to that option and pressing ENTER." << endl
         << endl
         << endl
         << "0. Linear equation               f(x) = mx + b" << endl
         << endl
         << "                                          2" << endl
         << "1. Quadratic equation            f(x) = ax  + b" << endl
         << endl
         << "                                         x" << endl
         << "2. Exponential equation          f(x) = a   + b" << endl
         << endl
         << "                                          4     3     2" << endl
         << "3. Equation of degree up to 4    f(x) = ax  + bx  + cx  + dx + e" << endl
         << endl
         << "Note: If you want to graph a cubic equation, simply use option 3 and set a to 0."
         << endl;
    /*
    string choice;
    getline(cin, choice);
    if (choice == "0") {
        cout << "Type in ";
    }
    if (choice == "1") {
        do another thing;
    }
    if (choice == "2") {
        do something else;
    }
    if (choice == "3") {
        do yet another thing;
    }
    else {
        cout << "Sorry, didn't understand you, bye" << endl;
        exit(EXIT_SUCCESS);
    }
    */
    // Set surface to opaque color (r, g, b)
    cairo_set_source_rgb(cr, 0.01, 0.01, 0.01);
    cairo_paint(cr);
    
    draw_green_line(10, 250, 490, 250); // Draw the axes
    draw_green_line(250, 10, 250, 490);
    draw_green_line(240, 20, 250, 10); // Draw the arrows on the axes
    draw_green_line(260, 20, 250, 10);
    draw_green_line(20, 240, 10, 250);
    draw_green_line(20, 260, 10, 250);
    draw_green_line(480, 240, 490, 250);
    draw_green_line(480, 260, 490, 250);
    draw_green_line(240, 480, 250, 490);
    draw_green_line(260, 480, 250, 490);
//                                           2
    draw_quadratic(1, -2); // Graphs f(x) = x  - 2. TODO: put in functionality allowing users to graph something else.


    draw_linear(0.5, 2); // Graphs f(x) = 0.5x + 2.

//                                         x
    draw_expo(1.2, 4); // Graphs f(x) = 1.2  + 4, except it doesn't work

    
    cairo_destroy(cr);
    cairo_surface_write_to_png(surface, "graph.png");
    cairo_surface_destroy(surface);

    return 0;
}