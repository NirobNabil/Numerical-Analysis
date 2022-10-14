from PyInquirer import prompt
from SLE import main as sle
from root_finding import main as rootfind
from pyfiglet import Figlet
from termcolor import colored

f = Figlet( font='slant', width=110 )

credit = colored('                                                               By Al-Mubin Nabil - 2019331084\n', 'yellow', attrs=['bold'])
description = colored('  A tool to find roots of equation and solve system of linear equations using numerical analysis methods ', 'cyan')
print(colored(f.renderText('Numerical Analysis'), 'green'), credit, description)
print('\n')



ans = prompt([
    {
        'type': 'list',
        'name': 'task',
        'qmark': '>>',
        'message': 'What do you want to do?',
        'choices': [
            'Find root of an equation',
            'Solve a system of linear equations',
            'Get LU Matrices',
            'Get inverse matrix',
        ]
    }
])



if ans['task'] == 'Solve a system of linear equations':
    sle.solve_equations()
elif ans['task'] == 'Get inverse matrix':
    sle.solve_inverse_matrix()
elif ans['task'] == 'Get LU Matrices':
    sle.solve_L_U_matrices()
elif ans['task'] == 'Find root of an equation':
    rootfind.get_root()
