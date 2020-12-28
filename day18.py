# Day 18: Like a Rogue

import sys

# ==============================================================================

# This is Wolfram's Rule 90!
trap_states = ["^^.", ".^^", "^..", "..^"]

def step(state):
  new_state = ["."]
  for i in range(1, len(state)-1):
    lcr = state[i-1:i+2]
    if lcr in trap_states:
      new_state.append("^")
    else:
      new_state.append(".")
  new_state.append(".")
  return "".join(new_state)

def build_map(init_state, rows):
  map = [init_state]
  state = "." + init_state + "."
  for i in range(rows-1):
    state = step(state)
    map.append(state[1:-1])
  return map

# -----------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

with open(sys.argv[1]) as f:
  init_state = f.readline().strip()

# -----------------------------------------
# Part 1

# init_state = ".^^.^.^^^^"
map = build_map(init_state, 40)

ans1 = 0
for row in map:
  ans1 += row.count(".")

print("Part 1:", ans1)

# ---------------------------------------
# Part 2

map = build_map(init_state, 400000)

ans2 = 0
for row in map:
  ans2 += row.count(".")

print("Part 2:", ans2)
