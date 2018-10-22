"""
This file is creating the class for linked list and using these for the upcoming problems
"""

class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

    def __repr__(self):
        return str(self.data)


class LinkedList:

    def __init__(self, data = None):
        self.head = None

    def __repr__(self):
        root = self.head
        li = []
        while root is not None:
            li.append(root.data)
            root = root.next
        return str(li)

    def addTail(self, item):
        current = self.head
        if current:
            while current.next is not None:
                current = current.next
            current.next = Node(item)
        else:
            self.head = Node(item)

    def addMany(self,data):
        for i in data:
            self.addTail(i)

    def checkList(self, sec_list):
        head1 = self.head
        head2 = sec_list.head
        while head1 is not None and head2 is not None:
            if head1.data != head2.data:
                return False
            head1 = head1.next
            head2 = head2.next
        if head1 is None and head2 is None:
            return True
        return False

# list = LinkedList()
# list.addTail(1)
# list.addMany([2,3,4,5])
#
# list2 = LinkedList()
# list2.addMany([1,2,3])

# print(list.checkList(list2))
# print(list)



