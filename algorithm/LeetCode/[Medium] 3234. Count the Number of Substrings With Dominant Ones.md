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
```
Runtime: 11238 ms
Memory: 16.78 MB
```
```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        result = 0
        
        # Iterate through possible zero counts (1 to sqrt(n))
        for k in range(1, int(n**0.5) + 1):
            zeros = deque()  # Queue to store positions of zeros
            lastzero = -1    # Position of the zero before the first zero in our window
            ones = 0         # Count of ones in our current window
            
            # Scan through the string
            for right in range(n):
                if s[right] == '0':
                    zeros.append(right)
                    # If we have more than k zeros, remove the leftmost one
                    while len(zeros) > k:
                        ones -= (zeros[0] - lastzero - 1)  # Subtract ones between lastzero and the removed zero
                        lastzero = zeros.popleft()
                else:
                    ones += 1
                
                # If we have exactly k zeros and at least k^2 ones
                if len(zeros) == k and ones >= k**2:
                    # Add the minimum of:
                    # 1. Number of ways to extend to the left (zeros[0] - lastzero)
                    # 2. Number of ways to extend to the right (ones - k**2 + 1)
                    result += min(zeros[0] - lastzero, ones - k**2 + 1)
        
        # Handle all-ones substrings
        i = 0
        while i < n:
            if s[i] == '0':
                i += 1
                continue
            sz = 0
            while i < n and s[i] == '1':
                sz += 1
                i += 1
            # Add number of all-ones substrings
            result += (sz * (sz + 1)) // 2
        
        return result
```

**Solution 2: (Sliding Window, O(n sqrt(n)))**

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

**Solution 3: (Sliding Window, Brute Force, O(n sqrt(n)))**

dominant ones
-> cnt[1] >= cnt[0]^2
  -------    ------
   >= z^2       z


        ...   0  ...   x
        ^i    ^p       ^j
        ------     ----
           p-i      cnt[1]-z^2   
cnt[0]                 z
cnt[1]                 >= z^2

          0  1  2  3  4
     s = "0  0  0  1  1"
cnt
0         1  2  3
1                  1  2
z: 0
                   i
                      j
                      p
ans               +1 +2
z: 1
                i
                      j
                p
ans               +1 +1
```
Runtime: 471 ms, Beats 38.93%
Memory: 13.98 MB, Beats 88.59%
```
```c++
class Solution {
public:
    int numberOfSubstrings(string s) {
        int n = s.size(), z, p, i, j, cnt[2], ans = 0;
        //          cnt[0]
        //              cnt[1]
        //          v   vvvvv
        for (z = 0; z + z * z <= n; z ++) {
            cnt[0] = 0, cnt[1] = 0, p = 0;
                                    ^first zero after i
            for (i = 0, j = 0; j < n; j ++) {
                cnt[s[j] == '1'] += 1;
                while (cnt[0] > z) {
                    cnt[s[i] == '1'] -= 1;
                    i += 1;
                }
                if (cnt[0] == z && cnt[1] && cnt[1] >= z * z) {
                    for (p = max(p, i); p < j && s[p] == '1'; p ++);
                    ans += 1 + min(p - i, cnt[1] - z * z);
                                          ^^^^^^^^^^^^^^
                                            1s >= 0s^2
                }
            }
        }
        return ans;
    }
};
```

**Solution 4: (Sliding Window, Prefix Sum, Brute Force, Enumeration, O(n sqrt(n)))**

        0    i
s      [ ... 0  ...]
pre            i       // position of the nearest zero before

             vpre[j]
        j2   j   i
s    [..0....0.......]
pre          j2  j
             ----^
        ------
                  cnt0
                  = s[i] == '0'
                  cnt1
                  = i - pre[i] - cnt0
             cnt0
             = cnt0 + 1
             cnt
             i - pre[j2] - cnt0


          0  1  2  3  4  5
s            0  0  0  1  1 
pre      -1  0  1  2  3  3
         xxxxx 
          1-base
                          
    i  j  pre[j]  cnt0  cnt1  res
    1  1      0      1     0
       0
    2  2      1      1     0
       1      0      2     0
       0
    3  3      2      1     0
       2      1      2     0
       1      0      3     0
       0
    4  4      3      0     1   +1
       3      2      1     1   +1
       2      1      2     1
       1      0      3     1
       0
    5  5      3      0     2   +2
       3      2      1     2   +1
       2      1      2     2
       1      0      3     2
       0
                  
              v
s     0 1 2 3 4 5
        0 0 0 1 1
pre  -1 0 1 2 3 3
              -  
cnt0          0
cbt1          1
ans        j - pre[j] = 1
                v
      0 1 2 3 4 5
s       1 0 1 1 0 1 
pre  -1 0 0 2 2 2 5
              ---
           ------

cnt0            1
cnt1            2
ans        cnt1 - cnt0*cnt0 + 1 = 2

```
Runtime: 155 ms, Beats 87.92%
Memory: 18.26 MB, Beats 35.57%
```
```c++
class Solution {
public:
    int numberOfSubstrings(string s) {
        int n = s.size();
        vector<int> pre(n + 1);  // position of the nearest zero before
        pre[0] = -1;  // 1-base
        for (int i = 0; i < n; i++) {
            if (i == 0 || (i > 0 && s[i - 1] == '0')) {
                pre[i + 1] = i;
            } else {
                pre[i + 1] = pre[i];
            }
        }
        int res = 0;
        for (int i = 1; i <= n; i++) {
            int cnt0 = s[i - 1] == '0';
            int j = i;
            while (j > 0 && cnt0 * cnt0 <= n) {
                int cnt1 = (i - pre[j]) - cnt0;
                if (cnt0 * cnt0 <= cnt1) {
                    res += min(j - pre[j], cnt1 - cnt0 * cnt0 + 1);
                }
                j = pre[j];
                cnt0++;
            }
        }
        return res;
    }
};
```
