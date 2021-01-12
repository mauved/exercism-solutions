class Matrix:
    """
    MAAATRIX
    """

    def __init__(self, matrix_string):
        """
        Initialize the matrix using matrix string.
        The matrix is implemented as a list of lists.
        """
        matrix = []
        for line in matrix_string.splitlines():
            row = []
            for number in line.split():
                row.append(int(number))
            matrix.append(row)

        self.matrix = matrix

    def row(self, index):
        """
        Returns the row at given index.
        Note: row indices begin at 1
        """
        return self.matrix[index - 1]

    def column(self, index):
        """
        Returns the column at a given index.
        """
        column = []
        for row in self.matrix:
            column.append(row[index - 1])

        return column
