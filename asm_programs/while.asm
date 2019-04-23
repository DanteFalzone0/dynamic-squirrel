;---------------------------------------------------;
; Implementation of a loop in x86-64 Assembly for   ;
; Linux. Assemble and link as follows:              ;
;   nasm -felf64 while.asm && gcc -static while.o   ;
;---------------------------------------------------;
        global  main
        extern  puts

        section .text
main:
        xor  rcx, rcx   ; first we ensure that our loop counter is empty
        mov  rcx, 4     ; then we move 4 into it bc we want to loop 4 times
        jmp  while      ; and move on to "while"
while:
        push rcx        ; we push rcx onto the stack because "puts" could hurt it
        mov  rdi, msg   ; then we move our message into the stdout register
        call puts       ; we print the contents of stdout
        pop  rcx        ; and we pop our loop counter from the stack
        dec  rcx        ; decrement it
        jnz  while      ; and goto "while" if it's not equal to zero yet
exit:
        ret             ; we reach this point only when our loop counter reaches zero

        section .data
msg:
        db   "foo", 0   ; this is the message we'll print
