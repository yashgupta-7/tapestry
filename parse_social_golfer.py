# vim: tabstop=2 expandtab shiftwidth=2 softtabstop=2
import string
import numpy as np
from matrices import mat_dir
import os

row_map = {}
upper = string.ascii_uppercase
lower = string.ascii_lowercase
for i in range(18):
  row_map[upper[i]] = i

for j in range(18):
  row_map[lower[j]] = j + 18

print(row_map)

M = np.zeros((36, 99), dtype=np.int32)
with open('36x99_social_golfer.txt') as f:
  lines = f.readlines()
  col = 0
  for line in lines:
    if line.strip() == "":
      continue
    rows = [row_map[ch] for ch in line.strip()]
    print(rows)
    M[rows, col] = 1
    col += 1
    
  assert col == 99  

print(np.sum(M))
print(np.sum(M, axis=1))
print(np.sum(M, axis=0))

full_path = os.path.join(mat_dir, "optimized_M_36_99_social_golfer.txt")
np.savetxt(full_path, M, fmt="%d")

