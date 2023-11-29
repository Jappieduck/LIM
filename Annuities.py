from Algemeen import v, d, delta, dp, ip, npx
import Benefits
from math import e
from mpmath import nsum, quad, inf


def AnnuityCertainDue(n, rente, annuity):
    return annuity(n, rente) * (1 - v(rente) ** n) / d(rente)


def AnnuityCertainImmediate(n, rente, annuity):
    return annuity(n, rente) * (1 - v(rente) ** n) / rente


def AnnuityCertainCont(n, rente, annuity):
    return annuity(n, rente) * (1 - v(rente) ** n) / delta(rente)


def AnnuityCertainDueMtly(n, m, rente, annuity):
    return annuity(n, m, rente) * (1 - v(rente) ** n) / dp(m, rente)


def AnnuityCertainImmediateMtly(n, m, rente, annuity):
    return annuity(n, m, rente) * (1 - v(rente) ** n) / ip(m, rente)


def WholeLifeAnnuityDue(x, rente, annuity):
    return annuity(x, rente) * (1 - Benefits.WholeLifeAnnual(x, rente, 1)) / d(rente)


def TermAnnuityDue(x, n, rente, annuity):
    return annuity(x, n, rente) * (nsum(lambda t: v(rente) ** t * npx(t, x), [0, n - 1]))


def WholeLifeAnnuityImmediate(x, rente, annuity):
    return annuity(x, rente) * (WholeLifeAnnuityDue(x, rente, 1) - 1)


def TermAnnuityImmediate(x, n, rente, annuity):
    return nsum(lambda t: v(rente) ** t * npx(t, x) * annuity(t, x, n), [0, n])


def WholeLifeContinuousAnnuity(x, rente, annuity):
    return quad(lambda t: e ** (-delta(rente) * t) * npx(t, x) * annuity(t, x, rente), [0, inf])


def TermContinuousAnnuity(x, n, rente, annuity):
    return quad(lambda t: e ** (-delta(rente) * t) * npx(t, x) * annuity(t, x, n, rente), [0, n])


def WholeLifeAnnuityMtlyDue(x, m, rente, annuity):
    return (1 / m) * nsum(lambda t: v(rente) ** (t / m) * npx(t / m, x) * annuity(t, x, m, rente), [0, inf])


def WholeLifeAnnuityMtlyImmediate(x, m, rente, annuity):
    return WholeLifeAnnuityMtlyDue(x, m, rente, annuity) - (annuity(x, m, rente) / m)


def TermAnnuityMtlyDue(x, m, n, rente, annuity):
    return (1 / m) * nsum(lambda t: v(rente) ** (t / m) * npx(t / m, x) * annuity(t, x, m, n, rente), [0, m * n - 1])


def TermAnnuityMtlyImmediate(x, m, n, rente, annuity):
    return TermAnnuityMtlyDue(x, m, n, rente, annuity) - (annuity(x, m, n, rente) / m) * (1 - v(rente) ** n * npx(n, x))


def DeferredWholeLifeAnnuityDue(u, x, rente, annuity):
    return WholeLifeAnnuityDue(x, rente, annuity) - TermAnnuityDue(x, u, rente, annuity)


def DeferredTermDueAnnuity(u, x, n, rente, annuity):
    return TermAnnuityDue(x, n, rente, annuity) - TermAnnuityDue(x, u, rente, annuity)


def DeferredTermImmediateAnnuity(u, x, n, rente, annuity):
    return TermAnnuityImmediate(x, n, rente, annuity) - TermAnnuityImmediate(x, u, rente, annuity)


def DeferredAnnuityDueMtly(u, m, x, rente, annuity):
    return WholeLifeAnnuityMtlyDue(x, m, rente, annuity) - TermAnnuityMtlyDue(x, m, u, rente, annuity)
