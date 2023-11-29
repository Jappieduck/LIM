import math
from scipy.integrate import quad
import numpy

l = 100000
A = 0.00022
B = 2.7 * 10 ** (-6)
c = 1.124


def mux(x):
    return A + B * (c ** x)


def tpx(t, x):
    return math.e ** ((-A * t) - ((B * (c ** x) * (c ** t - 1)) / math.log(c, math.e)))


def lx(x):
    if x == 20:
        return l
    else:
        return tpx(1, x - 1) * lx(x - 1)


def mubracket(x, s, p):
    return (0.9 ** (2 - (s + p))) * mux(x+s+p)


def tpbracketx(t, x, p):
    return math.e ** (-quad(mubracket, 0, t, args=(x, p))[0])


def lbracket1(x):
    return lx(x+2) / tpbracketx(x, 1, 1)


def lbracket(x):
    return lx(x+2)/tpbracketx(2, x, 0)


print(lbracket(20))
print(lbracket1(20))
print(lx(20+2))
