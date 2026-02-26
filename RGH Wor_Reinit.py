# Wor_Reinit this script will prompt the user to Reinit the World

import pymem

pm = pymem.Pymem('LyN_f.exe')

base = pm.base_address + 0x670BA0 # ViD_gpo_Engine

addr = pm.read_int(base)

final_Address = addr + 0x57d8

value = pm.read_int(final_Address)

user_input = input("Do you want to restart the World?: ")

if user_input.lower() == "yes":
    pm.write_int(final_Address, 1)
    print("Restarted")
