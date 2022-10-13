
import time
import pandas

threshold = 0.5*(10**-2)

equation = "x**3 - 0.165*(x**2) + 3.993 * (10**-4)"

def eq(x):
    return eval(equation)

def error_calc( xnew, xold ):
    return abs( ( xnew - xold ) / xnew )


def getxm( xl, xu ):
    return ( xu*eq(xl) - xl*eq(xu) ) / ( eq(xl) - eq(xu) )


def raphson( xip, xipp ):

    xi = xip - ( ( eq(xip) * (xip - xipp) ) / ( eq(xip) - eq(xipp) ) )

    error = error_calc( xi, xip )
    # print( eq(xm), eq(xip) )
    return ( error, xi )



xi = 0.05
xip = 0.02
it = 1

table = []

error = 10000000

# input( "Enter the equation:" )

while( error > threshold ):
    ( error, xi_new ) = raphson( xi, xip )

    table.append( [ it, xi_new, xi, xip,  error*100, eq(xi_new) ] )
    it = it+1
    time.sleep(0.1)
    xip = xi
    xi = xi_new


data = pandas.DataFrame(table, columns=['iteration', 'xi', 'xi-1', 'xi-2', 'e0%', 'f(xi)'], index=['']*len(table))
data = data.round(4)

print( data )