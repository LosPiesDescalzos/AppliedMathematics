import numpy as np
from matrix_Gilbert import generate_hilbert_matrix

ITERATION_LIMIT = 150000

# A = np.array([[10., -1., 2., 0.],
#               [-1., 11., -1., 3.],
#               [2., -1., 10., -1.],
#               [0.0, 3., -1., 8.]])
# b = np.array([6., 25., -11., 15.])

# A = np.array([[5., 3., 10., 0.],
#               [-1., 10., -1., 3.],
#               [2., -1., 10., 6.],
#               [0., 3., 2., 8.]])
# b = np.array([6., 20., 4., 12.])

# k = 4
# A = generate_hilbert_matrix(k)
# A = A.toarray()
# b = np.array([1.0, 1.0, 1.0, 1.0])

A = np.array([[10., -1., 1., 0.],
              [1., 10., 1., -1.],
              [1., -1., 10., 0.],
              [0., 1., -1., 10.]])
b = np.array([11., 10., 11., 10.])

# print("System of equations:")
# for i in range(A.shape[0]):
#     row = ["{0:3g}*x{1}".format(A[i, j], j + 1) for j in range(A.shape[1])]
#     print("[{0}] = [{1:3g}]".format(" + ".join(row), b[i]))

x = np.zeros_like(b)
iter = 0
for it_count in range(1, ITERATION_LIMIT):
    x_new = np.zeros_like(x)
    iter += 1
    # print("Iteration {0}: {1}".format(it_count, x))
    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x_new[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]

    if np.allclose(x, x_new, rtol=1e-8):
        break
    x = x_new
print("Iterations:", iter)
print("Answer: ", x)


# error = np.dot(A, x) - b
# print("Error: {0}".format(error))
