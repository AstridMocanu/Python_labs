import os
def ex6(target,to_search,callback = print):
    try:
        return cautare(target,to_search)
    except Exception as e:
        callback(e)




def cautare(target,to_search):
    if os.path.isfile(target):
        try:
            f=open(target)
            for line in f:
                if line.strip().__contains__(to_search):
                    return target
            return
        except:
            return "nu se poate deschide...sau ceva err"
    elif os.path.isdir(target):
        x=[]
        for root,dirs,files in os.walk(target):
            for name in files:
                x.append(cautare(os.path.abspath(os.path.join(root, name)),to_search,callback))
    else:
        raise ValueError("nici fis nici dir")
