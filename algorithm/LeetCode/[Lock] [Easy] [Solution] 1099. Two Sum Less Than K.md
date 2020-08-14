1099. Two Sum Less Than K

Given an array `A` of integers and integer `K`, return the maximum `S` such that there exists `i < j` with `A[i] + A[j] = S` and `S < K`. If no `i, j` exist satisfying this equation, return `-1`.

 

**Example 1:**
```
Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.
```

**Example 2:**
```
Input: A = [10,20,30], K = 15
Output: -1
Explanation: 
In this case it's not possible to get a pair sum less that 15.
```

**Note:**

* `1 <= A.length <= 100`
* `1 <= A[i] <= 1000`
* `1 <= K <= 2000`

# Solution
---
This problem is a variation of Two Sum. The main difference is that we are not searching for the exact target here. Instead, our sum is in some relation with the target. For this problem, we are looking for a maximum sum that is smaller than the target.

First, let's check solutions for the similar problems:

1. Two Sum uses a hashmap to find complement values, and therefore achieves $\mathcal{O}(N)$ time complexity.
1. Two Sum II uses the two pointers pattern and also has $\mathcal{O}(N)$ time complexity for a sorted array. We can use this approach for any array if we sort it first, which bumps the time complexity to $\mathcal{O}(n\log{n})$.

Since our sum can be any value smaller than the target, we cannot use a hashmap. We do not know which value to look up! Instead, we need to sort the array and use a binary search or the two pointers pattern, like in Two Sum II. In a sorted array, it is easy to find elements that are close to a given value.

## Approach 1: Brute Force
It is important to understand the input constraints to choose the most appropriate approach. For this problem, the size of our array is limited to 100. So, a brute force solution could be a reasonable option. It's simple and does not require any additional memory.

**Algorithm**

1. For each index `i` in `A`:

    * For each index `j > i` in `A`:
        * If `A[i] + A[j]` is less than k:
            * Track maximum `A[i] + A[j]` in the result `S`.
1. Return the result S.

```c++
int twoSumLessThanK(vector<int>& A, int K) {
    int S = -1;
    for (int i = 0; i < A.size(); ++i)
        for (int j = i + 1; j < A.size(); ++j)
            if (A[i] + A[j] < K)
                S = max(S, A[i] + A[j]);
    return S;
}
```

```python
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        S = -1
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i] + A[j] < K:
                    S = max(S, A[i] + A[j])
        return S
```

**Complexity Analysis**

* Time Complexity: $\mathcal{O}(n^2)$. We have 2 nested loops.

* Space Complexity: $\mathcal{O}(1)$.

## Approach 2: Two Pointers
We will follow the same two pointers approach as in Two Sum II. It requires the array to be sorted, so we'll do that first.

As a quick refresher, the pointers are initially set to the first and the last element respectively. We compare the sum of these two elements with the target. If it is smaller than the target, we increment the lower pointer `lo`. Otherwise, we decrement the higher pointer `hi`. Thus, the sum always moves toward the target, and we "prune" pairs that would move it further away. Again, this works only if the array is sorted. Head to the Two Sum II solution for the detailed explanation.

Since the sum here must be smaller than the target, we don't stop when we find a pair that sums exactly to the target. We decrement the higher pointer and continue until our pointers collide. For each iteration, we track the maximum sum - if it's smaller than the target.

![1099_1_1.png](img/1099_1_1.png)
![1099_1_2.png](img/1099_1_2.png)
![1099_1_3.png](img/1099_1_3.png)
![1099_1_4.png](img/1099_1_4.png)
![1099_1_5.png](img/1099_1_5.png)
![1099_1_6.png](img/1099_1_6.png)

**Algorithm**

1. Sort the array.

1. Set the `lo` pointer to zero, and `hi` - to the last index.

1. While `lo` is smaller than hi:

    * If `A[lo] + A[hi]` is less than `K`:
        * Track maximum `A[hi] + A[lo]` in the result `S`.
        * Increment `lo`.
    * Else:
        * Decrement `hi`.
1. Return the result `S`.

```c++
int twoSumLessThanK(vector<int>& A, int K) {
    int S = -1;
    sort(begin(A), end(A));
    int lo = 0, hi = A.size() - 1;
    while (lo < hi) {
        if (A[lo] + A[hi] < K) {
            S = max(S, A[lo] + A[hi]);
            ++lo;
        }
        else
            --hi;
    }
    return S;
}
```

```python
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        S = -1
        A.sort()
        lo, hi = 0, len(A) -1
        while lo < hi:
            if (A[lo] + A[hi] < K):
                S = max(S, A[lo] + A[hi])
                lo += 1
            else:
                hi -= 1
        return S
```

**Optimizations**

We can break from the loop as soon as `A[lo] > K / 2`. In the sorted array, `A[lo]` is the smallest of the remaining elements, so `A[hi] > K / 2` for any hi. Therefore, `A[lo] + A[hi]` will be equal or greater than `K` for the remaining elements.

**Complexity Analysis**

* Time Complexity: $\mathcal{O}(n\log{n})$ to sort the array. The two pointers approach itself is $\mathcal{O}(n)$, so the time complexity would be linear if the input is sorted.

* Space Complexity: from $\mathcal{O}(\log{n})$ to $\mathcal{O}(n)$, depending on the implementation of the sorting algorithm.

## Approach 3: Binary Search
Instead of moving two pointers towards the target, we can iterate through each element A[i], and binary-search for a complement value K - A[i]. This approach is less efficient than the two pointers one, however, it can be more intuitive to come up with. Same as above, we need to sort the array first for this to work.

Note that the binary search returns the "insertion point" for the searched value, i.e. the position where that value would be inserted to keep the array sorted. So, the binary search result points to the first element that is equal or greater than the complement value. Since our sum must be smaller than `K`, we consider the element immediately before the found element.

**Algorithm**

1. Sort the array.

1. For each index `i` in `A`:

    * Binary search for `K - A[i]` starting from `i + 1`.
    * Set `j` to the position before the found element.
    * If `j` is less than `i`:
        * Track maximum `A[i] + A[j]` in the result `S`.
1. Return the result S.

>Note that the binary search function in Java works a bit differently. If there are multiple elements that match the search value, it does not guarantee to point to the first one. That's why in the Java solution below we search for `K - A[i] - 1`. Note that we decrement the pointer only if the value we found is greater than `K - A[i] - 1`.

```c++
int twoSumLessThanK(vector<int>& A, int K) {
    int S = -1;
    sort(begin(A), end(A));
    for (int i = 0; i < A.size() && A[i] < K; ++i) {
        auto j = lower_bound(begin(A) + i + 1, end(A), K - A[i]) - begin(A) - 1;
        if (j > i)
            S = max(S, A[i] + A[j]);
    }
    return S;
}
```

```python
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        S = -1
        A.sort()
        for i in range(len(A)):
            j = bisect_left(A, K - A[i], i + 1) - 1
            if j > i:
                S = max(S, A[i] + A[j])
        return S
```

**Complexity Analysis**

* Time Complexity: $\mathcal{O}(n\log{n})$ to sort the array and do the binary search for each element.

* Space Complexity: from $\mathcal{O}(\log{n})$ to $\mathcal{O}(n)$, depending on the implementation of the sorting algorithm.

## Approach 4: Counting Sort
We can leverage the fact that the input number range is limited to `[1..1000]` and use a counting sort. Then, we can use the two pointers pattern to enumerate pairs in the `[1..1000]` range.

Note that the result can be a sum of two identical numbers, and that means that `lo` can be equal to hi. In this case, we need to check if the count for that number is greater than one.

**Algorithm**

1. Count each element using the array count.

1. Set the lo number to zero, and `hi` - to `1000`.

1. While `lo` is smaller than, or equals `hi`:

    * If `lo + hi` is greater than `K`, or `count[hi] == 0`:
        * Decrement `hi`.
    * Else:
        * If `count[lo]` is greater than `0` (when `lo < hi`), or `1` (when `lo == hi`):
            * Track maximum `lo + hi` in the result `S`.
        * Increment `lo`.
1. Return the result `S`.

```c++
int twoSumLessThanK(vector<int>& A, int K) {
    int S = -1;
    int count[1001] = {};
    for (int i: A)
        ++count[i];
    int lo = 1, hi = 1000;
    while (lo <= hi) {
        if (lo + hi >= K || count[hi] == 0)
            --hi;
        else {
            if (count[lo] > (lo < hi ? 0 : 1))
                S = max(S, lo + hi);
            ++lo;
        }
    }
    return S;
}
```

```python
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        S = -1
        count = [0] * 1001
        for i in A:
            count[i] += 1
        lo, hi = 0, 1000
        while lo < hi:
            if lo + hi >= K or count[hi] == 0:
                hi -= 1
            else:
                if count[lo] > 0 if lo < hi else 1:
                    S = max(S, lo + hi)
                lo += 1
        return S
```

**Optimizations**

1. We can set `hi` to either maximum number, or `K - 1`, whichever is smaller.
1. We can ignore numbers greater than `K - 1`.
1. We can use a boolean array (e.g. `seen`) instead of `count`. In the first loop, we will check if `i` is a duplicate (`seen[i]` is already `true`) and set `S` to the highest `i + i < K`. Note that the two pointers loop will run while `lo < hi`, not while `lo <= hi`.
1. We can break from the two pointers loop as soon as `A[lo] > K / 2`.

**Complexity Analysis**

* Time Complexity: $\mathcal{O}(n + m)$, where $m$ corresponds to the range of values in the input array.

* Space Complexity: $\mathcal{O}(m)$ to count each value.

## Further Thoughts
Always clarify the problem constraints and inputs during an interview. This would help you choose the right approach.

The Two Pointers approach is a good choice when the number of elements is large, and the range of possible values is not constrained. Also, if the input array is already sorted, this approach provides a linear time complexity and does not require additional memory.

# Submissions
---
**Solution 1: (Two Pointers)**
```
Runtime: 44 ms
Memory Usage: 13.6 MB
```
```python
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        S = -1
        A.sort()
        lo, hi = 0, len(A) -1
        while lo < hi:
            if (A[lo] + A[hi] < K):
                S = max(S, A[lo] + A[hi])
                lo += 1
            else:
                hi -= 1
        return S
```

**Solution 2: (Binary Search)**
```
Runtime: 44 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        S = -1
        A.sort()
        for i in range(len(A)):
            j = bisect_left(A, K - A[i], i + 1) - 1
            if j > i:
                S = max(S, A[i] + A[j])
        return S
```

**Solution 3: (Counting Sort)**
```
Runtime: 48 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        S = -1
        count = [0] * 1001
        for i in A:
            count[i] += 1
        lo, hi = 0, 1000
        while lo < hi:
            if lo + hi >= K or count[hi] == 0:
                hi -= 1
            else:
                if count[lo] > 0 if lo < hi else 1:
                    S = max(S, lo + hi)
                lo += 1
        return S
```