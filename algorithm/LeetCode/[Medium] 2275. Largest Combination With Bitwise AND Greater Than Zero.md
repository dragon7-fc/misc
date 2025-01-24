2275. Largest Combination With Bitwise AND Greater Than Zero

The **bitwise AND** of an array `nums` is the bitwise AND of all integers in `nums`.

* For example, for `nums = [1, 5, 3]`, the bitwise AND is equal to `1 & 5 & 3 = 1`.
* Also, for `nums = [7]`, the bitwise AND is `7`.

You are given an array of positive integers `candidates`. Evaluate the **bitwise AND** of every **combination** of numbers of `candidates`. Each number in `candidates` may only be used once in each combination.

Return the size of the **largest** combination of candidates with a bitwise AND **greater** than `0`.

 

**Example 1:**
```
Input: candidates = [16,17,71,62,12,24,14]
Output: 4
Explanation: The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0.
The size of the combination is 4.
It can be shown that no combination with a size greater than 4 has a bitwise AND greater than 0.
Note that more than one combination may have the largest size.
For example, the combination [62,12,24,14] has a bitwise AND of 62 & 12 & 24 & 14 = 8 > 0.
```

**Example 2:**
```
Input: candidates = [8,8]
Output: 2
Explanation: The largest combination [8,8] has a bitwise AND of 8 & 8 = 8 > 0.
The size of the combination is 2, so we return 2.
```

**Constraints:**

* `1 <= candidates.length <= 10^5`
* `1 <= candidates[i] <= 10^7`

# Submissions
---
**Solution 1: (Bit Manipulation)**
```
Runtime: 2974 ms
Memory Usage: 24.9 MB
```
```python
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        return max(sum(n & (1 << i) > 0 for n in candidates) for i in range(0, 24))
```

**Solution 2: (Direct Maximum Bit Count)**
```
Runtime: 27 ms
Memory: 60.24 MB
```
```c++
class Solution {
public:
    int largestCombination(vector<int>& candidates) {
        int maxCount = 0;  // Variable to track the maximum count of set bits.
        for (int i = 0; i < 24; i++) {
            int count = 0;  // Count of numbers with the i-th bit set.
            for (int num : candidates) {
                if ((num & (1 << i)) != 0) {  // Check if the i-th bit is set.
                    count++;
                }
            }
            maxCount = max(maxCount, count);  // Update the maximum count.
        }
        return maxCount;
    }
};
```

**Solution 3: (Bit Manipulation)**
```
Runtime: 11 ms
Memory: 60.21 MB
```
```c++
class Solution {
public:
    int largestCombination(vector<int>& candidates) {
        int cnt[25] = {0}, i, ans;
        for (auto c: candidates) {
            i = 0;
            while (c) {
                cnt[i] += c&1;
                c >>= 1;
                i += 1;
            }
        }
        ans = cnt[0];
        for (i = 1; i < 25; i ++) {
            ans = max(ans, cnt[i]);
        }
        return ans;
    }
};
```
