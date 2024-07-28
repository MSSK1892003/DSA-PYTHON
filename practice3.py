'''
Given an integer array your task is to find the k continious digits which gives you the maximum sum ,where k is entered by user

sample output:
[2,4,3,5,6,3,4,6,7,1,2,5]
output:[4,6,7]
'''
'''list=[2,4,3,5,6,3,4,6,7,1,2,5]
sum=max=0
for i in range(0,len(list)-2):
    sum=list[i]+list[i+1]+list[i+2]
    if max<=sum:
        
       max=sum
       pos=i
       
print(max,list[pos],list[pos+1],list[pos+2])'''

#for k contribute:
l=[2,4,3,5,6,3,4,6,7,1,2,5]
window=max=0
k=int(input("enter the no of continious digits="))

for j in range(0,k):
    window+=l[j]
for i in range(0,len(l)-k):
    if max<window:
        max=window
        pos=i
    window=window+l[i+k]-l[i]
print("result")
print(max)

for j in range(0,k):
    print(l[pos+j])
    
'''l = [2, 4, 3, 5, 6, 3, 4, 6, 7, 1, 2, 5]
k = int(input("Enter the number of continuous digits: "))

# Initialize variables
max_sum = 0
window_sum = 0
pos = 0

# Check if k is valid
if k > len(l) or k <= 0:
    print("Invalid window size")
else:
    # Calculate the sum of the first window
    for j in range(k):
        window_sum += l[j]

    max_sum = window_sum

    # Slide the window across the list
    for i in range(1, len(l) - k + 1):
        window_sum = window_sum - l[i - 1] + l[i + k - 1]
        if window_sum > max_sum:
            max_sum = window_sum
            pos = i

    print(f"The maximum sum is {max_sum} starting at position {pos}")'''
