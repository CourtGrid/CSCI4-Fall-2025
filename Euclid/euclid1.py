import math

def euclid (x,y,q,p): #Decided I wanted to try storing the coordinates up here. The coordinates are in order...
# ...meaning that point 1 is (x,y) and point 2 is (q,p)

    A = math.fabs(q-x) #The absolute value of these two numbers

    B = math.fabs(p-y)

    if not A == 0: #Squaring it does not work when the number ends up equaling 0, so I had to add this. 
        a = pow(A, 2)
    else:
        a = 0

    if not B == 0:
        b = pow(B, 2)
    else:
        b = 0

    d = a+b

    distance = math.sqrt(d) #Another way to find the square root (which was found from the library, my bad)
    return distance

print(euclid(-1,1,-1,-1))
