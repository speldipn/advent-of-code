def getScore(a, b): 
  if a == "A": # rock
    if b == "X":  # rock
        return 3 + 1
    elif b == "Y": # paper
      return 6 + 2
    else:  # scissors
      return 0 + 3
  elif a == "B": # paper
    if b == "X":  # rock
        return 0 + 1
    elif b == "Y": # paper
      return 3 + 2
    else:  # scissors
      return 6 + 3
  else: # scissors
    if b == "X":  # rock
        return 6 + 1
    elif b == "Y": # paper
      return 0 + 2
    else:  # scissors
      return 3 + 3


f = open("input.txt", "r")
s = 0
while True: 
    a = f.readline()
    if a == '': break

    [x, y] = a.split(" ")
    score = getScore(x,y.strip())
    print(score)

    s += score

print("sum", s)
