# region Quest
#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# 
#
#Example 1:
#
#
#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.
#Example 2:
#
#Input: l1 = [0], l2 = [0]
#Output: [0]
#Example 3:
#
#Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
#Output: [8,9,9,9,0,0,0,1]
# endregion

import time
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

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = 0
        result = ListNode(0)
        pointer = result


        while l1 or l2 or stack:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            current = num1 + num2 + stack
            num = current % 10
            stack = current // 10

            pointer.next = ListNode(num)
            pointer = pointer.next
        
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next


        
        
        
        
#        l1 = [str(x) for x in l1][::-1]
#        xl1 = int("".join(l1))
#
#        l2 = [str(x) for x in l2][::-1]
#        l2 = int("".join(l2))
#
#        l3 = str(l2 + l1)
#        result = [int(digit) for digit in l3]
#        result = result[::-1]
#
#
#        return result
    

solution = Solution()
timesum = 0
tries = 1
for x in range(tries):
    start_time = time.time()

    l1 = create_listnode([2,4,3]) 
    l2 = create_listnode([5,6,4])
    print(solution.addTwoNumbers(l1,l2))

    l1 = create_listnode([0])
    l2 = create_listnode([0])
    print(solution.addTwoNumbers(l1,l2))

    l1 = create_listnode([9,9,9,9,9,9,9])
    l2 = create_listnode([9,9,9,9])
    print(solution.addTwoNumbers(l1,l2))


    end_time = time.time()
    timesum += end_time - start_time

print()
print(f'average runtime: {format(round(timesum/tries,10),".10f")}')