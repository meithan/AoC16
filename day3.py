import sys
import numpy as np

triangles = []
with open(sys.argv[1]) as f:
  for line in f:
    triangles.append(tuple(map(int, line.strip().split())))

def isPossibleTriangle(a,b,c):
  return a+b > c and b+c > a and a+c > b

possible_triangles = 0
for a,b,c in triangles:
  if isPossibleTriangle(a, b, c): possible_triangles += 1
print("=== Part One ===")
print("Possible triangles: %i/%i" % (possible_triangles, len(triangles)))

possible_triangles = 0
trigs = np.asarray(triangles)
trigs2 = np.concatenate([trigs[:,0],trigs[:,1],trigs[:,2]])
for i in range(0, len(trigs2), 3):
  print(i)
  if isPossibleTriangle(trigs2[i], trigs2[i+1], trigs2[i+2]):
    possible_triangles += 1
print("\=== Part Two ===")
print("Possible triangles: %i/%i" % (possible_triangles, len(triangles)))
