1371. Find the Longest Substring Containing Vowels in Even Counts

Given the string `s`, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

 

**Example 1:**
```
Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
```

**Example 2:**
```
Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
```

**Example 3:**
```
Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
```

**Constraints:**

* `1 <= s.length <= 5 x 10^5`
* `s` contains only lowercase English letters.

# Submissions
---
**Solution 1: (Hash Table, Bit Manipulation)**

We can use 5 bits to represent the parity of the number of occurrences of vowels. For example, we can use 0/1 for even/odd numbers, then if we have 4a, 3e, 2i, 1o, 0u, the representation would be 01010. As we scan through the array, we can update the representation in O(1) time by using the XOR operation, and then store the index where every different representation first appeared. When we encounter a representation, say 01010 again at index j, we can look back on the index i where 01010 first appeared, and we know that the substring from i to j must be a valid string, and it is the longest valid substring that ends at j.
```
Runtime: 460 ms
Memory Usage: 18.3 MB
```
```python
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        d, n, r = {0: -1}, 0, 0
        for i, c in enumerate(s):
            if c in vowels:
                n ^= vowels[c]
            if n not in d:
                d[n] = i
            else:
                r = max(r, i - d[n])
        return r
```

**Solution 2: (Bitmasking)**
```
Runtime: 39 ms
Memory: 17.65 MB
```
```c++
class Solution {
public:
    int findTheLongestSubstring(string s) {
        int prefixXOR = 0;
        // Store the masks of all letters in an array.
        int characterMap[26] = {0};
        characterMap['a' - 'a'] = 1;
        characterMap['e' - 'a'] = 2;
        characterMap['i' - 'a'] = 4;
        characterMap['o' - 'a'] = 8;
        characterMap['u' - 'a'] = 16;
        // Initialize mp to store the previous index with this prefixXOR value.
        vector<int> mp(32, -1);
        int longestSubstring = 0;

        for (int i = 0; i < s.length(); i++) {
            // If the current character is a vowel, find it's prefix XOR and add
            // it in the map.
            prefixXOR ^= characterMap[s[i] - 'a'];
            if (mp[prefixXOR] == -1 and prefixXOR != 0) mp[prefixXOR] = i;

            // If the value of prefixXOR exists in the map, find the longest
            // subarray.
            longestSubstring = max(longestSubstring, i - mp[prefixXOR]);
        }

        return longestSubstring;
    }
};
```

**Solution 2: (Bitmasking, Hash Table)**
```
Runtime: 45 ms
Memory: 17.51 MB
```
```++
class Solution {
public:
    int findTheLongestSubstring(string s) {
        int m[26] = {0};
        m['a' - 'a'] = 1;
        m['e' - 'a'] = 2;
        m['i' - 'a'] = 4;
        m['o' - 'a'] = 8;
        m['u' - 'a'] = 16;
        vector<int> dp(32, INT_MIN);
        dp[0] = -1;
        int cur = 0, ans = 0;
        for (int i = 0; i < s.size(); i ++) {
            cur ^= m[s[i]-'a'];
            if (dp[cur] == INT_MIN) {
                dp[cur] = i;
            } else {
                ans = max(ans, i - dp[cur]);
            }
        }
        return ans;
    }
};
```
