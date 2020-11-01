def list_statistics(listt):


    s=set(listt)
    l=listt.copy()

    for elem in s:
        listt.remove(elem)
    a=len(l)-len(s)
    b=len(s)
    return a,b

print(list_statistics([1,1,2,3,4,4,5,5,5,6,7,8,10,6]))

