424. Longest Repeating Character Replacement

Given a string `s` that consists of only uppercase English letters, you can perform at most `k` operations on that string.

In one operation, you can choose **any** character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

**Note:**

* Both the string's length and `k` will not exceed `10^4`.

**Example 1:**
```
Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
```

**Example 2:**
```
Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
```

# Submissions
---
**Solution 1: (Two Pointers, Sliding Window, max count in sliding window)**

Maintain count of major chars in the sliding window

```
Runtime: 132 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        max_len = 0 # wndow length
        max_count = 0 # count of major chars in the window
        
        char_count = [0 for _ in range(26)]
        
        while end < len(s):
            end_char_idx = ord(s[end]) - ord('A')
            char_count[end_char_idx] += 1
            max_count = max(max_count, char_count[end_char_idx])
            
            # shrink window and update meta information
            # while condition is dynamic as the `start` value is changing in the while condtion
            # due to shrinking of the window
            while end - start + 1 - max_count > k:
                start_char_idx = ord(s[start]) - ord('A')
                char_count[start_char_idx] -= 1
                start += 1
                
            max_len = max(max_len, end - start + 1)
            end += 1
            
        return max_len
```

**Solution 2: (Two Pointers, Sliding Window, inverse increasing max count in sliding window)**

         0 1 2 3 4 5 6
    s = "A A B A B B A", k = 1
         i       j
           i     j 
           i       j
             i     j
             i       j
               i     j
cnt
A        1 2   3 2 1 2
B            1   2 3 2
mx    0  1 2   3      
ans   0  1 2 3 4 4 4 4

```
Runtime: 0 ms, Beats 100.00%
Memory: 10.80 MB, Beats 69.00%
```
```c++
class Solution {
public:
    int characterReplacement(string s, int k) {
        int n = s.size(), i = 0, j = 0, mx = 0, ans = 0;
        vector<int> cnt(26);
        while (j < n) {
            cnt[s[j] - 'A'] += 1;
            mx = max(mx , cnt[s[j] - 'A']);
            if (j - i + 1 - mx > k) {
                cnt[s[i] - 'A'] -= 1;
                i += 1;
            }
            ans = max(ans, j - i + 1);
            j += 1;
        }
        return ans;
    }
};
```
