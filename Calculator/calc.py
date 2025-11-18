# I think I misunderstood the assignment.
x = 3
y = 2
o = input('INPUT OPERATION:',)
# You cannot input the values while the code is running (like you said). You can input the operation. For some reason.


def evaluate():
    if o == '+':  # If you input + while the code is running, the values will add! The - will subtract, etc. 
        return {x+y}
    if o =='-':
        return {x-y}
    if o == 'x' or '*':
        return {x*y}
    if o == '/':
        return {x/y}
# It technically calculates the values...
# The values just aren't built into the code. You have to edit to do that.

print(evaluate())
# I kept forgetting to add the parenthesis after evaluate so I spent wayyy too long trying to figure out how to get it to print. 
# I am assuming that you were supposed to have the values built into the code, and depending on what the operation was decide how it is supposed to be calculated.
# I think I am going to have another file within the calculator folder of me trying to do it right.
