def f(x,y,z):
  if (z==0):
    print("sum",x+y)
  elif (z==1):
    print("difference", abs(x-y))
  else:
    print("z =/= {0,1}")

f(1,2,0)

f(1,2,1)

f(1,2,5)
