# Day 14: One-Time Pad

import hashlib
import re
import sys

# ==============================================================================

def gen_hash(salt, index, cycles):
  h = salt + str(index)
  for i in range(cycles):
    h = hashlib.md5(h.encode("ascii")).hexdigest()
  return h

def is_valid(index, l, quintuples, salt, cycles):
  h = gen_hash(salt, index, cycles)
  for i in quintuples[l]:
    if 1 <= i-index <= 1000:
      return True
  return False

def find_nth_key(salt, nth, cycles):

  possibles = []
  quintuples = {x:[] for x in "0123456789abcdef"}

  index = 0
  max_idx = 30000
  for i in range(max_idx):

    h = gen_hash(salt, index, cycles)

    m = re.search(r"([0-9a-f])\1{2}", h)
    if m is not None:
      possibles.append((index, m.group()[0]))

    m = re.findall(r"([0-9a-f])\1{4}", h)
    if len(m) > 0:
      for l in m:
        quintuples[l].append(index)

    index += 1

  num_found = 0
  for idx, l in possibles:
    if idx >= max_idx-1000:
      print("Reached end of stream; generate more hashes!")
      return None
    if is_valid(idx, l, quintuples, salt, cycles):
      num_found += 1
      if num_found == nth:
        return idx

# -----------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

with open(sys.argv[1]) as f:
  salt = f.readline().strip()

# -----------------------------------------
# Part 1

idx = find_nth_key(salt, 64, 1)

print("Part 1:", idx)

# ---------------------------------------
# Part 2

idx = find_nth_key(salt, 64, 2016+1)

print("Part 2:", idx)
