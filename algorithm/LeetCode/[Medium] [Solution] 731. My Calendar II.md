731. My Calendar II

Implement a `MyCalendarTwo` class to store your events. A new event can be added if adding the event will not cause a triple booking.

Your class will have one method, `book(int start, int end)`. Formally, this represents a booking on the half open interval `[start, end)`, the range of real numbers `x` such that `start <= x < end`.

A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)

For each call to the method `MyCalendar.book`, return `true` if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: `MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)`

**Example 1:**
```
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true
Explanation: 
The first two events can be booked.  The third event can be double booked.
The fourth event (5, 15) can't be booked, because it would result in a triple booking.
The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
```

**Note:**

* The number of calls to `MyCalendar.book` per test case will be at most `1000`.
* In calls to `MyCalendar.book(start, end)`, start and end are integers in the range `[0, 10^9]`.

# Solution
---
## Approach #1: Brute Force [Accepted]
**Intuition**

Maintain a list of bookings and a list of double bookings. When booking a new event `[start, end)`, if it conflicts with a double booking, it will have a triple booking and be invalid. Otherwise, parts that overlap the calendar will be a double booking.

**Algorithm**

Evidently, two events `[s1, e1)` and `[s2, e2)` do not conflict if and only if one of them starts after the other one ends: either `e1 <= s2` OR `e2 <= s1`. By De Morgan's laws, this means the events conflict when `s1 < e2` AND `s2 < e1`.

If our event conflicts with a double booking, it's invalid. Otherwise, we add conflicts with the calendar to our double bookings, and add the event to our calendar.

```python
class MyCalendarTwo:
    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start, end):
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where NN is the number of events booked. For each new event, we process every previous event to decide whether the new event can be booked. This leads to $\sum_k^N O(k) = O(N^2)$ complexity.

* Space Complexity: $O(N)$, the size of the calendar.


## Approach #2: Boundary Count [Accepted]
**Intuition and Algorithm**

When booking a new event `[start, end)`, count `delta[start]++` and `delta[end]--`. When processing the values of `delta` in sorted order of their keys, the running sum active is the number of events open at that time. If the sum is 3 or more, that time is (at least) triple booked.

A Python implementation was not included for this approach because there is no analog to TreeMap available.

```java
class MyCalendarTwo {
    TreeMap<Integer, Integer> delta;

    public MyCalendarTwo() {
        delta = new TreeMap();
    }

    public boolean book(int start, int end) {
        delta.put(start, delta.getOrDefault(start, 0) + 1);
        delta.put(end, delta.getOrDefault(end, 0) - 1);

        int active = 0;
        for (int d: delta.values()) {
            active += d;
            if (active >= 3) {
                delta.put(start, delta.get(start) - 1);
                delta.put(end, delta.get(end) + 1);
                if (delta.get(start) == 0)
                    delta.remove(start);
                return false;
            }
        }
        return true;
    }
}
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the number of events booked. For each new event, we traverse delta in $O(N)$ time.

* Space Complexity: $O(N)$, the size of delta.

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 492 ms
Memory Usage: 13.2 MB
```
```python
class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlaps = []
        
    def book(self, start: int, end: int) -> bool:
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
```

**Solution 2: (Boundary Count)**
```
Runtime: 6588 ms
Memory Usage: 13.2 MB
```
```python
class MyCalendarTwo:

    def __init__(self):
        self.delta = collections.defaultdict(int)
        
    def book(self, start: int, end: int) -> bool:
        self.delta[start] += 1
        self.delta[end] -= 1
        active = 0
        for _, d in sorted(self.delta.items()):
            active += d
            if active >= 3:
                self.delta[start] -= 1
                self.delta[end] += 1
                return False
            
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
```

**Solution 3: (Segment Tree)**
```
Runtime: 304 ms
Memory Usage: 13.3 MB
```
```python
class treeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.double = False

class MyCalendarTwo:

    def __init__(self):
        self.root = None
        
    def book(self, start: int, end: int) -> bool:
        if start >= end:
            return False
        if not self.root:
            self.root = treeNode(start, end)
            return True
        
        OK = self.check(self.root, start, end)
        if not OK:
            return False
        self.insert(self.root, start, end)
        return True
    
    def check(self, curNode, start, end):
        if start < curNode.end and end > curNode.start: # overlap
            if curNode.double:
                return False
            right_check = left_check = True
            if end > curNode.end:
                right_check = self.check(curNode, curNode.end, end)
            if start < curNode.start:
                left_check = self.check(curNode, start, curNode.start)
            return right_check and left_check
        if curNode.end <= start: # Move right
            if not curNode.right:
                return True
            return self.check(curNode.right, start, end)
        else: # Move left
            if not curNode.left:
                return True
            return self.check(curNode.left, start, end)
    
    def insert(self, curNode, start, end):
        if start < curNode.end and end > curNode.start: # overlap
            curNode.double = True
            # Merge overlapped interval and try to insert again for non-overlapped intervals
            new_start_left, new_start_right = min(curNode.start, start), max(curNode.start, start)
            new_end_left, new_end_right = min(curNode.end, end), max(curNode.end, end)
            curNode.start, curNode.end = new_start_right, new_end_left
            if new_end_right != new_end_left:
                self.insert(curNode, new_end_left, new_end_right)
            if new_start_left != new_start_right:
                self.insert(curNode, new_start_left, new_start_right)
        elif curNode.end <= start: # Move right
            if not curNode.right:
                curNode.right = treeNode(start, end)
            else:
                self.insert(curNode.right, start, end)
        else: # Move left
            if not curNode.left:
                curNode.left = treeNode(start, end)
            else:
                self.insert(curNode.left, start, end)
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
```

**Solution 4: (event point)**
```
Runtime: 197 ms
Memory: 38.9 MB
```
```c++
class MyCalendarTwo {
    map<int, int> cnt;
public:
    MyCalendarTwo() {
        
    }
    
    bool book(int start, int end) {
        cnt[start] += 1;
        cnt[end] -= 1;
        int cur = 0;
        for (auto [_, c]: cnt) {
            cur += c;
            if (cur >= 3) {
                cnt[start] -= 1;
                cnt[end] += 1;
                return false;
            }
        }
        return true;
    }
};

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo* obj = new MyCalendarTwo();
 * bool param_1 = obj->book(start,end);
 */
```
