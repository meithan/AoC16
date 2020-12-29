# Day 21: Scrambled Letters and Hash

import itertools
import re
import sys

# ==============================================================================

def swap(l, i, j):
  tmp = l[i]
  l[i] = l[j]
  l[j] = tmp

def rotate(l, s):
  N = len(l)
  nl = [0]*N
  for i in range(N):
    nl[(i+s)%N] = l[i]
  return nl

def apply_inst(inst, pswd):

  op = inst[0]
  args = inst[1:]

  if op == "swp_pos":
    swap(pswd, args[0], args[1])

  elif op == "swp_let":
    i1 = pswd.index(args[0])
    i2 = pswd.index(args[1])
    swap(pswd, i1, i2)

  elif op == "rot":
    s = -args[1] if args[0] == "left" else args[1]
    pswd = rotate(pswd, s)

  elif op == "rot_let":
    i1 = pswd.index(args[0])
    s = 1 + i1
    if i1 >= 4:
      s += 1
    pswd = rotate(pswd, s)

  elif op == "rev":
    i1 = args[0]
    i2 = args[1]
    pswd = pswd[:i1] + list(reversed(pswd[i1:i2+1])) + pswd[i2+1:]

  elif op == "mov":
    i1 = args[0]
    i2 = args[1]
    l = pswd.pop(i1)
    pswd.insert(i2, l)

  return pswd

def scramble(password):
  pswd = [c for c in password]
  for inst in instructions:
    pswd = apply_inst(inst, pswd)
  return "".join(pswd)

# -----------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

instructions = []
with open(sys.argv[1]) as f:
  for line in f:

    m = re.match("swap position ([0-9]+) with position ([0-9]+)", line)
    if m is not None:
      instructions.append(("swp_pos", int(m.group(1)), int(m.group(2))))

    m = re.match("swap letter ([a-z]) with letter ([a-z])", line)
    if m is not None:
      instructions.append(("swp_let", m.group(1), m.group(2)))

    m = re.match("rotate (left|right) ([0-9]+) steps*", line)
    if m is not None:
      instructions.append(("rot", m.group(1), int(m.group(2))))

    m = re.match("rotate based on position of letter ([a-z])", line)
    if m is not None:
      instructions.append(("rot_let", m.group(1)))

    m = re.match("reverse positions ([0-9]+) through ([0-9]+)", line)
    if m is not None:
      instructions.append(("rev", int(m.group(1)), int(m.group(2))))

    m = re.match("move position ([0-9]+) to position ([0-9]+)", line)
    if m is not None:
      instructions.append(("mov", int(m.group(1)), int(m.group(2))))

# -----------------------------------------
# Part 1

start_password = "abcdefgh"

print("Part 1:", scramble(start_password))

# ---------------------------------------
# Part 2

scrambled_password = "fbgdceah"

for pswd in itertools.permutations("abcdefgh"):
  if scramble(pswd) == scrambled_password:
    ans2 = "".join(pswd)
    break

print("Part 2:", ans2)
