1461. Check If a String Contains All Binary Codes of Size K

Given a binary string `s` and an integer `k`.

Return True if all binary codes of length `k` is a substring of `s`. Otherwise, return False.

 

**Example 1:**
```
Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.
```

**Example 2:**
```
Input: s = "00110", k = 2
Output: true
```

**Example 3:**
```
Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
```

**Example 4:**
```
Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and doesn't exist in the array.
```

**Example 5:**
```
Input: s = "0000000001011100", k = 4
Output: false
```

**Constraints:**

* `1 <= s.length <= 5 * 10^5`
* `s` consists of 0's and 1's only.
* `1 <= k <= 20`

# Submissions
---
**Solution 1: (Sliding Window, Set)**
```
Runtime: 300 ms
Memory Usage: 27 MB
```
```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len({s[i:i + k] for i in range(len(s) - k + 1)}) == 2 ** k
```

**Solution 2: (Sliding Window, Set)**
```
Runtime: 648 ms
Memory Usage: 71.6 MB
```
```c++
class Solution {
public:
    bool hasAllCodes(string s, int k) {
        //Edge case
        if(k > s.size()) return false;

        unordered_set<string> res_set;

        //Insertion into the set
        for(int i =0;i<= s.size()-k;i++)
            res_set.insert(s.substr(i,k));

        //Comparing res with 2^k
        return res_set.size() == pow(2,k);
    }
};
```

**Solution 2: (Sliding Window, Bit Manipulation)**

    s = "0 0 1 1 0 1 1 0", k = 2
a        0 0 1 
           0
visited
0      t
1      t
2
3

```
Runtime: 10 ms, Beats 95.29%
Memory: 23.43 MB, Beats 91.49%
```
```c++
class Solution {
public:
    bool hasAllCodes(string s, int k) {
        int n = s.length(), i, a = 0;
        vector<bool> visited(1 << k);
        for (i = 0; i < n; i ++) {
            a = (a << 1) + s[i] - '0';
            if (i >= k - 1) {
                a = a % (1 << k);
                visited[a] = true;
            }
        }
        return all_of(visited.begin(), visited.end(), [](auto b){return b == true;});
    }
};
```
