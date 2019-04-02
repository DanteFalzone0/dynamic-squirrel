#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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

int main(void) {
    char resource_name[64];
    char units[64];
    char demand[64];
    char supply[64];
    char cost[64];
    float demand0;
    float supply0;
    float cost0;
    float price;
    float sh;
    float abssh;

    printf("Stalinator Economic Planning Tool v.2 - Coded in C by Dante Falzone\n");

    printf("Input the resource to be calculated and press ENTER.\n");
    fgets(resource_name,64,stdin);
    if (resource_name[strlen(resource_name) - 1] == '\n') {
        resource_name[strlen(resource_name) - 1] = '\0';
    }

    printf("Input the units of measurement for that resource and press ENTER. (e.g. kg, L, etc.)\n");
    fgets(units,64,stdin);
    if (units[strlen(units) - 1] == '\n') {
        units[strlen(units) - 1] = '\0';
    }

    printf("Input the projected demand for that resource as a number and press ENTER.\n");
    printf("%s ",units);
    fgets(demand,64,stdin);
    if (demand[strlen(demand) - 1] == '\n') {
        demand[strlen(demand) - 1] = '\0';
    }
    demand0 = atof(demand); // Changes "demand" type from str to int, then stores in demand0.

    printf("Input the current supply for that resource as a number and press ENTER.\n");
    printf("%s ",units);
    fgets(supply,64,stdin);
    if (supply[strlen(supply) - 1] == '\n') {
        supply[strlen(supply) - 1] = '\0';
    }
    supply0 = atof(supply);

    printf("Input the estimated cost per unit to produce that resource and press ENTER.\n");
    printf("$ ");
    fgets(cost,64,stdin);
    if (cost[strlen(cost) - 1] == '\n') {
        cost[strlen(cost) - 1] = '\0';
    }
    cost0 = atof(cost);

    printf("Generating economic planning report...\n");

    price = ((cost0*demand0)/supply0);

    /* * * * * * * * * * * * * * * * *
     * This part is very similar to  *
     * its analog in the Python      *
     * version.                      *
     * * * * * * * * * * * * * * * * */

    sh = (supply0-demand0);

    if (sh < 0) {
        abssh = (sh - (2 * sh));
    }
    else {
        abssh = sh;
    }

    printf("Finished.\n");

    printf("----------------------------------------------------------------------------------------\n");
    printf("☭ Economic Planning Report ☭\n");
    printf("----------------------------------------------------------------------------------------\n");
    printf(">> Product: %s\n",resource_name);
    printf(">> Production volume: %s %s\n",supply,units);
    printf(">> Projected demand: %s %s\n",demand,units);
    printf(">> Ideal price: $ %f\n",price);
    printf(">> Resource scarcity status: ");

    if (sh > 0) {
        printf("surplus\n");
    }

    if (sh == 0) {
        printf("low supply, but no shortage\n");
    }

    if (sh < 0) {
        printf("shortage - recommend increasing supply by %f %s\n",abssh,units);
    }

    printf("----------------------------------------------------------------------------------------\n");

    return 0;
}

// I did it! Having successfully written `stalinator.c`,
// I now know that my knowledge of C is roughly on par
// with whatever my knowledge of Python was when I wrote
// `stalinator.py`. 2019-01-30

