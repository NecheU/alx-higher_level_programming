#!/usr/bin/python3
for z in range(ord('a'), ord('z') + 1):
    if chr(z) not in ['q', 'e']:
        print("{}".format(chr(z)), end='')
