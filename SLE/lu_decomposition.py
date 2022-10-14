from .util import *

# mat = Matrix([
#     [5., 3.],
#     [4., 1.],
# ])

# mat_val = Matrix([
#     [5.],
#     [3.]
# ])

mat = Matrix([
    [25., 5., 1.],
    [64., 8., 1.],
    [144., 12., 1.]
])

mat_val = Matrix([
    [106.8],
    [177.2],
    [279.2]
]) 

def get_matrices(mat):
    matU = Matrix( mat.mat )
    matL = Matrix([ [ 0 for i in range(mat.row_count()) ] for i in range(0, mat[0].size() ) ])
    
    rows = mat.row_count()
    for row in range(0,rows-1):
        for i in range(row, rows-1):
            matL[i+1][row] = matU[i+1][row] / matU[row][row]
            matU[i+1] = matU[i+1] - ( matU[row] * ( matU[i+1][row] / matU[row][row] ) )

    for i in range(rows):
        matL[i][i] = 1

    return ( matU, matL )


def find_roots_from_lower_triangular( mat, mat_val ):
    rows = mat.row_count()
    
    roots = [ 0 for i in range(rows) ]

    roots[0] = mat_val[0][0] / mat[0][0]

    for i in range(1, rows):
        right_side = mat_val[i][0]
        
        for ix in range(len(roots)):
            right_side -= mat[i][ix] * roots[ix] 
        roots[i] = right_side

    return roots


def find_roots_from_upper_triangular( mat, mat_val ):
    rows = mat.row_count()
    
    roots = [ 0 for i in range(rows) ]

    roots[rows-1] = mat_val[rows-1][0] / mat[rows-1][rows-1]

    for i in range(rows-2, -1, -1):
        right_side = mat_val[i][0]
        for ix in range(len(roots)):
            right_side -= mat[i][ix] * roots[ix] 
        roots[i] = right_side / mat[i][i]

    return roots


def lu( mat ):
    
    rows = mat.row_count()

    mat_val =  [ [ mat[i][rows] ] for i in range(rows) ]
    mat_val = Matrix(mat_val)

    mat = [ [ mat[row][col] for col in range(rows) ] for row in range(rows) ]
    mat = Matrix(mat)

    (matU, matL) = get_matrices(mat)
    
    z_arr = find_roots_from_lower_triangular( matL, mat_val )
    z = Matrix( [z_arr] ).transpose()

    return find_roots_from_upper_triangular( matU, z.mat )

    


def get_inverse( mat ):

    rows = len(mat.mat)
    identity = []
    for i in range(rows):
        row = [ 0 for i in range( rows ) ]
        row[i] = 1
        identity.append( row )
    
    identity = Matrix( identity )

    res = []
    for i in range(rows):
        col = lu( mat, Matrix([identity[i]]).transpose() )
        res.append(col)
    
    res = Matrix(res)
    res = res.transpose()

    return res




