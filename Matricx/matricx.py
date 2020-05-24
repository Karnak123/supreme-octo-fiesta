class Matricx:
    def __init__(self, mat):
        """Matricx constructor
        :argument
            self: reference to self
            mat: input matrix

        :returns
            None

        :raises
            TypeError: In case input is not a 2-D list"""
        try:
            self._n_row = len(mat)
            self._n_col = len(mat[0])
            self._mat = mat
            if self._n_row == self._n_col:
                self._square_mat = True
            else:
                self._square_mat = False
        except TypeError:
            raise TypeError('Expected 2-D list')

    def __repr__(self):
        """Returns matrix
        :argument
            self: reference to self

        :returns
            self._mat: matrix"""
        return self._mat

    def __add__(self, other):
        """Dunder to add two matrices
        :argument
            self: reference to self
            other: reference to other

        :returns
            mat: matrix holding summation of two matrices

        :raises
            ValueError: if shape of self not equals shape of other"""
        if [self._n_row, self._n_col] == other.get_shape():
            mat = []
            for i in range(self._n_row):
                temp1 = []
                for j in range(self._n_col):
                    temp1.append(self._mat[i][j] + other.get_element(i, j))
                mat.append(temp1)
            return mat
        else:
            raise ValueError('Matrix shape mismatch')

    def __sub__(self, other):
        """Dunder to subtract two matrices
        :argument
            self: reference to self
            other: reference to other

        :returns
            mat: matrix holding resultant of subtraction of two matrices

        :raises
            ValueError: if shape of self not equals shape of other"""
        if [self._n_row, self._n_col] == other.get_shape():
            mat = []
            for i in range(self._n_row):
                temp1 = []
                for j in range(self._n_col):
                    temp1.append(self._mat[i][j] - other.get_element(i, j))
                mat.append(temp1)
            return mat
        else:
            raise ValueError('Matrix shape mismatch')

    def __mul__(self, other):
        """Dunder to perform multiplication
        :argument
            self: reference to self
            other: reference to other

        :returns
            mat: Resultant of scalar or matrix multiplication, depending on other is scalar or matrix"""
        if type(other) == list:
            self.mul(other)
        else:
            self.scalar_mul(other)

    def get_shape(self):
        """Returns shape of matrix
        :argument
            self: reference to self

        :returns
            [self._n_row, self._n_col]: list with first argument number of rows, second argument number of columns"""
        return [self._n_row, self._n_col]

    def get_element(self, row, column):
        """Returns element at specific position of matrix
        :argument
            self: reference to self
            row: row
            column: column

        :returns
            self._mat[row][column]: element at position (row, column) of matrix

        :raises
            IndexError: if position not in matrix"""
        if row < self._n_row and column < self._n_col:
            return self._mat[row][column]
        else:
            raise IndexError('Desired position unavailable in matrix')

    def scalar_mul(self, n):
        """Performs scalar multiplication
        :argument
            self: reference to self
            n: scalar

        :returns
            mat: Resultant matrix"""
        mat = []
        for i in range(self._n_row):
            temp = []
            for j in range(self._n_col):
                temp.append(n * self._mat[i][j])
            mat.append(temp)
        return mat

    def mul(self, other):
        """Performs matrix multiplication
        :argument
            self: reference to self
            other: reference to other

        :returns
            Resultant matrix

        :raises
            ValueError: if self._n_col not equal other._n_row"""
        other_shape = other.get_shape()
        if self._n_col == other_shape[0]:
            return [[sum(a * b for a, b in zip(A_row, B_col))
                     for B_col in zip(*other)]
                    for A_row in self._mat]
        else:
            raise ValueError('Matrix shape mismatch')

    def transpose(self):
        """Transposes matrix
        :argument
            self: reference to self

        :returns
            mat: Transpose matrix"""
        mat = []
        for j in range(self._n_col):
            temp = []
            for i in range(self._n_row):
                temp.append(self._mat[i][j])
            mat.append(temp)
        return mat

    def trace(self):
        """Returns trace of square matrix
        :argument
            self: reference to self

        :returns
            s: trace of matrix

        :raises
            """
        if self._square_mat:
            s = 0
            for i in range(self._n_row):
                s = s + self._mat[i][i]
            return s
        else:
            raise ValueError('Square matrix expected')
