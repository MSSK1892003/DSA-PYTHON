"""A financial service company ,Futureinvest, uses advanced mathematical models to forecast market trands and make investment decidions>
one of the models they use is based on the fibonacci sequence due to its relevance in technical analysis,
particularly in identifying retrcement levels and predicting future price movemennts"""
n=int(input("enter the no of terms="))
a=0
b=1
c=a+b
if n==1:
    print(a)
elif n==2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for i in range(2,n):
      print(c)
      a=b
      b=c
      c=a+b