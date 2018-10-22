"""
Remove Duplicates: Write code to remove duplicated from an unsorted linked list. Solve the problem without temporary
buffer
"""

from data_structures.linkedList import LinkedList,Node

def deleteDuplicates_1(list):
    head = list.head
    duplicates = set()
    prev = head
    duplicates.add(head.data)
    head = head.next
    while head is not None:
        if head.data in duplicates:
            prev.next = head.next
        else:
            duplicates.add(head.data)
            prev = head
        head = head.next

def removeDuplicated(list):
    current = list.head
    while current is not None:
        runner = current
        while runner.next is not None:
            if current.data == runner.next.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next



list = LinkedList()
list.addMany([1,2,1,1,3,2])

removeDuplicated(list)
result = LinkedList()
result.addMany([1,2,3])

print(list.checkList(result))
