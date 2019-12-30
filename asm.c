/* In this program I use inline Assembly to successfully
   do something specific without fucking everything up.
   I recommend that you compile with GCC, and bear in mind
   that this program will only work on x86-64. Compile
   with the option -S to see the Assembly. */


#include <stdio.h>

int main(void) {
    int foo = 3;
    int bar = 0;

    /* Now for the wizardry... We're going to use inline
       assembly to swap foo and bar. */
    asm (

        "# These next 4 lines are Assembly I wrote."
      "\t movl  %0,    %%ebx\n" // move foo into ebx
      "\t movl  %1,    %%eax\n" // move bar into eax
      "\t movl  %%eax, %0\n"    // move eax into foo
      "\t movl  %%ebx, %1\n"    // move ebx into bar
        :
        : "g" (foo), "g" (bar)
        : "ebx", "eax"
    );

    printf("foo was changed from 3 to %d.\n", foo);
    printf("bar was changed from 0 to %d.\n", bar);
    return 0;
}
