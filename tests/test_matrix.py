import pytest
from project.matrix_operations import matrix_multiply, matrix_sum, matrix_transpose


def test_matrix_multiply():
    m1 = [[5, 5], [9, 1]]
    m2 = [[3, 4], [8, 2]]
    assert matrix_multiply(m1, m2) == [[55, 30], [35, 38]]

    m1 = [[1, 2], [3, 4]]
    m2 = [[0, 0], [0, 0]]
    assert matrix_multiply(m1, m2) == [[0, 0], [0, 0]]


def test_incompatible_matrix_multiply():
    m1 = [[12, 54, 77, 3], [5, 0, 46, 52]]
    m2 = [[32, 11], [90, 2], [45, 18]]
    with pytest.raises(ValueError):
        matrix_multiply(m1, m2)


def test_matrix_sum():
    m1 = [[4, 2, 7], [8, 7, 9], [0, 4, 5]]
    m2 = [[13, 6, 8], [32, 55, 0], [4, 21, 5]]
    assert matrix_sum(m1, m2) == [[17, 8, 15], [40, 62, 9], [4, 25, 10]]

    m1 = [[9, 8], [4, 5]]
    m2 = [[-5, 0], [6, -15]]
    assert matrix_sum(m1, m2) == [[4, 8], [10, -10]]


def test_incompatible_matrix_sum():
    m1 = [[3, 5, 7], [0, 9, 0]]
    m2 = [[2, 8], [6, 4]]
    with pytest.raises(ValueError):
        matrix_sum(m1, m2)


def test_matrix_transpose():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert matrix_transpose(m) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    m = [[11, 5], [97, 43], [1, 0]]
    assert matrix_transpose(m) == [[11, 97, 1], [5, 43, 0]]


def test_empty_matrix_transpose():
    m = []
    with pytest.raises(ValueError):
        matrix_transpose(m)
