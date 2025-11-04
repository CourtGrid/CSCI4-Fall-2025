q = [0,1,2,3,4,5]
head = 0 #The index of 0 is the front of the line

def tail(q):
    return len(q) #len is the number of elements in the queue

def push(q, e): #push: puts a new element into the queue
    q.append(e)
    return q 

def pop(q):
    return q.pop(0) #Pop: removes an element in the queue. 0 is the index that we want to remove


print(q)
print(pop(q))
print(pop(q))
