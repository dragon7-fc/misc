521. Longest Uncommon Subsequence I

Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A **subsequence** is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

**Example 1:**
```
Input: "aba", "cdc"
Output: 3
Explanation: The longest uncommon subsequence is "aba" (or "cdc"), 
because "aba" is a subsequence of "aba", 
but not a subsequence of any other strings in the group of two strings. 
```

**Note:**

1. Both strings' lengths will not exceed 100.
1. Only letters from a ~ z will appear in input strings.

# Solution
---
## Approach #1 Brute Force [Time Limit Exceeded]
In the brute force approach we will generate all the possible $2^n$ subsequences of both the strings and store their number of occurences in a hashmap. Longest subsequence whose frequency is equal to $1$ will be the required subsequence. And, if it is not found we will return $-1$.

```java
public class Solution {
    public int findLUSlength(String a, String b) {
        HashMap < String, Integer > map = new HashMap < > ();
        for (String s: new String[] {a, b}) {
            for (int i = 0; i < (1 << s.length()); i++) {
                String t = "";
                for (int j = 0; j < s.length(); j++) {
                    if (((i >> j) & 1) != 0)
                        t += s.charAt(j);
                }
                if (map.containsKey(t))
                    map.put(t, map.get(t) + 1);
                else
                    map.put(t, 1);
            }
        }
        int res = -1;
        for (String s: map.keySet()) {
            if (map.get(s) == 1)
                res = Math.max(res, s.length());
        }
        return res;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(2^x+2^y)$. where $x$ and $y$ are the lengths of strings $a$ and $b$ respectively . Number of subsequences will be $2^x+2^y$.

* Space complexity : $O(2^x+2^y)$. $2^x+2^y$ subsequences will be generated.

## Approach #2 Simple Solution[Accepted]
**Algorithm**

Simple analysis of this problem can lead to an easy solution.

These three cases are possible with string $a$ and $b$:-

1. $a=b$. If both the strings are identical, it is obvious that no subsequence will be uncommon. Hence, return `-1`.

1. $length(a)=length(b)$ and $a \ne b$. Example: $abc$ and $abd$. In this case we can consider any string i.e. $abc$ or $abd$ as a required subsequence, as out of these two strings one string will never be a subsequence of other string. Hence, return $length(a)$ or $length(b)$.

1. $length(a) \ne length(b)$. Example $abcd$ and $abc$. In this case we can consider bigger string as a required subsequence because bigger string can't be a subsequence of smaller string. Hence, return $max(length(a),length(b))$.

```java
public class Solution {
    public int findLUSlength(String a, String b) {
        if (a.equals(b))
            return -1;
        return Math.max(a.length(), b.length());
    }
}
```

**Complexity Analysis**

* Time complexity : $O(min(x,y))$. where $x$ and $y$ are the lengths of strings $a$ and $b$ respectively. Here equals method will take $min(x,y)$ time .

* Space complexity : $O(1)$. No extra space required.

# Submissions
---
**Solution: (Simple Solution, String)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))
```