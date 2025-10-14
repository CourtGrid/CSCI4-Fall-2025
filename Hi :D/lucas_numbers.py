#Check your notes for the formula
#Lucas numbers start with 2 and 1
# 0:2  1:1

def lucas(named_variable):
    l = [2, 1]  #list :D


#loop
    for n in range(2, named_variable):
        l.append(l[n-1] + l[n-2])  # <- Append gives the list space to add more values
    return l

print(lucas(6))  # <- it will print 6 lucas numbers

#finally got this to work idk how I did it