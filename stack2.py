'''
-------------Paranthesis checking---------
A student is given a task to create some mathematical expression for BODMAS.but due to some other work he forget to do that but in the night
he clicked that he have to create some expression for BODMAS due to sleepy mood he did some mistake while putting the brackets.
you job is to check ehether the expression given by that boy is nvalid or not
sample input:
[3=7{52/11(3+5)}] valid expression as all the brackets are properly
open and close:
[4-6{235(9+6)] in validexpression as some brackets are not proper
'''
class stack:
    def __init__(self):
        self.items=[]
        
    def push(self,data):
        self.items.append(data)
        
    def pop(self):
        return self.items.pop()
string=input()
stack = stack()
flag=0
for i in string:
    if i=='[' or i=='{' or i=='(':
        stack.push(i)
    if i==']' or i=='}' or i==')':
        x=stack.pop()
        if x=="(" and i == ")":
            pass
        elif x=="[" and i == "]":
            pass
        elif x=="{" and i == "}":
            pass
        else:
            flag = 1
            
            break
if flag==0  :
    print("valid")
else:
    print("invalid")
    


            
    
    
    