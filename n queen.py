# def is_queen(board,x,y):
# d={1:0,5:0,7:0}
# amount=18
# for i in [7,5,1]:
#     d[i]=amount//i
#     amount=amount%i
# print(d)
# def min_coins(amount,d,coin):
#     if not d:
#         print(coin)
#     for i in d:
#         value=d.pop(i)
#         min_coins(amount % i,d,coin//i)
# d={1:0,5:0,7:0}
# min_coins(18,0)
min=float('inf')
min_path=""
def min_coins(amount,d,coin,path):
    global min,min_path
    if amount<0:
        return
    if amount==0:
        if min>=coin:
            min=coin
            min_path=path
        return
    for i in d:
        min_coins(amount-i,d,coin+1,path+f',{i}.')
d={5:0,7:0,1:0}
min_coins(18,d,0,"")
print(min)
print(min_path)            