#!/bin/usr/python3

f = open("input.txt", "r")
a = 1
s = 0
_max = 0
while True: 
  line = f.readline();
  if line == '': 
      break
  elif line == '\n': 
    if s > _max:
      _max = s
    s = 0
  else:
    s += int(line)


print(_max)


