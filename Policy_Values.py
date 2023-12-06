import matplotlib.pyplot as plt
import numpy as np
import Benefits
import Annuities

mPay = 2
mGetPayed = 12
i = 3.75 / 100
b1 = 0.1 / 100


def const1(t, x, m, n, rente):
    return 1


def tVn(start, t, n, KO, KL, premium):
    return Benefits.EndowMtly(start + t, mPay, n - t, i - b1, KO, KL) - premium * Annuities.TermAnnuityMtlyDue(start + t, mGetPayed, n-t, i - b1, const1)


def plotting(x, n, KO, KL, premium):
    t = range(0, n+1)
    values = []
    for k in t:
        values.append(tVn(x, k, n, KO, KL, premium))
    print(values[0])
    print(values[-1])
    plt.scatter(t, values)
    plt.xlabel("t")
    plt.ylabel("Policy Value")
    plt.show()
