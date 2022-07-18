# Python3 implementation to convert a given
# BST to Max Heap
i = 0
class Node:
	def __init__(self):
		self.data = 0
		self.left = None
		self.right = None

# Helper function that allocates a new node
# with the given data and None left and right
# pointers.
def getNode(data):

	newNode = Node()
	newNode.data = data
	newNode.left = newNode.right = None
	return newNode

arr = []

# Function for the inorder traversal of the tree
# so as to store the node values in 'arr' in
# sorted order
def inorderTraversal( root):

	if (root == None):
		return arr

	# first recur on left subtree
	inorderTraversal(root.left)

	# then copy the data of the node
	arr.append(root.data)

	# now recur for right subtree
	inorderTraversal(root.right)

def BSTToMaxHeap(root):

	global i
	if (root == None):
		return None

	# recur on left subtree
	root.left = BSTToMaxHeap(root.left)

	# recur on right subtree
	root.right = BSTToMaxHeap(root.right)

	# copy data at index 'i' of 'arr' to
	# the node
	root.data = arr[i]
	i = i + 1
	return root

# Utility function to convert the given BST to
# MAX HEAP
def convertToMaxHeapUtil( root):
	global i
	
	# vector to store the data of all the
	# nodes of the BST
	i = 0

	# inorder traversal to populate 'arr'
	inorderTraversal(root)

	# BST to MAX HEAP conversion
	root = BSTToMaxHeap(root)
	return root

# Function to Print Postorder Traversal of the tree
def postorderTraversal(root):

	if (root == None):
		return

	# recur on left subtree
	postorderTraversal(root.left)

	# then recur on right subtree
	postorderTraversal(root.right)

	# print the root's data
	print(root.data ,end= " ")

# Driver Code

# BST formation
root = getNode(4)
root.left = getNode(2)
root.right = getNode(6)
root.left.left = getNode(1)
root.left.right = getNode(3)
root.right.left = getNode(5)
root.right.right = getNode(7)

root = convertToMaxHeapUtil(root)
print("Postorder Traversal of Tree:" )
postorderTraversal(root)

# This code is contributed by Arnab Kundu

