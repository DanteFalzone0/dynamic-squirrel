// Written on 6 June 2019 by Dante Falzone as an exercise in
// manual memory management in C

#include <stdio.h>
#include <stdlib.h>

int main() {

    // We malloc some heap space for the variable "foo"
    int *foo;
    foo = (int *)malloc(sizeof(int));

    // Error handling
    if (foo == 0) {
        printf("Error! Time to download some more RAM!\n");
        return 1;
    }

    *foo = 42; // meaning of life/universe/etc.
    printf("%d\n", *foo); // O great Computer, tell us!!!

    free(foo); // finally done with our heap memory, so give it back

    return 0;
}
