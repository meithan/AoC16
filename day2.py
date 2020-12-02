import sys

instructions = []
with open(sys.argv[1]) as f:
  for line in f:
    instructions.append(line.strip())

numbers = [[1,2,3],[4,5,6],[7,8,9]]
x = 1
y = 1
code = ""
for seq in instructions:
  for ins in seq:
    if ins == "U": x = max(x-1, 0)
    elif ins == "D": x = min(x+1, 2)
    elif ins == "L": y = max(y-1, 0)
    elif ins == "R": y = min(y+1, 2)
#    print(numbers[x][y])
#  print(">",numbers[x][y])
  code += str(numbers[x][y])
print("=== Part One ===")
print("Code:", code)

numbers = [
["",  "",  "1", "",  ""],
["",  "2", "3", "4", ""],
["5", "6", "7", "8", "9"],
["",  "A", "B", "C", ""],
["",  "",  "D", "",  ""]]
x = 2
y = 0
code = ""
for seq in instructions:
  for ins in seq:
    if ins == "U":
      if x-1 >= 0 and numbers[x-1][y] != "": x -= 1
    elif ins == "D":
      if x+1 <= 4 and numbers[x+1][y] != "": x += 1
    elif ins == "L":
      if y-1 >= 0 and numbers[x][y-1] != "": y -= 1
    elif ins == "R":
      if y+1 <= 4 and numbers[x][y+1] != "": y += 1
  code += str(numbers[x][y])
print("=== Part Two ===")
print("Code:", code)
