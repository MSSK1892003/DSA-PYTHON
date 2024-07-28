"""
I a tyre  factory many workers are working  there each workers is assigned with a integer number which help them to find their supervisor
the project manager having an array that consist of a integer numbers help the project manager to find their supervisors.
supervisors will be assigned as the first largest integer find on the right side of the array if not found return -1.
i/p:[3,5,2,14,5,3,7,9,4,6,9,4,2,5,3]
0/p:[5,14,14,-1,7,7,9,-1,9,9-1,5,5,-1,-1]
    """
class queue:
    def __init__(self):
        self.item=[]
    def push(self,data):
        self.item.append(data)
    def pop(self):
        return self.item.pop(0)
    def size(self):
        return len(self.item)
# l=[3,5,2,14,5,3,7,9,4,6,9,4,2,5,3]
# o=[0]*len(l)
# s=queue()
# for i in range(len(l)-1,-1,-1):
#     while s.size() !=0 and s.top()<=l[i]:
#         if s.top()<=l[i]:
#             s.pop()
#     if s.size()==0:
#         o[i]=-1
#     else:
#         o[i]=s.top()
#     s.push(l[i])
# print(o)