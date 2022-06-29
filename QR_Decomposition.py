#QR Decomposition without built-in function
import numpy as np
np.set_printoptions(precision=5, suppress=True)
m = int(input('請輸入多少列'))
n = int(input('請輸入多少行'))
A = np.zeros((m,n))
for i in range(m):
  print('輸入第', (i+1), '列的所有數字')
  for j in range(n):
    A[i,j] = float(input())
Q = np.zeros((m,n))
m1 = 0
for i in range(0,m):
  m1 = m1 + A[i,0]**2
m1 = m1**0.5
#print(m1)
Q[:,0] = (1/m1)*A[:,0]
m2 = 0
for j in range(1,n):
  for l in range(0,j):
    Q[:,j] =  Q[:,j] + np.dot(A[:,j], Q[:,l])*Q[:,l]
  Q[:,j] = A[:,j] - Q[:,j]
  for k in range(0,m):
    m2 = m2 + Q[k,j]**2
  m2 = m2**0.5
  #print(m2)
  Q[:,j] = (1/m2)*Q[:,j]
  m2 = 0
Q_t = np.transpose(Q)
R = Q_t.dot(A)
print('A : \n',A)
print('Q : \n',Q)
print('R : \n',R)