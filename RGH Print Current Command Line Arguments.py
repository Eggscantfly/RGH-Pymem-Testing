# This script will print the current command line arguments that the game is using!
import pymem

pm = pymem.Pymem('LyN_f.exe')

addr = pm.read_int(0x00a71c6c)

value = pm.read_string(addr)

print (value)