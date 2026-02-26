# This script prompts the user asking if they want to toggle the fps counter

import pymem

pm = pymem.Pymem('LyN_f.exe')


addr = pm.read_int(0x00A6E834) # fps counter address

final_Address = addr + 0x28

value = pm.read_int(final_Address)

user_input = input("Do you wish to toggle the fps counter?: ")

if user_input.lower() == "yes":
    pm.write_int(final_Address, 406401099)
    print ("Done!")