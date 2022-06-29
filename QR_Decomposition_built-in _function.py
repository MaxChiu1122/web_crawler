#QR Decomposition with built-in function
import numpy as np
import pprint
import scipy
import scipy.linalg
np.set_printoptions(precision=5, suppress=True)
m = int(input('請輸入多少列'))
n = int(input('請輸入多少行'))
A = np.zeros((m,n))
for i in range(m):
  print('輸入第', (i+1), '列的所有數字')
  for j in range(n):
    A[i,j] = float(input())
Q, R = scipy.linalg.qr(A)
print("A:")
pprint.pprint(A)

print("Q:")
pprint.pprint(Q)

print("R:")
pprint.pprint(R)