1737. Change Minimum Characters to Satisfy One of Three Conditions

You are given two strings `a` and `b` that consist of lowercase letters. In one operation, you can change any character in `a` or `b` to any lowercase letter.

Your goal is to satisfy one of the following three conditions:

* Every letter in `a` is strictly less than every letter in `b` in the alphabet.
* Every letter in `b` is strictly less than every letter in `a` in the alphabet.
* Both `a` and `b` consist of only one distinct letter.

Return the minimum number of operations needed to achieve your goal.

 

**Example 1:**
```
Input: a = "aba", b = "caa"
Output: 2
Explanation: Consider the best way to make each condition true:
1) Change b to "ccc" in 2 operations, then every letter in a is less than every letter in b.
2) Change a to "bbb" and b to "aaa" in 3 operations, then every letter in b is less than every letter in a.
3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b consist of one distinct letter.
The best way was done in 2 operations (either condition 1 or condition 3).
```

**Example 2:**
```
Input: a = "dabadd", b = "cda"
Output: 3
Explanation: The best way is to make condition 1 true by changing b to "eee".
```

**Constraints:**

* `1 <= a.length, b.length <= 105`
* `a` and `b` consist only of lowercase letters.

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 224 ms
Memory Usage: 15 MB
```
```python
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        c1 = Counter(ord(c) - 97 for c in a)
        c2 = Counter(ord(c) - 97 for c in b)
        res = m + n - max((c1 + c2).values()) # condition 3
        for i in range(25):
            c1[i + 1] += c1[i]
            c2[i + 1] += c2[i]
            res = min(res, m - c1[i] + c2[i]) # condition 1
            res = min(res, n - c2[i] + c1[i]) # condition 2
        return res
```

```
Runtime: 34 ms
Memory: 15.2 MB
```
```c++
class Solution {
public:
    int minCharacters(string a, string b) {
        int m = a.size(), n = b.size(), res = m + n;
        vector<int> c1(26), c2(26);
        for (char& c: a) c1[c - 'a']++;
        for (char& c: b) c2[c - 'a']++;

        for (int i = 0; i < 26; ++i) {
            res = min(res, m + n - c1[i] - c2[i]); // condition 3
            if (i > 0) {
                c1[i] += c1[i - 1];
                c2[i] += c2[i - 1];
            }
            if (i < 25) {
                res = min(res, m - c1[i] + c2[i]); // condition 1
                res = min(res, n - c2[i] + c1[i]); // condition 2
            }
        }
        return res;
    }
};
```
