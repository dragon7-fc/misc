3167. Better Compression of String

You are given a string `compressed` representing a compressed version of a string. The format is a character followed by its frequency. For example, `"a3b1a1c2"` is a compressed version of the string `"aaabacc"`.

We seek a better compression with the following conditions:

1. Each character should appear only once in the compressed version.
1. The characters should be in alphabetical order.

Return the better compression of `compressed`.

**Note**: In the better version of compression, the order of letters may change, which is acceptable.

 

**Example 1:**
```
Input: compressed = "a3c9b2c1"

Output: "a3b2c10"

Explanation:

Characters "a" and "b" appear only once in the input, but "c" appears twice, once with a size of 9 and once with a size of 1.

Hence, in the resulting string, it should have a size of 10.
```

**Example 2:**
```
Input: compressed = "c2b3a1"

Output: "a1b3c2"
```

**Example 3:**
```
Input: compressed = "a2b4c1"

Output: "a2b4c1"
```
 

**Constraints:**

`1 <= compressed.length <= 6 * 104`
`compressed` consists only of lowercase English letters and digits.
`compressed` is a valid compression, i.e., each character is followed by its frequency.
Frequencies are in the range `[1, 10^4]` and have no leading zeroes

# Submissions
---
**Solution 1: (Sliding window, string)**
```
Runtime: 26 ms
Memory: 14.88 MB
```
```c++
class Solution {
public:
    string betterCompression(string compressed) {
        int cnt[26], i = 0, j, c, n = compressed.size();
        while (i < n) {
            if (compressed[i] >= 'a' && compressed[i] <= 'z') {
                j = i+1;
                c = 0;
                while (j < n && compressed[j] >= '0' && compressed[j] <= '9') {
                    c *= 10;
                    c += compressed[j]-'0';
                    j += 1;
                }
                cnt[compressed[i]-'a'] += c;
                i = j;
            }
        }
        string ans;
        for (int i = 0; i < 26; i ++) {
            if (cnt[i]) {
                ans += 'a'+i;
                ans += to_string(cnt[i]);
            }
        }
        return ans;
    }
};
```
