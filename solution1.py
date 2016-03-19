#Solving a primary school algebra problem using random
# ABCD * 9 = DCBA

import random

abcd = random.randint(1000,1111)
dcba = 0
counter = 0

def reverse(num):
  return int(str(num)[::-1])


while abcd * 9 != dcba:
    abcd = random.randint(1000,1111)
    dcba = reverse(abcd)
    counter += 1

print "Sloved! ABCD =", abcd, 'x 9 = ', dcba, "counter:", counter
