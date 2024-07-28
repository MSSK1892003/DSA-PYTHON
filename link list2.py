class Node:
    def __init__(self,data):
        self.value=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def add_end(self,data):
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=Node(data)
        return temp
    def add_first(self,data):
        temp=Node(data)
        temp.next=self.head
        self.head=temp
        return temp
    def  delete_first(self):
        temp=self.head
        self.head=self.head.next
        return temp
    def delete_last(self):
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=temp
        return temp
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.value,end="->")
            temp=temp.next
        print("none")
node1=linkedlist()
node1.add_end(20)
node1.add_first(10)
node1.add_end(30)

node1.display()

        