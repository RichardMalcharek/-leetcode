# region Quest
#You are given two integers m and n, which represent the dimensions of a matrix.
#
#You are also given the head of a linked list of integers.
#
#Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.
#
#Return the generated matrix.
#
#Example 1:
#
#Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
#Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
#Explanation: The diagram above shows how the values are printed in the matrix.
#Note that the remaining spaces in the matrix are filled with -1.
#
#Example 2:
#
#Input: m = 1, n = 4, head = [0,1,2]
#Output: [[0,1,2,-1]]
#Explanation: The diagram above shows how the values are printed from left to right in the matrix.
#The last space in the matrix is set to -1.
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
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[None for _ in range(n) ] for _ in range(m)]
        curr = head
        counter = 0
        nums = n*m

        while nums > 0:
            for i in range(0+counter,n-counter):
                val = curr.val if curr else -1
                curr = curr.next if curr else None
                matrix[0+counter][i] = val
                nums -=1

            if nums <=0:
                break

            for j in range(1+counter,m-counter):
                val = curr.val if curr else -1
                curr = curr.next if curr else None
                matrix[j][n-1-counter]  = val
                nums -=1
            if nums <=0:
                break

            for k in range(n-counter-2,-1+counter,-1):
                val = curr.val if curr else -1
                curr = curr.next if curr else None
                matrix[m-1-counter][k]  = val
                nums -=1
            if nums <=0:
                break

            for l in range(m-counter-2,0+counter,-1):
                val = curr.val if curr else -1
                curr = curr.next if curr else None
                matrix[l][0+counter]  = val
                nums -=1
            if nums <=0:
                break

            counter += 1

        return matrix
    

solution = Solution()

m = 3
n = 5
head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
print(solution.spiralMatrix(m, n, create_listnode(head)))   #Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]

m = 1
n = 4
head = [0,1,2]
print(solution.spiralMatrix(m, n, create_listnode(head)))   #Output: [[0,1,2,-1]]