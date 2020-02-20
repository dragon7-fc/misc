995. Minimum Number of K Consecutive Bit Flips

In an array A containing only 0s and 1s, a `K`-bit flip consists of choosing a (contiguous) subarray of length `K` and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of `K`-bit flips required so that there is no 0 in the array.  If it is not possible, return `-1`.

 

**Example 1:**
```
Input: A = [0,1,0], K = 1
Output: 2
Explanation: Flip A[0], then flip A[2].
```

**Example 2:**
```
Input: A = [1,1,0], K = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we can't make the array become [1,1,1].
```

**Example 3:**
```
Input: A = [0,0,0,1,0,1,1,0], K = 3
Output: 3
Explanation:
Flip A[0],A[1],A[2]: A becomes [1,1,1,1,0,1,1,0]
Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]
``` 

**Note:**

* `1 <= A.length <= 30000`
* `1 <= K <= A.length`

# Solution
---
## Approach 1: Greedy + Events
**Intuition**

If the leftmost element is a 0, we must flip the subarray starting at index 0. Similarly, if the leftmost element is a 1, we should not flip the subarray starting at index 0. This proves we can proceed in a greedy manner: after finding out whether we have to flip the first subarray (positions 0 to K-1) or not, we can consider the array with the first element (value 1) removed, and repeat this process.

We can do better. Every time we flip a subarray `A[i], A[i+1], ..., A[i+K-1]`, we can consider this as two "events", one 'opening event' at position i that marks the start of the subarray, and one 'closing event' at position `i+K` that marks the end of the subarray. Using these events, we always know how many overlapping flipped subarrays there are: its simply the number of opening events minus the number of closing events.

**Algorithm**

When we flip a subarray, let's call the set of indices we flipped an interval. We'll keep track of `flip`, the number of overlapping intervals in our current position. We only care about the value of `flip` modulo 2.

When we flip an interval starting at `i`, we create a `hint` for a closing event at `i+K` telling us to flip our writing state back.

Please see the inline comments for more details.

```python
class Solution(object):
    def minKBitFlips(self, A, K):
        N = len(A)
        hint = [0] * N
        ans = flip = 0

        # When we flip a subarray like A[i], A[i+1], ..., A[i+K-1]
        # we can instead flip our current writing state, and put a hint at
        # position i+K to flip back our writing state.
        for i, x in enumerate(A):
            flip ^= hint[i]
            if x ^ flip == 0:  # If we must flip the subarray starting here...
                ans += 1  # We're flipping the subarray from A[i] to A[i+K-1]
                if i+K > N: return -1  # If we can't flip the entire subarray, its impossible
                flip ^= 1  
                if i+K < N: hint[i + K] ^= 1

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is length of `A`.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution 1: (Greedy + Events, Sliding Window)**
```
Runtime: 876 ms
Memory Usage: 13.4 MB
```
```python
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        N = len(A)
        hint = [0] * N
        ans = flip = 0

        # When we flip a subarray like A[i], A[i+1], ..., A[i+K-1]
        # we can instead flip our current writing state, and put a hint at
        # position i+K to flip back our writing state.
        for i, x in enumerate(A):
            flip ^= hint[i]
            if x ^ flip == 0:  # If we must flip the subarray starting here...
                ans += 1  # We're flipping the subarray from A[i] to A[i+K-1]
                if i+K > N: return -1  # If we can't flip the entire subarray, its impossible
                flip ^= 1  
                if i+K < N: hint[i + K] ^= 1

        return ans
```