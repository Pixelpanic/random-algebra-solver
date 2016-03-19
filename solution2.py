#Solving  a primary school algebra problem using random
# AB - CD = EF + GH = PPP

import random
import timeit

#Counting loop times and script runtime
start = timeit.default_timer()
counter = 0

# Init with random numbers
a, b, c, d, e, f, g, h, p = random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9),random.randint(0, 9)


#Validates all the numbers are never repeats and meet the equation requirements
def check(a,b,c,d,e,f,g,h,p):
    if a in (b, c, d, e, f, g, h, p):
        return True
    elif b in (a, c, d, e, f, g, h, p):
        return True
    elif c in (a, b, d, e, f, g, h, p):
        return True
    elif d in (a, c, b, e, f, g, h, p):
        return True
    elif e in (a, c, d, b, f, g, h, p):
        return True
    elif f in (a, c, d, e, b, g, h, p):
        return True
    elif g in (a, c, d, e, f, b, h, p):
        return True
    elif h in (a, c, d, e, f, g, b, p):
        return True
    elif p in (a, c, d, e, f, g, h, b):
        return True
    elif (a*10 + b) - (c*10+d) <= 0:
        return True
    elif (a*10 + b) - (c*10 + d) != (e*10 + f):
        return True
    elif (e*10 + f) + (g*10 + h) != (p*100 + p* 10 + p):
        return True
    else:
        return False

while check(a,b,c,d,e,f,g,h,p) == True:

    a, b, c, d, e, f, g, h, p = random.randint(1, 9),random.randint(0, 9),random.randint(1, 9),random.randint(0, 9),random.randint(1, 9),random.randint(0, 9),random.randint(1, 9),random.randint(0, 9),random.randint(0, 9)
    counter += 1

stop = timeit.default_timer()

print "Final Result", a, b, c, d, e, f, g, h, p, "Random:", counter, "Times"
print " AB : ", a, b
print "-CD : ", c, d
print "    = ", e, f
print " EF   ", e, f
print "+GH : ", g, h
print "    = ", p, p, p
print "Validation - AB-CD:", (a*10 + b) - (c*10 + d), "=", (e*10 + f), "EF+GH:", (e*10+f) + (g*10+h), "=", (p*100+p*10+p)
print "Finished in :", stop - start
