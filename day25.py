# Day 25: Clock Signal

import copy
import functools
import sys

# ==============================================================================

class Computer:

  def __init__(self):
    self.regs = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    self.output = []
    self.last_output = None

  def reset(self):
    self.regs = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    self.output = []
    self.last_output = None

  def eval(self, arg):
    if isinstance(arg, int):
      return arg
    else:
      return self.regs[arg]

  def run(self, program):

    ptr = 0
    while ptr < len(program):

      inst = program[ptr]
      op = inst[0]

      if op == "cpy":
        if inst[2] in self.regs:
          val = self.eval(inst[1])
          self.regs[inst[2]] = val
        ptr += 1

      elif op == "inc":
        if inst[1] in self.regs:
          self.regs[inst[1]] += 1
        ptr += 1

      elif op == "dec":
        if inst[1] in self.regs:
          self.regs[inst[1]] -= 1
        ptr += 1

      elif op == "jnz":
        val1 = self.eval(inst[1])
        if val1 != 0:
          val2 = self.eval(inst[2])
          ptr += val2
        else:
          ptr += 1

      elif op == "tgl":
        ptr1 = ptr + self.eval(inst[1])
        if ptr1 > len(program)-1:
          pass
        else:
          op1 = program[ptr1][0]
          if op1 == "inc": program[ptr1][0] = "dec"
          elif op1 == "dec": program[ptr1][0] = "inc"
          elif op1 == "tgl": program[ptr1][0] = "inc"
          elif op1 == "tgl": program[ptr1][0] = "inc"
          elif op1 == "jnz": program[ptr1][0] = "cpy"
          elif op1 == "cpy": program[ptr1][0] = "jnz"
        ptr += 1

      elif op == "out":
        value = self.eval(inst[1])
        self.output.append(value)
        if self.last_output is None:
          if value != 0:
            # print("".join(str(x) for x in self.output))
            return 1
        else:
          if (self.last_output == 0 and value != 1) or (self.last_output == 1 and value != 0):
            # print("".join(str(x) for x in self.output))
            return 1
        self.last_output = value
        # print(self.output)
        ptr += 1

      if len(self.output) == 1000:
        # print("".join(str(x) for x in self.output))
        return 0

# -----------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input into program
program = []
with open(sys.argv[1]) as f:
  for line in f:
    tokens = line.strip().split()
    instruction = [tokens[0]]
    for x in tokens[1:]:
      try:
        instruction.append(int(x))
      except:
        instruction.append(x)
    program.append(instruction)

# -----------------------------------------
# Part 1

computer = Computer()
a = 0
while True:
  computer.reset()
  computer.regs['a'] = a
  exit_code = computer.run(program)
  if exit_code == 0:
    ans1 = a
    break
  a += 1

print("Part 1:", ans1)

# ---------------------------------------
# Part 2

# No Part 2
