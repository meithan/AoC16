import sys

with open(sys.argv[1]) as f:
  directions = list(map(str.strip, f.readline().strip().split(",")))

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
x = 0
y = 0
facing = NORTH
for direc in directions:
  turn = direc[0]
  steps = int(direc[1:])
  if turn == "R": facing = (facing + 1) % 4
  elif turn == "L": facing = (facing - 1) % 4
  if facing == NORTH: y += steps
  elif facing == SOUTH: y -= steps
  elif facing == EAST: x += steps
  elif facing == WEST: x -= steps
print("=== Part One ===")
print("Eastern Bunny HQ:", (x,y))
print("Manhattan distance to origin:", abs(x) + abs(y))

x = 0; y = 0
facing = NORTH
visited = set()
visited.add((x,y))
HQ2 = None
for direc in directions:
  turn = direc[0]
  steps = int(direc[1:])
  if turn == "R": facing = (facing + 1) % 4
  elif turn == "L": facing = (facing - 1) % 4
  if facing == NORTH: dx = 0; dy = +1
  elif facing == SOUTH: dx = 0; dy = -1
  elif facing == EAST: dx = +1; dy = 0
  elif facing == WEST: dx = -1; dy = 0
  print(direc)
  for i in range(steps):
    x += dx
    y += dy
    print((x,y))
    if (x,y) in visited:
      HQ2 = (x,y)
      break
    else: visited.add((x,y))
  if HQ2 != None: break
print("\b=== Part Two ===")
print("Eastern Bunny HQ:", HQ2)
print("Manhattan distance to origin:", abs(HQ2[0]) + abs(HQ2[1]))
