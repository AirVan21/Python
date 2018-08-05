#! /usr/bin/env python3
acc = int(input())
power = [acc]
while acc != 0:
    next = int(input())
    acc += next
    power.append(next)
print(sum(map(lambda x: x ** 2, power)))