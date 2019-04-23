; Note: unfinished
;--------------------------------------------------------------;
; Program written in x86-64 Assembly for Linux by Dante.       ;
; Assemble and run with the following command:                 ;
;     nasm -felf64 greet.asm && gcc -static greet.o && ./a.out ;
;--------------------------------------------------------------;

        global  main
        extern  puts

        section .text
main:
; Title of the program
        xor     rdi, rdi
        mov     rdi, message0  ; put text in rdi
        call    puts           ; print the contents of rdi

; Prompt to get the resource name
        xor     rdi, rdi
        mov     rdi, message1
        call    puts

; Get the resource name from stdin and push it onto the stack
        mov     rdi, 0         ; prepare rdi to take stdin
        lea     rsi, [rsp+8]   ; set the buffer
        mov     rdx, 50        ; number of bytes to read (overestimate to be safe)
        mov     rax, 0         ; syscall to read from stdin
        syscall

        ;------------------------------------------------------------------;
        ; I will keep track of what is on the stack by writing a commented ;
        ; diagram of the stack next to each push/pop operation. This will  ;
        ; have syntax as follows:                                          ;
        ;                                                                  ;
        ;   ; abc|def|ghi>                                                 ;
        ; where "abc" is on top of the stack, "def" is in the middle, and  ;
        ; "ghi" is on the bottom.                                          ;
        ;------------------------------------------------------------------;

        push    rsi    ; resource_name>

; Prompt to get the units of measurement
        xor     rdi, rdi
        mov     rdi, message2
        call    puts

; Get units of measurement from stdin
        xor     rdi, rdi
        mov     rdi, 0
        lea     rsi, [rsp+8]
        mov     rdx, 50
        mov     rax, 0
        syscall
        push    rsi    ; units|resource_name>

; Prompt to get the current supply
        xor     rdi, rdi
        mov     rdi, message3
        call    puts

; TODO: learn either how to not put newlines with clib func or how to concatenate strings
; Get the current supply from stdin and push it onto the stack

        ret                      ; Finally we return from main

        section .data
message0:
        db      "Stalinator Economic Planning Tool v.4 - Coded in x86-64 Assembly by Dante Falzone", 0
message1:
        db      "Input the resource to be calculated and press ENTER.", 0
message2:
        db      "Input the units of measurement for that resource and press ENTER. (e.g. kg, L, etc.)", 0
message3:
        db      "Input the projected demand for that resource as a number and press ENTER.", 0
