# -*- coding: utf-8 -*-
"""
Python question for interview
"""

a = 2
b = 0
while a or b:
    a -= 1
print(a)

k = 1
for i in range(1, 5):
    k *= i
print(k, 1 * 2 * 3 * 4)

x = 3
print(x >> 2)

# List

if __name__ == "__main__":
    a = list("element1")
    b = [1, 2, 3, 4]

    c = []
    c.append("element")
    print(c)

    for e in a:
        print(e)

    for e in b:
        print(e)
