#! /usr/bin/env python3
args = [int(input()) for _ in range(3)]
print(max(args), '\n', min(args), '\n', sum(args) - max(args) - min(args))