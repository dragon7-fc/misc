703. Kth Largest Element in a Stream

Design a class to find the `k`th largest element in a stream. Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.

Your KthLargest class will have a constructor which accepts an integer `k` and an integer array `nums`, which contains initial elements from the stream. For each call to the method `KthLargest.add`, return the element representing the `k`th largest element in the stream.

**Example:**
```
int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
```

**Note:**

* You may assume that `nums' length ≥ k-1` and `k ≥ 1`.

# Submissions
---
**Solution 1: (Heap)**
```
Runtime: 84 ms
Memory Usage: 16.6 MB
```
```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h, self.k = nums, k
        heapq.heapify(self.h)
        while len(self.h) > self.k:
            heapq.heappop(self.h)

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        elif val > self.h[0]:
            heapq.heappushpop(self.h, val)
        return self.h[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```