# Day 9: Explosives in Cyberspace

# For Part 1 we can simply run the decompression algorithm
# on the message
def decompress(m):

  decoded = ""
  i = 0
  while True:

    if m[i] != "(":
      decoded += m[i]
      i += 1

    elif m[i] == "(":

      marker = ""
      i += 1
      while m[i] != ")":
        marker += m[i]
        i += 1
      i += 1

      n, r = [int(x) for x in marker.split("x")]

      for j in range(r):
        decoded += m[i:i+n]
      i += n

    if i > len(m)-1:
      break

  return decoded

# For Part 2, it's unpractical to decompress the message, but we can
# compute its final length without decompressing it.
# A normal character outside a marker sequence has length 1. The length
# of a marker sequence is the decoded length of its "payload" (a number
# of characters after it, as specified by the first value) multiplied
# by the indicated multiplier (the second value). The length of the
# "payload" is then computed recursively.
def compute_length(m):

  length = 0
  i = 0
  while i < len(m):

    if m[i] != "(":

      length += 1
      i += 1

    elif m[i] == "(":

      marker = ""
      i += 1
      while True:
        marker += m[i]
        i += 1
        if m[i] == ")":
          i += 1
          break

      n, r = [int(x) for x in marker.split("x")]
      payload = m[i:i+n]

      length += r * compute_length(payload)

      i += n

  return length

# --------------------------------------

with open("day9.in") as f:
  message = f.read().strip()

dec_message = decompress(message)
print("Part 1:", len(dec_message))

length = compute_length(message)
print("Part 2:", length)
