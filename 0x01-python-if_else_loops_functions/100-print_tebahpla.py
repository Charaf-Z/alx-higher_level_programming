#!/usr/bin/python3
alpha = 0
for c in range(122, 96, -1):
    print(f"{chr(c - alpha)}", end="")
    alpha = 32 if alpha == 0 else 0
