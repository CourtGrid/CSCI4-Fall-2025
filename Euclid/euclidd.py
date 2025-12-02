# The distance formula is 
import math



def euclid (x,y,q,p):

    if q > x: #Might want to do something like this to determine the quadrant it is in?
        A = math.fabs(q-x) #The absolute value of these two numbers

    if p > y:
        B = math.fabs(p-y)

    a = pow(A, 2)

    b = pow(B, 2)

    d = a+b

    distance = math.sqrt(d)
    return distance

print(euclid(1,1,2,2))