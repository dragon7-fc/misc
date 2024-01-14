2840. Check if Strings Can be Made Equal With Operations II

You are given two strings `s1` and `s2`, both of length `n`, consisting of lowercase English letters.

You can apply the following operation on **any** of the two strings **any** number of times:

* Choose any two indices `i` and `j` such that `i < j` and the difference `j - i` is **even**, then **swap** the two characters at those indices in the string.

Return `true` if you can make the strings `s1` and `s2` equal, and `false` otherwise.

 

**Example 1:**
```
Input: s1 = "abcdba", s2 = "cabdab"
Output: true
Explanation: We can apply the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
- Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
- Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.
```

**Example 2:**
```
Input: s1 = "abe", s2 = "bea"
Output: false
Explanation: It is not possible to make the two strings equal.
```

**Constraints:**

* `n == s1.length == s2.length`
* `1 <= n <= 10^5`
* `s1` and `s2` consist only of lowercase English letters.

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 96 ms
Memory: 17.6 MB
```
```python
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])
```

**Solution 1: (Counter)**
```
Runtime: 70 ms
Memory: 18.49 MB
```
```c++
class Solution {
public:
    bool checkStrings(string s1, string s2) {
        unordered_map<char, int> s1even;
        unordered_map<char, int> s1odd;
        unordered_map<char, int> s2even;
        unordered_map<char, int> s2odd;

        for (int i = 0; i < s1.length(); i++) {
            if (i % 2 == 0) {
                s1even[s1[i]]++;
                s2even[s2[i]]++;
            } else {
                s1odd[s1[i]]++;
                s2odd[s2[i]]++;
            }
        }

        return (s1even == s2even && s1odd == s2odd);
    }
};
```
