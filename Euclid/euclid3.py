
import math

point1 = [-1,1] #Wanted to try storing them as actual coordinate points
point2 = [-1,-1]

def euclid():
   
    A = point2[0]-point1[0] #don't need the absolute value BECAUSE they are being squared

    B = point2[1]-point1[1]

    d = (A*A) + (B*B)

    distance = math.sqrt(d)
    return distance

print(euclid())
