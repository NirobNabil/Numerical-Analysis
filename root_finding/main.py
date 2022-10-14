from PyInquirer import prompt, Separator
from termcolor import colored

from .false_position import *
from .bisection import *
from .newton_raphson import *
from .secant import *

def get_root():
    ans = prompt([
        {
            'type': 'list',
            'name': 'method',
            'qmark': '>>',
            'message': 'What method do you want to use?',
            'choices': [
                Separator(),
                'Bisection',
                'False Position',
                'Newton Raphson',
                'Secant',
            ]
        },
        {
            'type': 'input',
            'name': 'equation',
            'message': 'Enter left side of the equation in python\'s syntax. FORMAT: 5*x + x**3'
        }
    ])

    method = ans['method']
    eqn = ans['equation']
    if( method == 'Bisection' or method == 'False Position' ):
        data = prompt([
            {
                'type': 'input',
                'name': 'xl',
                'message': 'Enter the lower guess of x. FORMAT: x'
            },
            {
                'type': 'input',
                'name': 'xu',
                'message': 'Enter the upper guess of x. FORMAT: x'
            },
        ])

        xl = float( data['xl'] )
        xu = float( data['xu'] )

        if( method == 'Bisection' ):
            print( bisection( eqn, xl, xu ) )
        else:
            print( false_position( eqn, xl, xu ) )

    elif method == 'Newton Raphson':
        data = prompt([
            {
                'type': 'input',
                'name': 'xi',
                'message': 'Enter the first guess x. FORMAT: x'
            },
        ])

        xi = float( data['xi'] )

        print( raphson( eqn, xi ) )

    elif method == 'Secant':
        data = prompt([
            {
                'type': 'input',
                'name': 'xi',
                'message': 'Enter the first guess x. FORMAT: x'
            },
            {
                'type': 'input',
                'name': 'xip',
                'message': 'Enter the second guess x. FORMAT: x'
            },
            
        ])

        xi = float( data['xi'] )
        xip = float( data['xip'] )

        print( secant( eqn, xi, xip ) )


    