5. Longest Palindromic Substring

Given a string `s`, find the longest palindromic substring in `s`. You may assume that the maximum length of `s` is `1000`.

**Example 1:**
```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

**Example 2:**
```
Input: "cbbd"
Output: "bb"
```

# Solutions
---
## Summary
This article is for intermediate readers. It introduces the following ideas: Palindrome, Dynamic Programming and String Manipulation. Make sure you understand what a palindrome means. A palindrome is a string which reads the same in both directions. For example, $S$ = "aba" is a palindrome, $S$ = "abc" is not.

## Solution
## Approach 1: Longest Common Substring
Common mistake

Some people will be tempted to come up with a quick solution, which is unfortunately flawed (however can be corrected easily):

Reverse $S$ and become $S'$. Find the longest common substring between $S$ and $S'$, which must also be the longest palindromic substring.

This seemed to work, let’s see some examples below.

For example, $S$ = "caba", $S'$ = "abac".

The longest common substring between $S$ and $S'$ is "aba", which is the answer.

Let’s try another example: $S$ = "abacdfgdcaba", $S'$ = "abacdgfdcaba".

The longest common substring between $S$ and $S'$ is "abacd". Clearly, this is not a valid palindrome.

**Algorithm**

We could see that the longest common substring method fails when there exists a reversed copy of a non-palindromic substring in some other part of SS. To rectify this, each time we find a longest common substring candidate, we check if the substring’s indices are the same as the reversed substring’s original indices. If it is, then we attempt to update the longest palindrome found so far; if not, we skip this and find the next candidate.

This gives us an $O(n^2)$ Dynamic Programming solution which uses $O(n^2)$ space (could be improved to use $O(n)$ space). Please read more about Longest Common Substring here.


##  Approach 2: Brute Force
The obvious brute force solution is to pick all possible starting and ending positions for a substring, and verify if it is a palindrome.

**Complexity Analysis**

* Time complexity : $O(n^3)$. Assume that $n$ is the length of the input string, there are a total of $\binom{n}{2} = \frac{n(n-1)}{2}$

  such substrings (excluding the trivial solution where a character itself is a palindrome). Since verifying each substring takes $O(n)$ time, the run time complexity is $O(n^3)$.

* Space complexity : $O(1)$.


## Approach 3: Dynamic Programming
To improve over the brute force solution, we first observe how we can avoid unnecessary re-computation while validating palindromes. Consider the case "ababa". If we already knew that "bab" is a palindrome, it is obvious that "ababa" must be a palindrome since the two left and right end letters are the same.

We define $P(i,j)$ as following:

$$
P(i,j) = \begin{cases} \text{true,} &\quad\text{if the substring } S_i \dots S_j \text{ is a palindrome}\\ \text{false,} &\quad\text{otherwise.} \end{cases}
$$

Therefore,

$P(i, j) = ( P(i+1, j-1) \text{ and } S_i == S_j )$

The base cases are:

$P(i, i) = true$

$P(i, i+1) = ( S_i == S_{i+1} )$

This yields a straight forward DP solution, which we first initialize the one and two letters palindromes, and work our way up finding all three letters palindromes, and so on...

**Complexity Analysis**

* Time complexity : $O(n^2)$. This gives us a runtime complexity of $O(n^2)$.

* Space complexity : $O(n^2)$. It uses $O(n^2)$ space to store the table.

**Additional Exercise**

Could you improve the above space complexity further and how?

## Approach 4: Expand Around Center
In fact, we could solve it in $O(n^2)$ time using only constant space.

We observe that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center, and there are only $2n - 1$ such centers.

You might be asking why there are $2n - 1$ but not $n$ centers? The reason is the center of a palindrome can be in between two letters. Such palindromes have even number of letters (such as "abba") and its center are between the two 'b's.

```java
public String longestPalindrome(String s) {
    if (s == null || s.length() < 1) return "";
    int start = 0, end = 0;
    for (int i = 0; i < s.length(); i++) {
        int len1 = expandAroundCenter(s, i, i);
        int len2 = expandAroundCenter(s, i, i + 1);
        int len = Math.max(len1, len2);
        if (len > end - start) {
            start = i - (len - 1) / 2;
            end = i + len / 2;
        }
    }
    return s.substring(start, end + 1);
}

private int expandAroundCenter(String s, int left, int right) {
    int L = left, R = right;
    while (L >= 0 && R < s.length() && s.charAt(L) == s.charAt(R)) {
        L--;
        R++;
    }
    return R - L - 1;
}
```

**Complexity Analysis**

* Time complexity : $O(n^2)$. Since expanding a palindrome around its center could take $O(n)$ time, the overall complexity is $O(n^2)$.

* Space complexity : $O(1)$.

## Approach 5: Manacher's Algorithm
There is even an $O(n)$ algorithm called Manacher's algorithm, explained here in detail. However, it is a non-trivial algorithm, and no one expects you to come up with this algorithm in a 45 minutes coding session. But, please go ahead and understand it, I promise it will be a lot of fun.

# Submissions
---
**Solution 1: (DP Bottom-Up)**
```
Runtime: 4736 ms
Memory Usage: N/A
```
```python
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        palindrom_begin_at = 0
        max_len = 0
        palindrom = [[0 for x in range(n)] for y in range(n)]

        # trivial case: single letter palindroms
        for i in range(n):
            palindrom[i][i] = True
            palindrom_begin_at = i
            max_len = 1

        # finding palindroms of 2 characters
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                palindrom[i][i + 1] = True
                palindrom_begin_at = i
                max_len = 2

        # finding palindroms of length 3 to n and saving the longest
        for cur_len in range(3, n+1):
            for i in range(n - cur_len+1):
                j = i + cur_len-1

                # the first last character should match
                # and rest of the substring should be a palindrom
                if s[i] == s[j] and palindrom[i + 1][j - 1] == True: 
                    palindrom[i][j] = True
                    palindrom_begin_at = i
                    max_len = cur_len

        if max_len >= 1:
            return s[palindrom_begin_at:palindrom_begin_at+max_len]
        else:
            return ""
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 2308 ms
Memory Usage: 20.4 MB
```
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, max_len, N= '', 0, len(s)
        dp = [[0]*N for _ in range(N)]
        for i in range(N):
            dp[i][i] = 1
            res = s[i]
            max_len = 1
        for i in range(N-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                res = s[i:i+2]
                max_len = 2
        for j in range(N):
            for i in range(j-1):
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = 1
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        res = s[i:j + 1]
                        
        return res
```

**Solution 4: (Dp Top-Down, Memory Limit Exceeded)**
```python
import functools
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        N = len(s)
        globMax = [0, 1]
        
        @functools.lru_cache(None)
        def dfs(left, right):
            nonlocal globMax
            # base case
            if left == right:
                return True
            if left > right:
                return False
            isPalindrome = False
            if s[left] == s[right] and (left + 1 == right or dfs(left + 1, right - 1)):
                isPalindrome = True
                if globMax[1] < right - left + 1:
                    globMax[0] = left;
                    globMax[1] = right - left + 1
            else:
                dfs(left + 1, right)
                dfs(left, right - 1)
            return isPalindrome
        
        dfs(0, N - 1)
        return s[globMax[0]:globMax[0] + globMax[1]]
```

**Solution 4: (Dp Top-Down)**
```
Runtime: 8024 ms
Memory Usage: 131.6 MB
```
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        N = len(s)
        start, max_len = 0, 1
        memo = [[False]*N for _ in range(N)]
        visited = [[False]*N for _ in range(N)]
        
        def dfs(left, right):
            nonlocal memo, visited, start, max_len
            # base case
            if left == right:
                return True
            if left > right:
                return False
            if visited[left][right]:
                return memo[left][right]
            isPalindrome = False
            if s[left] == s[right] and (left + 1 == right or dfs(left + 1, right - 1)):
                isPalindrome = True
                cur_len = right - left + 1
                if max_len < cur_len:
                    start = left
                    max_len = cur_len
            else:
                dfs(left + 1, right)
                dfs(left, right - 1)
            memo[left][right] = isPalindrome
            visited[left][right] = True
            return isPalindrome
        
        dfs(0, N - 1)
        return s[start:start + max_len]
```

**Solution 5: (Expand Around Center)**
```
Runtime: 936 ms
Memory Usage: 12.9 MB`
``
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        
        def expandAroundCenter(left, right):
            L, R = left, right
            while L >= 0 and R < len(s) and s[L] == s[R]:
                L -= 1
                R += 1
            return R - L - 1
        
        start, end = 0, 0
        for i in range(len(s)):
            len1 = expandAroundCenter(i, i);
            len2 = expandAroundCenter(i, i + 1);
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2;
                end = i + max_len // 2;

        return s[start:end + 1]
```