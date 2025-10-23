

def farey(named_variable):
    farey_sequence = [(0,1), (0,.5,1)]

# 0<n<1 
# a/b < a+c/b+d < c/d
# a/b + c/d = (a+c)/(b+d)

    for n in range(2, named_variable):
        