# Welcome to my RGH python testing I am learning how to use Pymem!
# In this example I am printing out the Players X, Y and Z cordinates to the console

import pymem

pm = pymem.Pymem('LyN_f.exe')

# Pointer offsets

x_offsets = [0x0, 0x80]
y_offsets = [0x0, 0x88]
z_offsets = [0x0, 0x84]

while True:
    addr = pm.read_int(0x00a71890)
    for offset in x_offsets[:-1]:
        addr = pm.read_int(addr + offset)
    final_x_address = addr + x_offsets[-1]
    x_value = pm.read_float(final_x_address)

    addr = pm.read_int(0x00a71890)
    for offset in y_offsets[:-1]:
        addr = pm.read_int(addr + offset)
    final_y_address = addr + y_offsets[-1]
    y_value = pm.read_float(final_y_address)

    addr = pm.read_int(0x00a71890)
    for offset in z_offsets[:-1]:
        addr = pm.read_int(addr + offset)
    final_z_address = addr + z_offsets[-1]
    z_value = pm.read_float(final_z_address)

    print(x_value, y_value, z_value)