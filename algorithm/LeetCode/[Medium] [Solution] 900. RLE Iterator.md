900. RLE Iterator

Write an iterator that iterates through a run-length encoded sequence.

The iterator is initialized by `RLEIterator(int[] A)`, where `A` is a run-length encoding of some sequence.  More specifically, for all even `i`, `A[i]` tells us the number of times that the non-negative integer value `A[i+1]` is repeated in the sequence.

The iterator supports one function: `next(int n)`, which exhausts the next n elements (n >= 1) and returns the last element exhausted in this way.  If there is no element left to exhaust, next returns `-1` instead.

For example, we start with `A = [3,8,0,9,2,5]`, which is a run-length encoding of the sequence `[8,8,8,5,5]`.  This is because the sequence can be read as "three eights, zero nines, two fives".

 

**Example 1:**
```
Input: ["RLEIterator","next","next","next","next"], [[[3,8,0,9,2,5]],[2],[1],[1],[2]]
Output: [null,8,8,5,-1]
Explanation: 
RLEIterator is initialized with RLEIterator([3,8,0,9,2,5]).
This maps to the sequence [8,8,8,5,5].
RLEIterator.next is then called 4 times:

.next(2) exhausts 2 terms of the sequence, returning 8.  The remaining sequence is now [8, 5, 5].

.next(1) exhausts 1 term of the sequence, returning 8.  The remaining sequence is now [5, 5].

.next(1) exhausts 1 term of the sequence, returning 5.  The remaining sequence is now [5].

.next(2) exhausts 2 terms, returning -1.  This is because the first term exhausted was 5,
but the second term did not exist.  Since the last term exhausted does not exist, we return -1.
```

**Note:**

1. `0 <= A.length <= 1000`
1. `A.length` is an even integer.
1. `0 <= A[i] <= 10^9`
1. There are at most `1000` calls to `RLEIterator.next(int n)` per test case.
1. Each call to `RLEIterator.next(int n)` will have `1 <= n <= 10^9`.

# Solution
---
## Approach 1: Store Exhausted Position and Quantity
**Intuition**

We can store an index `i` and quantity `q` which represents that `q` elements of `A[i]` (repeated `A[i+1]` times) are exhausted.

For example, if we have `A = [1,2,3,4]` (mapping to the sequence `[2,4,4,4]`) then `i = 0, q = 0` represents that nothing is exhausted; `i = 0, q = 1` represents that `[2]` is exhausted, `i = 2, q = 1` will represent that we have currently exhausted `[2, 4]`, and so on.

**Algorithm**

Say we want to exhaust `n` more elements. There are currently `D = A[i] - q` elements left to exhaust (of value `A[i+1]`).

If `n > D`, then we should exhaust all of them and continue: `n -= D; i += 2; q = 0`.

Otherwise, we should exhaust some of them and return the current element's value: `q += D; return A[i+1]`.

```python
class RLEIterator(object):

    def __init__(self, A):
        self.A = A
        self.i = 0
        self.q = 0

    def next(self, n):
        while self.i < len(self.A):
            if self.q + n > self.A[self.i]:
                n -= self.A[self.i] - self.q
                self.q = 0
                self.i += 2
            else:
                self.q += n
                return self.A[self.i+1]
        return -1
```

**Complexity Analysis**

* Time Complexity: $O(N + Q)$, where $N$ is the length of `A`, and $Q$ is the number of calls to `RLEIterator.next`.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution**
```
Runtime: 48 ms
Memory Usage: 14.1 MB
```
```python
class RLEIterator:

    def __init__(self, A: List[int]):
        self.A = A
        self.i = 0
        self.q = 0

    def next(self, n: int) -> int:
        while self.i < len(self.A):
            if self.q + n > self.A[self.i]:
                n -= self.A[self.i] - self.q
                self.q = 0
                self.i += 2
            else:
                self.q += n
                return self.A[self.i+1]
        return -1
        
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
```