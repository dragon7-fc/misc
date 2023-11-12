1845. Seat Reservation Manager

Design a system that manages the reservation state of n seats that are numbered from `1` to `n`.

Implement the `SeatManager` class:

* `SeatManager(int n)` Initializes a `SeatManager` object that will manage n seats numbered from `1` to `n`. All seats are initially available.
* `int reserve()` Fetches the **smallest-numbered** unreserved seat, reserves it, and returns its number.
* `void unreserve(int seatNumber)` Unreserves the seat with the given `seatNumber`.
 

**Example 1:**
```
Input
["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]
Output
[null, 1, 2, null, 2, 3, 4, 5, null]

Explanation
SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
seatManager.reserve();    // All seats are available, so return the lowest numbered seat, which is 1.
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.reserve();    // The available seats are [3,4,5], so return the lowest of them, which is 3.
seatManager.reserve();    // The available seats are [4,5], so return the lowest of them, which is 4.
seatManager.reserve();    // The only available seat is seat 5, so return 5.
seatManager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].
```

**Constraints:**

* `1 <= n <= 10^5`
* `1 <= seatNumber <= n`
* For each call to reserve, it is guaranteed that there will be at least one unreserved seat.
* For each call to unreserve, it is guaranteed that `seatNumber` will be reserved.
* At most 10^5 calls in total will be made to reserve and unreserve.

# Submissions
---
**Solution 1: (Heap)**
```
Runtime: 592 ms
Memory Usage: 41.2 MB
```
```python
class SeatManager:

    def __init__(self, n: int):
        self.hq = list(range(1, n+1))
        heapq.heapify(self.hq)

    def reserve(self) -> int:
        return heapq.heappop(self.hq)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.hq, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
```

**Solution 2: (Heap)**
```
Runtime: 289 ms
Memory: 148.3 MB
```
```c++
class SeatManager {
    priority_queue<int, vector<int>, greater<int>> pq;
public:
    SeatManager(int n) {
        for (int i = 0; i < n; i ++) {
            pq.push(i);
        }
    }
    
    int reserve() {
        int rst = pq.top();
        pq.pop();
        return rst+1;
    }
    
    void unreserve(int seatNumber) {
        pq.push(seatNumber-1);
    }
};

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager* obj = new SeatManager(n);
 * int param_1 = obj->reserve();
 * obj->unreserve(seatNumber);
 */
```

**Solution 3: (Min Heap (without pre-initialization))**
```
Runtime: 272 ms
Memory: 142 MB
```
```c++
class SeatManager {
    // Marker to point to unreserved seats.
    int marker;

    // Min heap to store all unreserved seats.
    priority_queue<int, vector<int>, greater<int>> availableSeats;
public:
    SeatManager(int n) {
        // Set marker to the first unreserved seat.
        marker = 1;
    }
    
    int reserve() {
        // If min-heap has any element in it, then,
        // get the smallest-numbered unreserved seat from the min heap.
        if (!availableSeats.empty()) {
            int seatNumber = availableSeats.top();
            availableSeats.pop();
            return seatNumber;
        }

        // Otherwise, the marker points to the smallest-numbered seat.
        int seatNumber = marker;
        marker++;
        return seatNumber;
    }
    
    void unreserve(int seatNumber) {
        // Push unreserved seat in the min heap.
        availableSeats.push(seatNumber);
    }
};

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager* obj = new SeatManager(n);
 * int param_1 = obj->reserve();
 * obj->unreserve(seatNumber);
 */
```

**Solution 4: (Sorted/Ordered Set)**
```
Runtime: 275 ms
Memory: 148.5 MB
```
```c++
class SeatManager {
    // Marker to point to unreserved seats.
    int marker;

    // Sorted set to store all unreserved seats.
    set<int> availableSeats;
    
public:
    SeatManager(int n) {
        // Set marker to the first unreserved seat.
        marker = 1;
    }
    
    int reserve() {
        // If the sorted set has any element in it, then,
        // get the smallest-numbered unreserved seat from it.
        if (!availableSeats.empty()) {
            int seatNumber = *availableSeats.begin();
            availableSeats.erase(availableSeats.begin());
            return seatNumber;
        }

        // Otherwise, the marker points to the smallest-numbered seat.
        int seatNumber = marker;
        marker++;
        return seatNumber;
    }
    
    void unreserve(int seatNumber) {
        // Push unreserved seat in the sorted set.
        availableSeats.insert(seatNumber);
    }
};

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager* obj = new SeatManager(n);
 * int param_1 = obj->reserve();
 * obj->unreserve(seatNumber);
 */
```
