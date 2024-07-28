ls=[2,2,3,5,1,8,1,6,8,7,49,5,8,1,5,4,6,12,2,2,5,4,6,8,4,2,4,2,5,6,78,9,4,5,1,2,1,2,11,2,1,2,1]

max_value=max(ls)
min_value=min(ls)
count=[0]*(max_value+1)
for n in ls:
    count[n-min_value]+=1
for k in range(1,len(count)):
    count[k]+=count[k-1]
sort=[0]*len(ls)
for n in reversed(ls):
    sort[count[n-min_value]-1]=n
    count[n-min_value]-=1
print(sort)
