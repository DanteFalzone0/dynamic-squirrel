;------------------------------------------------------------------;
; Program written in x86-64 Assembly for Linux by Dante.           ;
; Assemble and run with the following command:                     ;
;     nasm -felf64 greeter.asm && gcc -static greeter.o && ./a.out ;
;------------------------------------------------------------------;

          global    main
          extern    puts

          section   .text
main:
; Say hello
          mov       rdi, message0  ; put text in rdi
          call      puts           ; print the contents of rdi

; Get from stdin
          mov       rdi, 0         ; prepare rdi to take stdin
          lea       rsi, [rsp+8]   ; set the buffer
          mov       rdx, 10        ; number of bytes to read
          mov       rax, 0         ; syscall to read from stdin
          syscall
          push      rsi            ; push the stdin buffer onto the stack

; Be polite
          xor       rdi, rdi       ; empty out the stdout register
          mov       rdi, message1  ; put our next message into stdout
          call      puts           ; print it
          xor       rdi, rdi       ; empty the stdout register yet again
          pop       rdi            ; we pushed our stdin buffer onto the stack, now we pop it into stdout
          call      puts           ; and print it out
          ret                      ; Finally we return from main

message0:
          db        "Hello, what's your name?", 0
message1:
          db        "It's very nice to meet you, ", 0
