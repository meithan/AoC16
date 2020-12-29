# Day 19: An Elephant Named Joseph

from math import log, floor
import sys

# ==============================================================================

class Elf:

  def __init__(self, num):
    self.num = int(num)
    self.presents = 1
    self.prev = None
    self.next = None

  def steal(self, victim):
    # print("Elf {} takes {} present{} from elf {}".format(self.num, victim.presents, "s" if victim.presents > 1 else "", victim.num))
    self.presents += victim.presents
    victim.presents = 0
    old_prev = victim.prev
    victim.prev.next = victim.next
    victim.next.prev = old_prev

  def __repr__(self):
    return "<{} ({}) -> ({},{})>".format(self.num, self.presents, self.prev.num if self.prev is not None else "None", self.next.num if self.next is not None else "None")

# -----------------------------------------

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

with open(sys.argv[1]) as f:
  num_elves = int(f.readline())

# -----------------------------------------
# Part 1

first = Elf(1)
current = first
for i in range(2, num_elves+1):
  e = Elf(i)
  e.prev = current
  current.next = e
  current = e
first.prev = current
current.next = first

elf = first
while True:
  victim = elf.next
  elf.steal(victim)
  if elf.next.num == elf.num:
    winner = elf
    break
  elf = elf.next

print("Part 1:", winner.num)

# ---------------------------------------
# Part 2

def solve_direct(ne):

  first = Elf(1)
  elves = {1: first}
  current = first
  for i in range(2, ne+1):
    e = Elf(i)
    elves[i] = e
    e.prev = current
    current.next = e
    current = e
  first.prev = current
  current.next = first

  n = ne
  elf = first
  while True:
    victim = elf
    for i in range(n//2):
      victim = victim.next
    if victim.num == elf.num:
      return elf.num
    elf.steal(victim)
    n -= 1
    elf = elf.next

# for ne in range(1, 100+1):
#   print(ne, solve_direct(ne))

# After running the above code for a number of elves (n) from 1 to 100 we get
# the following winner numbers (w):
#
# n  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
# w  1  1  3  1  2  3  5  7  9  1  2  3  4  5  6  7  8  9 11 13 15 17 19 21 23
#
# n 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50
# w 25 27  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
#
# n 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75
# w 24 25 26 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69
#
# n 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100
# w 71 73 75 77 79 81  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
#
# The pattern is clear:
# 1) If n is a power of 3, n = 3**k, then w is that power of 3, w = n = 3**k.
# 2) Otherwise, compute the largest power of 3 *smaller* than n; call it e0.
#    Starting with n=e0+1, the next e0 winners are the sequence starting
#    with 1 and counting up to n=2*e0 (for which the winner is e0). After that,
#    the next e0 winners countinue the count but in steps of 2, up to n=3*e0,
#    at which point we've reached the next power of 3.
#
# This can be written mathematically as:
#        { e0           if n = e0 (i.e. n = 3^k for some integer k)
# w(n) = { n - e0       if e0 < n <= 2*e0
#        { 2*n - 3*e0   if 2*e0 < n < 3*e0
# where e0 = floor(log_3(n)), i.e. largest e0 = 3**k such that e0 <= n.
#
# For instance, consider n = 23. The largest power of 3 smaller than 23 is 9,
# so w(9) = 9. Then w(10) = 1, w(11) = 2, etc, up to w(18) = 9. Starting with
# n = 19, now w goes up in steps of 2: w(19) = 11, w(20) = 13, etc. up to
# w(23) = 19, which is the answer. The count would continue w(24) = 21, etc,
# up to w(27) = 27, which si the next power of 3.
def compute_winner(n):
  k = floor(log(n)/log(3))
  e0 = 3**k
  if e0 == n:
    return e0
  elif n <= 2*e0:
    return n - e0
  else:
    return 2*n - 3*e0     #(2*e0 - e0) + 2*(n - 2*e0)

# for ne in range(1, 100+1):
#   print(ne, solve_direct(ne), compute_winner(ne))

winner_num = compute_winner(num_elves)

print("Part 2:", winner_num)
