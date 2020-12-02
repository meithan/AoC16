# Day 5: How About a Nice Game of Chess?

import hashlib

def find_password(door_ID, part):

  def print_found():
    print("\r{} {:,}".format("".join(password), idx))
    print_current()
  def print_current():
    print("\r{:,} searched".format(idx), end="")

  password = ["_"]*8
  idx = 0
  found = 0
  while found < 8:
    if idx % 1000000 == 0:
      print_current()
    s = "{}{}".format(door_ID, idx).encode("ascii")
    hash = hashlib.md5(s).hexdigest()
    if hash.startswith("00000"):
      if part == 1:
        password[found] = hash[5]
        found += 1
        print_found()
      elif part == 2:
        if hash[5] in "01234567" and password[int(hash[5])] == "_":
          password[int(hash[5])] = hash[6]
          found += 1
          print_found()
    idx += 1

  print()
  return "".join(password)

# ==========================================

puzzle_input = "uqwqemis"
# puzzle_input = "abc"

# pswd1 = find_password(puzzle_input, 1)
# print("Part 1:", pswd1)

pswd2 = find_password(puzzle_input, 2)
print("Part 2:", pswd2)
