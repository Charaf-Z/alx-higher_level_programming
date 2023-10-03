#!/usr/bin/python3
def islower(c):
    return ord(c) >= 97 and ord(c) <= 122

def uppercase(str):
    for c in str:
        print(f"{ord(c) if not islower(c) else ord(c) - 32 :c}", end="")
    print("")