# This script restores the health value to the default 3 if it's less than 3

import pymem

pm = pymem.Pymem('LyN_f.exe')

base = pm.base_address + 0x00671890

addr = pm.read_int(base)

num_Offsets = [0x2C, 0x1C, 0xD0, 0x2A3C]


for offset in num_Offsets[:-1]:
    addr = pm.read_int(addr + offset)

final_Address = addr + 0x2A3C

value = pm.read_int(final_Address)

#unused unless if I want to print out the current health before triggering the while loop :p
#print (value)

while True: 
    value = pm.read_int(final_Address)  
    if value < 3:
        pm.write_int(final_Address, 3)
        print ("Restored")
