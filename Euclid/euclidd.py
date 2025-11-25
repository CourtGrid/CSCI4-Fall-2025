# The distance formula is 
import math

def euclid (x,y,q,p):

    if q > x:
        A = q-x
        
    if p > y:
        B = p-y

    a = pow(A, 2)

    b = pow(B, 2)

    d = a+b

    distance = math.sqrt(d)
    return distance

print(euclid(1,1,2,2))