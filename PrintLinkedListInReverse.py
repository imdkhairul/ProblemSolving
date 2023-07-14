
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
 

def print_in_reverse(head):
    if head is None:
        return
    print_in_reverse(head.next)
    print(head.data)


def getNthNodeFromLast(head,n):
    if head is None:
        return
    getNthNodeFromLast(head.next,n)
    getNthNodeFromLast.count += 1
    if getNthNodeFromLast.count == n:
        print(head.data)

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

#print_in_reverse(list.head)
getNthNodeFromLast.count = 0
getNthNodeFromLast(list.head,3)