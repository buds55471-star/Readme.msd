from functools import reduce 

l = [1,2,543,645,67,55,87]

def greater(a,b):
    if(a>b):
        return a
    return b
    
print(reduce(greater,l))