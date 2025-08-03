898. Bitwise ORs of Subarrays

We have an array `A` of non-negative integers.

For every (contiguous) subarray `B = [A[i], A[i+1], ..., A[j]]` (with `i <= j`), we take the bitwise OR of all the elements in `B`, obtaining a result `A[i] | A[i+1] | ... | A[j]`.

Return the number of possible results.  (Results that occur more than once are only counted once in the final answer.)

 

**Example 1:**

```
Input: [0]
Output: 1
Explanation: 
There is only one possible result: 0.
```

**Example 2:**

```
Input: [1,1,2]
Output: 3
Explanation: 
The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.
```

**Example 3:**

```
Input: [1,2,4]
Output: 6
Explanation: 
The possible results are 1, 2, 3, 4, 6, and 7.
```

**Note:**

* `1 <= A.length <= 50000`
* `0 <= A[i] <= 10^9`

# Solution
---
## Approach 1: Frontier Set
**Intuition**

Let's try to speed up a brute force answer. Evidently, the brute force approach is to calculate every result `result(i, j) = A[i] | A[i+1] | ... | A[j]`. We can speed this up by taking note of the fact that `result(i, j+1) = result(i, j) | A[j+1]`. Naively, this approach has time complexity $O(N^2)$, where $N$ is the length of the array.

Actually, this approach can be better than that. At the `k`th step, say we have all the `result(i, k)` in some set `cur`. Then we can find the next `cur` set (for `k -> k+1`) by using `result(i, k+1) = result(i, k) | A[k+1]`.

However, the number of unique values in this set `cur` is at most 32, since the list `result(k, k)`, `result(k-1, k)`, `result(k-2, k)`, ... is monotone increasing, and any subsequent values that are different must have more 1s in it's binary representation (to a maximum of 32 ones).

**Algorithm**

In the kth step, we'll maintain `cur`: the set of results `A[i] | ... | A[k]` for all `i`. These results will be included in our final answer set.

```python
class Solution(object):
    def subarrayBitwiseORs(self, A):
        ans = set()
        cur = {0}
        for x in A:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)
```

**Complexity Analysis**

* Time Complexity: $O(N \log W)$, where $N$ is the length of `A`, and $W$ is the maximum size of elements in `A`.

* Space Complexity: $O(N \log W)$, the size of the answer.

# Submissions
---
**Solution: (Frontier Set, DP Bottom-Up)**
```
Runtime: 836 ms
Memory Usage: 39.3 MB
```
```python
class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans = set()
        cur = {0}
        for x in A:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)
```

**Solution 2: (Frontier Set, DP Bottom-Up, O(N log W))**
```
Runtime: 971 ms, Beats 69.01%
Memory: 334.86 MB, Beats 60.27%
```
```c++
class Solution {
public:
    int subarrayBitwiseORs(vector<int>& arr) {
        unordered_set<int> ans, cur, pre;
        for (auto &a: arr){
            cur.insert(a);
            for (auto &b: pre) {
                cur.insert(a|b);
            }
            pre = move(cur);
            ans.insert(pre.begin(), pre.end());
        }
        return ans.size();
    }
};
```
