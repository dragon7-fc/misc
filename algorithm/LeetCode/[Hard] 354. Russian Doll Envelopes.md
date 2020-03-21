354. Russian Doll Envelopes

You have a number of envelopes with widths and heights given as a pair of integers `(w, h)`. One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

**Note:**

Rotation is not allowed.

**Example:**
```
Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
```

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 192 ms
Memory Usage: 15.2 MB
```
```python
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:    
        # sort in one property and find the longest increasing subsequence
        # in the other property, that's it
        # to avoid cases such as [(3, 4), (3, 6)] - output should be 1
        # sort the (w) in ascending and (h) in descending

        #let's sort in second property(h) and then find LIS using first property(w)
        ln = len(envelopes)
        if ln <= 1:
            return ln

        envelopes = sorted(envelopes, key=lambda x:(x[1], -x[0]))
        #now find the LIS
        q = [envelopes[0][0]]
        
        def upperbound(ls, num):
            ln = len(ls)
            s, e = 0, ln-1
            while s <= e:
                mid = (e-s)//2 + s
                if ls[mid] == num:
                    #we can or we don't have to replace this
                    return mid
                elif ls[mid] < num:
                    if mid+1 < ln and ls[mid+1] > num:
                        return mid+1
                    s = mid + 1
                else:
                    if mid == 0:
                        return mid
                    e = mid-1

        for i in range(1, ln):
            num = envelopes[i][0]
            if q[-1] < num:
                q.append(num)
            elif q[-1] > num:
                # use binary search 
                idx = upperbound(q, num)
                q[idx] = num

        return len(q)
```

**Solution 2: (Binary Search)**
```
Runtime: 168 ms
Memory Usage: 15.4 MB
```
```python
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:    
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights = [0x3f3f3f3f] * len(envelopes)
        for _, h in envelopes:
            heights[bisect.bisect_left(heights, h)] = h
        return bisect.bisect_right(heights, 0x3f3f3f3f - 1)
```

**Solution 3: (Binary Search)**
```
Runtime: 164 ms
Memory Usage: 15.1 MB
```
```python
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:    
        
        # longest increasing subsequence
        def lis(arr):
            dp = [0] * len(arr)
            L = 0
            for x in arr:
                i = bisect.bisect_left(dp, x, lo = 0, hi = max(L, 0))
                if i == L:
                    L += 1
                dp[i] = x
            return L
        
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        return lis([x[1] for x in envelopes])
```