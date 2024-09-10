# region Quest
#Given the head of a linked list head, in which each node contains an integer value.
#Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.
#Return the linked list after insertion.
#The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
#
#Example 1:
#
#Input: head = [18,6,10,3]
#Output: [18,6,6,2,10,1,3]
#Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
#- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
#- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
#- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
#There are no more adjacent nodes, so we return the linked list.
#
#Example 2:
#
#Input: head = [7]
#Output: [7]
#Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
#There are no pairs of adjacent nodes, so we return the initial linked list.
# 
#
#Constraints:
#
#The number of nodes in the list is in the range [1, 5000].
#1 <= Node.val <= 1000
# endregion


import time
from typing import Optional, List

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
            print(f'{list.val} -> ', end='')
            list = list.next
        print()
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = head

        while previous.next:
            n, m = previous.val, previous.next.val
            while m != 0:
                n, m = m, n%m
            newNode = ListNode(n)
            newNode.next = previous.next
            previous.next = newNode

            previous = previous.next.next
        
        return head


solution = Solution()

head = [18,6,10,3]
ListNode.printNod(solution.insertGreatestCommonDivisors(create_listnode(head)))    # Output: [18,6,6,2,10,1,3]

head = [7]
ListNode.printNod(solution.insertGreatestCommonDivisors(create_listnode(head)))    # Output: [7]