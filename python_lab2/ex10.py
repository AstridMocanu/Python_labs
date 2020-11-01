def spectacol(scaune):


    locuri_proaste = list()
    for j in range(0, len(scaune[0])):
        maxx=0
        for i in range(0,len(scaune)):
            if i > 0:
                if(scaune[i][j]<=maxx):
                    locuri_proaste.append((i, j))
                else:
                    maxx=scaune[i][j]

    return locuri_proaste


print(spectacol([[1, 2, 3, 2, 1, 1],
                 [2, 4, 4, 3, 7, 2],
                 [5, 5, 2, 5, 6, 4],
                 [6, 6, 7, 6, 7, 5]]))
