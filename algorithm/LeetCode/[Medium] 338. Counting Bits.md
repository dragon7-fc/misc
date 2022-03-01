338. Counting Bits

Given a non negative integer number `num`. For every numbers i in the range **0 ≤ i ≤ num** calculate the number of 1's in their binary representation and return them as an array.

**Example 1:**
```
Input: 2
Output: [0,1,1]
```

**Example 2:**
```
Input: 5
Output: [0,1,1,2,1,2]
```

**Follow up:**

* It is very easy to come up with a solution with run time **O(n*sizeof(integer))**. But can you do it in linear time **O(n)** /possibly in a single pass?
* Space complexity should be **O(n)**.
* Can you do it like a boss? Do it without using any builtin function like **__builtin_popcount** in c++ or in any other language.

# Submissions
---
**Solution 1: (DP Bottom-Up, Bit Manipulation)**
```
Runtime: 132 ms
Memory Usage: N/A
```
```python
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]*(num+1)
        for i in range(num+1):
            ans[i] = (i&1) + ans[i>>1]
        return ans
```

**Solution 2: (DP Top-Down)**
```
Runtime: 100 ms
Memory Usage: 24.7 MB
```
```python
class Solution:
    def countBits(self, num: int) -> List[int]:
        
        @functools.lru_cache(None)
        def dfs(n):
            if n == 0:
                return 0
            return (n&1) + dfs(n>>1)
            
        return [dfs(i) for i in range(num+1)]
```

**Solution 3: (DP Bottom-Up)**
```
Runtime: 4 ms
Memory Usage: 7.9 MB
```
```c++
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans(n+1);
        for (int i = 1; i < n+1; i ++)
            ans[i] = ans[i>>1] + (i&1);
        return ans;
    }
};
```

**Solution 4: (__builtin_popcount)**
```
Runtime: 7 ms
Memory Usage: 7.7 MB
```
```c++
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans(n+1);
        for (int i = 0; i < n+1; i ++)
            ans[i] = __builtin_popcount(i);
        return ans;
    }
};
```
