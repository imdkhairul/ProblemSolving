class Node:
    def __init__(self, data=None) :
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node

    def listprint(self):
        tempNode = self.head
        while tempNode is not None:
            print(tempNode.val)
            tempNode = tempNode.next
    
    

def getLength(headNode) :
    tempNode = headNode
    count = 0
    while tempNode is not None:
        count = count + 1
        tempNode = tempNode.next

    return count
    
    
def getMiddleNode(head) :
    tempNode = head
    if tempNode is not None:
        length = getLength(tempNode)
        for x in range(int(length/2)):
            tempNode = tempNode.next
        return tempNode.data
    else :
        return -1
    
list = LinkedList()
e1 = Node(10)
e2 = Node(20)
e3 = Node(30)
e4 = Node(4)
e1.next = e2
e2.next = e3
#e3.next = e4
list.head = e1
list.listprint()
#getMiddleNode(list.head)
print(getMiddleNode(None))