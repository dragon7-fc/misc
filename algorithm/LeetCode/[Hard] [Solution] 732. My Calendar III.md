732. My Calendar III

Implement a `MyCalendarThree` class to store your events. A new event can **always** be added.

Your class will have one method, `book(int start, int end)`. Formally, this represents a booking on the half open interval `[start, end)`, the range of real numbers `x` such that `start <= x < end`.

A K-booking happens when **K** events have some non-empty intersection (ie., there is some time that is common to all K events.)

For each call to the method `MyCalendar.book`, return an integer `K` representing the largest integer such that there exists a `K`-booking in the calendar.

Your class will be called like this: `MyCalendarThree cal = new MyCalendarThree();` `MyCalendarThree.book(start, end)`

**Example 1:**
```
MyCalendarThree();
MyCalendarThree.book(10, 20); // returns 1
MyCalendarThree.book(50, 60); // returns 1
MyCalendarThree.book(10, 40); // returns 2
MyCalendarThree.book(5, 15); // returns 3
MyCalendarThree.book(5, 10); // returns 3
MyCalendarThree.book(25, 55); // returns 3
Explanation: 
The first two events can be booked and are disjoint, so the maximum K-booking is a 1-booking.
The third event [10, 40) intersects the first event, and the maximum K-booking is a 2-booking.
The remaining events cause the maximum K-booking to be only a 3-booking.
Note that the last event locally causes a 2-booking, but the answer is still 3 because
eg. [10, 20), [10, 40), and [5, 15) are still triple booked.
``` 

**Note:**

* The number of calls to `MyCalendarThree.book` per test case will be at most `400`.
* In calls to `MyCalendarThree.book(start, end)`, `start` and `end` are integers in the range `[0, 10^9]`.

# Solution
---
## Approach #1: Boundary Count [Accepted]
**Intuition and Algorithm**

When booking a new event `[start, end)`, count `delta[start]++` and `delta[end]--`. When processing the values of `delta` in sorted order of their keys, the largest such value is the answer.

In Python, we sort the set each time instead, as there is no analog to TreeMap available.

```python
class MyCalendarThree(object):

    def __init__(self):
        self.delta = collections.Counter()

    def book(self, start, end):
        self.delta[start] += 1
        self.delta[end] -= 1

        active = ans = 0
        for x in sorted(self.delta):
            active += self.delta[x]
            if active > ans: ans = active

        return ans
```
**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the number of events booked. For each new event, we traverse delta in $O(N)$ time. In Python, this is $O(N^2 \log N)$ owing to the extra sort step.

* Space Complexity: $O(N)$, the size of `delta`.

# Submissions
---
**Solution 1: (Boundary Count)**
```
Runtime: 1464 ms
Memory Usage: 12.9 MB
```
```python
class MyCalendarThree:

    def __init__(self):
        self.delta = collections.Counter()

    def book(self, start: int, end: int) -> int:
        self.delta[start] += 1
        self.delta[end] -= 1

        active = ans = 0
        for x in sorted(self.delta):
            active += self.delta[x]
            if active > ans: ans = active

        return ans


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
```

**Solution 2: (bisect.insort)**

Maintain a sorted list of (timestamp, 1 or -1) tuple where second element is 1 indicates the start of event and -1 indicates the end, note that tuples are sorted by timestamp by default. When calculating K, just tranverse the list and keep track of max number of events in one moment.
```
Runtime: 1436 ms
Memory Usage: 12.9 MB
```
```python
class MyCalendarThree:

    def __init__(self):
         self.events = []

    def book(self, start: int, end: int) -> int:
        bisect.insort(self.events, (start, 1))
        bisect.insort(self.events, (end, -1))
        
        cur = 0
        res = 0
        
        for event in self.events:
            cur += event[1]
            res = max(res, cur)
        
        return res


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
```

**Solution 3: (ordered map)**
```
Runtime: 244 ms
Memory: 6.4 MB
```
```c++
class MyCalendarThree {
    map<int,int>mp;
public:
    MyCalendarThree() {
        
    }
    
    int book(int start, int end) {
        mp[start]++;
        mp[end]--;
        int sum=0; int ans=0;
        for(auto it : mp)
        {
            sum+=it.second;
            ans=max(ans,sum);
        }
        return ans;
    }
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree* obj = new MyCalendarThree();
 * int param_1 = obj->book(start,end);
 */
```
