from typing import List


def matrix_sum(mat1: List[List[float]], mat2: List[List[float]]) -> List[List[float]]:
    """
    Summarises two martices

    Args:
    mat1:List[List[float]] - first matrix
    mat2:List[List[float]] - second matrix

    Return:
    List[List[float] - matrix-result

    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Matrices must have the same shape")
    res: List[List[float]] = []
    for i in range(len(mat1)):
        row: List = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        res.append(row)
    return res


def matrix_multiply(
    mat1: List[List[float]], mat2: List[List[float]]
) -> List[List[float]]:
    """
    Multiplies two matrices

    Args:
    mat1:List[List[float]] - first matrix
    mat2:List[List[float]] - second matrix

    Return:
    List[List[float] - matrix-result

    """
    if len(mat1[0]) != len(mat2):
        raise ValueError(
            "The number of the coloumns of the first matrix must equal the number of the rows of the second matrix"
        )
    res: List[List[float]] = []
    for i in range(len(mat1)):
        row: List = []
        for j in range(len(mat2[0])):
            temp: float = 0
            for n in range(len(mat1[0])):
                temp += mat1[i][n] * mat2[n][j]
            row.append(temp)
        res.append(row)
    return res


def matrix_transpose(mat: List[List[float]]) -> List[List[float]]:
    """
    Tranposes matrix

    Args:
    mat:List[List[float]] - matrix

    Return:
    List[List[float]] - transposed matrix
    """
    if not mat:
        raise ValueError("Matrix must be non empty")
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
