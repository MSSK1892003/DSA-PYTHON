#recursion FAB series
# t=0 #time complexity of the series
# def fib(n):
#     global t
#     t+=1
    
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fib(n-1)+fib(n-2)
# if __name__=="__main__":
#     n=int(input())
#     print(fib(n))
#     print(f" time complexity = {t}") 
d={0:1,1:0,2:1}
t=0
def fib(n):
    global t
    t+=1
    if n in d:
        return d[n]
    else:
        d[n-1]=fib(n-1)
        d[n-2]=fib(n-2)
        return d[n-1]+d[n-2]
if __name__=="__main__":
    n=int(input())
    print(fib(n),t)
    
