896. Monotonic Array

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array `A` is monotone increasing if for all `i <= j, A[i] <= A[j]`.  An array `A` is monotone decreasing if for all `i <= j, A[i] >= A[j]`.

Return true if and only if the given array `A` is monotonic.

 

**Example 1:**
```
Input: [1,2,2,3]
Output: true
```

**Example 2:**
```
Input: [6,5,4,4]
Output: true
```

**Example 3:**
```
Input: [1,3,2]
Output: false
```

**Example 4:**
```
Input: [1,2,4,5]
Output: true
```

**Example 5:**
```
Input: [1,1,1]
Output: true
```

# Solution
---
## Approach 1: Two Pass
**Intuition**

An array is monotonic if it is monotone increasing, or monotone decreasing. Since `a <= b` and `b <= c` implies `a <= c`, we only need to check adjacent elements to determine if the array is monotone increasing (or decreasing, respectively). We can check each of these properties in one pass.

**Algorithm**

To check whether an array `A` is monotone increasing, we'll check `A[i] <= A[i+1]` for all `i`. The check for monotone decreasing is similar.

```python
class Solution(object):
    def isMonotonic(self, A):
        return (all(A[i] <= A[i+1] for i in xrange(len(A) - 1)) or
                all(A[i] >= A[i+1] for i in xrange(len(A) - 1)))
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `A`.

* Space Complexity: $O(1)$.

## Approach 2: One Pass
**Intuition**

To perform this check in one pass, we want to handle a stream of comparisons from $\{-1, 0, 1\}$, corresponding to `<`, `==`, or `>`. For example, with the array `[1, 2, 2, 3, 0]`, we will see the stream `(-1, 0, -1, 1)`.

**Algorithm**

Keep track of store, equal to the first non-zero comparison seen (if it exists.) If we see the opposite comparison, the answer is False.

Otherwise, every comparison was (necessarily) in the set $\{-1, 0\}$, or every comparison was in the set $\{0, 1\}$, and therefore the array is monotonic.

```python
class Solution(object):
    def isMonotonic(self, A):
        store = 0
        for i in xrange(len(A) - 1):
            c = cmp(A[i], A[i+1])
            if c:
                if c != store != 0:
                    return False
                store = c
        return True
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `A`.

* Space Complexity: $O(1)$.

## Approach 3: One Pass (Simple Variant)
**Intuition and Algorithm**

To perform this check in one pass, we want to remember if it is monotone increasing or monotone decreasing.

It's monotone increasing if there aren't some adjacent values `A[i], A[i+1]` with `A[i] > A[i+1]`, and similarly for monotone decreasing.

If it is either monotone increasing or monotone decreasing, then `A` is monoton

```python
class Solution(object):
    def isMonotonic(self, A):
        increasing = decreasing = True

        for i in xrange(len(A) - 1):
            if A[i] > A[i+1]:
                increasing = False
            if A[i] < A[i+1]:
                decreasing = False

        return increasing or decreasing
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `A`.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution 1:**
```
Runtime: 560 ms
Memory Usage: 19.8 MB
```
```python
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        ans = True
        
        inc_dec = 0
        for i in range(1, len(A)):
            if inc_dec == 0:
                if A[i] > A[i-1]:
                    inc_dec = 1
                elif A[i] < A[i-1]:
                    inc_dec = -1
            elif inc_dec == 1 and A[i] < A[i-1]:
                return False
            elif inc_dec == -1 and A[i] > A[i-1]:
                return False
            
        return ans
```