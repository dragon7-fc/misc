1177. Can Make Palindrome from Substring

Given a string `s`, we make queries on substrings of `s`.

For each query `queries[i] = [left, right, k]`, we may **rearrange** the substring `s[left], ..., s[right]`, and then choose **up to** `k` of them to replace with any lowercase English letter. 

If the substring is possible to be a palindrome string after the operations above, the result of the query is `true`. Otherwise, the result is `false`.

Return an array `answer[]`, where `answer[i]` is the result of the `i`-th query `queries[i]`.

Note that: Each letter is counted individually for replacement so if for example `s[left..right] = "aaa"`, and `k = 2`, we can only replace two of the letters.  (Also, note that the initial string `s` is never modified by any query.)

 

**Example :**
```
Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
Output: [true,false,false,true,true]
Explanation:
queries[0] : substring = "d", is palidrome.
queries[1] : substring = "bc", is not palidrome.
queries[2] : substring = "abcd", is not palidrome after replacing only 1 character.
queries[3] : substring = "abcd", could be changed to "abba" which is palidrome. Also this can be changed to "baab" first rearrange it "bacd" then replace "cd" with "ab".
queries[4] : substring = "abcda", could be changed to "abcba" which is palidrome.
``` 

**Constraints:**

* `1 <= s.length, queries.length <= 10^5`
* `0 <= queries[i][0] <= queries[i][1] < s.length`
* `0 <= queries[i][2] <= s.length`
* `s` only contains lowercase English letters.

# Submissions
---
**Solution 1: (DP, Bit Manipulation)**

First, the key is understanding we are allowed to rearrange. Knowing this, we can forget about order and only count the occurences of each letter.
Furthermore, we only care if the count is odd. If it's even, we can place an equal amount of letter on either side:
'aaaac' => 'aacaa'
Since 'a''s count is even (4), we can ignore it.

In order to convert a string to a palindrome using replace, we need only to replace half of the letters. For example,
'abcd' => 'abba' (4 // 2 = 2)
'abcde' => 'abcba' (5 // 2 = 2)
Hence, we only need k to be at least half rounded down.

Naively, we can use collections.Counter() to count the letters in the substring, check how many are odd, divide that by 2 (rounded down) and check <= k.
```
  def canMakePaliQueries(s, queries):
      ans = []
      for l, r, k in queries:
          ss = s[l:r+1]
          rem = 0
          for letter, n in collections.Counter(ss).items():
              rem += n % 2
          need = rem // 2
          ans.append(need <= k)
      return ans
```
However, we are counting letters for every substring, which may overlap with previous calculations. This solution gives Time Limit Exceeded.

Therefore, we can optimize by caching previous results. We can say dp[i] represents the count of all the letters in s[:i]. Then we know that the counts of dp[l] subtracted from dp[r+1] will give us the count of all the letters in the substring s[l:r+1]. We could naively store them all in collections.Counter():
```python
  def canMakePaliQueries(s, queries):
      dp = [collections.Counter()]
      for i in range(1, len(s)+1):
          dp.append(dp[i-1] + collections.Counter(s[i-1]))
      ans = []
      for l, r, k in queries:
          c = dp[r+1] - dp[l]
          need = sum(v % 2 for v in c.values()) // 2
          ans.append(need <= k)
      return ans
```
However, the overhead is too great. This solution still gives Time Limit Exceeded. We can simplify by realizing we only care about lowercase letters, 26 in total. We can store our data in an array of size 26 for each substring:

```python
  def canMakePaliQueries(s, queries):
      N = 26
      a = ord('a')
      dp = [[0] * N]
      for i in range(1, len(s)+1):
          new = dp[i-1][:]
          j = ord(s[i-1]) - a
          new[j] += 1
          dp.append(new)
      ans = []
      for l, r, k in queries:
          L = dp[l]
          R = dp[r+1]
          ans.append(sum((R[i] - L[i]) & 1 for i in range(N)) // 2 <= k)
      return ans
```
This solution is accepted!

Furthermore, observe that once we subtract the sums we are only looking at & 1 (the last bit) to see if it's odd or even. Therefore, we only need to store binary values of either 0 or 1 in the first place. Thus we make our final optimization by storing the count of the letters in a single 32-bit integer, since we only need to use 26 bits. Then we can XOR the substrings' counts to get the difference. Then we can count the number of 1 bits to know how many letters need to be changed.

Final solution:
```python
def canMakePaliQueries(s, queries):
    N = 26
    S = len(s) + 1
    ints = list(map(lambda c: ord(c) - ord('a'), s))

    dp = [0] * S
    for i in range(1, S):
        dp[i] = dp[i-1] ^ (1 << ints[i-1])

    ones = lambda x: bin(x).count('1')
    return [
        ones(dp[r+1] ^ dp[l]) >> 1 <= k
        for l, r, k in queries
    ]
```
```
Runtime: 1608 ms
Memory Usage: 61 MB
```
```python
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        N = 26
        S = len(s) + 1
        ints = list(map(lambda c: ord(c) - ord('a'), s))

        dp = [0] * S
        for i in range(1, S):
            dp[i] = dp[i-1] ^ (1 << ints[i-1])

        ones = lambda x: bin(x).count('1')
        return [
            ones(dp[r+1] ^ dp[l]) >> 1 <= k
            for l, r, k in queries
        ]
```

**Solution 2: (DP, Bit Manipulation)**
```
Runtime: 541 ms
Memory: 95.2 MB
```
```c++
class Solution {
public:
    vector<bool> canMakePaliQueries(string s, vector<vector<int>>& queries) {
        int mask = 0;
        vector<int> dp(1);
        for (char c : s)
            dp.push_back(mask ^= 1 << (c - 'a'));

        vector<bool> ans;
        for (auto &q : queries) {
            int ones = __builtin_popcount(dp[q[1] + 1] ^ dp[q[0]]);
            ans.push_back(q[2] >= ones / 2);
        }
        return ans;
    }
};
```
