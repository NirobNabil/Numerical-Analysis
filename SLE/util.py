
mat_arr = [
    [25, 5, 1],
    [64, 8, 1],
    [144, 12, 1]
]


class Row:
    row = []
    def __init__( self, arr ):
        self.row = arr.copy()

    def size( self ):
        return len(self.row)

    def __getitem__(self, i):
        return self.row[i]

    def __setitem__(self, i, v):
        self.row[i] = v

    def __add__( self, to_add ):

        row = self.row.copy()
        for i in range( len(row) ):
            if type(to_add) == Row:
                row[i] = row[i] + to_add.row[i]
            elif isinstance(to_add, list):
                row[i] = row[i] + to_add[i]
            elif isinstance(to_add, int) or isinstance(to_add, float):
                row[i] = row[i] + to_add
        
        return Row(row)
    
    def __sub__( self, to_sub ):
        
        row = self.row.copy()
        for i in range( len(row) ):
            if type(to_sub) == Row:
                row[i] = row[i] - to_sub.row[i]
            elif isinstance(to_sub, list):
                row[i] = row[i] - to_sub[i]
            elif isinstance(to_sub, int) or isinstance(to_mul, float):
                row[i] = row[i] - to_sub
        
        return Row(row)
        
    def __mul__(self, to_mul ):

        row = self.row.copy()
        for i in range( len(row) ):
            if type(to_mul) == Row:
                row[i] = row[i] * to_mul.row[i]
            elif isinstance(to_mul, list):
                row[i] = row[i] * to_mul[i]
            elif isinstance(to_mul, int) or isinstance(to_mul, float):
                row[i] = row[i] * to_mul
        
        return Row(row)

    def __truediv__(self, to_div):
        row = self.row.copy()
        for i in range( len(row) ):
            if type(to_div) == Row:
                row[i] = row[i] / to_div.row[i]
            elif isinstance(to_div, list):
                row[i] = row[i] / to_div[i]
            elif isinstance(to_div, int) or isinstance(to_div, float):
                row[i] = row[i] / to_div
        
        return Row(row)

    def __str__(self):
        ret = "["
        for i in self.row:
            ret = ret + f'{i:12.3f},'
        ret = ret + "  ]"
        return ret
        
    


class Matrix:

    mat = []
    def __init__( self, mat_arr ):
        mat = []
        for row in mat_arr:
            if isinstance(row, list):
                mat.append(Row(row))
            elif isinstance(row, Row):
                mat.append(Row(row.row))

        self.mat = mat

    def __getitem__(self, i):
        return self.mat[i]

    def __setitem__(self, i, v):
        self.mat[i] = v

    def __mul__(self, mul):
        new_mat = Matrix([ [ 0 for i in range(self.mat[0].size()) ] for i in range(0, self.row_count() ) ])
        mul = mul.transpose()
        for row_i in range(self.row_count()):
            for col_i in range(mul.row_count()):
                for i in range( mul[col_i].size() ):
                    new_mat[row_i][col_i] += self[row_i][i] * mul[col_i][i]
        
        return new_mat
    
    def row_count(self):
        return len(self.mat)

    def transpose( self ):
        new_mat = Matrix([ [ 0 for i in range(self.row_count()) ] for i in range(0, self.mat[0].size() ) ])
        for row_num in range(0, self.row_count()):
            for col_num in range(0, self.mat[row_num].size()):
                new_mat[col_num][row_num] = self[row_num][col_num]

        return new_mat

    def __str__(self):
        ret = ""
        for row in self.mat:
            ret += row.__str__()
            ret += "\n"
        
        return ret


# print( Matrix(mat_arr) * Matrix([[1,0,0],[0,1,0],[0,0,1]]) )