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

def getNthNode(head, index) :
    temp = head
    while temp is not None:
        if index == 0:
            break
        temp = temp.next
        index = index - 1
    if temp is None:
        return -1
    return temp.data
    
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
print(getNthNode(list.head,2))