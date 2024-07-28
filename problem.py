'''s=input("enter the string")
# list=['a','A','e','E','i','I','o','O','U','u']
ca=0
ci=0
ce=0
co=0
cu=0
for i in s:
    if i == 'A' or i == "A":
        ca=ca+1
    elif i == 'E' or i == "e":
        ce=ce+1
    elif i == 'I' or i == "i":
        ci=ci+1
    elif i == 'o' or i == "O":
        co=co+1
    elif i == 'U' or i == "u":
        cu=cu+1
    else:
        pass
print(f"Aa= {ca} E,e= {ce} i,I= {ci} o,O = {co} u,U = {cu}")
0
list=[ca,ci,ce,co,cu]

print(max(list))'''

def count_vowel(s):
    dic={'A':0,'E':0,'I':0,'O':0,'U':0,}
    for i in s:
        if i == 'A' or i == "a":
            dic['A']+=1
          
        elif i == 'E' or i == "e":
            dic['E']+=1
        
        elif i == 'I' or i == "i":
            dic['I']+=1
        
        elif i == 'o' or i == "O":
            dic['O']+=1
        
        elif i == 'U' or i == "u":
            dic['U']+=1
       
        
    x=max(dic.values())
    result=[]
    for i , j in dic.items():
        if j == x:
            result.append(i)
    return result
    
i_p=[
    ["nanjundi","I am good boy"],
    ["suri","the coder surya"],
    ["manohar","miracle guy"],
    ["sampatha","coco guy"],
]
o_p={}
for i in i_p:
    o_p[i[0]]=count_vowel(i[1])
print(o_p)