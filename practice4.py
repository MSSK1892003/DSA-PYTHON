'''you are given an integer array cards where cards[i] reprsentsthe value of the ith card.A pair of cards are matchig if the cards have the same 
value.
return the minimum number of consecutive cards you have topick up to have a pair of matching cards among the picked cards,
if it is impossible to have matching cards, return -1 
input:cards=[3,4,2,3,4,7],[3,4,5,3,2,4,2,6,6]'''
import math
n=[3,4,5,3,2,4,2,6,6]
d={}
min=math.inf
value=-1
for i in range(len(n)):
    if n[i] in d:
        temp =i-d[n[i]]
        d[i]=1
        if min >=temp:
            min = temp
            value = n[i]
    d[n[i]] =i
print(min +1,value)