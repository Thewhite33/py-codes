class LinkedList:
    def __init__(self,val,nxt=None):
        self.val=val
        self.nxt=nxt
def insertAtBeginning(head:LinkedList,val):
    temp=LinkedList(val)
    temp.nxt=head
    head=temp
    return temp
def insertAtEnd(head:LinkedList,val):
    temp=LinkedList(val)
    if head is None:
        return temp
    curr=head
    while curr.nxt:
        curr=curr.nxt
    curr.nxt=temp
    return head

def removeFirstNode(head:LinkedList):
    head=head.nxt
    return head

def display(head:LinkedList):
    curr=head
    while curr:
        print(curr.val,end=" ")
        curr=curr.nxt
    print()

Head=None
while True:
    choice=int(input("Enter operation number: "))
    if choice==1:
        val=int(input("Enter value to insert: "))
        Head=insertAtBeginning(Head,val)
    elif choice==2:
        val=int(input("Enter value to insert at end: "))
        Head=insertAtEnd(Head,val)
    elif choice==3:
        Head=removeFirstNode(Head)
    elif choice==4:
        display(Head)
    elif choice==5:
        break