# The distance formula is 
import math
x = -1
y = 1
q = -1
p = -1

point1 = (x,y)
point2 = (q,p)

def euclid():
   
    A = q-x #don't need the absolute value BECAUSE they are being squared

    B = p-y

    a = A*A

    b = B*B

    d = a+b

    distance = math.sqrt(d)
    return distance

print(euclid())
