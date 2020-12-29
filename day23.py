# Day 23: Safe Cracking

import copy
import functools
import sys

# ==============================================================================

class Computer:

  def __init__(self):
    self.regs = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

  def eval(self, arg):
    if isinstance(arg, int):
      return arg
    else:
      return self.regs[arg]

  def run(self, program):

    debug = False; c = 0

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

# -----------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input into program
program_orig = []
with open(sys.argv[1]) as f:
  for line in f:
    tokens = line.strip().split()
    instruction = [tokens[0]]
    for x in tokens[1:]:
      try:
        instruction.append(int(x))
      except:
        instruction.append(x)
    program_orig.append(instruction)

# -----------------------------------------
# Part 1

computer = Computer()
program = copy.deepcopy(program_orig)

computer.regs['a'] = 7
computer.run(program)

print("Part 1:", computer.regs['a'])

# ---------------------------------------
# Part 2

# What the computer is calculating is the factorial of the initial value
# in register 'a', plus the product of the two positive two-digit numbers
# elsewhere in the program (70 and 87 in this case)

def fact(n):
  if n == 0 or n == 1:
    return 1
  else:
    return functools.reduce(lambda a, b: a*b, list(range(2,n+1)))

ans2 = fact(12) + 70*87

print("Part 2:", ans2)
