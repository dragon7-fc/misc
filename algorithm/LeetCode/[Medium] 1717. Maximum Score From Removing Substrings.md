1717. Maximum Score From Removing Substrings

You are given a string `s` and two integers `x` and `y`. You can perform two types of operations any number of times.

* Remove substring "ab" and gain x points.
    * For example, when removing `"ab"` from `"cabxbae"` it becomes `"cxbae"`.
* Remove substring "ba" and gain y points.
    * For example, when removing `"ba"` from `"cabxbae"` it becomes `"cabxe"`.

Return the maximum points you can gain after applying the above operations on `s`.

 

**Example 1:**
```
Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
```

**Example 2:**
```
Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
```

**Constraints:**

* `1 <= s.length <= 105`
* `1 <= x, y <= 104`
* `s` consists of lowercase English letters.

# Submissions
---
**Solution 1: (Greedy, Focus on some pattern)**
```
Runtime: 1140 ms
Memory Usage: 14.9 MB
```
```python
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a = 'a'
        b = 'b'
        if x < y:
            x, y = y, x
            a, b = b, a
        seen = Counter()
        ans = 0
        for c in s + 'x':
            if c in 'ab':
                if c == b and 0 < seen[a]:
                    ans += x
                    seen[a] -= 1
                else:
                    seen[c] += 1
            else:
                ans += y * min(seen[a], seen[b])
                seen = Counter()

        return ans
```

**Solution 1: (Greedy, Stack)**
```
Runtime: 97 ms
Memory: 29.3 MB
```
```c++
class Solution {
    string greedy(string s, char a, char b) {
        string st;
        for (auto ch : s) {
            if (!st.empty() && st.back() == a && ch == b) {
                st.pop_back();
            } else
                st.push_back(ch);
        }
        return st;
    }
public:
    int maximumGain(string s, int x, int y, char a = 'a', char b = 'b') {
        if (y > x) {
            swap(x, y);
            swap(a, b);
        }
        auto s1 = greedy(s, a, b), s2 = greedy(s1, b, a);
        return (s.size() - s1.size()) / 2 * x + (s1.size() - s2.size()) /2 * y;
    }
};
```
