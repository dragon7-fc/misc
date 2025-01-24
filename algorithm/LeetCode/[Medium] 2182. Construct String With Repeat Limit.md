2182. Construct String With Repeat Limit

You are given a string `s` and an integer `repeatLimit`. Construct a new string `repeatLimitedString` using the characters of `s` such that no letter appears more than `repeatLimit` times in a row. You do not have to use all characters from `s`.

Return the **lexicographically largest** `repeatLimitedString` possible.

A string `a` is **lexicographically larger** than a string `b` if in the first position where `a` and `b` differ, string `a` has a letter that appears later in the alphabet than the corresponding letter in `b`. If the first `min(a.length, b.length)` characters do not differ, then the longer string is the lexicographically larger one.

 

**Example 1:**
```
Input: s = "cczazcc", repeatLimit = 3
Output: "zzcccac"
Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
The letter 'a' appears at most 1 time in a row.
The letter 'c' appears at most 3 times in a row.
The letter 'z' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.
```

**Example 2:**
```
Input: s = "aababab", repeatLimit = 2
Output: "bbabaa"
Explanation: We use only some of the characters from s to construct the repeatLimitedString "bbabaa". 
The letter 'a' appears at most 2 times in a row.
The letter 'b' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa".
Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it is not a valid repeatLimitedString.
```

**Constraints:**

* `1 <= repeatLimit <= s.length <= 10^5`
* `s` consists of lowercase English letters.

# Submissions
---
**Solution 1: (Heap)**
```
Runtime: 1128 ms
Memory Usage: 16.8 MB
```
```python
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        pq = [(-ord(k), v) for k, v in Counter(s).items()] 
        heapify(pq)
        ans = []
        cnt = 0 
        while pq: 
            k, v = heappop(pq)
            if ans and ans[-1] == k and cnt == repeatLimit: 
                if not pq: break 
                kk, vv = heappop(pq)
                ans.append(kk)
                cnt = 1
                if vv-1: heappush(pq, (kk, vv-1))
                heappush(pq, (k, v))
            else: 
                if not ans or ans[-1] != k: cnt = 0 
                cnt += 1
                ans.append(k)
                if v-1: heappush(pq, (k, v-1))
        return "".join(chr(-x) for x in ans)
```

**Solution 2: (Heap)**
```
Runtime: 49 ms
Memory: 28.29 MB
```
```c++
class Solution {
public:
    string repeatLimitedString(string s, int repeatLimit) {
        unordered_map<char, int> freq;
        for (char ch : s) {
            freq[ch]++;
        }

        priority_queue<char> maxHeap;
        for (auto& [ch, count] : freq) {
            maxHeap.push(ch);
        }

        string result;

        while (!maxHeap.empty()) {
            char ch = maxHeap.top();
            maxHeap.pop();
            int count = freq[ch];

            int use = min(count, repeatLimit);
            result.append(use, ch);

            freq[ch] -= use;

            if (freq[ch] > 0 && !maxHeap.empty()) {
                char nextCh = maxHeap.top();
                maxHeap.pop();

                result.push_back(nextCh);
                freq[nextCh]--;

                if (freq[nextCh] > 0) {
                    maxHeap.push(nextCh);
                }

                maxHeap.push(ch);
            }
        }

        return result;
    }
};
```

**Solution 3: (Counter, two pointer)**
```
Runtime: 17 ms
Memory: 30.38 MB
```
```c++
class Solution {
public:
    string repeatLimitedString(string s, int repeatLimit) {
        int cnt[26] = {0}, i = 25, j = 26, k;
        string ans;
        for (auto c: s) {
            cnt[c-'a'] += 1;
        }
        while (i >= 0) {
            while (i >= 0 && !cnt[i]) {
                i -= 1;
            }
            if (i < 0) {
                break;
            }
            k = min(cnt[i], repeatLimit);
            ans += string(k, i+'a');
            cnt[i] -= k;
            if (cnt[i]) {
                while (j >= i) {
                    j = i-1;
                }
                while (j >= 0 && !cnt[j]) {
                    j -= 1;
                }
                if (j < 0) {
                    return ans;
                }
                cnt[j] -= 1;
                ans += string(1, j+'a');
            }
        }
        return ans;
    }
};
```
