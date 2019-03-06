#include <cairo.h>
#include <iostream>
#include <vector>

using namespace std;

cairo_surface_t *surface =
    cairo_image_surface_create(CAIRO_FORMAT_ARGB32, 240, 300);
cairo_t *cr =
    cairo_create(surface); // Watch out, world. I just used pointers.

float shift(float point, float towards, float depth){ // for shifting points according to perspective
    return (point + (towards * depth)) / (depth + 1);
}

void draw_green_line(float x0, float y0, float x1, float y1){
    cairo_set_source_rgb(cr, 0.0, 5.0, 0.2);
    cairo_move_to(cr, x0, y0);
    cairo_line_to(cr, x1, y1);
    cairo_set_line_width(cr, 2);
    cairo_stroke(cr);
}

void draw_red_line(float x0, float y0, float x1, float y1){ // for the left lens
    cairo_set_source_rgb(cr, 6.0, 0.0, 0.0);
    cairo_move_to(cr, x0, y0);
    cairo_line_to(cr, x1, y1);
    cairo_set_line_width(cr, 2);
    cairo_stroke(cr);
}

void draw_cyan_line(float x0, float y0, float x1, float y1){ // for the right lens
    cairo_set_source_rgb(cr, 0.0, 0.4, 4.0);
    cairo_move_to(cr, x0, y0);
    cairo_line_to(cr, x1, y1);
    cairo_set_line_width(cr, 2);
    cairo_stroke(cr);
}

void draw_magenta_line(float x0, float y0, float x1, float y1){ // for where they overlap
    cairo_set_source_rgb(cr, 2.5, 0.25, 2.65); // average between red and cyan
    cairo_move_to(cr, x0, y0);
    cairo_line_to(cr, x1, y1);
    cairo_set_line_width(cr, 2);
    cairo_stroke(cr);
}

void draw_3d_line(float x0, float y0, float z0, float x1, float y1, float z1){
    float red_start; float red_end;
    float cyan_start;    float cyan_end;
    red_start = x0 + z0;
    cyan_start = x0 - z0;
    red_end = x1 + z1;
    cyan_end = x1 - z1; // Cyan goes on the left, red on the right
    draw_red_line(red_start, y0, red_end, y1);
    draw_cyan_line(cyan_start, y0, cyan_end, y1);
    if (y0 == y1){
        draw_magenta_line(red_start, y0, cyan_end, y0); // for when horizontal lines overlap perfectly
    }

    if ((x0 == x1) and (z0 == 0) and (z1 == 0)){
        draw_magenta_line(x0, y0, x0, y1); // for when vertical lines overlap perfectly
    }
}

class Cube{

    public:

    float start_vertex_x;
    float start_vertex_y;
    float start_vertex_z;
    float edge_length;
    float perspective_point_x;
    float perspective_point_y;

    void draw(){
        float front_right_x;
        float front_bottom_y;
        float back_start_x;
        float back_start_y;
        float back_shifted_x;
        float back_shifted_y;

        front_right_x = (start_vertex_x + edge_length);
        front_bottom_y = (start_vertex_y + edge_length);
        back_start_x = shift(start_vertex_x, perspective_point_x, 1.0);
        back_start_y = shift(start_vertex_y, perspective_point_y, 1.0);
        back_shifted_x = shift(front_right_x, perspective_point_x, 1.0);
        back_shifted_y = shift(front_bottom_y, perspective_point_y, 1.0);

        // this block draws the face closest to the viewer
        draw_3d_line(start_vertex_x, start_vertex_y, start_vertex_z, front_right_x,  start_vertex_y, start_vertex_z); // Top edge of square
        draw_3d_line(start_vertex_x, start_vertex_y, start_vertex_z, start_vertex_x, front_bottom_y, start_vertex_z); // Left edge of square
        draw_3d_line(front_right_x,  start_vertex_y, start_vertex_z, front_right_x,  front_bottom_y, start_vertex_z); // Right edge of square
        draw_3d_line(start_vertex_x, front_bottom_y, start_vertex_z, front_right_x,  front_bottom_y, start_vertex_z); // Bottom edge of square

        // this block draws the lines connecting the closest face to the farthest
        draw_3d_line(start_vertex_x, start_vertex_x, start_vertex_z, back_start_x,   back_start_y,   (start_vertex_z - 3)); // Top-left
        draw_3d_line(front_right_x,  start_vertex_x, start_vertex_z, back_shifted_x, back_start_y,   (start_vertex_z - 3)); // Top-right
        draw_3d_line(start_vertex_x, front_bottom_y, start_vertex_z, back_start_x,   back_shifted_y, (start_vertex_z - 3)); // Bottom-left
        draw_3d_line(front_right_x,  front_bottom_y, start_vertex_z, back_shifted_x, back_shifted_y, (start_vertex_z - 3)); // Bottom-right

        // this block draws the farther face
        draw_3d_line(back_start_x,   back_start_y,   (start_vertex_z - 3), back_shifted_x, back_start_y,   (start_vertex_z - 3));
        draw_3d_line(back_start_x,   back_start_y,   (start_vertex_z - 3), back_start_x,   back_shifted_y, (start_vertex_z - 3));
        draw_3d_line(back_shifted_x, back_start_y,   (start_vertex_z - 3), back_shifted_x, back_shifted_y, (start_vertex_z - 3));
        draw_3d_line(back_start_x,   back_shifted_y, (start_vertex_z - 3), back_shifted_x, back_shifted_y, (start_vertex_z - 3));
    }
}; // It is my opinion that, considering how the rest of C++ works, it is very weird that you need a semicolon here.

int main(int argc, char *argv[]){

    // Set surface to opaque color (r, g, b)
    cairo_set_source_rgb(cr, 0.01, 0.01, 0.01);
    cairo_paint(cr);

    // Put a caption on the image
    cairo_select_font_face(cr, "monospace", CAIRO_FONT_SLANT_NORMAL, CAIRO_FONT_WEIGHT_NORMAL);
    cairo_set_font_size(cr, 14.0);
    cairo_set_source_rgb(cr, 5.0, 5.0, 5.0); // (0.0, 5.0, 0.2) for the characteristic green colour
    cairo_move_to(cr, 3.0, 270.0);
    cairo_show_text(cr, "Coded in C++ by Dante Falzone");

    float focus_depth;
    float xpers;
    float ypers;

    cout << "\nWelcome to the Anaglyphic 3-Dimensional Cube Image Generator, coded"
         << endl
         << "in C++ by Dante Falzone."
         << endl;

    cout << "Type in the depth of focus for the anaglyph as a number between 0 and 8,"
         << endl
         << "where 0 means it looks farther away and 8 means it looks closer."
         << endl;

    cin >> focus_depth;

    cout << "Type in the x-coordinate for the point of perspective (a number between"
         << endl
         << "-100 and 100 is ideal)."
         << endl;
         
    cin >> xpers;
    
    cout << "Type in the y-coordinate for the point of perspective (a number between"
         << endl
         << "-100 and 100 is ideal)."
         << endl;
         
    cin >> ypers;
    
    Cube anaglyph; // Declare an instantiation of class Cube only after necessary data has been got
    anaglyph.start_vertex_x = 20;
    anaglyph.start_vertex_y = 20;
    anaglyph.start_vertex_z = focus_depth + 4;
    anaglyph.edge_length = 200;
    anaglyph.perspective_point_x = xpers + 120; // If (0, 0) is entered for the perspective point, it will point towards
    anaglyph.perspective_point_y = ypers + 120; // the exact center, which is (120, 120) since it's a 240x240 image.
    anaglyph.draw();

    cairo_destroy(cr);
    cairo_surface_write_to_png(surface, "cube.png");
    cairo_surface_destroy(surface);
    return 0;
}
