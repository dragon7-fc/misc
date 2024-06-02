3023. Find Pattern in Infinite Stream I

You are given a binary array `pattern` and an object stream of class `InfiniteStream` representing a **0-indexed** infinite stream of bits.

The class InfiniteStream contains the following function:

* `int next()`: Reads a single bit (which is either `0` or `1`) from the stream and returns it.

Return the first starting index where the `pattern` matches the bits read from the stream. For example, if the pattern is `[1, 0]`, the first match is the highlighted part in the stream `[0, 1, 0, 1, ...]`.

 

**Example 1:**
```
Input: stream = [1,1,1,0,1,1,1,...], pattern = [0,1]
Output: 3
Explanation: The first occurrence of the pattern [0,1] is highlighted in the stream [1,1,1,0,1,...], which starts at index 3.
```

**Example 2:**
```
Input: stream = [0,0,0,0,...], pattern = [0]
Output: 0
Explanation: The first occurrence of the pattern [0] is highlighted in the stream [0,...], which starts at index 0.
```

**Example 3:**
```
Input: stream = [1,0,1,1,0,1,1,0,1,...], pattern = [1,1,0,1]
Output: 2
Explanation: The first occurrence of the pattern [1,1,0,1] is highlighted in the stream [1,0,1,1,0,1,...], which starts at index 2.
 ```

**Constraints:**

* `1 <= pattern.length <= 100`
* `pattern` consists only of `0` and `1`.
* `stream` consists only of `0` and `1`.
* The input is generated such that the pattern's start index exists in the first `10^5` bits of the stream.

# Submissions
---
**Solution 1: (KMP)**
```
Runtime: 287 ms
Memory: 320.30 MB
```
```c++
/**
 * Definition for an infinite stream.
 * class InfiniteStream {
 * public:
 *     InfiniteStream(vector<int> bits);
 *     int next();
 * };
 */
class Solution {
public:
    int findPattern(InfiniteStream* stream, vector<int>& pattern) {
        int n = pattern.size(), i, k, cur;
        vector<int> dp(n);
        k = 0, i = 1;
        while (i < n) {
            if (pattern[k] == pattern[i]) {
                dp[i] = k+1;
                k += 1;
                i += 1;
            } else {
                if (k) {
                    k = dp[k-1];
                } else {
                    dp[i] = 0;
                    i += 1;
                }
            }
        }
        k = 0, i = 0;
        bool flag = false;
        while (true) {
            if (!flag) {
                cur = stream->next();
                flag = true;
            }
            if (cur == pattern[k]) {
                k += 1;
                i += 1;
                if (k == n) {
                    return i-k;
                }
                flag = false;
            } else {
                if (k) {
                    k = dp[k-1];
                } else {
                    k = 0;
                    i += 1;
                    flag = false;
                }
            }
        }
        return -1;
    }
};
```
