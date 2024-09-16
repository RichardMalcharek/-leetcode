# region Quest
#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#Merge all the linked-lists into one sorted linked-list and return it.
#
#Example 1:
#
#Input: lists = [[1,4,5],[1,3,4],[2,6]]
#Output: [1,1,2,3,4,4,5,6]
#Explanation: The linked-lists are:
#[
#  1->4->5,
#  1->3->4,
#  2->6
#]
#merging them into one sorted list:
#1->1->2->3->4->4->5->6
#
#Example 2:
#
#Input: lists = []
#Output: []
#
#Example 3:
#
#Input: lists = [[]]
#Output: []
# 
#
#Constraints:
#
#k == lists.length
#0 <= k <= 104
#0 <= lists[i].length <= 500
#-104 <= lists[i][j] <= 104
#lists[i] is sorted in ascending order.
#The sum of lists[i].length will not exceed 104.
# endregion


import time
from typing import Optional, List


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
    def create_listnode(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return ListNode([])
        elif len(lists) == 1:
            return lists[0]
        else:
            head_result = lists[0]
            for i in range(1,len(lists)):
                head = lists[i]

                if head_result.val > head.val:
                    stack = head_result
                    head_result = head
                    head = stack
                
                current = head
                current_result = head_result
                previous_result = current_result

                while current:
                    if current_result == None:
                        previous_result.next = current
                        current = None

                    elif current_result.val <= current.val:
                        previous_result = current_result
                        current_result = current_result.next
                    else:
                        previous = current
                        current = current.next
                        stack = current_result

                        previous_result.next = previous
                        current_result = previous_result.next
                        current_result.next = stack
            return head_result






        
    

solution = Solution()

lists = [[1,3,5],[2,4],[2,6,7,8,9,10,11]]
ListNode.printNod(solution.mergeKLists(lists))      # Output: [1,1,2,3,4,4,5,6]


lists = [[1,4,5],[1,3,4],[2,6]]
ListNode.printNod(solution.mergeKLists(lists))      # Output: [1,1,2,3,4,4,5,6]

lists = []
ListNode.printNod(solution.mergeKLists(lists))      # Output: []

lists = [[]]
ListNode.printNod(solution.mergeKLists(lists))      # Output: []
 