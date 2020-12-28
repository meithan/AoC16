# Day 13: A Maze of Twisty Little Cubicles

import queue
import sys

# ==============================================================================

def is_wall(seed, x, y):
  binstr = bin(x*x + 3*x + 2*x*y + y + y*y + seed)[2:]
  return binstr.count('1') % 2 == 1

def print_maze(seed, xmax, ymax, path=None):
  for y in range(ymax+1):
    s = ""
    for x in range(xmax+1):
      if path is not None and (x,y) in path:
        s += "O"
      elif is_wall(seed, x, y):
        s += "#"
      else:
        s += "."
    print(s)

class Node:
  def __init__(self, pos, depth, parent):
    self.pos = pos
    self.depth = depth
    self.parent = parent
  def get_children(self, seed):
    children = []
    x,y = self.pos
    for dx,dy in ((1,0), (0,1), (-1,0), (0,-1)):
      nx, ny = x+dx, y+dy
      if nx < 0 or ny < 0:
        continue
      if not is_wall(seed, nx, ny):
        child = Node((nx,ny), self.depth+1, self)
        children.append(child)
    return children
  def __repr__(self):
    return "<{},{}>".format(*self.pos)

def find_path(seed, start, goal, max_depth=None):
  seen = set([start])
  q = queue.Queue()
  q.put(Node(start, 0, None))
  while not q.empty():
    node = q.get()
    if max_depth is not None and node.depth == max_depth:
      return len(seen)
    if node.pos == goal:
      break
    for child in node.get_children(seed):
      if child.pos not in seen:
        q.put(child)
        seen.add(child.pos)
  path = [node]
  while node.parent is not None:
    node = node.parent
    path.append(node)
  path.reverse()
  return path

# -----------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

with open(sys.argv[1]) as f:
  seed = int(f.readline())

# -----------------------------------------
# Part 1

start = (1,1)
goal = (31,39)

path = find_path(seed, start, goal)

print("Part 1:", len(path)-1)

# ---------------------------------------
# Part 2

start = (1,1)
goal = (-1,-1)
num_nodes = find_path(seed, start, goal, max_depth=50)

print("Part 2:", num_nodes)
