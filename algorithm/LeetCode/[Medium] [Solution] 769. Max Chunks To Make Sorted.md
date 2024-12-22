769. Max Chunks To Make Sorted

Given an array `arr` that is a permutation of `[0, 1, ..., arr.length - 1]`, we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

**Example 1:**
```
Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
```

**Example 2:**
```
Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
```

**Note:**

* `arr` will have length in range `[1, 10]`.
* `arr[i]` will be a permutation of `[0, 1, ..., arr.length - 1]`.

# Solution
---
## Approach #1: Brute Force [Accepted]
**Intuition and Algorithm**

Let's try to find the smallest left-most chunk. If the first `k` elements are `[0, 1, ..., k-1]`, then it can be broken into a chunk, and we have a smaller instance of the same problem.

We can check whether `k+1` elements chosen from `[0, 1, ..., n-1]` are `[0, 1, ..., k]` by checking whether the maximum of that choice is `k`.

```python
class Solution(object):
    def maxChunksToSorted(self, arr):
        ans = ma = 0
        for i, x in enumerate(arr):
            ma = max(ma, x)
            if ma == i: ans += 1
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of arr

* Space Complexity: $O(1)$.

# Submissions
---
**Solution**
```
Runtime: 32 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = ma = 0
        for i, x in enumerate(arr):
            ma = max(ma, x)
            if ma == i: ans += 1
        return ans
```

**Solution 1: (Brute Force)**
```
Runtime: 0 ms
Memory Usage: 7.2 MB
```
```c++
class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int ans = 0, ma = 0;
        for (int i = 0; i< arr.size(); i ++) {
            ma = max(ma, arr[i]);
            if (ma == i)
                ans += 1;
        }
        return ans;
    }
};
```

**Solution 2: (Prefix Sum)**
```
Runtime: 0 ms
Memory: 9.28 MB
```
```c++
class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int n = arr.size(), i, cur, ans = 0;
        vector<int> dp(n);
        dp[n-1] = arr[n-1];
        for (i = n-2; i >= 0; i --) {
            dp[i] = min(arr[i], dp[i+1]);
        }
        i = 0;
        while (i < n) {
            cur = arr[i];
            while (i+1 < n && cur >= dp[i+1]) {
                cur = max(cur, arr[i+1]);
                i += 1;
            }
            ans += 1;
            i += 1;
        }
        return ans;
    }
};
```

**Solution 3: (Stack, mono stack)**
```
Runtime: 0 ms
Memory: 9.38 MB
```
```c++
class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        stack<int> stk;
        for (auto a: arr) {
            if (!stk.size() || a > stk.top()) {
                stk.push(a);
            } else {
                auto cur = stk.top();
                while (stk.size() && a < stk.top()) {
                    stk.pop();
                }
                stk.push(cur);
            }
        }
        return stk.size();
    }
};
```
