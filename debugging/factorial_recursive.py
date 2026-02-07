#!/usr/bin/env python3
import sys

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

if len(sys.argv) != 2:
    print("Usage: ./factorial.py <number>")
    sys.exit(1)

num = int(sys.argv[1])

if num < 0:
    print("Factorial is not defined for negative numbers")
    sys.exit(1)

print(factorial(num))

