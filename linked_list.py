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
                print("Name: {}\nAge: {}\nSex: {}\n".format(cur_node.name,
                                                            cur_node.age, cur_node.sex))
            cur_node = cur_node.next


my_list = linked_list()
my_list.append('Zeus Amadis', 1, 'Male')
my_list.append('Katia Ramona', 3, 'Female')
my_list.append('Immy', 30, 'Female')
my_list.append('Kyojo', 30, 'Male')

# leng = my_list.length()
# print("Linked list length {}".format(leng))

my_list.display()
