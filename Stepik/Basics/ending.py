#! /usr/bin/env python3
body = 'программист'
number = int(input())
if 10 < (number % 100) < 20:
    print(number, body + 'ов')
elif number % 10 == 1:
    print(number, body)
elif (number % 10) in set([2, 3, 4]):
    print(number, body + 'а')
else:
    print(number, body + 'ов')