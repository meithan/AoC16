# Day 6: Signals and Noise

with open("day6.in") as f:
  messages = [line.strip() for line in f]

N = len(messages[0])
counts = [dict() for i in range(N)]
for msg in messages:
  for i,c in enumerate(msg):
    if c not in counts[i]:
      counts[i][c] = 0
    counts[i][c] += 1

msg1 = ""
msg2 = ""
for i in range(N):
  foo = [(k, counts[i][k]) for k in counts[i].keys()]
  foo.sort(key=lambda x: x[1], reverse=True)
  msg1 += foo[0][0]
  msg2 += foo[-1][0]

print("Part 1:", msg1)
print("Part 2:", msg2)
