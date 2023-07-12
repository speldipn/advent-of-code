#!/bin/usr/python3
from functools import reduce

result = []

f = open("input.txt", "r")
a = 1
s = 0
_max = 0
while True: 
  line = f.readline();
  if line == '': 
      break
  elif line == '\n': 
    result.append(s)
    if s > _max:
      _max = s
    s = 0
  else:
    s += int(line)
    result.append(int(line))


# problem1
print("[prob1]", _max)

# problem2
a = sorted(set(result))
found = a[len(a)-3:len(a)]
print("[prob2]", found, reduce(lambda found, cur: found + cur, found, 0))
