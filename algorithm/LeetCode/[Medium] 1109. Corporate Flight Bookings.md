1109. Corporate Flight Bookings

There are `n` flights, and they are labeled from `1` to `n`.

We have a list of flight bookings.  The `i`-th booking `bookings[i] = [i, j, k]` means that we booked `k` seats from flights labeled `i` to `j` inclusive.

Return an array answer of length `n`, representing the number of seats booked on each flight in order of their label.

 

**Example 1:**
```
Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
```

**Constraints:**

* `1 <= bookings.length <= 20000`
* `1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000`
* `1 <= bookings[i][2] <= 10000`

# Submissions
---
**Solution 1: (Prefix Sum)**
```
Runtime: 1000 ms
Memory Usage: 27.8 MB
```
```python
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        
        for booking in bookings:
            i, j, k = booking
            # mark all the i and js to the res
            res[i-1] = k + res[i-1]
            try: # handling the index out of range problem, can use "if" instead
                res[j] = res[j] - k 
            except:
                continue
        
        # calculate the accumulative sum
        for i in range(1, len(res)):
            res[i] = res[i-1] + res[i]
        return res
```