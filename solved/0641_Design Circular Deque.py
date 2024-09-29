# region Quest
#Design your implementation of the circular double-ended queue (deque).
#
#Implement the MyCircularDeque class:
#
#MyCircularDeque(int k) Initializes the deque with a maximum size of k.
#boolean insertFront() Adds an item at the front of Deque. Returns True if the operation is successful, or False otherwise.
#boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
#boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
#boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
#int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
#int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
#boolean isEmpty() Returns true if the deque is empty, or false otherwise.
#boolean isFull() Returns true if the deque is full, or false otherwise.
# 
#
#Example 1:
#
#Input
#["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
#[[3], [1], [2], [3], [4], [], [], [], [4], []]
#Output
#[null, true, true, true, false, 2, true, true, true, 4]
#
#Explanation
#MyCircularDeque myCircularDeque = new MyCircularDeque(3);
#myCircularDeque.insertLast(1);  // return True
#myCircularDeque.insertLast(2);  // return True
#myCircularDeque.insertFront(3); // return True
#myCircularDeque.insertFront(4); // return False, the queue is full.
#myCircularDeque.getRear();      // return 2
#myCircularDeque.isFull();       // return True
#myCircularDeque.deleteLast();   // return True
#myCircularDeque.insertFront(4); // return True
#myCircularDeque.getFront();     // return 4
# 
#
#Constraints:
#
#1 <= k <= 1000
#0 <= value <= 1000
#At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.
# endregion


import time
from typing import Optional, List

class MyCircularDeque:

    def __init__(self, k: int):
        self.Deck = [None for _ in range(0,k)]
        self.front = 0
        self.rear = 0
        self.cap = [0,k]

    def insertFront(self, value: int) -> bool:
        if self.cap[0] == self.cap[1]:
            return False
        if self.Deck[self.front] == None:
            self.Deck[self.front] = value
            self.cap[0] += 1
            return True
        if self.front==0:
            self.front=self.cap[1]-1
        else:
            self.front -= 1
        self.Deck[self.front] = value
        self.cap[0] += 1
        return True
        
    def insertLast(self, value: int) -> bool:
        if self.cap[0] == self.cap[1]:
            return False
        if self.Deck[self.rear] == None:
            self.Deck[self.rear] = value
            self.cap[0] += 1
            return True
        if self.rear==self.cap[1]-1:
            self.rear=0
        else:
            self.rear += 1
        self.Deck[self.rear] = value
        self.cap[0] += 1
        return True

    def deleteFront(self) -> bool:
        if self.Deck[self.front]==None:
            return False
        
        self.Deck[self.front] = None
        self.cap[0] -= 1
        if self.front==self.cap[1]-1:
            self.front = 0
        elif self.cap[0]==0:
            self.rear = self.front
        else:
            self.front += 1
        return True
        
    def deleteLast(self) -> bool:
        if self.Deck[self.rear]==None:
            return False
        
        self.Deck[self.rear] = None
        self.cap[0] -= 1
        if self.rear==0:
            self.rear = self.cap[1] -1
        elif self.cap[0]==0:
            self.rear = self.front
        else:
            self.rear -= 1
        return True
        
    def getFront(self) -> int:
        return self.Deck[self.front] if self.Deck[self.front] != None else -1
        
    def getRear(self) -> int:
        return self.Deck[self.rear] if self.Deck[self.rear] != None else -1 
        
    def isEmpty(self) -> bool:
        return self.cap[0] == 0
        
    def isFull(self) -> bool:
        return self.cap[0] == self.cap[1]
        

operations = ["insertFront","getRear","deleteLast","getRear","insertFront","insertFront","insertFront","insertFront","isFull","insertFront","isFull","getRear","deleteLast","getFront","getFront","insertLast","deleteFront","getFront","insertLast","getRear","insertLast","getRear","getFront","getFront","getFront","getRear","getRear","insertFront","getFront","getFront","getFront","getFront","deleteFront","insertFront","getFront","deleteLast","insertLast","insertLast","getRear","getRear","getRear","isEmpty","insertFront","deleteLast","getFront","deleteLast","getRear","getFront","isFull","isFull","deleteFront","getFront","deleteLast","getRear","insertFront","getFront","insertFront","insertFront","getRear","isFull","getFront","getFront","insertFront","insertLast","getRear","getRear","deleteLast","insertFront","getRear","insertLast","getFront","getFront","getFront","getRear","insertFront","isEmpty","getFront","getFront","insertFront","deleteFront","insertFront","deleteLast","getFront","getRear","getFront","insertFront","getFront","deleteFront","insertFront","isEmpty","getRear","getRear","getRear","getRear","deleteFront","getRear","isEmpty","deleteFront","insertFront","insertLast","deleteLast"]
values = [[89],[],[],[],[19],[23],[23],[82],[],[45],[],[],[],[],[],[74],[],[],[98],[],[99],[],[],[],[],[],[],[8],[],[],[],[],[],[75],[],[],[35],[59],[],[],[],[],[22],[],[],[],[],[],[],[],[],[],[],[],[21],[],[26],[63],[],[],[],[],[87],[76],[],[],[],[26],[],[67],[],[],[],[],[36],[],[],[],[72],[],[87],[],[],[],[],[85],[],[],[91],[],[],[],[],[],[],[],[],[],[34],[44],[]]
outputs = [True,89,True,-1,True,True,True,True,False,True,False,19,True,45,45,True,True,82,True,98,True,99,82,82,82,99,99,True,8,8,8,8,True,True,75,True,True,True,59,59,59,False,True,True,22,True,98,22,False,False,True,75,True,74,True,21,True,True,74,False,63,63,True,True,76,76,True,True,74,True,26,26,26,67,True,False,36,36,True,True,True,True,87,74,87,True,85,True,True,False,74,74,74,74,True,74,False,True,True,True,True]
# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(77)

for methoden_string, wert, output in zip(operations, values, outputs):
    methode = getattr(obj, methoden_string)
    if wert != []:
        print(f'{methode(wert[0]) == output} : {methoden_string}({wert[0]})={methode(wert[0])} == {output}')
    else:
        print(f'{methode() == output} : {methoden_string}({wert})={methode()} == {output}')
