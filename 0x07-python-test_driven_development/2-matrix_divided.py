#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix
    Args:
        matrix: list of lists of ints/floats
        div: int/float, can't be equal to 0
    Returns:
        quotients of all elements of a matrix
    Raises:
        TypeError: if not matrix of ints and/or floats,
            or if each row of matrix is not the same size,
            or if div is not a number
        ZeroDivisionError: if div is 0
    Doctest Examples:
        see dir: /tests/2-matrix_divided.txt
    """
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if isinstance(element, (int, float)) is False:
                raise TypeError("matrix must be a matrix (list of lists)"
                                "of integers/floats")
    return [[round(element / div, 2) for element in row] for row in matrix]
