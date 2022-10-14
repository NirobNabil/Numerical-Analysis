
import time
import pandas
import sympy  

threshold = 0.5*(10**-2)
x = sympy.Symbol('x')
equation = ""
eq = ""


def eq(x):
    return eval(equation)

def error_calc( xnew, xold ):
    return abs( ( xnew - xold ) / xnew )


def getxm( xl, xu ):
    return ( xu*eq(xl) - xl*eq(xu) ) / ( eq(xl) - eq(xu) )


def recurse( xip, xipp ):

    xi = xip - ( ( eq(xip) * (xip - xipp) ) / ( eq(xip) - eq(xipp) ) )

    error = error_calc( xi, xip )
    # print( eq(xm), eq(xip) )
    return ( error, xi )


def secant( eqn, xi, xip ):

    global eq
    eq = sympy.lambdify( x, eval(eqn) )

    # xi = 0.05
    # xip = 0.02
    it = 1

    table = []

    error = 10000000

    # input( "Enter the equation:" )

    while( error > threshold ):
        ( error, xi_new ) = recurse( xi, xip )

        table.append( [ it, xi_new, xi, xip,  error*100, eq(xi_new) ] )
        it = it+1
        time.sleep(0.1)
        xip = xi
        xi = xi_new


    data = pandas.DataFrame(table, columns=['iteration', 'xi', 'xi-1', 'xi-2', 'e0%', 'f(xi)'], index=['']*len(table))
    data = data.round(4)

    return data