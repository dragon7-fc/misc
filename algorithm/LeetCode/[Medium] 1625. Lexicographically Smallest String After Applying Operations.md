1625. Lexicographically Smallest String After Applying Operations

You are given a string `s` of **even length** consisting of digits from `0` to `9`, and two integers `a` and `b`.

You can apply either of the following two operations any number of times and in any order on `s`:

* Add `a` to all odd indices of `s` (`0`-indexed). Digits post `9` are cycled back to `0`. For example, if `s = "3456"` and `a = 5`, `s` becomes `"3951"`.
* Rotate `s` to the right by `b` positions. For example, if `s = "3456"` and `b = 1`, `s` becomes `"6345"`.

Return the **lexicographically smallest** string you can obtain by applying the above operations any number of times on `s`.

A string `a` is lexicographically smaller than a string `b` (of the same length) if in the first position where `a` and `b` differ, string `a` has a letter that appears earlier in the alphabet than the corresponding letter in `b`. For example, `"0158"` is lexicographically smaller than `"0190"` because the first position they differ is at the third letter, and `'5'` comes before `'9'`.

 

**Example 1:**
```
Input: s = "5525", a = 9, b = 2
Output: "2050"
Explanation: We can apply the following operations:
Start:  "5525"
Rotate: "2555"
Add:    "2454"
Add:    "2353"
Rotate: "5323"
Add:    "5222"
​​​​​​​Add:    "5121"
​​​​​​​Rotate: "2151"
​​​​​​​Add:    "2050"​​​​​​​​​​​​
There is no way to obtain a string that is lexicographically smaller then "2050".
```

**Example 2:**
```
Input: s = "74", a = 5, b = 1
Output: "24"
Explanation: We can apply the following operations:
Start:  "74"
Rotate: "47"
​​​​​​​Add:    "42"
​​​​​​​Rotate: "24"​​​​​​​​​​​​
There is no way to obtain a string that is lexicographically smaller then "24".
```

**Example 3:**
```
Input: s = "0011", a = 4, b = 2
Output: "0011"
Explanation: There are no sequence of operations that will give us a lexicographically smaller string than "0011".
```

**Example 4:**
```
Input: s = "43987654", a = 7, b = 3
Output: "00553311"
```

**Constraints:**

* `2 <= s.length <= 100`
* `s.length is even`.
* `s` consists of digits from `0` to `9` only.
* `1 <= a <= 9`
* `1 <= b <= s.length - 1`

# Submissions
---
**Solution 1: (BFS, BFS with seen)**

1. Use a Queue / deque to held the strings after applying operations;
1. Use a Set to avoid duplication;
1. During BFS, for each polled out string, compare it to the currently smallest string and update the smallest if necessary; apply the 2 operations and put the resulted 2 strings into the Queue / deque if never seen them before;
1. The smallest string found after BFS is the solution.

```
Runtime: 1484 ms
Memory Usage: 15.7 MB
```
```python
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        dq, seen, smallest = deque([s]), {s}, s
        while dq:
            cur = dq.popleft()
            if smallest > cur:
                smallest = cur
            addA = list(cur)    
            for i, c in enumerate(addA):
                if i % 2 == 1:
                    addA[i] = str((int(c) + a) % 10)
            addA = ''.join(addA)        
            if addA not in seen:
                seen.add(addA);
                dq.append(addA)
            rotate = cur[-b :] + cur[: -b]
            if rotate not in seen:
                seen.add(rotate)
                dq.append(rotate)
        return smallest
```

**Solution 2: (DFS, DFS with seen)**
```
Runtime: 2004 ms
Memory Usage: 33.8 MB
```
```python
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        rec = set()
        
        def dfs(s):
            if s in rec:
                return           
            rec.add(s)
            dfs(s[-b:] + s[:-b])
            dfs("".join([str((int(c) + a * (i % 2)) % 10) for i, c in enumerate(s)]))
            
        dfs(s)
        return min(rec)
```

**Solution 3: (BFS, Brute Force, O(n^2 * d^2))**
```
Runtime: 171 ms, Beats 75.22%
Memory: 90.84 MB, Beats 50.88%
```
```c++
class Solution {
public:
    string findLexSmallestString(string s, int a, int b) {
        int n = s.size(), i;
        queue<string> q;
        unordered_set<string> st;
        string ns, ans = s;
        q.push(s);
        st.insert(s);
        while (q.size()) {
            auto cs = q.front();
            q.pop();
            ns = cs.substr(n - b) + cs.substr(0, n - b);
            if (!st.count(ns)) {
                q.push(ns);
                st.insert(ns);
                ans = min(ans, ns);
            }
            for (i = 1; i < n; i += 2) {
                cs[i] = (cs[i] + a - '0') % 10 + '0';
            }
            if (!st.count(cs)) {
                q.push(cs);
                st.insert(cs);
                ans = min(ans, cs);
            }
        }
        return ans;
    }
};
```

**Solution 4: (Enumeration, better brute force, O(n^2 * d^2))**
```
Runtime: 3 ms, Beats 94.69%
Memory: 9.05 MB, Beats 92.92%
```
```c++
class Solution {
public:
    string findLexSmallestString(string s, int a, int b) {
        int n = s.size();
        string res = s;
        s = s + s;
        int g = gcd(b, n);

        auto add = [&](string& t, int start) {
            int minVal = 10, times = 0;
            for (int i = 0; i < 10; i++) {
                int added = ((t[start] - '0') + i * a) % 10;
                if (added < minVal) {
                    minVal = added;
                    times = i;
                }
            }
            for (int i = start; i < n; i += 2) {
                t[i] = '0' + ((t[i] - '0') + times * a) % 10;
            }
        };

        for (int i = 0; i < n; i += g) {
            string t = s.substr(i, n);
            add(t, 1);
            if (b % 2) {
                add(t, 0);
            }
            res = min(res, t);
        }
        return res;
    }
};
```
