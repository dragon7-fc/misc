4. Median of Two Sorted Arrays

There are two sorted arrays `nums1` and `nums2` of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume `nums1` and `nums2` cannot be both empty.

**Example 1:**
```
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```

**Example 2:**
```
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```

# Solution
---
## Approach 1: Recursive Approach
To solve this problem, we need to understand "What is the use of median". In statistics, the median is used for:

> Dividing a set into two equal length subsets, that one subset is always greater than the other.

If we understand the use of median for dividing, we are very close to the answer.

First let's cut $\text{A}$ into two parts at a random position $i$:

```
          left_A             |        right_A
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
```
Since $\text{A}$ has $m$ elements, so there are $m+1$ kinds of cutting $(i = 0 \sim m)$.

And we know:

$\text{len}(\text{left_A}) = i, \text{len}(\text{right_A}) = m - i$.

Note: when $i = 0$, $\text{left_A}$ is empty, and when $i = m$, $\text{right_A}$ is empty.

With the same way, cut $\text{B}$ into two parts at a random position $j$:

```
          left_B             |        right_B
    B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
```
Put $\text{left_A}$ and $\text{left_B}$ into one set, and put $\text{right_A}$ and $\text{right_B}$ into another set. Let's name them $\text{left_part}$ and $\text{right_part}$:

```
          left_part          |        right_part
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
    B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
```
If we can ensure:

> 1. $\text{len}(\text{left_part}) = \text{len}(\text{right_part})$
1. $\max(\text{left_part}) \leq \min(\text{right_part})$

then we divide all elements in $\{\text{A}, \text{B}\}$ into two parts with equal length, and one part is always greater than the other. Then

$\text{median} = \frac{\text{max}(\text{left}\_\text{part}) + \text{min}(\text{right}\_\text{part})}{2}$

To ensure these two conditions, we just need to ensure:

>1. $i + j = m - i + n - j$ (or: $m - i + n - j + 1$) \
if $n \geq m$, we just need to set: $i = 0 \sim m, j = \frac{m + n + 1}{2} - i$
>1. $\text{B}[j-1] \leq \text{A}[i]$ and $\text{A}[i-1] \leq \text{B}[j]$

ps.1 For simplicity, I presume $\text{A}[i-1], \text{B}[j-1], \text{A}[i], \text{B}[j]$ are always valid even if $i=0$, $i=m$, $j=0$, or $j=n$. I will talk about how to deal with these edge values at last.

ps.2 Why $n \geq m$? Because I have to make sure $j$ is non-negative since $0 \leq i \leq m$ and $j = \frac{m + n + 1}{2} - i$. If $n < m$, then $j$ may be negative, that will lead to wrong result.

So, all we need to do is:

> Searching $i$ in $[0, m]$, to find an object $i$ such that: \
$\qquad \text{B}[j-1] \leq \text{A}[i]$ and $\text{A}[i-1] \leq \text{B}[j]$, where $j = \frac{m + n + 1}{2} - i$

And we can do a binary search following steps described below:

1. Set $\text{imin} = 0$, $\text{imax} = m$, then start searching in $[\text{imin}, \text{imax}]$
1. Set $i = \frac{\text{imin} + \text{imax}}{2}$, $j = \frac{m + n + 1}{2} - i$
1. Now we have $\text{len}(\text{left}\_\text{part})=\text{len}(\text{right}\_\text{part})$. And there are only 3 situations that we may encounter:

    * $\text{B}[j-1] \leq \text{A}[i]$ and $\text{A}[i-1] \leq \text{B}[j]$
        * Means we have found the object $i$, so stop searching.

    * $\text{B}[j-1] > \text{A}[i]$
        * Means $\text{A}[i]$ is too small. We must adjust $i$ to get $\text{B}[j-1] \leq \text{A}[i]$.
        * Can we increase $i$?
            * Yes. Because when $i$ is increased, $j$ will be decreased.
            * So $\text{B}[j-1]$ is decreased and $\text{A}[i]$ is increased, and $\text{B}[j-1] \leq \text{A}[i]$ may be satisfied.
        * Can we decrease $i$?
            * No! Because when $i$ is decreased, $j$ will be increased.
            * So $\text{B}[j-1]$ is increased and $\text{A}[i]$ is decreased, and $\text{B}[j-1] \leq \text{A}[i]$ will be never satisfied.
        * So we must increase $i$. That is, we must adjust the searching range to $[i+1, \text{imax}]$.
        * So, set $\text{imin} = i+1$ and goto 2.
    * $\text{A}[i-1] > \text{B}[j]$:
        * Means $\text{A}[i-1]$ is too big. And we must decrease $i$ to get $\text{A}[i-1]\leq \text{B}[j]$.
        * That is, we must adjust the searching range to [\text{imin}, i-1][imin,i−1].
        * So, set $\text{imax} = i-1$, and goto 2.

When the object $i$ is found, the median is:

> $\max(\text{A}[i-1], \text{B}[j-1])$, when m + nm+n is odd

> $\frac{\max(\text{A}[i-1], \text{B}[j-1]) + \min(\text{A}[i], \text{B}[j])}{2}$, when $m + n$ is even

Now let's consider the edges values $i=0,i=m,j=0,j=n$ where $\text{A}[i-1],\text{B}[j-1],\text{A}[i],\text{B}[j]$ may not exist. Actually this situation is easier than you think.

What we need to do is ensuring that $\text{max}(\text{left}\_\text{part}) \leq \text{min}(\text{right}\_\text{part})$. So, if $i$ and $j$ are not edges values (means $\text{A}[i-1], \text{B}[j-1],\text{A}[i],\text{B}[j]$ all exist), then we must check both $\text{B}[j-1] \leq \text{A}[i]$ and $\text{A}[i-1] \leq \text{B}[j]$. But if some of $\text{A}[i-1],\text{B}[j-1],\text{A}[i],\text{B}[j]$ don't exist, then we don't need to check one (or both) of these two conditions. For example, if $i=0$, then $\text{A}[i-1]$ doesn't exist, then we don't need to check $\text{A}[i-1] \leq \text{B}[j]$. So, what we need to do is:

> Searching $i$ in $[0, m]$, to find an object $i$ such that:
1. ($j = 0$ or $i = m$ or $\text{B}[j-1] \leq \text{A}[i])$ and
1. ($i = 0$ or $j = n$ or $\text{A}[i-1] \leq \text{B}[j])$, where $j = \frac{m + n + 1}{2} - i$

And in a searching loop, we will encounter only three situations:

> 1. ($j = 0$ or $i = m$ or $\text{B}[j-1] \leq \text{A}[i])$ and \
($i = 0$ or $j = n$ or $\text{A}[i-1] \leq \text{B}[j])$ \
Means $i$ is perfect, we can stop searching.
1. $j > 0$ and $i < m$ and $\text{B}[j - 1] > \text{A}[i]$ \
Means $i$ is too small, we must increase it.
1. $i > 0$ and $j < n$ and $\text{A}[i - 1] > \text{B}[j]$ \
Means $i$ is too big, we must decrease it.

Thanks to @Quentin.chen for pointing out that: $i < m \implies j > 0$ and $i > 0 \implies j < n$. Because:

> 1. $m \leq n, i < m \implies j = \frac{m+n+1}{2} - i > \frac{m+n+1}{2} - m \geq \frac{2m+1}{2} - m \geq 0$
1. $m \leq n, i > 0 \implies j = \frac{m+n+1}{2} - i < \frac{m+n+1}{2} \leq \frac{2n+1}{2} \leq n$

So in situation 2. and 3. , we don't need to check whether $j > 0$ and whether $j < n$.

```python
def median(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) / 2
    while imin <= imax:
        i = (imin + imax) / 2
        j = half_len - i
        if i < m and B[j-1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: min_of_right = B[j]
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0
```

**Complexity Analysis**

* Time complexity: $O\big(\log\big(\text{min}(m,n)\big)\big)$.
At first, the searching range is $[0, m]$. And the length of this searching range will be reduced by half after each loop. So, we only need $\log(m)$ loops. Since we do constant operations in each loop, so the time complexity is $O\big(\log(m)\big)$. Since $m \leq n$, so the time complexity is $O\big(\log\big(\text{min}(m,n)\big)\big)$.

* Space complexity: $O(1)$.
We only need constant memory to store 99 local variables, so the space complexity is $O(1)$.

# Submissions
---
**Solution: (Recursive Approach, Divide and Conquer)**
```
Runtime: 100 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0
```

**Solution 2: (Binary Search)**
```
Runtime: 31 ms
Memory: 89.4 MB
```
```c++
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            swap(nums1, nums2);
        }
        
        int m = nums1.size();
        int n = nums2.size();
        int low = 0, high = m;
        
        while (low <= high) {
            int partitionX = (low + high) / 2;
            int partitionY = (m + n + 1) / 2 - partitionX;
            
            int maxX = (partitionX == 0) ? INT_MIN : nums1[partitionX - 1];
            int maxY = (partitionY == 0) ? INT_MIN : nums2[partitionY - 1];
            
            int minX = (partitionX == m) ? INT_MAX : nums1[partitionX];
            int minY = (partitionY == n) ? INT_MAX : nums2[partitionY];
            
            if (maxX <= minY && maxY <= minX) {
                if ((m + n) % 2 == 0) {
                    return (max(maxX, maxY) + min(minX, minY)) / 2.0;
                } else {
                    return max(maxX, maxY);
                }
            } else if (maxX > minY) {
                high = partitionX - 1;
            } else {
                low = partitionX + 1;
            }
        }
        throw invalid_argument("Input arrays are not sorted.");
    }
};
```
