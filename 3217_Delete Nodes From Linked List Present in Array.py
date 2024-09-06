# region Quest
#You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.
#
#Example 1:
#
#Input: nums = [1,2,3], head = [1,2,3,4,5]
#Output: [4,5]
#Explanation:
#Remove the nodes with values 1, 2, and 3.
#
#Example 2:
#
#Input: nums = [1], head = [1,2,1,2,1,2]
#Output: [2,2,2]
#Explanation:
#Remove the nodes with value 1.

#Example 3:
#
#Input: nums = [5], head = [1,2,3,4]
#Output: [1,2,3,4]
#Explanation:
#No node has value 5.
# endregion


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
            print(list.val, end='')
            list = list.next
        print()
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        search = set(nums)
        current = head
        previous = None

        while current and current.val in search:
            head = current.next
            current = head

        # Jetzt iteriere durch die Liste und entferne die Knoten, deren Werte in nums sind
        while current:
            if current.val in search:
                previous.next = current.next  # Überspringe den aktuellen Knoten
            else:
                previous = current  # Setze previous auf den aktuellen Knoten
            
            current = current.next  # Gehe zum nächsten Knoten

        return head  # Gib den modifizierten Kopf der Liste zurück


    

solution = Solution()

nums = [1,2,3]
head = [1,2,3,4,5]
head2 = create_listnode(head)
ListNode.printNod(solution.modifiedList(nums, head2))  # Output: [4,5]

nums = [1]
head = [1,2,1,2,1,2]
head2 = create_listnode(head)
ListNode.printNod(solution.modifiedList(nums, head2))  # Output: [2,2,2]

nums = [5]
head = [1,2,3,4]
head2 = create_listnode(head)
ListNode.printNod(solution.modifiedList(nums, head2))  # Output: [1,2,3,4]