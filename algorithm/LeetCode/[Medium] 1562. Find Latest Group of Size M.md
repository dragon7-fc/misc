1562. Find Latest Group of Size M

Given an array `arr` that represents a permutation of numbers from `1` to `n`. You have a binary string of size `n` that initially has all its bits set to zero.

At each step `i` (assuming both the binary string and `arr` are 1-indexed) from `1` to `n`, the bit at position `arr[i]` is set to 1. You are given an integer `m` and you need to find the latest step at which there exists a group of ones of length `m`. A group of ones is a contiguous substring of 1s such that it cannot be extended in either direction.

Return the **latest** step at which there exists a group of ones of length **exactly** `m`. If no such group exists, return `-1`.

 

**Example 1:**
```
Input: arr = [3,5,1,2,4], m = 1
Output: 4
Explanation:
Step 1: "00100", groups: ["1"]
Step 2: "00101", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "11101", groups: ["111", "1"]
Step 5: "11111", groups: ["11111"]
The latest step at which there exists a group of size 1 is step 4.
```

**Example 2:**
```
Input: arr = [3,1,5,4,2], m = 2
Output: -1
Explanation:
Step 1: "00100", groups: ["1"]
Step 2: "10100", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "10111", groups: ["1", "111"]
Step 5: "11111", groups: ["11111"]
No group of size 2 exists during any step.
```

**Example 3:**
```
Input: arr = [1], m = 1
Output: 1
```

**Example 4:**
```
Input: arr = [2,1], m = 2
Output: 2
```

**Constraints:**

* `n == arr.length`
* `1 <= n <= 10^5`
* `1 <= arr[i] <= n`
* All integers in arr are **distinct**.
* `1 <= m <= arr.length`

# Submissions
---
**Solution 1: (Counter)**

**Explanation**

* `count[i]` means the length of the group.
* When we set bit a, where a = A[i],
    * we check the length of group on the `left` `length[a - 1]`
    * also the length of group on the `right` `length[a + 1]`.
* Then we update `length[a], length[a - left], length[a + right]` to `left + right + 1`.

Note that the length value is updated on the leftmost and the rightmost bit of the group.
The length value inside the group may be out dated.

* As we do this, we also update the count of length.
    * If count[m] > 0, we update res to current step index i + 1.


**Complexity**

* Time O(N)
* Space O(N)

```
Runtime: 1752 ms
Memory Usage: 27.8 MB
```
```python
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        length = [0] * (len(arr) + 2)
        count = [0] * (len(arr) + 1)
        res = -1
        for i, a in enumerate(arr):
            left, right = length[a - 1], length[a + 1]
            length[a] = length[a - left] = length[a + right] = left + right + 1
            count[left] -= 1
            count[right] -= 1
            count[length[a]] += 1
            if count[m]:
                res = i + 1
        return res
```

**Solution 2: (Counter)**
```
Runtime: 320 ms
Memory Usage: 82.6 MB
```
```c++
class Solution {
public:
    int findLatestStep(vector<int>& arr, int m) {
        int res = -1, n = arr.size();
        vector<int> length(n + 2), count(n + 1);
        for (int i = 0; i < n; ++i) {
            int a = arr[i], left = length[a - 1], right = length[a + 1];
            length[a] = length[a - left] = length[a + right] = left + right + 1;
            count[left]--;
            count[right]--;
            count[length[a]]++;
            if (count[m])
                res = i + 1;
        }
        return res;
    }
};
```

**Solution 3: (Union Find)**
```
Runtime: 2760 ms
Memory Usage: 27.8 MB
```
```python
class UnionFindSet:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
        
    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
            self.ranks[pu] += self.ranks[pv]
        elif self.ranks[pv] > self.ranks[pu]:
            self.parents[pu] = pv
            self.ranks[pv] += self.ranks[pu]
        else:
            self.parents[pu] = pv
            self.ranks[pv] += self.ranks[pu]
        return True

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n, ans = len(arr), -1
        uf = UnionFindSet(n)
        
        for step, i in enumerate(arr):
            i -= 1
            uf.ranks[i] = 1
            for j in (i - 1, i + 1):
                if 0 <= j < n:
                    if uf.ranks[uf.find(j)] == m:
                        ans = step
                    if uf.ranks[j]:
                        uf.union(i, j)
        
        for i in range(n):
            if uf.ranks[uf.find(i)] == m:
                return n
            
        return ans
```