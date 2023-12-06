import Benefits
import Annuities
import Policy_Values

b1 = 0.1 / 100
b2 = 0.001 / 100
i = 3.75 / 100
C = 12 / 100

r = 1 / 100

mPay = 2
mGetPayed = 12


def KO(t, x, m, n, rente):
    return 8500


def KL(n, x, rente):
    return KO(1, 1, 1, 1, 1) * (1 + r) ** lengteContract


def const1(t, x, m, n, rente):
    return 1


#leeftijden = [20, 40, 55]
#for leeftijd in leeftijden:
#    lengteContract = 65 - leeftijd
#    benefit = Benefits.EndowMtly(leeftijd, mPay, lengteContract, i - b1, KO, KL)
#    annuity = Annuities.TermAnnuityMtlyDue(leeftijd, mGetPayed, lengteContract, i - b1, const1)
#    inventaris = KO(0, leeftijd, mGetPayed, lengteContract, i - b1) * b2 * annuity
#    UP = (benefit + inventaris) / (1 - C)
#    PP = UP / annuity
#    print("Starting age: " + str(leeftijd))
#    print("KO: \N{euro sign}" + str(KO(1, 1, 1, 1, 1)))
#    print("KL: \N{euro sign}" + str(KL(lengteContract, leeftijd, i - b1)))
#    print("UP: \N{euro sign}" + str(UP))
#    print("PP: \N{euro sign}" + str(PP))
#    print("-----------------------")

leeftijd = 40
lengteContract = 65-leeftijd
benefit = Benefits.EndowMtly(leeftijd, mPay, lengteContract, i - b1, KO, KL)
annuity = Annuities.TermAnnuityMtlyDue(leeftijd, mGetPayed, lengteContract, i - b1, const1)
inventaris = KO(0, leeftijd, mGetPayed, lengteContract, i - b1) * b2 * annuity
UP = (benefit + inventaris) / (1 - C)
PP = UP / annuity
Policy_Values.plotting(40, 65-40, KO, KL, PP)