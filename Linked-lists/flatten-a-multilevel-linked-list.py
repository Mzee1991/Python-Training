# Python3 Program to flatten list with
# next and child pointers

# A linked list node has data,
# next pointer and child pointer
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.child = None

# Return Node
def newNode(data):
	return Node(data)

# The main function that flattens
# a multilevel linked list
def flattenlist(head):
	
	# Base case
	if not head:
		return
	
	# Find tail node of first level linked list
	temp = head
	while(temp.next != None):
		temp = temp.next
	currNode = head
	
	# One by one traverse through all nodes
	# of first level linked list
	# till we reach the tail node
	while(currNode != temp):
		
		# If current node has a child
		if(currNode.child):
			
			# then append the child
			# at the end of current list
			temp.next = currNode.child
			
			# and update the tail to new last node
			tmp = currNode.child
			while(tmp.next):
				tmp = tmp.next
			temp = tmp
			
		# Change current node
		currNode = currNode.next
	
# A utility function to print
# all nodes of a linked list
def printList(head):
	if not head:
		return
	while(head):
		print("{}".format(head.data), end = " ")
		head = head.next

# Driver code
if __name__=='__main__':
	
	# Child list of 13
	child13 = newNode(16)
	child13.child = newNode(3)
	
	# Child List of 10
	head1 = newNode(4)
	head1.next = newNode(20)
	head1.next.child = newNode(2) #Child of 20
	head1.next.next = newNode(13)
	head1.next.next.child = child13
	
	# Child of 9
	child9 = newNode(19)
	child9.next = newNode(15)

	# Child List of 17
	child17 = newNode(9)
	child17.next = newNode(8)
	child17.child = child9

	# Child List of 7
	head2 = newNode(17)
	head2.next = newNode(6)
	head2.child = child17
	
	# Main List
	head = newNode(10)
	head.child = head1
	head.next = newNode(5)
	head.next.next = newNode(12)
	head.next.next.next = newNode(7)
	head.next.next.next.child = head2
	head.next.next.next.next = newNode(11)

	flattenlist(head)

	print("\Flattened list is: ", end = "")
	printList(head)

# This code is contributed by 0_hero

