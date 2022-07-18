'''package whatever #do not write package name here '''
class Node:
	def __init__(self):
		self.data = 0;
		self.next = None;
		self.child = None;

# A function to create a linked list
# with n(size) Nodes returns head pointer
def createList(arr, n):
	head = None;
	tmp = None;

	# Traversing the passed array
	for i in range(n):

		# Creating a Node if the list
		# is empty
		if (head == None):
			tmp = head = Node();
		else:
			tmp.next = Node();
			tmp = tmp.next;
		
		# Created a Node with data and
		# setting child and next pointer
		# as NULL.
		tmp.data = arr[i];
		tmp.next = tmp.child = None;
	
	return head;

# To print linked list
def printMultiLevelList(head):

	# While head is not None
	while (head != None):
		if (head.child != None):
			printMultiLevelList(head.child);
		
		print(head.data, end=" ");
		head = head.next;
	
# Driver code
if __name__ == '__main__':
	arr1 = [ 1, 2, 3 ];
	arr2 = [ 5, 6] ;
	arr3 = [ 4 ];
	arr4 = [ 7, 8, 9] ;

	# creating Four linked lists
	# Passing array and size of array
	# as parameters
	head1 = createList(arr1, 3);
	head2 = createList(arr2, 2);
	head3 = createList(arr3, 1);
	head4 = createList(arr4, 3);

	# Initializing children and next pointers
	# as shown in given diagram
	head1.child = head2;
	head1.next.next.child = head3;
	head2.next.child = head4;

	# Creating a None pointer.
	head = None;
	head = head1;

	# Function Call to print
	printMultiLevelList(head);

# This code is contributed by umadevi9616

