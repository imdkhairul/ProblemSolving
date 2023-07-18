class Node:
    def __init__(self, data=None) :
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node

    def listprint(self):
        tempNode = self.head
        while tempNode is not None:
            print(tempNode.data)
            tempNode = tempNode.next

def reverseLinkedList(head) :
    current = head
    prev = None
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    
    head = prev
    return head

def reverseLinkedListV2(head,newHead) :
    if head is None:
        return newHead
    next = head.next
    head.next = newHead
    return reverseLinkedListV2(next,head)

list = LinkedList()
e1 = Node(10)
e2 = Node(20)
e3 = Node(30)
e4 = Node(40)
e5 = Node(50)
e1.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
list.head = e1
#list.listprint()

list.head = reverseLinkedListV2(list.head,None)
list.listprint()