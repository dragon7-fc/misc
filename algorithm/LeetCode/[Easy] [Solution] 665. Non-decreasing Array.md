665. Non-decreasing Array

Given an array with `n` integers, your task is to check if it could become non-decreasing by modifying **at most** `1` element.

We define an array is non-decreasing if `array[i] <= array[i + 1]` holds for every `i` (1 <= i < n).

**Example 1:**
```
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
```
**Example 2:**
```
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
```
**Note:** The `n` belongs to [1, 10,000].

# Solution
---
## Approach #1: Brute Force [Time Limit Exceeded]
**Intuition**

For the given array $\text{A}$, if we are changing at most one element $\text{A[i]}$, we should change $\text{A[i]}$ to $\text{A[i-1]}$, as it would be guaranteed that $\text{A[i-1]} ≤ \text{A[i]}$, and $\text{A[i]}$ would be the smallest possible to try and achieve $\text{A[i]} ≤ \text{A[i+1]}$.

**Algorithm**

For each possible change $\text{A[i]}$, check if the sequence is monotone increasing. We'll modify $\text{new}$, a copy of the array $\text{A}$.

```python
class Solution(object):
    def checkPossibility(self, A):
        def monotone_increasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i+1]:
                    return False
            return True

        new = A[:]
        for i in xrange(len(A)):
            old_ai = A[i]
            new[i] = new[i-1] if i > 0 else float('-inf')
            if monotone_increasing(new):
                return True
            new[i] = old_ai

        return False
```

**Complexity Analysis**

* Time Complexity: Let $N$ be the length of the given array. For each element $\text{A[i]}$, we check if some sequence is monotone increasing, which takes $O(N)$ steps. In total, this is a complexity of $O(N^2)$.

* Space Complexity: To hold our array $\text{new}$, we need $O(N)$ space.

## Approach #2: Reduce to Smaller Problem [Accepted]
**Intuition**

If $\text{A[0]} ≤ \text{A[1]} ≤ \text{A[2]}$, then we may remove $\text{A[0]}$ without changing the answer. Similarly, if $\text{A}\big[\text{len(A)-3}\big] ≤ \text{A}\big[\text{len(A)-2}\big] ≤ \text{A}\big[\text{len(A)-1}\big]$, we may remove $\text{A[len(A)-1]}$ without changing the answer.

If the problem is solvable, then after these removals, very few numbers will remain.

**Algorithm**

Consider the interval $\text{[i, j]}$ corresponding to the subarray $\big[\text{A[i], A[i+1], ..., A[j]}\big]$. When $\text{A[i]} ≤ \text{A[i+1]} ≤ \text{A[i+2]}$, we know we do not need to modify $\text{A[i]}$, and we can consider solving the problem on the interval $\text{[i+1, j]}$ instead. We use a similar approach for $j$.

Afterwards, with the length of the interval under consideration being $\text{j - i + 1}$, if the interval has size 2 or less, then we did not find any problem.

If our interval under consideration has 5 or more elements, then there are two disjoint problems that cannot be fixed with one replacement.

Otherwise, our problem size is now at most 4 elements, which we can easily brute force.

```python
class Solution(object):
    def checkPossibility(self, A):
        def brute_force(A):
            #Same as in approach 1

        i, j = 0, len(A) - 1
        while i+2 < len(A) and A[i] <= A[i+1] <= A[i+2]:
            i += 1
        while j-2 >= 0 and A[j-2] <= A[j-1] <= A[j]:
            j -= 1

        if j - i + 1 <= 2:
            return True
        if j - i + 1 >= 5:
            return False

        return brute_force(A[i: j+1])
```

**Complexity Analysis**

* Time Complexity: Let $N$ be the length of the given array. Our pointers $i$ and $j$ move at most $O(N)$ times. Our brute force is constant time as there are at most 4 elements in the array. Hence, the complexity is $O(N)$.

* Space Complexity: The extra array $\text{A[i: j+1]}$ only has at most 4 elements, so it is constant space, and so is the space used by our auxillary brute force algorithm. In total, the space complexity is $O(1)$.

## Approach #3: Locate and Analyze Problem Index [Accepted]
**Intuition**

Consider all indices $p$ for which $%\text{A[p]} > \text{A[p+1]}$. If there are zero, the answer is True. If there are 2 or more, the answer is False, as more than one element of the array must be changed for $\text{A}$ to be monotone increasing.

At the problem index $p$, we only care about the surrounding elements. Thus, immediately the problem is reduced to a very small size that can be analyzed by casework.

**Algorithm**

As before, let $p$ be the unique problem index for which $\text{A[p]} > \text{A[p+1]}$. If this is not unique or doesn't exist, the answer is False or True respectively. We analyze the following cases:

* If $\text{p = 0}$, then we could make the array good by setting $\text{A[p] = A[p+1]}$.
* If $\text{p = len(A) - 2}$, then we could make the array good by setting $\text{A[p+1] = A[p]}$.
* Otherwise, $\text{A[p-1], A[p], A[p+1], A[p+2]}$ all exist, and:
    * We could change $\text{A[p]}$ to be between $\text{A[p-1]}$ and $\text{A[p+1]}$ if possible, or;
    * We could change $\text{A[p+1]}$ to be between $\text{A[p]}$ and $\text{A[p+2]}$ if possible.
    
```python
class Solution(object):
    def checkPossibility(self, A):
        p = None
        for i in xrange(len(A) - 1):
            if A[i] > A[i+1]:
                if p is not None:
                    return False
                p = i

        return (p is None or p == 0 or p == len(A)-2 or
                A[p-1] <= A[p+1] or A[p] <= A[p+2])
```

**Complexity Analysis**

* Time Complexity: Let $N$ be the length of the given array. We loop through the array once, so our time complexity is $O(N)$.

* Space Complexity: We only use $p$ and $i$, and the answer itself as the additional space. The additional space complexity is $O(1)$.

# Submissions
---
**Solution**
```
Runtime: 220 ms
Memory Usage: 15.1 MB
```
```python
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        p = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if p is not None:
                    return False
                p = i

        return (p is None or p == 0 or p == len(nums)-2 or
                nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2])
```
