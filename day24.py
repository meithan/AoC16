# Day 24: Air Duct Spelunking

import itertools
from math import inf
import queue
import sys

# ==============================================================================

class SearchNode:

  deltas = [(1,0), (0,1), (-1,0), (0,-1)]

  def __init__(self, pos, depth):
    self.pos = pos
    self.depth = depth

  def children(self):
    children = []
    for dx, dy in SearchNode.deltas:
      x1 = self.pos[0] + dx
      y1 = self.pos[1] + dy
      if 0 <= x1 < nx and 0 <= y1 < ny:
        if maze[y1][x1] == ".":
          children.append(SearchNode((x1,y1), self.depth+1))
    return children

def find_distances(start_number):

  start_pos = numbers_pos[start_number]
  start = SearchNode(start_pos, 0)

  openset = queue.Queue()
  seen = set()
  openset.put(start)
  seen.add(start.pos)

  distances = [None]*len(numbers)
  found = 0
  while not openset.empty():

    node = openset.get()

    if node.pos in pos_numbers:
      distances[pos_numbers[node.pos]] = node.depth
      found += 1

    if found == len(numbers):
      break

    for child in node.children():
      if child.pos not in seen:
        openset.put(child)
        seen.add(child.pos)

  return distances

def path_distance(path):
  current = 0
  dist = 0
  for n in path:
    dist += distances[current][n]
    current = n
  return dist

# -----------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

numbers_pos = {}
maze = []
with open(sys.argv[1]) as f:
  y = 0
  for line in f:
    line = line.strip()
    row = []
    for x in range(len(line)):
      if line[x].isnumeric():
        numbers_pos[int(line[x])] = (x,y)
        row.append(".")
      else:
        row.append(line[x])
    maze.append(row)
    y += 1

numbers = sorted(list(numbers_pos.keys()))
pos_numbers = {numbers_pos[n]:n for n in numbers_pos}
nx = len(maze[0])
ny = len(maze)

# -----------------------------------------
# Part 1

# Determine distance between all pairs of numbers
distances = []
for n in numbers:
  distances.append(find_distances(n))

best_dist = inf
for path in itertools.permutations(numbers[1:]):
  dist = path_distance(path)
  if dist < best_dist:
    best_dist = dist
    best_path = path

print("Part 1:", best_dist)

# ---------------------------------------
# Part 2

best_dist = inf
for path in itertools.permutations(numbers[1:]):
  dist = path_distance(path+(0,))
  if dist < best_dist:
    best_dist = dist
    best_path = path

print("Part 2:", best_dist)
