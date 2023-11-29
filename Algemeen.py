from math import e, log, floor

k = 1000450.59 * 0.7 + 1000079.39 * 0.3
s = 0.999106875782 * 0.7 + 0.999257048061 * 0.3
g = 0.999549614043 * 0.7 + 0.999902624311 * 0.3
c = 1.103798111448 * 0.7 + 1.118239062025 * 0.3


def v(rente):
    return 1 / (1 + rente)


def d(rente):
    return 1 - v(rente)


def dp(p, rente):
    return p * (1 - v(rente) ** (1 / p))


def ip(p, rente):
    return ((1+rente)**(1/p)-1)*p


def delta(rente):
    return log(e, 1 + rente)


def lx(x):
    return k * (s ** x) * (g ** (c ** x))


def qx(x):
    return 1 - npx(1, x)


def dx(x):
    return lx(x) - lx(x + 1)


def tuqx(t, u, x):
    geheel1 = floor(x + t)
    geheel2 = floor(x + t + u)
    decimaal1 = x + t - geheel1
    decimaal2 = x + t + u - geheel2
    l1 = lx(geheel1) - decimaal1 * dx(geheel1)
    l2 = lx(geheel2) - decimaal2 * dx(geheel2)
    return (l1 - l2) / lx(x)


def npx(n, x):
    if n == 0:
        return 1
    else:
        geheel1 = floor(x + n)
        geheel2 = floor(x)
        decimaal1 = x + n - geheel1
        decimaal2 = x - geheel2
        l1 = lx(geheel1) - decimaal1 * dx(geheel1)
        l2 = lx(geheel2) - decimaal2 * dx(geheel2)
        return l1 / l2


def mux(x):
    geheel = floor(x)
    decimaal = x - geheel
    return qx(geheel) / npx(decimaal, geheel)