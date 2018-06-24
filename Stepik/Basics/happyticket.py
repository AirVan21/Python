#! /usr/bin/env python3
arg = [int(i) for i in input()]
print('Счастливый' if sum(arg[:3]) == sum(arg[3:]) else 'Обычный')