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
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution:
    def mergeKLists(self, lists: List):
        if len(lists) == 0:
            result = []
        elif len(lists) == 1:
            result = lists[0]
        else:
            for i in range(1,len(lists)):
                lists[0] = lists[0]+lists[i]
            result = sorted(lists[0])
        
        return result

solution = Solution()

lists = [[1,3,5],[2,4],[2,6,7,8,9,10,11]]
print(solution.mergeKLists(lists))                  # Output: 


lists = [[1,4,5],[1,3,4],[2,6]]
print(solution.mergeKLists(lists))                  # Output: [1,1,2,3,4,4,5,6]

lists = []
print(solution.mergeKLists(lists))                  # Output: []

lists = [[]]
print(solution.mergeKLists(lists))                  # Output: []
 