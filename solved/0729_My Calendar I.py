# region Quest
#You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.
#
#A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).
#
#The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.
#
#Implement the MyCalendar class:
#
#MyCalendar() Initializes the calendar object.
#boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
# endregion

# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]
# Constraints:
#
# 0 <= start < end <= 109
# At most 1000 calls will be made to book.
#
# start <= x < end

import random

class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for s,e in self.bookings:
            if not (start >= e or end <= s):
                return False
        self.bookings.append([start, end])
        return True

dates = [[10, 20], [15, 25], [20, 30]]
obj = MyCalendar()
for pair in dates:
    param_1 = obj.book(pair[0],pair[1])
    print(param_1)

#dates = [[97,100],[33,51],[89,100],[83,100],[75,92],[76,95],[19,30],[53,63],[8,23],[18,37],[87,100],[83,100],[54,67],[35,48],[58,75],[70,89],[13,32],[44,63],[51,62],[2,15]]
#      
#obj = MyCalendar()
#for pair in dates:
#    param_1 = obj.book(pair[0],pair[1])
#    print(param_1)
#
#
#
#dates = [[x, x + random.randint(1, 20)] for x in [random.randint(1, 20) for _ in range(1000)]]
#      
#obj = MyCalendar()
#for pair in dates:
#    param_1 = obj.book(pair[0],pair[1])
#    print(param_1)
