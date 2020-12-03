# Day 10: Balance Bots

import sys
import re

# ----------------------------------------

class Bot:
  def __init__(self, number):
    self.number = number
    self.chips = []
    self.low_type = None
    self.low_to = None
    self.high_type = None
    self.high_to = None
  def __repr__(self):
    return "<Bot {} | {} | {} {}, {} {}>".format(self.number, self.chips, self.low_type, self.low_to, self.high_type, self.high_to)

# regexes for easy parsing
p_receive = re.compile("value ([0-9]+) goes to bot ([0-9]+)")
p_transfer = re.compile("bot ([0-9]+) gives low to (\w+) ([0-9]+) and high to (\w+) ([0-9]+)")

# ----------------------------------------

# Puzzle input: chip values to look for in Part 1
value1 = 61
value2 = 17

# Read instructions from file input
instructions = []
with open(sys.argv[1]) as f:
  for line in f:
    instructions.append(line.strip())

# Parse all instructions and assign chips and tranfers to bots
bots = {}
outputs = {}
ready = []
for inst in instructions:

  # Parse 'value goes to bot' instructions
  # Bots that get two chips are added to the ready list
  if inst.startswith("value"):

    m = p_receive.match(inst)
    value = int(m.group(1))
    bot_num = int(m.group(2))

    if bot_num not in bots:
      bots[bot_num] = Bot(bot_num)

    bots[bot_num].chips.append(value)

    if len(bots[bot_num].chips) == 2:
      ready.append(bots[bot_num])

  # Parse 'bot gives low/high to' instructions
  elif inst.startswith("bot"):

    m = p_transfer.match(inst)
    bot_num = int(m.group(1))
    low_type = m.group(2)
    low_to = int(m.group(3))
    high_type = m.group(4)
    high_to = int(m.group(5))

    if bot_num not in bots:
      bots[bot_num] = Bot(bot_num)

    bots[bot_num].low_type = low_type
    bots[bot_num].low_to = low_to
    bots[bot_num].high_type = high_type
    bots[bot_num].high_to = high_to

    if low_type == "bot":
      if low_to not in bots:
        bots[low_to] = Bot(low_to)
    elif low_type == "output":
      if low_to not in outputs:
        outputs[low_to] = []
    if high_type == "bot":
      if high_to not in bots:
        bots[high_to] = Bot(high_to)
    elif high_type == "output":
      if high_to not in outputs:
        outputs[high_to] = []

# Execute all chip transfers
target_values = sorted([value1, value2])
part1_solved = False
while len(ready) > 0:

  bot = ready.pop()
  bot.chips.sort()

  # Part 1 check
  if not part1_solved and bot.chips == target_values:
    ans1 = bot.number
    print("Part 1:", ans1)
    part1_solved = True

  # Transfer low value chip
  value = bot.chips[0]
  if bot.low_type == "bot":
    bots[bot.low_to].chips.append(value)
    if len(bots[bot.low_to].chips) == 2:
      ready.append(bots[bot.low_to])
  elif bot.low_type == "output":
    outputs[bot.low_to].append(value)

  # Transfer high value chip
  value = bot.chips[1]
  if bot.high_type == "bot":
    bots[bot.high_to].chips.append(value)
    if len(bots[bot.high_to].chips) == 2:
      ready.append(bots[bot.high_to])
  elif bot.high_type == "output":
    outputs[bot.high_to].append(value)

  bot.chips = []

# Part 2:
ans2 = outputs[0][0] * outputs[1][0] * outputs[2][0]
print("Part 2:", ans2)
