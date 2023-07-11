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
    
def geMiddleNodeV2(head) :
    fast = head.next
    slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow.data
    
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
#getMiddleNode(list.head)
print(geMiddleNodeV2(list.head))