#include <stdio.h>

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

char x;
char y;
char z;
char q;

char secondchar()
{
    char placeholder;
    placeholder = y;
    return placeholder;
}


int main()
{
    printf("Type in one to three characters and press ENTER. \n");
    scanf("%c",&x);
    scanf("%c",&y);
    if (y == '\n')
    {
        printf("You typed %c \n", x);
    }
    else
    {
        scanf("%c",&z);
        if (z == '\n')
        {
            printf("You typed in %c", x);
            printf("%c \n", y);
            q = secondchar();
            printf("The second character was %c \n", q);
        }
        else
        {
            printf("You typed in %c", x);
            printf("%c", y);
            printf("%c \n", z);
            q = secondchar();
            printf("The second character was %c \n", q);
        }
    }
    return 0;
}   
