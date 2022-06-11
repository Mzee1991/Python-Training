#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
if number >= 0:
    last_digit = number % 10
else:
    last_digit = ((number * -1) % 10) * -1

message = f"The last digit of {number} is {last_digit} and is"

if last_digit > 5:
    print(message, "More than 5")
elif last_digit == 0:
    print(message, "0")
else:
    print(message, "less than 6 and not 0")
