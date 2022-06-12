#!/usr/python3

class Node:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    # insert node at the front
    def insert_front(self, name, age, sex):

        new_node = Node(name, age, sex)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_after(self, prev_node, name, age, sex):
        if (self.head == None):
            return
        if (prev_node != 0):
            cur_node = self.head
            for i in range(prev_node - 1) and cur_node is not None:
                cur_node = cur_node->next
            if cur_node == None:
                return None
        new_node = Node(name, age, sex)
        if new_node == None:
            return None
        new_node->name = name
        new_node->age = age
        new_node->sex = sex
        if prev_node == 0:
            new_node->next = self.head
            self.head->prev = new_node
            self.head = new_node
        new_node.next = cur_node.next
    cur_node.next = new_node
        new_node.prev = cur_node
        if new_node.next:
            new_node.next.prev = new_node

    def insert_end(self, name, age, sex):
        new_node = Node(name, age, sex)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        return

    def deleteNode(self, dele):
        if self.head is None or dele is None:
            return
        if self.head == dele:
            self.head = dele.next
        if dele.next is not None:
            dele.next.prev = dele.prev
        if dele.prev is not None:
            dele.prev.next = dele.next

    def display_list(self):
        cur_node = self.head
        while cur_node is not None:
            print("Name: {}\nAge: {}\nSex: {}\n".format(
                cur_node.name, cur_node.age, cur_node.sex))
            last = cur_node
            cur_node = cur_node.next


# initialize an empty node
my_list = DoublyLinkedList()

my_list.insert_end("Mzee John", 30, "Male")
my_list.insert_front("Mukasa Joseph", 27, "Male")
my_list.insert_front("Cecilia Tusingwire", 24, "Female")
my_list.insert_end("Charles Mwesige", 32, "Male")

my_list.insert_after(2, "Aaron", 20, "Male")

my_list.insert_after(0, "Karungi", 23, "Female")

my_list.display_list()

my_list.deleteNode(my_list.head.next.next.next.next.next)

print()
my_list.display_list()
