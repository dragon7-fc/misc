214. Shortest Palindrome

Given a string **s**, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

**Example 1:**
```
Input: "aacecaaa"
Output: "aaacecaaa"
```

**Example 2:**
```
Input: "abcd"
Output: "dcbabcd"
```

# Solution
---
## Approach #1 Brute force [Accepted]
**Intuition**

According to the question, we are allowed to insert the characters only at the beginning of the string. Hence, we can find the largest segment from the beginning that is a palindrome, and we can then easily reverse the remaining segment and append to the beginning. This must be the required answer as no shorter palindrome could be found than this by just appending at the beginning.

For example: Take the string $\text{"abcbabcab"}$. Here, the largest palindrome segment from beginning is $\text{"abcba"}$, and the remaining segment is $\text{"bcab"}$. Hence the required string is reverse of $\text{"bcab"}$( = $\text{"bacb"}$) + original string( = $\text{"abcbabcab"}$) = $\text{"bacbabcbabcab"}$.

**Algorithm**

* Create the reverse of the original string $s$, say $\text{rev}$. This is used for comparison to find the largest palindrome segment from the front.
* Iterate over the variable $i$ from 0 to the $\text{size(s)}-1$:
    * If $s[0:n-i] == rev[i:]$ (i.e. substring of $s$ from $0$ to $n-i$ is equal to the substring of $\text{rev}$ from $i$ to the end of string). This essentially means that that substring from $0$ to $n-i$ is a palindrome, as $\text{rev}$ is the reverse of $s$.
    * Since, we find the larger palindromes first, we can return reverse of largest palindrome + $s$ as soon as we get it.
    
```c++
string shortestPalindrome(string s)
{
    int n = s.size();
    string rev(s);
    reverse(rev.begin(), rev.end());
    int j = 0;
    for (int i = 0; i < n; i++) {
        if (s.substr(0, n - i) == rev.substr(i))
            return rev.substr(0, i) + s;
    }
    return "";
}
```

**Complexity Analysis**

* Time complexity: $O(n^2)$.

We iterate over the entire length of string $s$.
In each iteration, we compare the substrings which is linear in size of substrings to be compared.
Hence, the total time complexity is $O(n*n) = O(n^2)$.

* Space complexity: $O(n)$ extra space for the reverse string $\text{rev}$.

## Approach #2 Two pointers and recursion [Accepted]
**Intuition**

In Approach #1, we found the largest palindrome substring from the string using substring matching which is $O(n)$ in length of substring. We could make the process more efficient if we could reduce the size of string to search for the substring without checking the complete substring each time.

Lets take a string $\text{"abcbabcaba"}$. Let us consider 2 pointers $i$ and $j$. Initialize $i = 0$. Iterate over $j$ from $n-1$ to $0$, incrementing $i$ each time $\text{s[i]==s[j]}$. Now, we just need to search in range $\text[0,i)$. This way, we have reduced the size of string to search for the largest palindrome substring from the beginning. The range $\text{[0,i)}$ must always contain the largest palindrome substring. The proof of correction is that: Say the string was a perfect palindrome, $i$ would be incremented $n$ times. Had there been other characters at the end, $i$ would still be incremented by the size of the palindrome. Hence, even though there is a chance that the range $\text{[0,i)}$ is not always tight, it is ensured that it will always contain the longest palindrome from the beginning.

The best case for the algorithm is when the entire string is palindrome and the worst case is string like $\text{"aababababababa"}$, wherein $i$ first becomes $12$(check by doing on paper), and we need to recheck in [0,12) corresponding to string $\text{"aabababababa"}$. Again continuing in the same way, we get ${i=10}$. In such a case, the string is reduced only by as few as 2 elements at each step. Hence, the number of steps in such cases is linear($n/2$).

This reduction of length could be easily done with the help of a recursive routine, as shown in the algorithm section.

**Algorithm**

The routine $\text{shortestPalindrome}$ is recursive and takes string $s$ as parameter:

* Initialize $i=0$
* Iterate over $j$ from $n-1$ to $0$:
    * If $\text{s[i]==s[j]}$, increase $i$ by $1$
* If ii equals the size of $s$, the entire string is palindrome, and hence return the entire string $s$.
* Else:
    * Return reverse of remaining substring after $i$ to the end of string + $\text{shortestPalindrome}$ routine on substring from start to index $i-1$ + remaining substring after $i$ to the end of string.

```c++
string shortestPalindrome(string s)
{
    int n = s.size();
    int i = 0;
    for (int j = n - 1; j >= 0; j--) {
        if (s[i] == s[j])
            i++;
    }
    if (i == n)
        return s;
    string remain_rev = s.substr(i, n);
    reverse(remain_rev.begin(), remain_rev.end());
    return remain_rev + shortestPalindrome(s.substr(0, i)) + s.substr(i);
}
```

**Complexity analysis**

* Time complexity: $O(n^2)$.
Each iteration of $\text{shortestPalindrome}$ is linear in size of substring and the maximum number of recursive calls can be $n/2$ times as shown in the Intuition section.
Let the time complexity of the algorithm be T(n). Since, at the each step for the worst case, the string can be divide into 2 parts and we require only one part for further computation. Hence, the time complexity for the worst case can be represented as : $T(n)=T(n-2)+O(n)$. So, $T(n) = O(n) + O(n-2) + O(n-4) + ... + O(1)$ which is $O(n^2)$.
Thanks @CONOVER for the time complexity analysis.

* Space complexity: $O(n)$ extra space for $\text{remain_rev}$ string.


## Approach #3 KMP [Accepted]
**Intuition**

We have seen that the question boils down to finding the largest palindrome substring from the beginning.

The people familiar with KMP(Knuth–Morris–Pratt) algorithm may wonder that the task at hand can be easily be compared with the concept of the lookup table in KMP.

KMP Overview:

KMP is a string matching algorithm that runs in $O(n+m)$ times, where $n$ and $m$ are sizes of the text and string to be searched respectively. The key component of KMP is the failure function lookup table,say $f(s)$. The purpose of the lookup table is to store the length of the proper prefix of the string $b_{1}b_{2}...b_{s}$ that is also a suffix of $b_{1}b_{2}...b_{s}$. This table is important because if we are trying to match a text string for $b_{1}b_{2}...b_{n}$, and we have matched the first ss positions, but when we fail, then the value of lookup table for ss is the longest prefix of $b_{1}b_{2}...b_{n}$ that could possibly match the text string upto the point we are at. Thus, we don't need to start all over again, and can resume searching from the matching prefix.

The algorithm to generate the lookup table is easy and inutitive, as given below:
```
f(0) = 0
for(i = 1; i < n; i++)
{
	t = f(i-1)
	while(t > 0 && b[i] != b[t])
		t = f(t-1)
	if(b[i] == b[t]){
		++t
	f(i) = t
}
```
* Here, we first set f(0)=0 since, no proper prefix is available.
* Next, iterate over $i$ from $1$ to $n-1$:
    * Set $t=f(i-1)$
    * While t>0 and char at $i$ doesn't match the char at $t$ position, set $t=f(t)$, which essentially means that we have problem matching and must consider a shorter prefix, which will be $b_{f(t-1)}$, until we find a match or t becomes 0.
    * If $b_{i}==b_{t}$, add 1 to t
    * Set $f(i)=t$
    
The lookup table generation is as illustrated below:

![214_shortest_palindrome.png](img/214_shortest_palindrome.png)

Wait! I get it!!

In Approach #1, we reserved the original string ss and stored it as $\text{rev}$. We iterate over $i$ from $0$ to $n-1$ and check for $s[0:n-i] == rev[i:]$. Pondering over this statement, had the $\text{rev}$ been concatenated to $s$, this statement is just finding the longest prefix that is equal to the suffix. Voila!

**Algorithm**

* We use the KMP lookup table generation
* Create $\text{new_s} as s + \text{"#"} + \text{reverse(s)}$ and use the string in the lookup-generation algorithm
* The "#" in the middle is required, since without the #, the 2 strings could mix with each other, producing wrong answer. For example, take the string $\text{"aaaa"}$. Had we not inserted "#" in the middle, the new string would be $\text{"aaaaaaaa"}$ and the largest prefix size would be 7 corresponding to "aaaaaaa" which would be obviously wrong. Hence, a delimiter is required at the middle.
* Return reversed string after the largest palindrome from beginning length(given by n-\$text{f[n_new-1]}$) + original string $s$

```c++
string shortestPalindrome(string s)
{
    int n = s.size();
    string rev(s);
    reverse(rev.begin(), rev.end());
    string s_new = s + "#" + rev;
    int n_new = s_new.size();
    vector<int> f(n_new, 0);
    for (int i = 1; i < n_new; i++) {
        int t = f[i - 1];
        while (t > 0 && s_new[i] != s_new[t])
            t = f[t - 1];
        if (s_new[i] == s_new[t])
            ++t;
        f[i] = t;
    }
    return rev.substr(0, n - f[n_new - 1]) + s;
}
```

**Complexity analysis**

* Time complexity: $O(n)$.

In every iteration of the inner while loop, tt decreases until it reaches 0 or until it matches. After that, it is incremented by one. Therefore, in the worst case, tt can only be decreased up to nn times and increased up to $n$ times.
Hence, the algorithm is linear with maximum $(2 * n) * 2$ iterations.

* Space complexity: $O(n)$. Additional space for the reverse string and the concatenated string.

# Submissions
---
**Solution 1: (Brute force)**
```
Runtime: 520 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        N = len(s)
        for i in range(N):
            if s[:N-i] == s[::-1][i:]:
                return s[::-1][:i] + s
        
        return ""
```

**Solution 2: (Two pointers and recursion)**
```
Runtime: 52 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        N = len(s)
        i = 0
        for j in range(N-1, -1, -1):
            if s[i] == s[j]:
                i += 1
        if i == N:
            return s
        remain_rev = s[i:][::-1]
        return remain_rev + self.shortestPalindrome(s[:i]) + s[i:]
```

**Solution 3: (KMP)**
```
Runtime: 112 ms
Memory Usage: 17 MB
```
```python
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        rev = s[::-1]
        s_new = s + "#" + rev
        n_new = len(s_new)
        f = [0]*n_new
        for i in range(1, n_new):
            t = f[i - 1]
            while t > 0 and s_new[i] != s_new[t]:
                t = f[t - 1]
            if s_new[i] == s_new[t]:
                t += 1
            f[i] = t
            
        return rev[:n - f[n_new - 1]] + s
```

**Solution 4: (Brute force, Time Limit Exceeded)**
```c++
class Solution {
public:
    string shortestPalindrome(string s) {
        int n = s.size();
        string rev(s);
        reverse(rev.begin(), rev.end());
        int j = 0;
        for (int i = 0; i < n; i++) {
            if (s.substr(0, n - i) == rev.substr(i))
                return rev.substr(0, i) + s;
        }
        return "";
    }
};
```

**Solution 5: (Two pointers and recursion)**
```
Runtime: 12 ms
Memory Usage: 7.4 MB
```
```c++
class Solution {
public:
    string shortestPalindrome(string s) {
        int n = s.size();
        int i = 0;
        for (int j = n - 1; j >= 0; j--) {
            if (s[i] == s[j])
                i++;
        }
        if (i == n)
            return s;
        string remain_rev = s.substr(i, n);
        reverse(remain_rev.begin(), remain_rev.end());
        return remain_rev + shortestPalindrome(s.substr(0, i)) + s.substr(i);
    }
};
```

**Solution 6: (KMP)**
```
Runtime: 20 ms
Memory Usage: 8 MB
```
```c++
class Solution {
public:
    string shortestPalindrome(string s) {
        int n = s.size();
        string rev(s);
        reverse(rev.begin(), rev.end());
        string s_new = s + "#" + rev;
        int n_new = s_new.size();
        vector<int> f(n_new, 0);
        for (int i = 1; i < n_new; i++) {
            int t = f[i - 1];
            while (t > 0 && s_new[i] != s_new[t])
                t = f[t - 1];
            if (s_new[i] == s_new[t])
                ++t;
            f[i] = t;
        }
        return rev.substr(0, n - f[n_new - 1]) + s;
    }
};
```