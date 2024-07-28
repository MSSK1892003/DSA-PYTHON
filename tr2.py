import os
'''with open("file.txt",'w') as f:
    f.write("hello")
    f.write("welcome to world")
    f.close()'''
'''with open("file.txt","r") as f:
    for i in f.readlines():
        print(i)'''
        
        
# replace  the name in the file
with open("demo.txt",'w') as f:
    f.write("my name is Nanjundi \n")
    f.write("i am currently in bellary \n")
    f.write("i am student of the super code batch")
    f.close()
with open("demo.txt",'r') as f:
    s=f.read()
    print(s)
    f.close()
s1=s.replace("bellary","BITM")
print(s1)   
    