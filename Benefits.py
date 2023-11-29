from Algemeen import delta, npx, mux, tuqx, v
from math import e
from mpmath import nsum, inf, quad


def WholeLifeCont(x, rente, KO):
    return quad(lambda t: e ** (-delta(rente) * t) * npx(t, x) * mux(x + t) * KO(t, x, rente), [0, inf])


def WholeLifeAnnual(x, rente, KO):
    return nsum(lambda t: v(rente) ** (t + 1) * tuqx(t, 1, x) * KO(t, x, rente), [0, inf])


def WholeLifeMtly(x, m, rente, KO):
    return nsum(lambda t: v(rente) ** ((t + 1) / m) * tuqx(t / m, 1 / m, x) * KO(t, m, rente), [0, inf])


def TermCont(x, n, rente, KO):
    return quad(lambda t: e ** (-delta(rente) * t) * npx(t, x) * mux(x + t) * KO(t, n, rente), [0, n])


def TermAnnual(x, n, rente, KO):
    return nsum(lambda t: v(rente) ** (t + 1) * tuqx(t, 1, x) * KO(t, n, rente), [0, n - 1])


def TermMtly(x, m, n, rente, KO):
    return nsum(lambda t: v(rente) ** ((t + 1) / m) * tuqx(t / m, 1 / m, x) * KO(t, x, m, n, rente), [0, n * m - 1])


def PureEndow(n, x, rente, KL):
    return KL(n, x, rente)*v(rente)**n * npx(n, x)


def EndowCont(n, x, rente, KO, KL):
    return TermCont(x, n, rente, KO) + PureEndow(n, x, rente, KL)


def EndowAnnual(x, n, rente, KO, KL):
    return TermAnnual(x, n, rente, KO) + PureEndow(n, x, rente, KL)


def EndowMtly(x, m, n, rente, KO, KL):
    return TermMtly(x, m, n, rente, KO) + PureEndow(n, x, rente, KL)


def DefferedTermCont(u, x, n, rente, KO):
    return quad(lambda t: e ** (-delta(rente) * t) * npx(t, x) * mux(x + t) * KO(t, u, x, n, rente), [u, u+n])
