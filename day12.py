# Day 12: Leonardo's Monorail

import sys

# ==============================================================================

class Computer:

  def __init__(self):
    self.regs = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

  def get_val(self, arg):
    if isinstance(arg, int):
      return arg
    else:
      return self.regs[arg]

  def exec_program(self, program):

    ptr = 0
    while ptr < len(program):

      inst = program[ptr]
      op = inst[0]

      # print("ptr=", ptr)
      # print(inst)

      if op == "cpy":
        val = self.get_val(inst[1])
        self.regs[inst[2]] = val
        ptr += 1

      elif op == "inc":
        self.regs[inst[1]] += 1
        ptr += 1

      elif op == "dec":
        self.regs[inst[1]] -= 1
        ptr += 1

      elif op == "jnz":
        val1 = self.get_val(inst[1])
        if val1 != 0:
          val2 = self.get_val(inst[2])
          ptr += val2
        else:
          ptr += 1

      # print(self.regs)

    return self.regs

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

comp = Computer()
comp.exec_program(program)

print("Part 1:", comp.regs['a'])

# ---------------------------------------
# Part 2

comp = Computer()
comp.regs['c'] = 1
comp.exec_program(program)

print("Part 1:", comp.regs['a'])
