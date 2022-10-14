from PyInquirer import prompt, Separator
from termcolor import colored

from .lu_decomposition import *
from .util import * 
from .gaussian_elimination import * 

def get_matrix():
    ans = prompt( [ 
        {
            'type': 'input',
            'name': 'dim',
            'message': 'enter the dimension of your matrix. FORMAT: NxM'
        }
    ] )

    dim = ans['dim'].split('x')

    # if int(dim[0])+1 != int(dim[1]):
    #     raise FatalError('Number of columns must be one greater than number of rows')

    dim = int(dim[0])

    ans = prompt( [ 
        {
            'type': 'input',
            'name': 'row-'+str(i),
            'message': f'Enter the {i}-th row of matrix. FORMAT: x1, x2, x3, ... , x4 ',
        } for i in range(dim)
    ]  )

    mat = []
    for i in range(dim):
        row = map( lambda x : float(x),  ans['row-'+str(i)].split(',') )
        mat.append(list(row))

    return Matrix( mat )


def solve_equations():
    ans = prompt([
        {
            'type': 'list',
            'name': 'method',
            'qmark': '>>',
            'message': 'What method do you want to use?',
            'choices': [
                Separator(),
                'Gaussian Elimination',
                'Gaussian Elimination with partial pivoting',
                'LU Decomposition',
            ]
        },
    ])

    mat = get_matrix()

    print('\n')

    roots = []

    if ans['method'] == 'Gaussian Elimination':
        roots = elimination(mat)
    elif ans['method'] == 'Gaussian Elimination with partial pivoting':
        roots = elimination_pivoting(mat)
    elif ans['method'] == 'LU Decomposition':
        roots = lu(mat)

    print(colored('roots = ','yellow'), colored( Row(roots), 'green') )


def solve_inverse_matrix():
    mat = get_matrix()

    print( colored(get_inverse(mat), 'green') )


def solve_L_U_matrices():

    mat = get_matrix()
    (matU, matL) = get_matrices(mat)

    print(colored("Matrix U:","white"))
    print(colored(matU, "green"))

    print(colored("Matrix L:","white"))
    print(colored(matL,"green"))
