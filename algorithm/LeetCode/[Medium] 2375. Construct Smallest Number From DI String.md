2375. Construct Smallest Number From DI String

You are given a **0-indexed** string `pattern` of length `n` consisting of the characters `'I'` meaning **increasing** and `'D'` meaning **decreasing**.

A **0-indexed** string `num` of length `n + 1` is created using the following conditions:

* `num` consists of the digits `'1'` to `'9'`, where each digit is used at most once.
* If `pattern[i] == 'I'`, then `num[i] < num[i + 1]`.
* `If pattern[i] == 'D'`, then `num[i] > num[i + 1]`.

Return the lexicographically **smallest** possible string `num` that meets the conditions.

 

**Example 1:**
```
Input: pattern = "IIIDIDDD"
Output: "123549876"
Explanation:
At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
Some possible values of num are "245639871", "135749862", and "123849765".
It can be proven that "123549876" is the smallest possible num that meets the conditions.
Note that "123414321" is not possible because the digit '1' is used more than once.
```

**Example 2:**
```
Input: pattern = "DDD"
Output: "4321"
Explanation:
Some possible values of num are "9876", "7321", and "8742".
It can be proven that "4321" is the smallest possible num that meets the conditions.
```

**Constraints:**

* `1 <= pattern.length <= 8`
* `pattern` consists of only the letters `'I'` and `'D'`.

# Submissions
---
**Solution 1: (stack)**
```
Runtime: 26 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res, stack = [], []
        for i,c in enumerate(pattern + 'I', 1):
            stack.append(str(i))
            if c == 'I':
                res += stack[::-1]
                stack = []
        return ''.join(res)
```

**Solution 2: (Backtracking, O(9^n))**
```
Runtime: 0 ms, Beats 100.00%
Memory: 9.06 MB, Beats 9.74%
```
```c++
class Solution {
    void bt(int i, int &visited, string &cur, string &ans, string pattern) {
        if (ans != "" && cur > ans) {
            return;
        }
        if (i == pattern.length()) {
            ans = min(ans, cur);
            return;
        }
        if (pattern[i] == 'I') {
            for (int a = cur.back() - '0'; a <= 1+pattern.length(); a++) {
                if ((visited&(1<<a)) == 0) {
                    visited ^= (1<<a);
                    cur += string(1, a+'0');
                    bt(i+1, visited, cur, ans, pattern);
                    visited ^= (1<<a);
                    cur.pop_back();
                }
            }
        } else {
            for (int a = cur.back() - '0'; a >= 1; a--) {
                if ((visited&(1<<a)) == 0) {
                    visited ^= (1<<a);
                    cur += string(1, a+'0');
                    bt(i+1, visited, cur, ans, pattern);
                    visited ^= (1<<a);
                    cur.pop_back();
                }
            }
        }
    }
public:
    string smallestNumber(string pattern) {
        int a, visited = 0;
        string cur, ans = string(pattern.length()+1, '9');
        for (a = 1; a <= 1+pattern.length(); a ++) {
            visited ^= (1<<a);
            cur += string(1, a+'0');
            bt(0, visited, cur, ans, pattern);
            visited ^= (1<<a);
            cur.pop_back();
        }
        return ans;
    }
};
```

**Solution 3: (Optimized Greedy Approach with Precomputed 'D' Segments)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 7.81 MB, Beats 73.43%
```
```c++
class Solution {
public:
    string smallestNumber(string pattern) {
        int patternLength = pattern.length();
        int maxSoFar = 0, currMax = 0, temp;

        // Array to store lengths of decreasing subsequences in the pattern
        vector<int> arrD(patternLength + 1, 0);

        // Compute the lengths of decreasing subsequences in the pattern
        for (int patternIndex = patternLength - 1; patternIndex >= 0;
             patternIndex--) {
            if (pattern[patternIndex] == 'D')
                // If 'D', increment the length of the decreasing sequence
                arrD[patternIndex] = arrD[patternIndex + 1] + 1;
        }

        string result = "";

        // Build the result string based on the pattern
        for (int position = 0; position <= patternLength; position++) {
            if (pattern[position] == 'I') {
                // If 'I', assign the next maximum digit and append it to the
                // result
                maxSoFar++;
                result += '0' + maxSoFar;

                // Update the max digit encountered so far
                maxSoFar = max(maxSoFar, currMax);

                // Reset current max for the next iteration
                currMax = 0;
            } else {
                // If 'D', calculate the appropriate digit and append it to the
                // result
                temp = 1 + maxSoFar + arrD[position];
                result += '0' + temp;

                // Update the current max value
                currMax = max(currMax, temp);
            }
        }

        return result;
    }
};
```

**Solution 4: (stack, keep increasing then reverse)**
```
Runtime: 0 ms
Memory Usage: 5.9 MB
```
```c++
class Solution {
public:
    string smallestNumber(string pattern) {
        string res, stack;
        for (int i = 0; i <= pattern.length(); i++) {
            stack.push_back('1' + i);
            if (i == pattern.length() || pattern[i] == 'I') {
                while (!stack.empty()) {
                    res.push_back(stack.back());
                    stack.pop_back();
                }
            }
        }
        return res;
    }
};
```
