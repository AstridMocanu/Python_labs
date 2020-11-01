def comp(d1:dict, d2:dict):
    if type(d1) is not dict and type(d2) is not dict:
        return [],[]
    diff_d1_d2 = []
    diff_d2_d1 = []
    for i in d1.items():
        flag = 1
        for j in d2.items():
            if type(i) is not dict and type(j) is not dict:
                if i == j:
                    flag = 0
            else:
                if comp(i[1], j[1]) == ([], []):
                    flag = 0
        if flag == 1:
            diff_d1_d2.append(i)

    for i in d2.items():
        flag = 1
        for j in d1.items():
            if type(i) is not dict and type(j) is not dict:
                if i == j:
                    flag = 0
            else:
                if comp(i[1], j[1]) == ([], []):
                    flag = 0
        if flag == 1:
            diff_d2_d1.append(i)

        print(i)
    return diff_d1_d2, diff_d2_d1


print(comp({"key": "abab", "u": 2,"ala": {"key": "abab", "u": 2}}, {"ala": {"key": "abab", "u": 2},"u": 2,"pepa":"groh"}))
print(1 == {1})
print(comp({"a": [1, 2, 3, 1, 2, 3], "b": 1, 2: 'cvbn', 3: {'a': 1} , "set" : {1,1,2,3,3,3} , 111:111},
    {"a": [1, 2, 3, 1, 2, 3], "b": 1, 2: 'cvbn', 3: {'a': 1}, "set" : {1,2,3,} , 111:111}
))

