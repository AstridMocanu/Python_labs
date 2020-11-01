import os
import sys


def paths_in_file(director,fisier):
    try:
        f=open("ex2.txt",mode="wt")

        for root,dirs,files in os.walk(director):
            for name in files:
                if name[0].lower()=='a':
                    f.write(os.path.abspath(os.path.join(root,name)))
                    f.write("\n")
        f.close()
    except:
        print("File could not be opened")

    #print (os.path.abspath("lab4"))


paths_in_file("C:\\Users\Astrid\PycharmProjects","C:\\Users\Astrid\PycharmProjects\lab1")