import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve
from LU import LU
#  Define a system of linear equations. A  is the coefficient matrix and b is the vector of knowns
#  We are using the same matrix as above
A = np.array([[2, -1, 0],
              [-1, 2, -1.],
              [0, -1, 2.]])

#  Do the matrix factorization.  In our case, the permutation matrix P is the identity
L, U = LU(A)

print('The L matrix is:')
print(L)
print()
print('The U matrix is:')
print(U)
