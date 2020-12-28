# Day 15: Timing is Everything

import re
import sys

# ==============================================================================

class Disc:

  def __init__(self, name, N, t0, x0):
    self.name = name
    self.N = int(N)
    self.t0 = int(t0)
    self.x0 = int(x0)

  def pos_at(self, t):
    return (self.x0 + t - self.t0) % self.N

  def __repr__(self):
    return "<Disc {}, N={}: x0={} at t0={}>".format(self.name, self.N, self.x0, self.t0)

def try_drop(discs, time):
  t = time
  for disc in discs:
    t += 1
    if disc.pos_at(t) != 0:
      return False
  return True

# -----------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

discs = []
with open(sys.argv[1]) as f:
  for line in f:
    m = re.match("Disc (#[0-9]+) has ([0-9]+) positions; at time=([0-9]+), it is at position ([0-9]+).", line.strip())
    discs.append(Disc(m.group(1), m.group(2), m.group(3), m.group(4)))

# -----------------------------------------
# Part 1

t = 0
while True:
  if try_drop(discs, t):
    ans1 = t
    break
  t += 1

print("Part 1:", ans1)

# ---------------------------------------
# Part 2

discs.append(Disc("#{}".format(len(discs)), 11, 0, 0))

t = 0
while True:
  if try_drop(discs, t):
    ans2 = t
    break
  t += 1

print("Part 2:", ans2)
