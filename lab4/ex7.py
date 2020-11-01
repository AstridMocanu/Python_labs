import os


def funct7(path):
    try:
        f=open(path,"rb")

        can_read=can_write=False
        full_path=os.path.abspath(path)
        file_size=os.stat(path).st_size
        try:
            file_extension=os.path.splitext(path)[1]
        except:
            return "eroare la extragerea extensiei"
        if f.mode=="rb" or f.mode=="rt" or f.mode=="r":
            can_read=True
        if f.mode=="wb" or f.mode=="wt" or f.mode=="w":
            can_write=True
        #sau din stat iau st_mode ca in linux si se traduce
        f.close()
        return full_path,file_size,file_extension[1:],can_read,can_write
    except:
        return ("file cannot be used")

print(funct7("ex2.txt"))