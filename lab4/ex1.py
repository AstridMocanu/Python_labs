import os


def extensii(director):
    print(os.listdir(director))
    l=[]
    l=os.listdir(director)
    x=[x[x.index(".")+1:] for x in l if x.__contains__(".") and x.index(".")+1<len(x)-1 ]
    x=set(x)
    y=[el for el in x]
    y.sort()
    print(y)


#os.path.splittext(x)->(nume fara ext, ext cu punct)
#atentie .idea

extensii("C:\\Users\Astrid\PycharmProjects\lab1")
#print(os.listdir("C:\\Users\Astrid\PycharmProjects\lab1"))
