
section .data
    msg db 'Hello, World!', 0

section .text
    global main
    extern puts

main:
    sub rsp, 28h
    mov rcx, msg
    call puts
    add rsp, 28h
    ret
