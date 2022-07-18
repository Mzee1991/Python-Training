# Python3 program to merge sort of linked list

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
	
	def append(self, new_value):
		
		new_node = Node(new_value)
		
		if self.head is None:
			self.head = new_node
			return
		curr_node = self.head
		while curr_node.next is not None:
			curr_node = curr_node.next
			
		curr_node.next = new_node
		
	def sortedMerge(self, left, right):
		sorted_list = None
		
		# Base cases
		if left == None:
			return right
		if right == None:
			return left
			
		if left.data <= right.data:
			sorted_list = left
			sorted_list.next = self.sortedMerge(left.next, right)
		else:
			sorted_list = right
			sorted_list.next = self.sortedMerge(left, right.next)
		return sorted_list
	
	def mergeSort(self, h):
		
		# Base case if head is None
		if h == None or h.next == None:
			return h

		# get the middle of the list
		middle = self.getMiddle(h)
		nexttomiddle = middle.next

		middle.next = None

		left = self.mergeSort(h)
		
		right = self.mergeSort(nexttomiddle)

		sortedlist = self.sortedMerge(left, right)
		return sortedlist
	
	# Utility function to get the middle
	# of the linked list
	def getMiddle(self, head):
		if (head == None):
			return head

		slow = head
		fast = head

		while (fast.next != None and
			fast.next.next != None):
			slow = slow.next
			fast = fast.next.next
			
		return slow
		
# Utility function to print the linked list
def printList(head):
	if head is None:
		print(' ')
		return
	curr_node = head
	while curr_node:
		print(curr_node.data, end = " ")
		curr_node = curr_node.next
	print(' ')
	
# Driver Code
if __name__ == '__main__':
	li = LinkedList()
	
	# Let us create a unsorted linked list
	# to test the functions created.
	# The list shall be a: 2->3->20->5->10->15
	li.append(15)
	li.append(10)
	li.append(5)
	li.append(20)
	li.append(3)
	li.append(2)
	
	# Apply merge Sort
	li.head = li.mergeSort(li.head)
	print ("Sorted Linked List is:")
	printList(li.head)

# TC: O(nlogn)
# SC: O(n)

