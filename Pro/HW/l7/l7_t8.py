from typing import List


def transpose_matrix(matrix):
    """
    Транспонує матрицю.

    >>> transpose_matrix([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]
    """
    return list(map(list, zip(*matrix)))


def matrix_multiply(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    """
    Помноження 2-х матриць.
    >>> matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]
    >>> matrix_multiply([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
    [[58, 64], [139, 154]]
    >>> matrix_multiply([[1, 2]], [[3], [4]])
    [[11]]
    >>> matrix_multiply([[1]], [[1]])
    [[1]]
    """
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Кількість стовпців першої матриці повинно дорівнювати кількості строк другої матриці.")

    result = []
    for i in range(len(matrix1)):
        row_result = []
        for j in range(len(matrix2[0])):
            row_result.append(sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))))
        result.append(row_result)

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
