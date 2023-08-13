class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None

def insert(root, val):
	if root == None:
		return Node(val)
	elif root.key < val:
		root.right = insert(root.right, val)
	elif root.key > val:
		root.left = insert(root.left, val)
	return root

def size(root):
	if root is None:
		return 0
	else:
		return 1 + size(root.left) + size(root.right)

if __name__ == '__main__':
	
	root = None

	print("Inserting Element:", 100)
	root = insert(root, 100)
	print("Inserting Element:", 50)
	root = insert(root, 50)
	print("Inserting Element:",150)
	root = insert(root, 150)
	print("Inserting Element:", 125)
	root = insert(root, 125)
	
