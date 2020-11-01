def frecv(a):
    d=dict()
    for c in a:
        d[c]=d.get(c,0)+1

    return d

print(frecv("parametru "))