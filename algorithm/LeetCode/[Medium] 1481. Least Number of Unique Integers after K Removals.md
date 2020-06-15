1481. Least Number of Unique Integers after K Removals

Given an array of integers `arr` and an integer `k`. Find the least number of unique integers after removing **exactly** `k` elements.

 

**Example 1:**
```
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
```

**Example 2:**
```
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
```

**Constraints:**

* `1 <= arr.length <= 10^5`
* `1 <= arr[i] <= 10^9`
* `0 <= k <= arr.length`

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 492 ms
Memory Usage: 32.7 MB
```
```python
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = collections.Counter(arr)
        ans = 0
        for a, n in count.most_common()[::-1]:
            k -= n
            if k < 0:
                ans += 1
            
        return ans
```

**Solution 2: (Counter, Heap)**
```
Runtime: 608 ms
Memory Usage: 33.6 MB
```
```python
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hp = [(cnt, key) for key, cnt in collections.Counter(arr).items()]
        heapq.heapify(hp)
        while k > 0:
            k -= heapq.heappop(hp)[0]
        return len(hp) + (k < 0)   
```