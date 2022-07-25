from math import acos, degrees

a = int(input("a >>> "))
b = int(input("b >>> "))
c = int(input("c >>> "))

alf_ = - (a*a - b*b - c*c) / 2 / b / c
bet_ = - (b*b - a*a - c*c) / 2 / a / c
gam_ = - (c*c - a*a - b*b) / 2 / a / b

alf = degrees(acos(alf_))
bet = degrees(acos(bet_))
gam = degrees(acos(gam_))

print("alf = %.2f, bet =  %.2f, gam = %.2f" % (alf_, bet_, gam_))
print("alf = %.2f, bet =  %.2f, gam = %.2f" % (alf, bet, gam))
