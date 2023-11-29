import Benefits
import Annuities

leeftijd = 25
lengteContract = 5

b1 = 0.1 / 100
b2 = 0.001 / 100
i = 4.75 / 100
C = 12 / 100

r = 1 / 100
start = 500

mPay = 2
mGetPayed = 12


def KO(t, x, m, n, rente):
    return 8500


def KL(t, x, m, n, rente):
    return start * (1 + r) ** t


def const1(t, x, m, n, rente):
    return 1


benefit = (Benefits.TermMtly(leeftijd, mPay, lengteContract, i - b1, KO)
           + Annuities.TermAnnuityMtlyDue(leeftijd, mPay, lengteContract, i-b1, KL))
annuity = Annuities.TermAnnuityMtlyDue(leeftijd, mGetPayed, lengteContract, i - b1, const1)
inventaris = KO(0, leeftijd, mGetPayed, lengteContract, i-b1)*b2 * annuity

UP = (benefit + inventaris) / (1 - C)
PP = UP / annuity

som = 0
for k in range(0, lengteContract):
    som = som + KL(k, leeftijd, mPay, lengteContract, i-b1)

print("UP: " + str(UP))
print("PP: " + str(PP))
print("mtly payments: " + str(PP/mGetPayed))