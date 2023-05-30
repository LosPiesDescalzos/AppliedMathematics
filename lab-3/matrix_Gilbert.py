import scipy.sparse


def empty_matrix(n, m, format):
    """Пустой нулевой двумерный массив
    :param n: количество строк
    :param m: количество столбцов
    :return: python array
    """
    Matrix = scipy.sparse.__dict__[format + "_matrix"]
    return Matrix((n, m))


def generate_hilbert_matrix(k):
    """Генерирует тестовое уравнение для решения с матрицей Гильберта
    :param k: номер уравнения в последовательности
    :return: пара (A_k, F_k) для уравнения A_k * x_k = F_k
    None - если уравнение несовместно
    """
    A_k = empty_matrix(k, k, "lil")
    for i in range(k):
        for j in range(k):
            A_k[i, j] = 1.0 / (i + j + 1.0)

    return A_k.tocsr()


# k = 3
# A = generate_hilbert_matrix(k)
# print(A)