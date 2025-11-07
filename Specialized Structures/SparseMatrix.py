class SparseMatrix:
    def __init__(self):
        self.values = []
        self.row_indices = []
        self.col_indices = []

    def add_value(self, row, col, value):
        if value == 0:
            return
        self.values.append(value)
        self.row_indices.append(row)
        self.col_indices.append(col)

    def to_dense(self, rows, cols):
        dense = [[0]*cols for _ in range(rows)]
        for v, r, c in zip(self.values, self.row_indices, self.col_indices):
            dense[r][c] = v
        return dense

# Test
sm = SparseMatrix()
sm.add_value(0, 1, 5)
sm.add_value(2, 0, 3)
dense = sm.to_dense(3, 3)
assert dense == [[0,5,0],[0,0,0],[3,0,0]][web:6][web:20]
