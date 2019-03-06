#include <stdio.h>
#include <stdlib.h>

/*
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
*/

int main (void) {

char quer[2];
    
printf("Orson Program 1 - coded in C by Dante Falzone.\n");
printf("This program is for determining whether Orson has the bone.\n");
printf("Question 0: Is Orson a dog? Type \"y\" for yes or \"n\" for no.\n");

fgets(quer,2,stdin);

if (quer[0] == 'y') {
    printf("\nBased on the data you entered, the program has deduced that Orson must have the bone.\n");
}

if (quer[0] == 'n') {
    printf("\nSince Orson is not a dog, he can't possibly have the bone.\n");
}

return 0;
    
}
