# import heapq
# # l=[3,2,4,6,1,5,8]
# l=[10,20,30,40,50,70,80,55,65,72,82,91,92,85,81]
# l.append(101)
# # heapq.heapify(l)
# heapq.heapify(l)
# print(l)
class head:
    def __init__(self):
        self.heap=[]
    
    def parent(self,index):
        return index//2
    
    def Rightchild(self,index):
        return (index//2)+1
    
    def leftchild(self,index):
        return index//2
    
        