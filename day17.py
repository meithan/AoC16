# Day

import hashlib
import queue
import sys

# ==============================================================================

class State:

  dirs = ("U", "D", "L", "R")
  valids = ('b', 'c', 'd', 'e', 'f')
  deltas = {"U": (0,-1), "D": (0,1), "L": (-1,0), "R": (1,0)}

  def __init__(self, pos, path):
    self.pos = pos
    self.path = path

  def is_goal(self):
    return self.pos == (3,3)

  def get_children(self):
    h = hashlib.md5((passcode+self.path).encode("ascii")).hexdigest()[:4]
    children = []
    for i,dir in enumerate(State.dirs):
      new_x = self.pos[0] + self.deltas[dir][0]
      new_y = self.pos[1] + self.deltas[dir][1]
      if 0 <= new_x <= 3 and 0 <= new_y <= 3:
        if h[i] in self.valids:
          children.append(State((new_x, new_y), self.path + dir))
    return children

  def __repr__(self):
    return "<{}, {}>".format(self.pos, self.path)

# -----------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

with open(sys.argv[1]) as f:
  passcode = f.readline().strip()

# -----------------------------------------
# Part 1

start_state = State((0,0), "")
q = queue.Queue()
q.put(start_state)

while not q.empty():

  state = q.get()

  if state.is_goal():
    ans1 = state.path
    break

  for child in state.get_children():
    q.put(child)

print("Part 1:", ans1)

# ---------------------------------------
# Part 2

longest_len = 0
longest_path = None

start_state = State((0,0), "")
q = queue.Queue()
q.put(start_state)

while not q.empty():

  state = q.get()

  if state.is_goal():
    if len(state.path) > longest_len:
      longest_len = len(state.path)
      longest_path = state.path
    continue

  for child in state.get_children():
    q.put(child)

print("Part 2:", longest_len)
