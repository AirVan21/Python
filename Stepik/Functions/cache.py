#! /usr/bin/env python3
def f(x):
    return x ** 10
cache = {}
for i in range(int(input())):
    num = int(input())
    if num in cache:
        print(cache[num])
    else:
        cache[num] = f(num)
        print(cache[num])