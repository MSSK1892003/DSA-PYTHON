
    

class node:
    def __init__(self,data):
        self.value=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None
    
    
    def insert_first(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
    
    def insert_last(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node
    def delete(self,data):
        curr=self.head
        prev=None
        while curr is not None:
            if curr.value==data:
                if prev is None:
                    self.head=curr.next
                else:
                    prev.next=curr.next
                return
            prev=curr
            curr=curr.next
            print(f"values {data } is not found")
    def insert_position(self,data,pos):
        new_node=node(data)
        if pos==0:
            self.insert_first(data)
        curr=self.head
        count=0
        while curr is not None and count<pos-1:
            curr=curr.next
            count+=1
        if curr is None:
            print(f"position  {pos} is out of bound")
        else:
            new_node.next=curr.next
            curr.next=new_node
            
            
    def display(self):
        curr=self.head
        while curr is not None:
            print(curr.value,end="->")
            curr=curr.next
        print("None")
node1=linked_list()
node1.insert_first(20)
node1.insert_first(10)
node1.insert_last(30)
node1.insert_last(40)


node1.display()
node1.delete(10)
node1.insert_position(25,1)
node1.display()



        
        
        
        



    
