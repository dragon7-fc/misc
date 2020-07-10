668. Kth Smallest Number in Multiplication Table

Nearly every one have used the Multiplication Table. But could you find out the `k`-th smallest number quickly from the multiplication table?

Given the height `m` and the length `n` of a `m * n` Multiplication Table, and a positive integer `k`, you need to return the `k`-th smallest number in this table.

**Example 1:**
```
Input: m = 3, n = 3, k = 5
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6
3	6	9

The 5-th smallest number is 3 (1, 2, 2, 3, 3).
```

**Example 2:**
```
Input: m = 2, n = 3, k = 6
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6

The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
```

**Note:**

* The `m` and `n` will be in the range `[1, 30000]`.
* The `k` will be in the range `[1, m * n]`

# Solution
---
## Approach #1: Brute Force [Memory Limit Exceeded]
**Intuition and Algorithm**

Create the multiplication table and sort it, then take the $k^{th}$ element.

```python
class Solution(object):
    def findKthNumber(self, m, n, k):
        table = [i*j for i in range(1, m+1) for j in range(1, n+1)]
        table.sort()
        return table[k-1]
```

**Complexity Analysis**

* Time Complexity: $O(m*n)$ to create the table, and $O(m*n\log(m*n))$ to sort it.

* Space Complexity: $O(m*n)$ to store the table.

## Approach #2: Next Heap [Time Limit Exceeded]
**Intuition**

Maintain a heap of the smallest unused element of each row. Then, finding the next element is a pop operation on the heap.

**Algorithm**

Our `heap` is going to consist of elements $\text{(val, root)}$, where $\text{val}$ is the next unused value of that row, and $\text{root}$ was the starting value of that row.

We will repeatedly find the next lowest element in the table. To do this, we pop from the heap. Then, if there's a next lowest element in that row, we'll put that element back on the heap.

```python
class Solution(object):
    def findKthNumber(self, m, n, k):
        heap = [(i, i) for i in range(1, m+1)]
        heapq.heapify(heap)

        for _ in xrange(k):
            val, root = heapq.heappop(heap)
            nxt = val + root
            if nxt <= root * n:
                heapq.heappush(heap, (nxt, root))

        return val
```

**Complexity Analysis**

* Time Complexity: $O(k * m \log m) = O(m^2 n \log m)$. Our initial heapify operation is $O(m)$. Afterwards, each pop and push is $O(m \log m)$, and our outer loop is $O(k) = O(m*n)$

* Space Complexity: $O(m)$. Our heap is implemented as an array with $m$ elements.

## Approach #3: Binary Search [Accepted]
**Intuition**

As $\text{k}$ and $\text{m*n}$ are up to $9 * 10^8$, linear solutions will not work. This motivates solutions with $\log$ complexity, such as binary search.

**Algorithm**

Let's do the binary search for the answer $\text{A}$.

Say `enough(x)` is true if and only if there are $\text{k}$ or more values in the multiplication table that are less than or equal to $\text{x}$. Colloquially, enough describes whether $\text{x}$ is large enough to be the $k^{th}$ value in the multiplication table.

Then (for our answer $\text{A}$), whenever $\text{x ≥ A}$, `enough(x)` is True; and whenever $\text{x < A}$, `enough(x)` is False.

In our binary search, our loop invariant is `enough(hi) = True`. At the beginning, `enough(m*n) = True`, and whenever `hi` is set, it is set to a value that is "enough" (enough(mi) = True). That means `hi` will be the lowest such value at the end of our binary search.

This leaves us with the task of counting how many values are less than or equal to $\text{x}$. For each of $\text{m}$ rows, the $i^{th}$ row looks like $\text{[i, 2*i, 3*i, ..., n*i]}$. The largest possible $\text{k*i ≤ x}$ that could appear is $\text{k = x // i}$. However, if $\text{x}$ is really big, then perhaps $\text{k > n}$, so in total there are $\text{min(k, n) = min(x // i, n)}$ values in that row that are less than or equal to $\text{x}$.

After we have the count of how many values in the table are less than or equal to $\text{x}$, by the definition of `enough(x)`, we want to know if that count is greater than or equal to $\text{k}$.

```python
class Solution(object):
    def findKthNumber(self, m, n, k):
        def enough(x):
            count = 0
            for i in xrange(1, m+1):
                count += min(x // i, n)
            return count >= k

        lo, hi = 1, m * n
        while lo < hi:
            mi = (lo + hi) / 2
            if not enough(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo
```

**Complexity Analysis**

* Time Complexity: $O(m * \log (m*n))$. Our binary search divides the interval $\text{[lo, hi]}$ into half at each step. At each step, we call enough which requires $O(m)$ time.

* Space Complexity: $O(1)$. We only keep integers in memory during our intermediate calculations.

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 1456 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(x):
            count = 0
            for i in range(1, m+1):
                count += min(x // i, n)
            return count >= k

        lo, hi = 1, m * n
        while lo < hi:
            mi = (lo + hi) // 2
            if not enough(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo
```

**Solution 2: (Binary Search)**
```
Runtime: 324 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if n > m:
            m, n = n, m
        l = 1
        r = m * n
        while l < r:
            mid = (l + r) // 2
            cnt = 0
            for col in range(n, 0, -1):
                col_cnt = mid // col
                if col_cnt < m:
                    cnt += col_cnt
                else:
                    cnt += col * m
                    break
            if cnt < k:
                l = mid + 1
            else:
                r = mid
        return l
```

**Solution 3: (Binary Search)**
```
Runtime: 20 ms
Memory Usage: 5.9 MB
```
```c++
class Solution {
public:
    int CountOfNumbersTillMid(int x, int m, int n) {
        int count = 0;
        int i = m;
        int j = 1;
        while (i >= 1 && j <= n)         // i goes from m to 1, j goes from 1 to n
        {
            if (i*j <= x)
            {
                count += i;
                j++;
            }
            else
                i--;
        }
        return count;
    }
    int findKthNumber(int m, int n, int k) {
        int low = 1, hi = m * n;
        while (low < hi) {
            int mid = low + (hi - low) / 2;
            int count = CountOfNumbersTillMid(mid, m, n);
            if (count < k)
                low = mid + 1;
            else
                hi = mid;
        }
        return low;
    }
};
```