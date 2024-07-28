# # list=[45,17,10,7,5]
list=list(map(int,input().split()))
n=len(list)
for i in range(0,n):
    swap=False
    for j in range(0,n-1-i):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print(list)
# print(min(list))
def min_value(list):
    min_value=list[0]
    for i in range(0,len(list)):
        if list[i]<min_value:
            min_value=list[i]
            
    return min_value
a=min_value(list)
print(f"printing the minimum number after sorting in the list  = = > {a}")
# maximum value after sorting
def max_value(list):
    max_value=list[0]
    for i in range(0,len(list)):
        if list[i]>max_value:
            max_value=list[i]
    return max_value
b=max_value(list)
print(f"printing the maximum number after sorting in the list  = = >  {b}")
#selection sorting
def selection_sorting(list,n):
    for j in range(0,n):

       pos=j
       min=list[j]
       for i in range (j,n):
            if list[i]<min:
                min=list[i]
                pos=i
       list[j],list[pos]=list[pos],list[j]
list=[45,17,10,7,5]
n=len(list)
selection_sorting(list,n)
print(list)
