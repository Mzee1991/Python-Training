#!/usr/bin/python3
for i in range(0, 101):
    if i == 100:
        print(f"{i}")
    else:
        print(f"{i:03}", end=", ")
