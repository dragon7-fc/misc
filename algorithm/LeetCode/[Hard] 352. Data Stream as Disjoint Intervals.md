352. Data Stream as Disjoint Intervals

Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are `1, 3, 7, 2, 6, ...,` then the summary will be:
```
[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
```

**Follow up:**

* What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?

# Submissions
---
**Solution 1: (Binary Search)**

In this approach, we save all the intervals in their raw format i.e we are optimizing for `getIntervals`.
We internally represent the intervals as a list of intervals (as expected in the `getIntervals`. Initially this will be an empty list i.e `self._X = []`.

When we invoke a call to `addNum`, we first do a binary search of [val] on the intervals `self._X`. i.e `idx = bisect(self._X, [val])`. Our goal here is to find multiple things based on `idx`. Let's list them

1. We have to find if the leftmost bound for this val i.e as seen to the left, can be it added to an existing interval or does it warrant a new interval (keep in mind, we are only looking to the left). It warrants a new interval iff, `idx` is `0` (this means that there is no interval smaller than val) OR if the next smaller interval's end + 1 is smaller than val. .

    **Examples**

    * `self._X = [1,1], [4,4], [10,12]` and `val = 0` .. this gives `idx = 0` and we have to create a new interval for this at `0` such as that `self._X = [[0,0, [1,1],[4,4], [10,12]]`

    * If `self._X = [1,1], [4,4], [10,12]` and `val = 6`, then `idx = 2`. But we see that the interval at `idx-1` i.e `[4,4]`'s end value + 1 is smaller than val. This we cannot touch any existing interval.

    In both these cases, the starting index as seen to the left is `idx` (referred to as `l_idx` going forward) i.e we cannot touch/extend the interval at position `idx-1`. Correspondingly, the value is val(referred to as `l_val` going forward). If these conditions do not meet, we can extend the interval on the left i.e

    Example if `self._X = [1,1], [4,4], [10,12]` and `val = 5`, then `idx=2` as well but the interval on the left's end value `4` is just 1 smaller than val, so it can be extended. In cases like these, `l_idx` will be idx and `l_val` will be val.

1. Similar to what we did for left side of `self._X`, we have to do it for right side as well. If the `idx` is equal to length of `self._X` (i.e if it's greater than the last interval), or if the interval to the right's start value -1 is greater than the val, then it warrant's a new interval as seen from the right. Only additionaly care we have to take is consider the element on the left's end range as well as bisect does not respect the end of the interval. This is the reason why we do `r_val = max(val, self._X[idx-1][1] if idx > 0 else -float('inf'))`. If it can extend the interval on the right, we simply take r_idx to idx+1 and r_val to be the end of interval on the right. The examples for these can be built similar to the case (i)

1. Finally, we update the part of the array where we have to insert the new interval as `self._X[l_idx:r_idx] = [[l_val, r_val]]`

For getIntervals, we don't have to do any work as `self._X` already stores the intervals.
```
Runtime: 172 ms
Memory Usage: 17.1 MB
```
```python
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._X = []

    def addNum(self, val: int) -> None:
        idx = bisect.bisect(self._X, [val])
        if idx == 0 or self._X[idx-1][1] + 1 < val:  # new interval
            l_idx = idx
            l_val = val
        else:  # extend interval
            l_idx = idx-1
            l_val = self._X[idx-1][0]
        
        if idx == len(self._X) or self._X[idx][0]-1 > val:  # new interval
            r_idx = idx
            r_val = max(val, self._X[idx-1][1] if idx > 0 else -float('inf'))
        else:  # extend interval
            r_idx = idx+1
            r_val = self._X[idx][1]
        
        self._X[l_idx:r_idx] = [[l_val, r_val]]

    def getIntervals(self) -> List[List[int]]:
        return self._X


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
```