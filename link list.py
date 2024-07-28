class Node:
    def __init__(self,data):
        self.value=data
        self.next=None

    
        
Head=Tail=Node(10)

Tail.next=Node(20)
Tail=Tail.next
Tail.next=Node(30)
Tail=Tail.next
Tail.next=Node(40)
Tail=Tail.next

print(Head)
print(Head.next)
print(Tail)
print(Head.next.next)
def print_link_list(Head):
    if Head==None:
        print("List is empty")
        return
    curr=Head
    while curr!=None:
        print(curr.value)
        curr=curr.next
print_link_list(Head)
new_node=Node(50)
def first_insert(Head):
    new_node=Head
    Head.next=new_node
    print(first_insert)

first_insert(Head)
    
