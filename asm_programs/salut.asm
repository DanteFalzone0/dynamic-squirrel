;-----------------------------------------------------------------;
; Program written in x86-64 Assembly for Linux by Dante Falzone.  ;
; Assemble and run with the following command:                    ;
;     nasm -felf64 salut.asm && gcc -static salut.o && ./a.out    ;
;-----------------------------------------------------------------;

          global    main
          extern    puts

          section   .text
main:                                       ; Have to have this when using C library functions
          mov       rdi, message0           ; rdi is where text to write goes
          call      puts                    ; prints the contents of rdi in the shell
          mov       rdi, message1           ; now we put something new into rdi
          call      puts                    ; call puts again
          mov       rdi, message2           ; this "rdi" memory register sure is neat
          call      puts                    ; and so are clib funcs
          ret                               ; Finally we return from main

message0:
          db        "Salut, monde", 0       ; null-terminated string ends with 0

message1:
          db        "Comment ca va?", 0

message2:
          db        "Je fais bien", 0

; this indentation style seems wasteful to me but I'm not one to
; contradict the Grand Masters
