# s=input()
# op=["+","-","*","/"]
# for i in s:
#     if i in op:
#         x=i
#         s.replace(i," ")
# L=list(map(float,s.split(" ")))
# match s:
#     case '+':return L[0] + L[1]
#     case '-':print("substraction")
#     case '/':print("division")
def evaluate(exp):
    op=["+","-","*","/"]
    opr=' '
    for i in exp:
        if i in op:
            opr=i
            break
    expr = exp.split(opr)
    expr = list(map(float,expr))
    if opr == "+": return expr[0] + expr [1]
    if opr == "-": return expr[0] - expr [1]
    if opr == "*": return expr[0] * expr [1]
    if opr == "/": return expr[0] / expr [1]
    if opr == "%": return expr[0] % expr [1]
print(evaluate('3*4'))
print(evaluate('3+4'))
print(evaluate('3-4'))
print(evaluate('3/4'))