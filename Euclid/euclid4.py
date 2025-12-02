import math
x = -1
y = 1
q = -1
p = -1

point1 = [x,y]
point2 = [q,p]

def euclid():
    D = math.fabs(q-x)**2 + math.fabs(p-y)**2

    d = math.fabs(D**(1/2))

    return d

print(euclid())
