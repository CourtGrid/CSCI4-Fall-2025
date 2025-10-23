def main(x,y,z):
    print(x,y,z)

l=[1,2,3,4,5]
i=[0,1,2,3,4]
main("hello", l[i[4]], l[i[3]])
# l[i[4]] tells us the value of the list l at i index 4. 
# In this scenario (unless i changed it) the value is 5
# If you change the values of i, the output of main will
# change in some weird way that I still don't fully understand.