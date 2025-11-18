stack = [0,1,2,3,4,5]


def push(stack, e): #push: puts a new element into the stack
    stack.append(e) #Insert will put e at the top of the stack
    return stack 


def pop(stack):
    stack.pop(-1) # -1 removes the top item in the stack
    return stack


print(stack)
print(pop(stack))
print(pop(stack))




