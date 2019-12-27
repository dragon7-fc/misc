961. N-Repeated Element in Size 2N Array

In a array `A` of size `2N`, there are `N+1` unique elements, and exactly one of these elements is repeated `N` times.

Return the element repeated `N` times.

 

**Example 1:**
```
Input: [1,2,3,3]
Output: 3
```

**Example 2:**
```
Input: [2,1,2,5,3,2]
Output: 2
```

**Example 3:**
```
Input: [5,1,5,2,5,3,5,4]
Output: 5
``` 

**Note:**

* `4 <= A.length <= 10000`
* `0 <= A[i] < 10000`
* `A.length` is even

# Solution
---
## Approach 1: Count
**Intuition and Algorithm**

Let's count the number of elements. We can use a `HashMap` or an array - here, we use a `HashMap`.

After, the element with a count larger than `1` must be the answer.

```python
class Solution(object):
    def repeatedNTimes(self, A):
        count = collections.Counter(A)
        for k in count:
            if count[k] > 1:
                return k
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `A`.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution:**
```
Runtime: 236 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        count = collections.Counter(A)
        for k in count:
            if count[k] > 1:
                return k
```