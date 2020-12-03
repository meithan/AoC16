# Day 8: Two-Factor Authentication

import re

class Screen:

  def __init__(self, rows=6, cols=50):
    self.rows = rows
    self.cols = cols
    self.pixels = [['.']*cols for i in range(rows)]
    self.p_rect = re.compile("(rect) ([0-9]+)x([0-9]+)")
    self.p_rotrow = re.compile("rotate (row) y=([0-9]+) by ([0-9]+)")
    self.p_rotcol = re.compile("rotate (column) x=([0-9]+) by ([0-9]+)")

  def exec_inst(self, inst):
    for p in [self.p_rect, self.p_rotrow, self.p_rotcol]:
      m = p.match(inst)
      if m is not None:
        op = m.group(1)
        A = int(m.group(2))
        B = int(m.group(3))
        if op == "rect":
          self.rect(A, B)
        elif op == "row":
          self.rotate_row(A, B)
        elif op == "column":
          self.rotate_column(A, B)
        return

  def rect(self, A, B):
    for i in range(B):
      for j in range(A):
        self.pixels[i][j] = "#"

  def rotate_row(self, A, B):
    old_row = [self.pixels[A][j] for j in range(self.cols)]
    for j in range(self.cols):
      new_j = (j + B) % self.cols
      self.pixels[A][new_j] = old_row[j]

  def rotate_column(self, A, B):
    old_column = [self.pixels[i][A] for i in range(self.rows)]
    for i in range(self.rows):
      new_i = (i + B) % self.rows
      self.pixels[new_i][A] = old_column[i]

  def print(self):
    for row in self.pixels:
      print("".join(row))

  def count_lit(self):
    lit = 0
    for i in range(self.rows):
      for j in range(self.cols):
        if self.pixels[i][j] == "#":
          lit += 1
    return lit

# ================================================

s = Screen()

with open("day8.in") as f:
  for line in f:
    s.exec_inst(line.strip())

print("Part 1:", s.count_lit())
print("Part 2:")
s.print()
