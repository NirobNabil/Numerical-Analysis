
import time
import pandas
import sympy

threshold = 0.5*(10**-2)
x = sympy.Symbol('x')
equation = ""
eq = ""

# def eq(x):
#     return sympy.lambdify(x, equation)
    # return x**3 - 0.165*(x**2) + 3.993 * (10**-4)


def error_calc( xnew, xold ):
    return abs( ( xnew - xold ) / xnew )


def getxm( xl, xu ):
    return ( xu*eq(xl) - xl*eq(xu) ) / ( eq(xl) - eq(xu) )


def recurse( xl, xu, xip, xm ):

    error = error_calc( xm, xip )
    # print( eq(xm), eq(xip) )
    if( error > threshold ):
        if( eq(xm)*eq(xl) < 0 ):
            return ( xl, xm )
        else:
            return ( xm, xu )
    else:
        return (xm, xm )



def false_position(eqn,xl,xu):
    # xl = 0
    # xu = 0.11
    global eq
    eq = sympy.lambdify( x, eval(eqn) )

    xm = xu
    it = 1

    table = []

    table.append( [ it, xl, xu, xm, 'N/A', eq(xm) ] )

    while( xl != xu ):
        xip = xm
        xm = getxm( xl, xu )
        ( xl, xu ) = recurse( xl, xu, xip, xm )

        it = it+1
        table.append( [ it, xl, xu, xm, error_calc( xm, xip )*100, eq(xm) ] )
        print( [ it, xl, xu, xm, error_calc( xm, xip )*100, eq(xm) ] )

        # time.sleep(0.1)


    data = pandas.DataFrame(table, columns=['iteration', 'xl', 'xu', 'xm', 'e0%', 'f(xm)'], index=['']*len(table))
    data = data.round(4)

    return data