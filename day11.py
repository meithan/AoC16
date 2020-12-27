# Day 11: Radioisotope Thermoelectric Generators

import itertools
import queue
import re
import sys

# ==============================================================================

# A state is given by the floor the elevator is on
# and the floors each microchip and generator are in
# Chips are the first N elements, generators the next N
class State:

  def __init__(self, floors):
    self.elev = 1
    self.N = len(floors) // 2
    self.floors = floors
    self.parent = None

  def __repr__(self):
    s = "\n"
    for fl in [4,3,2,1]:
      s += "{} ".format(fl)
      if self.elev == fl:
        s += "E"
      else:
        s += " "
      for i in range(self.N):
        if self.floors[i] == fl:
          s += " " + names[i][:2].capitalize() +  "M"
        if self.floors[self.N+i] == fl:
          s += " " + names[i][:2].capitalize() +  "G"
      s += "\n"
    return s

  def __hash__(self):
    return hash((self.elev, tuple(self.floors)))

  # Checks equality with another State object
  def __eq__(self, other):
    return self.elev == other.elev and self.floors == other.floors

  # Returns a copy of itself
  def copy(self):
    s = State([x for x in self.floors])
    s.elev = self.elev
    s.N = self.N
    return s

  # Determine whether the state is the goal state
  def is_goal(self):
    for f in self.floors:
      if f != 4:
        return False
    return True

  # Retuns whether the state is valid
  # Chips are the first N elements, generators the next N
  def is_valid(self):
    for i in range(self.N):
      if self.floors[i] != self.floors[self.N+i]:
        for j in range(self.N):
          if j != i and self.floors[i] == self.floors[self.N+j]:
            # print(self.floors); input()
            return False
    return True

  # Returns the child states of this state, i.e. the legal states
  # accessible from it
  def get_children(self):

    # Neighboring floors the elevator can go to
    if self.elev == 1:
      dest_floors = [2]
    elif self.elev == 4:
      dest_floors = [3]
    else:
      dest_floors = (self.elev-1, self.elev+1)

    # Possible cargo to be transported: choose one or two (if possible)
    # of the items in the current floor
    items = [i for i in range(2*self.N) if self.floors[i] == self.elev]
    if len(items) == 0:
      raise(Exception("Elevator is at an empty floor!"))
    elif len(items) == 1:
      cargo = [(items[0],)]
    else:
      cargo = [(x,) for x in items] + list(itertools.combinations(items, 2))

    # Generate child states and keep those that are valid
    children = []
    for dest in dest_floors:
      for items in cargo:
        new_state = self.copy()
        new_state.elev = dest
        for i in items:
          new_state.floors[i] = dest
        if new_state.is_valid():
          children.append(new_state)
    return children

# -----------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input into stuff dict
stuff = {}
with open(sys.argv[1]) as f:
  for line in f:
    if "first floor" in line:
      floor = 1
    elif "second floor" in line:
      floor = 2
    elif "third floor" in line:
      floor = 3
    elif "fourth floor" in line:
      floor = 4
    for name in re.findall("(\w+) generator", line):
      if name not in stuff:
        stuff[name] = {"gen": None, "chip": None}
      stuff[name]["gen"] = floor
    for name in re.findall("(\w+)-compatible microchip", line):
      if name not in stuff:
        stuff[name] = {"gen": None, "chip": None}
      stuff[name]["chip"] = floor

# Do a breadth-first search looking for the goal state
def solve(start_state):

  q = queue.Queue()
  q.put((0, start_state))
  seen = set()
  seen.add(start_state.__hash__())
  count = 0
  while not q.empty():

    depth, state = q.get()
    count += 1

    if count % 100000 == 0:
      s = "depth={} seen={:,} queue={:,}".format(depth, count, q.qsize())
      print(s)

    if state.is_goal():
      print("\nGoal state found at depth={}".format(depth))
      break

    for child in state.get_children():
      if child.__hash__() not in seen:
        q.put((depth+1, child))
        seen.add(child.__hash__())
        child.parent = state

  print(state)
  return depth

# ---------------------------------------
# Part 1

names = list(stuff.keys())
_floors = [stuff[name]["chip"] for name in names] + [stuff[name]["gen"] for name in names]

start_state = State(_floors)
print(start_state)

ans1 = solve(start_state)

print("Part 1:", ans1)

# ---------------------------------------
# Part 2

stuff["elerium"] = {"chip": 1, "gen": 1}
stuff["dilithium"] = {"chip": 1, "gen": 1}

names = list(stuff.keys())
_floors = [stuff[name]["chip"] for name in names] + [stuff[name]["gen"] for name in names]

start_state = State(_floors)
print(start_state)

ans2 = solve(start_state)

print("Part 1:", ans2)
