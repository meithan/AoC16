# Day 20: Firewall Rules

import sys

# ==============================================================================

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

rules = []
with open(sys.argv[1]) as f:
  for line in f:
    tokens = tuple(int(x) for x in line.strip().split("-"))
    rules.append(tokens)

# -----------------------------------------
# Part 1

def clip_interval(interval, rule):
  a, b = interval
  ra, rb = rule
  if ra > b or rb < a:
    # No overlap: return full interval
    return [(a,b)]
  elif ra <= a and rb >= b:
    # Interval contained in rule: return nothing
    return []
  elif ra <= a and rb < b:
    # Left portion clipped
    return [(rb+1, b)]
  elif ra > a and rb >= b:
    # Right portion clipped
    return [(a,ra-1)]
  elif ra > a and rb < b:
    # Split into two intervals
    return [(a,ra-1), (rb+1,b)]

# valids = [(0,9)]
# rules = [(5,8), (0,2), (4,7)]
valids = [(0, 2**32-1)]

for rule in rules:
  new_valids = []
  for valid in valids:
    new_valids += clip_interval(valid, rule)
  valids = new_valids

ans1 = valids[0][0]

print("Part 1:", ans1)

# ---------------------------------------
# Part 2

ans2 = 0
for a,b in valids:
  ans2 += b-a+1

print("Part 2:", ans2)
