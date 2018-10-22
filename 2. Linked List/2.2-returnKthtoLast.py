"""
Implement an algorithm to find the kth to last element of a singly linked list.
k =1 means last element and k=2 is second to last element, so on.
"""

# Approach 1: write all the elements in the list and return the kth to last
# Approach 2: use 2 pointers which are k distance apart
from data_structures.linkedList import LinkedList

def kthtolast_1(list,k):
    head = list.head
    list_val = []
    while head is not None:
        list_val.append(head.data)
        head = head.next
    return list_val[-k]

def kthtolast_2(list,k):
    first = list.head
    second = first
    for i in range(k):
        second = second.next
    while second is not None:
        second = second.next
        first = first.next
    return first.data


list= LinkedList()
list.addMany([1,2,3,4,5])
assert kthtolast_1(list,2) == 4
assert kthtolast_2(list,2) == 4
assert kthtolast_2(list,) == -1
