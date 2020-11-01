import os


def fisier_director(my_path):
    #if fis -> ultimele 20 caractere
    # elif dir -> lista (extensie,count)\
    try:
        #sau os.path.isfile
        f=open(my_path,"rt")
        x=[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1]
        i=0
        for line in f:
            for c in line.strip():
                if i==19:
                    i=0
                x[i]=c
                i+=1
                x[20]=i #semnaleaza cat ma rescris
        f.close()
        return x[x[20]:]+x[:x[20]-1]
    except (FileNotFoundError,FileExistsError,PermissionError):
        #practic.. daca este director
        #sau os.path.isdir
        l=[]
        l=os.listdir(my_path)
        x=[x[x.index(".")+1:] for x in l if x.index(".")+1<len(x)-1]
       # x.sort()
        y=x
        y=set(x)
        dictionar=dict()
        for elem in y:
            dictionar[elem]=x.count(elem)
        return dictionar.items()
    except:
        return "nu se poate efectua niciuna dintre operatii"

print(fisier_director("C:\\Users\Astrid\PycharmProjects\lab4"))

