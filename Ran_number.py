#!/usr/bin/python3
import random
number = random.randint(-5, 20)
if number > 0:
    print(f"{number} is Positive")
if number == 0:
    print(f"{number} is Zero")
if number < 0:
    print(f"{number} is Negative")
