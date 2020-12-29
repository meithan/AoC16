# Day 22: Grid Computing

import re
import sys

# ==============================================================================

class Node:

  def __init__(self, pos, size, used, avail):
    self.pos = pos
    self.size = size
    self.used = used
    self.avail = avail

  def __repr__(self):
    return "<Node {}, {}, {}, {}>".format(self.pos, self.size, self.used, self.avail)

  def __eq__(self, other):
    return self.pos == other.pos

# -----------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

pos0 = None
xmax = ymax = 0
nodes_dict = {}
with open(sys.argv[1]) as f:
  for i in range(2):
    f.readline()
  for line in f:
    m = re.match("/dev/grid/node-x([0-9]+)-y([0-9]+) +([0-9]+)T  +([0-9]+)T  +([0-9]+)T  +([0-9]+)%", line)
    x = int(m.group(1))
    y = int(m.group(2))
    if x > xmax: xmax = x
    if y > ymax: ymax = y
    pos = (x,y)
    size = int(m.group(3))
    used = int(m.group(4))
    avail = int(m.group(5))
    nodes_dict[pos] = Node(pos, size, used, avail)
    if used == 0:
      pos0 = pos

numx = xmax+1
numy = ymax+1
nodes = [[None]*numy for _ in range(numx)]
for x in range(numx):
  for y in range(numy):
    if (x,y) in nodes_dict:
      nodes[x][y] = nodes_dict[(x,y)]

# -----------------------------------------
# Part 1

viable_pairs = []
for x1 in range(numx):
  for y1 in range(numy):
    for x2 in range(numx):
      for y2 in range(numy):
        if x1 == x2 and y1 == y2: continue
        nodeA = nodes[x1][y1]
        nodeB = nodes[x2][y2]
        if nodeA.used > 0 and nodeA.used <= nodeB.avail:
          viable_pairs.append((nodeA, nodeB))

print("Part 1:", len(viable_pairs))

# ---------------------------------------
# Part 2

class Cluster:

  deltas = {"U": (0,-1), "D": (0,1), "L": (-1,0), "R": (1,0)}

  def __init__(self, grid, pos0):
    self.grid = grid
    self.pos = pos0
    self.moves = 0

  def __repr__(self):
    s = " "*3 + " ".join("{}".format(x).ljust(7) for x in range(numx)) + "\n"
    for y in range(numy):
      row = []
      for x in range(numx):
        node = self.grid[x][y]
        row.append("{:3}/{:<3}".format(node.used,node.size))
      s += "{:2}".format(y) + " ".join(row)
      if y < numy-1:
        s += "\n"
    return s

  def execute(self, sequence):
    for dir in sequence:
      nx, ny = self.neighbor(self.pos, dir)
      source = self.grid[nx][ny]
      dest = self.grid[self.pos[0]][self.pos[1]]
      if dest.avail >= source.used:
        dest.used += source.used
        dest.avail -= source.used
        source.avail += source.used
        source.used = 0
        self.pos = (nx,ny)
        self.moves += 1
      else:
        raise(Exception("Can't move data from {} to {}".format(source, dest)))

  def neighbor(self, pos, dir):
    dx,dy = self.deltas[dir]
    nx = pos[0]+dx
    ny = pos[1]+dy
    if 0 <= nx < numx and 0 <= ny < numy:
      return (nx, ny)
    else:
      raise(Exception("Invalid direction {} at position {}".format(dir, pos)))

# ---------------------------------------

cluster = Cluster(nodes, pos0)

# Sequence determined by visual inspection
cluster.execute("U"*7 + "L"*4 + "U"*15 + "R"*21 + "RDLLU"*28 + "R")
# print(cluster)

print("Part 2:", cluster.moves)
