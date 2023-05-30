from jacobi import jacobi
import matrix_norm
import numpy as np

if __name__ == "__main__":
    a = np.array([[2, -1, 0],
                  [-1, 2, -1.],
                  [0, -1, 2.]])

    # a = np.array([[-4, -1, 0],
    #               [-1, -10, -1.],
    #               [0, -1, -2.]])

    # a = np.array([[2, -1, 0],
    #               [-1, 2, -1.],
    #               [0, -1, -2.]])

    print("matrix")
    print(a)
    print()
    print("jacobi")
    print(jacobi(a))

    print("matrix")
    print(a)

    print("max_matrix_norm")
    print(matrix_norm.max_matrix_norm(a))

    print("invert_matrix")
    invert = matrix_norm.plu_inverse(a)
    print(invert)

    print("max_matrix_norm_invert")
    print(matrix_norm.max_matrix_norm(invert))

    print("get_condition_number")
    print(matrix_norm.get_condition_number(a))

