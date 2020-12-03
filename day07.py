# Day 7: Internet Protocol Version 7

def is_ABBA(s):
  for i in range(len(s)-3):
    if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
      return True
  return False

def split_sequences(IP):

  super = True
  super_seqs = []
  hyper_seqs = []
  seq = []
  for c in IP:
    if c == "[":
      super = False
      if len(seq) > 0:
        super_seqs.append("".join(seq))
      seq = []
    elif c == "]":
      super = True
      if len(seq) > 0:
        hyper_seqs.append("".join(seq))
      seq = []
    else:
      seq.append(c)
  if len(seq) > 0:
    super_seqs.append("".join(seq))

  return super_seqs, hyper_seqs

def supports_TLS(IP):

  super_seqs, hyper_seqs = split_sequences(IP)

  # Check supernet sequences
  is_abba_super = False
  for seq in super_seqs:
    if is_ABBA(seq):
      is_abba_super = True
      break
  if not is_abba_super:
    return False

  # Check hypernet sequences
  is_abba_hyp = False
  for seq in hyper_seqs:
    if is_ABBA(seq):
      is_abba_hyp = True
      break

  if is_abba_super and not is_abba_hyp:
    return True
  else:
    return False

def supports_SSL(IP):

  super_seqs, hyper_seqs = split_sequences(IP)

  # Find ABA blocks in supernet sequences
  ABA_blocks = []
  for s in super_seqs:
    for i in range(len(s)-2):
      if s[i] == s[i+2] and s[i] != s[i+1]:
        ABA_blocks.append(s[i:i+3])

  # Check if any ABA block has a corresponding
  # BAB block in hypernet sequences
  for aba in ABA_blocks:
    bab = aba[1] + aba[0] + aba[1]
    for s in hyper_seqs:
      for i in range(len(s)-2):
        if s[i:i+3] == bab:
          return True

  return False

# ---------------------------------------

IPs = []
with open("day7.in") as f:
  for line in f:
    IPs.append(line.strip())

do_support = 0
for IP in IPs:
  if supports_TLS(IP):
    do_support += 1

print("Part 1:", do_support)

do_support = 0
for IP in IPs:
  if supports_SSL(IP):
    do_support += 1
print("Part 2:", do_support)
