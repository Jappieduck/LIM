import Benefits
import Annuities
import Algemeen
from mpmath import nsum

leeftijd = 20
lengteContract = 65 - leeftijd

b1 = 0.1 / 100
b2 = 0.001 / 100
i = 4.75 / 100
C = 12 / 100

r = 1 / 100
KO = 8500
start = 5000 / 12
print("Gemiddelde zorgkosten België: " + str(3743 / 12))

mPay = 2
mGetPayed = 2


def KL(t):
    return start * (1 + r) ** t


benefit = (Benefits.TermMtly(leeftijd, mPay, leeftijd + lengteContract, i - b1, KO)
           + nsum(lambda t: Algemeen.v(i - b1) ** (t / mPay) * Algemeen.npx(t, leeftijd) * KL(t),
                  [0, mPay * lengteContract - 1]))
annuity = Annuities.TermAnnuityMtlyDue(leeftijd, mGetPayed, lengteContract, i - b1, 1)
inventaris = b2 * annuity

UP = (benefit + inventaris) / (1 - C)
PP = UP / annuity

som = 0
for k in range(0, lengteContract):
    som = som + KL(k)

print("UP: " + str(UP))
print("PP: " + str(PP))
print("KL: " + str(som))
print("Maandelijkse betaling totaal: " + str(mGetPayed * PP * lengteContract))
print(som - UP)
