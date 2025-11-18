x = 3
y = 2
o = input('INPUT OPERATION:',)


def evaluate():
    if o == '+':
        return {x+y}
    if o =='-':
        return {x-y}
    if o == 'x' or '*':
        return {x*y}
    if o == '/':
        return {x/y}

print(evaluate())
