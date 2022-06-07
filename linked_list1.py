#!/usr/python3

class node:
    def __init__(self, name=None, age=None, sex=None):
        self.name = name
        self.age = age
        self.sex = sex
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, name, age, sex):
        new_node = node(name, age, sex)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        cur_node = self.head
        while cur_node is not None:
            if cur_node != self.head:
                print("Name: {}\nAge: {}\nSex: {}\n".format(
                    cur_node.name, cur_node.age, cur_node.sex))
            cur_node = cur_node.next

    def get(self, index):
        if index >= self.length():
            print("Error: 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        print("Member at index {}:".format(index))
        while cur_node is not None:
            cur_node = cur_node.next
            if cur_idx == index:
                print("Name: {}\nAge: {}\nSex: {}\n".format(
                    cur_node.name, cur_node.age, cur_node.sex))
            cur_idx += 1

    def delete(self, index):
        if index >= self.length():
            print("ERROR: 'Delete' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while cur_node is not None:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1


my_list = linked_list()
my_list.append('Zeus Amadis', 1, 'Male')
my_list.append('Katia Ramona', 3, 'Female')
my_list.append('Immy', 30, 'Female')
my_list.append('Kyojo', 30, 'Male')
my_list.append('Lilly', 29, 'Female')

# leng = my_list.length()
# print("Linked list length {}".format(leng))

my_list.display()
my_list.get(4)
my_list.delete(4)
my_list.display()
