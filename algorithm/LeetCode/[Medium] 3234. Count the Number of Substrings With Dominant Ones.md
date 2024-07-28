3234. Count the Number of Substrings With Dominant Ones

You are given a binary string `s`.

Return the number of **substrings** with **dominant** ones.

A string has **dominant** ones if the number of ones in the string is **greater than or equal to** the **square** of the number of zeros in the string.

 

**Example 1:**
```
Input: s = "00011"

Output: 5

Explanation:

The substrings with dominant ones are shown in the table below.

i	j	s[i..j]	Number of Zeros	Number of Ones
3	3	1	0	1
4	4	1	0	1
2	3	01	1	1
3	4	11	0	2
2	4	011	1	2
```

**Example 2:**
```
Input: s = "101101"

Output: 16

Explanation:

The substrings with non-dominant ones are shown in the table below.

Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.

i	j	s[i..j]	Number of Zeros	Number of Ones
1	1	0	1	0
4	4	0	1	0
1	4	0110	2	2
0	4	10110	2	3
1	5	01101	2	3
```

**Constraints:**

* `1 <= s.length <= 4 * 10^4`
* `s` consists only of characters `'0'` and `'1'`.

# Submissions
---
**Solution 1: (Sliding Window, O(n sqrt(n)))**

The maximum number of zeros z in a dominant string is ~sqrt(n).

> sqrt(n + 0.25) - 0.5 to be exact, which is the solution for the z + z * z = n equation.

For each z in [0, sqrt(n)), we can count dominant substrings in O(n) with the sliding window.

> We move left and right side of the window so it contains exactly z zeros.

The tricky part is to count substrings in the window as we extend the right side.

Consider this example when z == 2:

* 110101: one substring
* 1101011: +2 substrings (1101011 and 1101011)
* 11010111: +3 substrings (11010111, 11010111, and 11010111)
* 110101111: +3 substrings (110101111, 110101111, and 110101111)

As you can see, we need to track the position of the first zero in the window (p).

Every time we extend our window, it generates 1 + min(p - j, cnt[1] - z * z) additional substrings.

```
Runtime: 601 ms
Memory: 12.87 MB
```
```c++
class Solution {
public:
    int numberOfSubstrings(string s) {
        int res = 0;
        for (int z = 0; z + z * z <= s.size(); ++z) {
            int cnt[2] = {}, p = 0;
            for (int i = 0, j = 0; i < s.size(); ++i) {
                ++cnt[s[i] == '1'];
                while (cnt[0] > z)
                    --cnt[s[j++] == '1'];
                if (cnt[0] == z && cnt[1] && cnt[1] >= z * z) {
                    for (p = max(p, j); p < i && s[p] == '1'; ++p);
                    res += 1 + min(p - j, cnt[1] - z * z);              
                }
            }
        }
        return res;
    }
};
```
