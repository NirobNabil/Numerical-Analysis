from util import *

# mat = Matrix([
#     [5., 3., 5.],
#     [4., 1., 3.],
# ])

mat = Matrix([
    [25., 5., 1., 106.8],
    [64., 8., 1., 177.2],
    [144., 12., 1., 279.2]
])

mat_val = Matrix([
    [106.8],
    [177.2],
    [279.2]
]) 


def upper_triangular(mat):
    mat = Matrix( mat.mat )
    rows = mat.row_count()
    for row in range(0,rows-1):
        for i in range(row, rows-1):
            mat[i+1] = mat[i+1] - ( mat[row] * ( mat[i+1][row] / mat[row][row] ) )

    return mat



def elimination( mat ):
    
    mat = upper_triangular(mat)
    
    rows = mat.row_count()
    
    roots = [ 0 for i in range(rows) ]

    roots[rows-1] = mat[rows-1][rows] / mat[rows-1][rows-1]

    for i in range(rows-2, -1, -1):
        right_side = mat[i][rows]
        for ix in range(len(roots)):
            right_side -= mat[i][ix] * roots[ix] 
        roots[i] = right_side / mat[i][i]


    return roots



print( elimination(mat) )
        



