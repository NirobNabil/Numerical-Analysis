
import time
import pandas

threshold = 0.5*(10**-2)


def eq(x):
    return x**3 - 0.165*(x**2) + 3.993 * (10**-4)

def eqp(x):
    return 3*(x**2) - 0.33*x


def error_calc( xnew, xold ):
    return abs( ( xnew - xold ) / xnew )


def getxm( xl, xu ):
    return ( xu*eq(xl) - xl*eq(xu) ) / ( eq(xl) - eq(xu) )


def raphson( xip ):

    xi = xip - ( eq(xip) / eqp(xip) )

    error = error_calc( xi, xip )
    # print( eq(xm), eq(xip) )
    return ( error, xi )



xi = 0.05
it = 1

table = []

table.append( [ it, xi, 'N/A', eq(xi) ] )

error = 10000000

while( error > threshold ):
    ( error, xi ) = raphson( xi )

    it = it+1
    table.append( [ it, xi, error*100, eq(xi) ] )
    print( [ it, xi, error*100, eq(xi) ] )

    # time.sleep(0.1)


data = pandas.DataFrame(table, columns=['iteration', 'xi', 'e0%', 'f(xm)'], index=['']*len(table))
data = data.round(4)

print( data )