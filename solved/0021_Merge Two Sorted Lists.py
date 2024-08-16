# region Quest
#You are given the heads of two sorted linked lists list1 and list2.
#
#Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
#Return the head of the merged linked list.
#
# 
#
#Example 1:
#
#
#Input: list1 = [1,2,4], list2 = [1,3,4]
##Output: [1,1,2,3,4,4]
#Example 2:
#
#Input: list1 = [], list2 = []
#Output: []
#Example 3:
#
#Input: list1 = [], list2 = [0]
#Output: [0]
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
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        stack = []
        result = ListNode(0)
        pointer = result
        
        while list1 or list2:
            num1 = list1.val if list1 else None
            num2 = list2.val if list2 else None
            if num1 is not None:
                stack.append(num1) 
            if num2 is not None:
                stack.append(num2) 

            current = min(stack)
            stack.remove(current)
            pointer.next = ListNode(current)
            pointer = pointer.next

            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None

        while len(stack) >0:
            current = min(stack)
            stack.remove(current)
            pointer.next = ListNode(current)
            pointer = pointer.next

        return result.next

solution = Solution()
timesum = 0
tries = 1
for x in range(tries):
    start_time = time.time()

    l1 = create_listnode([1,2,4])
    l2 = create_listnode([1,3,4])
    print(solution.mergeTwoLists(l1,l2))    # 1,1,2,3,4,4
    

    l1 = create_listnode([])
    l2 = create_listnode([])
    print(solution.mergeTwoLists(l1,l2))    # ''

    l1 = create_listnode([])
    l2 = create_listnode([0])
    print(solution.mergeTwoLists(l1,l2))    # 0

    end_time = time.time()
    timesum += end_time - start_time

print()
print(f'average runtime: {format(round(timesum/tries,10),".10f")}')