import Benefits
import Annuities

leeftijd = 20
lengteContract = 65-leeftijd

b1 = 0
b2 = 0
i = 3.75 / 100
C = 0

r = 1 / 100
start = 500

mPay = 2
mGetPayed = 12


def KO(t, x, m, n, rente):
    return 8500


def KL(n, x, rente):
    return KO(1, 1, 1, 1, 1) * (1 + r) ** lengteContract


def const1(t, x, m, n, rente):
    return 1


benefit = Benefits.EndowMtly(leeftijd, mPay, lengteContract, i - b1, KO, KL)
annuity = Annuities.TermAnnuityMtlyDue(leeftijd, mGetPayed, lengteContract, i - b1, const1)
inventaris = KO(0, leeftijd, mGetPayed, lengteContract, i - b1) * b2 * annuity

UP = (benefit + inventaris) / (1 - C)
PP = UP / annuity

print("Starting age: " + str(leeftijd))
print("KO: " + str(KO(1, 1, 1, 1, 1)))
print("KL: " + str(KL(lengteContract, leeftijd, i - b1)))
print("UP: " + str(UP))
print("PP: " + str(PP))