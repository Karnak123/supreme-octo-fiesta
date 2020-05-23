class Matricx:
    def __init__(self, mat):
        """Matricx constructor

        # Arguments
            self: reference to self
            mat: input matrix

        # Returns
            None

        # Raises
            TypeError: In case input is not a 2-D list"""
        try:
            self._n_row = len(mat)
            self._n_col = len(mat[0])
            self._mat = mat
            if self.n_row == self.n_col:
                self._square_mat = True
            else:
                self._square_mat = False
        except TypeError:
            raise TypeError('Expected 2-D list')
