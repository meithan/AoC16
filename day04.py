# Day 4: Security Through Obscurity

import re

def calc_checksum(name):

  counts = {}
  for l in name:
    if l != "-":
      if l not in counts:
        counts[l] = 0
      counts[l] += 1

  counts_list = [(l, counts[l]) for l in counts.keys()]
  counts_list.sort(key=lambda x: (-x[1], x[0]))

  checksum = "".join([x[0] for x in counts_list[:5]])
  return checksum

def decrypt(cipher, rot):

  plain = ""
  for c in cipher:
    if c == "-":
      plain += " "
    else:
      enc_code = ord(c) - 97
      dec_code = (enc_code + rot) % 26
      l = chr(97 + dec_code)
      plain += l

  return plain

# ==============================================

# name = "aaaaa-bbb-z-y-x"
# name = "a-b-c-d-e-f-g-h"
# name = "not-a-real-room"
# name = "totally-real-room"

# Read input
pattern = re.compile(r"(.+)-([0-9]+)\[(.+)\]")
rooms = []
with open("day4.in") as f:
  for line in f:
    m = pattern.match(line.strip())
    name = m.group(1)
    room_ID = int(m.group(2))
    checksum = m.group(3)
    rooms.append((name, room_ID, checksum))

# Part 1
total = 0
real_rooms = []
for name, room_ID, checksum in rooms:
  chk = calc_checksum(name)
  if chk == checksum:
    real_rooms.append((name, room_ID))
    total += room_ID

print("Part 1:", total)

# Part 2
for name, room_ID in real_rooms:
  print(decrypt(name, room_ID), room_ID)
