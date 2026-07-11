3756. Concatenate Non-Zero Digits and Multiply by Sum II

You are given a string `s` of length `m` consisting of digits. You are also given a 2D integer array `queries`, where `queries[i] = [li, ri]`.

For each `queries[i]`, extract the substring `s[li..ri]`. Then, perform the following:

* Form a new integer `x` by concatenating all the non-zero digits from the substring in their original order. If there are no non-zero digits, `x = 0`.
* Let sum be the sum of digits in `x`. The answer is `x * sum`.

Return an array of integers `answer` where `answer[i]` is the answer to the `i`th query.

Since the answers may be very large, return them modulo `10^9 + 7`.

 

**Example 1:**
```
Input: s = "10203004", queries = [[0,7],[1,3],[4,6]]

Output: [12340, 4, 9]

Explanation:

s[0..7] = "10203004"
x = 1234
sum = 1 + 2 + 3 + 4 = 10
Therefore, answer is 1234 * 10 = 12340.
s[1..3] = "020"
x = 2
sum = 2
Therefore, the answer is 2 * 2 = 4.
s[4..6] = "300"
x = 3
sum = 3
Therefore, the answer is 3 * 3 = 9.
```

**Example 2:**
```
Input: s = "1000", queries = [[0,3],[1,1]]

Output: [1, 0]

Explanation:

s[0..3] = "1000"
x = 1
sum = 1
Therefore, the answer is 1 * 1 = 1.
s[1..1] = "0"
x = 0
sum = 0
Therefore, the answer is 0 * 0 = 0.
```

**Example 3:**
```
Input: s = "9876543210", queries = [[0,9]]

Output: [444444137]

Explanation:

s[0..9] = "9876543210"
x = 987654321
sum = 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45
Therefore, the answer is 987654321 * 45 = 44444444445.
We return 44444444445 modulo (109 + 7) = 444444137.
```

**Constraints:**

* `1 <= m == s.length <= 10^5`
* `s` consists of digits only.
* `1 <= queries.length <= 10^5`
* `queries[i] = [li, ri]`
* `0 <= li <= ri < m`

# Submissions
---
**Solution 1: (Prefix Sum)**
```
Runtime: 48 ms, Beats 55.59%
Memory: 160.42 MB, Beats 57.54%
```
```c++
class Solution {
public:
    vector<int> sumAndMultiply(string s, vector<vector<int>>& queries) {
        int n = s.length(), m = queries.size(), MOD = 1e9 + 7, i, dig, l, r;
        long long cnt;
        vector<long long> pre(n), count(n), sum(n), pow10(n + 1);
        pow10[0] = 1;
        for (i = 1; i <= n; i ++) {
            pow10[i] = (pow10[i - 1] * 10) % MOD;
        }
        for (i = 0; i < n; i ++) {
            dig = (s[i] - '0');
            if (i) { 
                pre[i] = pre[i - 1];
                sum[i] = sum[i - 1];
                count[i] = count[i - 1];
            }
            if (dig) { 
                pre[i] = (pre[i] * 10 + dig) % MOD;
                sum[i] += dig;
                count[i] += 1;
            }
        }
        i = 0;
        vector<int> res(m);
        for (auto &query : queries) {
            l = query[0];
            r = query[1];
            cnt = count[r] - (l ? count[l - 1] : 0);
            if (!cnt) {
                res[i] = 0;
            } else {
                long long dig_sum = sum[r] - (l ? sum[l - 1] : 0);
                long long left_sum = l ? pre[l - 1] : 0;
                long long px = (pre[r] - left_sum * pow10[cnt]) % MOD;
                if (px < 0) {
                    px += MOD;
                }
                res[i] = (px * dig_sum) % MOD;
            }
            i += 1;
        }
        return res;
    }
};
```

**Solution 2: (Prefix Sum, Math, generate number from precomputed non-zero prefix and count difference)**

pre[i]
= non-zero digit till i
cnt[i]
= non-zero digit count till i
query[left,right]
= pre[right + 1] - pre[left] * 10**(cnt[right + 1] - cnt[left])
                                   ------------k---------------
                               --------------------------------
                                       power10[k]

queries
                 v   v
           x   x
         v             v
idx      0   2   4     7
    s = "1 0 2 0 3 0 0 4", queries = [[0,7],[1,3],[4,6]]
pre      0 1   12  123   1234
cnt      0 1   2   3     4
sum      0 1   3   6     10

```
Runtime: 36 ms, Beats 74.61%
Memory: 155.22 MB, Beats 63.21%
```
```c++
class Solution {
    const int MOD = 1e9 + 7;
public:
    vector<int> sumAndMultiply(string s, vector<vector<int>>& queries) {
        int m = s.length();
        vector<long long> power10(m + 1);
        vector<long long> pre(m + 1);
        vector<int> cnt(m + 1);
        vector<long long> sum(m + 1);
        power10[0] = 1;
        for (int i = 1; i <= m; i ++) {
            power10[i] = (power10[i - 1] * 10) % MOD;
        }
        for (int i = 0; i < m; i ++) {
            int d = s[i] - '0';
            if (d) {
                pre[i + 1] = (pre[i] * 10 + d) % MOD;
                cnt[i + 1] = cnt[i] + 1;
            } else {
                pre[i + 1] = pre[i];
                cnt[i + 1] = cnt[i];
            }
            sum[i + 1] = sum[i] + d;
        }
        int n = queries.size();
        vector<int> ans(n);
        for (int i = 0; i < n; i ++) {
            int left = queries[i][0];
            int right = queries[i][1];
            int k = cnt[right + 1] - cnt[left];
            long long x = ((pre[right + 1] - (pre[left] * power10[k]) % MOD) + MOD) % MOD;
            int csum = sum[right + 1] - sum[left];
            ans[i] = (x * csum) % MOD;
        }
        return ans;
    }
};
```

**Solution 3: (Prefix Sum, Math, generate number from precomputed non-zero prefix and count difference)**
```
Runtime: 16 ms, Beats 98.96%
Memory: 145.40 MB, Beats 88.60%
```
```c++
const static int MOD = 1e9 + 7;
static long long power10[100001];
int init = []() {
    power10[0] = 1;
    for (int i = 1; i <= 100000; i ++) {
        power10[i] = (power10[i - 1] * 10) % MOD;
    }
    return 0;
}();

class Solution {
public:
    vector<int> sumAndMultiply(string s, vector<vector<int>>& queries) {
        int m = s.length();
        vector<long long> pre(m + 1);
        vector<int> cnt(m + 1);
        vector<long long> sum(m + 1);
        for (int i = 0; i < m; i ++) {
            int d = s[i] - '0';
            if (d) {
                pre[i + 1] = (pre[i] * 10 + d) % MOD;
                cnt[i + 1] = cnt[i] + 1;
            } else {
                pre[i + 1] = pre[i];
                cnt[i + 1] = cnt[i];
            }
            sum[i + 1] = sum[i] + d;
        }
        int n = queries.size();
        vector<int> ans(n);
        for (int i = 0; i < n; i ++) {
            int left = queries[i][0];
            int right = queries[i][1];
            int k = cnt[right + 1] - cnt[left];
            long long x = ((pre[right + 1] - (pre[left] * power10[k]) % MOD) + MOD) % MOD;
            int csum = sum[right + 1] - sum[left];
            ans[i] = (x * csum) % MOD;
        }
        return ans;
    }
};
```
