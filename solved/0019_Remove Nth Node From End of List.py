# region Quest
#Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
#Example 1:
#
#Input: head = [1,2,3,4,5], n = 2
#Output: [1,2,3,5]
#
#Example 2:
#
#Input: head = [1], n = 1
#Output: []
#Example 3:
#
#Input: head = [1,2], n = 1
#Output: [1]
# endregion


from typing import Optional


def create_listnode(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def printNod(list):
        while list:
            print(list.val, end=' -> ')
            list = list.next
        print()
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        length = 0

        while current:
            length +=1
            current = current.next
        current = head
        previous = current

        if length <= 1:
            head = None
        elif length == n:
            head = current.next
        else:
            for _ in range(length-n):
                previous = current
                current = current.next
            previous.next = current.next
        return head
    

solution = Solution()

head = [1,2]
n = 2
ListNode.printNod(solution.removeNthFromEnd(create_listnode(head),n))    # Output: [2]

head = [1,2,3,4,5]
n = 2
ListNode.printNod(solution.removeNthFromEnd(create_listnode(head),n))    # Output: [1,2,3,5]

head = [1]
n = 1
ListNode.printNod(solution.removeNthFromEnd(create_listnode(head),n))    # Output: []

head = [1,2]
n = 1
ListNode.printNod(solution.removeNthFromEnd(create_listnode(head),n))    # Output: [1]