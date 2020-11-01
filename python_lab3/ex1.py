

def make_set(a,b):
    s=[]
    s.append(set((set(a)|set(b)))) # reuniunea
    print(s)
    s.append(set((set(a)&set(b)))) # intersectia
    print(s)
    s.append(set((set(a)-set(b)))) # dif dintre a si b
    print(s)
    s.append(set((set(b)-set(a)))) # dif dintre b si a
    print(s)

    t=set()
    '''
    for i in s:
        elem=frozenset(i)
        elem=set(elem)
        t.update(elem)
        print(elem)
    '''
    #nu se poate set de ste-uri!!!!
    t = set(frozenset(i) for i in s)
    return t


print([{1,2,3},{2,3,4}])

print(make_set([2,4,6,8],[1,2,3,4,5,6,7]))