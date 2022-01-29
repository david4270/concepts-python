# File handling, OS module, multiprocessing and multithreading, socket

import os

def main():
    #os.getcwd - get current directory
    dir = os.getcwd()
    print(dir)
    
    #os.path.join - joins two strings to make path
    expdir = os.path.join(dir,"example project")

    #os.path.exists - finds if the directory exists
    if(not(os.path.exists(expdir))):
        #os.mkdir - makes directory
        os.mkdir("example project")
    
    #Read/Write file
    # w - write file, r - read file, a - append file
    f = open("example project\demo.txt","w")
    f.write("Glory Glory Tottenham Hotspur\nGlory Glory Tottenham Hotspur\nGlory Glory Tottenham Hotspur\nAnd the Spurs go marching on\n")
    f.close()

    f = open("example project\demo.txt","r")
    t = f.read()
    print(t)
    f.close()

    f = open("example project\demo.txt","a")
    f.write("\nTottenham are the greatest team that the world has ever seen\nTottenham are the greatest team that the world has ever seen\nTottenham are the greatest team that the world has ever seen\nAnd the Spurs go marching on\n")
    f.close()

    f = open("example project\demo.txt","r")
    t = f.read()
    print(t)
    f.close()

    #Another way of file handling
    with open("example project\demo2.txt","w") as f2:
        f2.write("hello\n")
    
    #os.listdir - lists directory
    print(os.listdir(expdir))
    
    #os.path.getsize - gets size
    sz = os.path.getsize(os.path.join(expdir,"demo.txt"))
    print("demo.txt is",sz,"Bytes")

    sz = os.path.getsize(os.path.join(expdir,"demo2.txt"))
    print("demo2.txt is",sz,"Bytes")

    #os.remove - removes file
    os.remove("example project\demo.txt")
    os.remove("example project\demo2.txt")

    if(os.path.exists(expdir)):
        #os.rmdir - removes directory
        os.rmdir("example project")
        print("Removed directory")
    
    #os.name prints name of os - if runs in windows 11, returns 'nt'
    print(os.name)

    

if __name__ == "__main__":
    main()