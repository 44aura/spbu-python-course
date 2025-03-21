def matrix_sum(mat1: list[list[float]], mat2: list[list[float]]) -> list[list[float]]:
    """
    Summarises two martices

    Args:
    mat1:list[list[float]] - first matrix
    mat2:list[list[float]] - second matrix

    Return:
    list[list[float] - matrix-result

    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Matrices must have the same shape")
    res: list[list[float]] = []
    for i in range(len(mat1)):
        row: list = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        res.append(row)
    return res


def matrix_multiply(
    mat1: list[list[float]], mat2: list[list[float]]
) -> list[list[float]]:
    """
    Multiplies two matrices

    Args:
    mat1:list[list[float]] - first matrix
    mat2:list[list[float]] - second matrix

    Return:
    list[list[float] - matrix-result

    """
    if len(mat1[0]) != len(mat2):
        raise ValueError(
            "The number of the coloumns of the first matrix must equal the number of the rows of the second matrix"
        )
    res: list[list[float]] = []
    for i in range(len(mat1)):
        row: list = []
        for j in range(len(mat2[0])):
            temp: float = 0
            for n in range(len(mat1[0])):
                temp += mat1[i][n] * mat2[n][j]
            row.append(temp)
        res.append(row)
    return res


def matrix_transpose(mat: list[list[float]]) -> list[list[float]]:
    """
    Tranposes matrix

    Args:
    mat:list[list[float]] - matrix

    Return:
    list[list[float]] - transposed matrix
    """
    if not mat:
        raise ValueError("Matrix must be non empty")
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
