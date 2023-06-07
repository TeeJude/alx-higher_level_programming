#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    n = 0
    print("{}".format(chr(c-n)), end="")
    n = 32 if n == 0 else 0
