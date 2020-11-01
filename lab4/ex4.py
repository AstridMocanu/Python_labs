import os
import sys


def extensii2():
    director=sys.argv[1]
    l=os.listdir(director)
    x=[]
    x=[x[x.index(".")+1:] for x in l if x.__contains__(".") and x.index(".")+1<len(x)-1 ]
    x=set(x)
    #y=[x for elem in x]
    y = list(set(x))
    y.sort()
    return y

print (extensii2())