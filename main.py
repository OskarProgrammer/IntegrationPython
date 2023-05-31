# calkowanie 
import matplotlib.pyplot as pyplot
import numpy
import scipy.integrate
import sympy


class Integration:
    def __init__(self, symbol):
        self.x = sympy.Symbol(symbol)
        print(sympy.integrate(pow(self.x,2)- 3*pow(self.x,3) + self.x-25, self.x))

class IntegrationWithRange(object):

    def __init__(self,symbol, xp, xk):
        self.xp = xp
        self.xk = xk
        # x = sympy.Symbol(symbol)
        self.wynik = scipy.integrate.quad(self.funkcja,self.xp,self.xk)
        print("Wynik: ",  self.wynik[0]) # wynik

    def funkcja(self,x):
        return pow(x,2)- 3*pow(x,3) + x-25# tu wstaw funkcje

    def rysowanie(self):
        self.z = numpy.linspace(self.xp-2,self.xk+1)
        pyplot.plot(self.z, self.funkcja(self.z))
        pyplot.show()

obiekt = IntegrationWithRange("x", 0, 1)
obiekt.rysowanie()