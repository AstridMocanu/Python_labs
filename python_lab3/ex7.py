def to_string(a):
    string = "{"
    for i in a:
        string += str(i) + ","
    string += "}"
    return string


def operations_dict(*s):
    d = dict()
    i=0
    for a in s:
        i+=1
        j=0
        for b in s:
            j+=1
            if i<j:
                d[to_string(a) + "|" + to_string(b)] = a | b
                d[to_string(a) + "&" + to_string(b)] = a & b
                d[to_string(a) + "-" + to_string(b)] = a - b
                d[to_string(b) + "-" + to_string(a)] = b - a
    return d


print(operations_dict({1, 2}, {2, 3},{2,4}))
