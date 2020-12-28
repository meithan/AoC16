# Day 16: Dragon Checksum

import sys

# ==============================================================================

def expand(a):
  b = []
  for i in range(len(a)-1, -1, -1):
    if a[i] == '0':
      b.append('1')
    elif a[i] == '1':
      b.append('0')
  return a + "0" + "".join(b)

def checksum(a):
  while len(a) % 2 == 0:
    s = []
    for i in range(len(a)//2):
      if a[2*i:2*i+2] in ["00", "11"]:
        s.append("1")
      else:
        s.append("0")
    a = "".join(s)
  return a

def disk_checksum(length, init_state):
  a = init_state
  while len(a) < length:
    a = expand(a)
  return checksum(a[:length])

# -----------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

with open(sys.argv[1]) as f:
  init_a = f.readline().strip()

# -----------------------------------------
# Part 1

disk_length = 272
ans1 = disk_checksum(disk_length, init_a)

print("Part 1:", ans1)

# ---------------------------------------
# Part 2

disk_length = 35651584
ans2 = disk_checksum(disk_length, init_a)

print("Part 2:", ans2)
