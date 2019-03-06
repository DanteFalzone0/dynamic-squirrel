#include <stdio.h>  // This program in C was written by Dante Falzone, mostly on 2019-01-29.
#include <string.h> // That day, it was extremely cold in the American midwest.
#include <math.h>

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
    
    /* * * * * * * * * * * * * * * * * * * *
     * Using Pycharm as my IDE for Python  *
     * has trained me to want to wrap any  *
     * lines that are so long they go off  *
     * the screen. Hence, many of my       *
     * printf() functions look weirdly     *
     * broken up. Also, I really like the  *
     * way C does block comments :D        *
     * * * * * * * * * * * * * * * * * * * */
    char input[32];
    printf("\nThis is Dante's basic cypher encoder, written in C. It's very");
    printf(" trivial to crack, so definitely don't use it for anything that needs to be cryptog");
    printf("raphically secure. Seriously, this was only written to be an exercise in C.\n");
    printf("----------------\n");
    printf("Type in some phrase that's equal to or less than 32 characters.");
    printf(" Then press ENTER.\n");
    printf("String input (32 characters max please): ");
    fgets(input,32,stdin);
    printf("The string you entered was %s",input);
    printf("\nHere is the level-0 encryption (extremely insecure):\n");
    int u=input[0]; // For the 32-char string, program uses last six min chars of alphabet
    int v=input[1]; // plus 26 maj chars for a total of 32 char vars.
    int w=input[2];
    int x=input[3];
    int y=input[4];
    int z=input[5];
    int A=input[6];
    int B=input[7];
    int C=input[8];
    int D=input[9];
    int E=input[10];
    int F=input[11];
    int G=input[12];
    int H=input[13];
    int I=input[14];  // Did you ever hear the wondrous legend
    int J=input[15];  // of Guido van Rossum the wise?
    int K=input[16];  // Our beloved Benevolent Dictator for Life
    int L=input[17];  // did look upon the C-based languages
    int M=input[18];  // And He saw that they sucked.
    int N=input[19];  //
    int O=input[20];  // And so van Rossum
    int P=input[21];  // did create a new language,
    int Q=input[22];  // with dynamicity of typing and orientation towards objects,
    int R=input[23];  // and He atheistened it Python,
    int S=input[24];  // And there was much rejoicing.
    int T=input[25];
    int U=input[26];
    int V=input[27];
    int W=input[28];
    int X=input[29];
    int Y=input[30];
    int Z=input[31];
    long au = (u * 10000000000);
    long av = (v * 10000000);
    long aw = (w * 10000);
    long ax = (x * 10);
    long firstfour = ((au + av + aw + ax) / 10); // Takes the ascii values of the first three chars and
    printf("%.12ld\n",firstfour);                // turns them into a single long integer. This is
                                                 // necessary so that the 4-char numerals can be sqrted.
    /* * * * * * * * * * * * *
     * Can I just remark on  *
     * how profoundly stupid *
     * it is that C, unlike  *
     * Python, puts limits   *
     * on how big your       *
     * numbers can be?       *
     * ~ Dante Falzone       *
     * * * * * * * * * * * * */

    long ay = (y * 10000000000);
    long az = (z * 10000000);
    long aA = (A * 10000);
    long aB = (B * 10);
    long secondfour = ((ay + az + aA + aB) / 10);
    printf("%.12ld\n",secondfour);

    long aC = (C * 10000000000);
    long aD = (D * 10000000);
    long aE = (E * 10000);
    long aF = (F * 10);
    long thirdfour = ((aC + aD + aE + aF) / 10);
    printf("%.12ld\n",thirdfour);

    long aG = (G * 10000000000);
    long aH = (H * 10000000);
    long aI = (I * 10000);
    long aJ = (J * 10);
    long fourthfour = ((aG + aH + aI + aJ) / 10);
    printf("%.12ld\n",fourthfour);

    long aK = (K * 10000000000);
    long aL = (L * 10000000);
    long aM = (M * 10000);
    long aN = (N * 10);
    long fifthfour = ((aK + aL + aM + aN) / 10);
    printf("%.12ld\n",fifthfour);

    long aO = (O * 10000000000);
    long aP = (P * 10000000);
    long aQ = (Q * 10000);
    long aR = (R * 10);
    long sixthfour = ((aO + aP + aQ + aR) / 10);
    printf("%.12ld\n",sixthfour);

    long aS = (S * 10000000000);
    long aT = (T * 10000000);
    long aU = (U * 10000);
    long aV = (V * 10);
    long seventhfour = ((aS + aT + aU + aV) / 10);
    printf("%.12ld\n",seventhfour);

    long aW = (W * 10000000000);
    long aX = (X * 10000000);
    long aY = (Y * 10000);
    long aZ = (Z * 10);
    long eighthfour = ((aW + aX + aY + aZ) / 10);
    printf("%.12ld\n",eighthfour);

    printf("\nYou can decode this simply by putting it directly into a converter");
    printf(" for turning ascii numbers into plaintext.\n");

    printf("Here is your level-1 encryption (still not very secure, but slightly ");
    printf("harder to crack):\n");
    
    double foo;   // 0th
    double bar;   // 1st
    double baz;   // 2nd
    double qux;   // 3rd
    double frob;  // 4th
    double xyzzy; // 5th
    double fum;   // 6th
    double fred;  // 7th

    /* * * * * * * * * * * * * * * *
     * Yes, these are not the best *
     * possible variable names.    *
     * What will you do, give me a *
     * slap on the wrist? I was    *
     * reading the Jargon File and *
     * I wanted to feel extra      *
     * geekish. I recognize the    *
     * cheesiness of this.         *
     * * * * * * * * * * * * * * * */

    foo = sqrt(firstfour);
    bar = sqrt(secondfour);
    baz = sqrt(thirdfour);
    qux = sqrt(fourthfour);
    frob = sqrt(fifthfour);
    xyzzy = sqrt(sixthfour);
    fum = sqrt(seventhfour);
    fred = sqrt(eighthfour);

    printf("%f\n",foo);
    printf("%f\n",bar);
    printf("%f\n",baz);
    printf("%f\n",qux);
    printf("%f\n",frob);
    printf("%f\n",xyzzy);
    printf("%f\n",fum);
    printf("%f\n",fred);

    printf("\nTo decode this, find the squares");
    printf(" of each value. This will return sequences of ascii numbers.\n");
    printf("Should one of these values have a square that is less than twelve ");
    printf("digits long, simply put enough zeroes at the beginning to bring its");
    printf(" length up to twelve digits.\n");
    return 0;
}
