l = []

def push_q(s, e):
    s.append(e)
    return s


def pop_q(s):
    return s.pop(0)


l = push_q(l, 1)
l = push_q(l, 2)

print(l)

print(pop_q(l))