471. Encode String with Shortest Length

Given a **non-empty** string, encode the string such that its encoded length is the shortest.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly k times.

**Note:**

* k will be a positive integer and encoded string will not be empty or have extra space.
* You may assume that the input string contains only lowercase English letters. The string's length is at most 160.
* If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them is fine.
 

**Example 1:**
```
Input: "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.
```

**Example 2:**
```
Input: "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
```

**Example 3:**
```
Input: "aaaaaaaaaa"
Output: "10[a]"
Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
```

**Example 4:**
```
Input: "aabcaabcd"
Output: "2[aabc]d"
Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
```

**Example 5:**
```
Input: "abbbabbbcabbbabbbc"
Output: "2[2[abbb]c]"
Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", so one answer can be "2[2[abbb]c]".
```

# Submissions
---
**Solution 1: (DP Top-Down)**

For any s, you can either

1. Do not encode it
1. Or encode it to one string if possible
1. Or, split it into two, encode the two substring to their shortest possible length, and combine them

Pick up the shortest result from 1~3.
During this process, you should remember the best encoding result for all substrings so that it can be reused.

For #2, you can use LeetCode 459: Repeated Substring Pattern to find out whether the "s" is repeated or not, and how many times it is repeated:
"i=(s+s).find(s,1)"
"i" is the length of repeating pattern. If i>=len(s), then s is not repeated.

```
Runtime: 264 ms
Memory Usage: 16.1 MB
```
```python
class Solution:
    @functools.lru_cache(None)
    def encode(self, s: str) -> str:
        i = (s+s).find(s,1)
        encoded = str(len(s)//i) + '[' + self.encode(s[:i])+ ']' if i < len(s) else s
        splitEncoded = [self.encode(s[:i]) + self.encode(s[i:]) for i in range(1,len(s))]
        return min(splitEncoded + [encoded], key=len)
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 87 ms, Beats 20.00%
Memory: 29.30 MB, Beats 33.33%
```
```c++
class Solution {
    vector<vector<string>> dp;
	string collapse(string& s, int i, int j) {
	    string temp = s.substr(i, j - i + 1);
		auto pos = (temp+temp).find(temp, 1);
		if (pos >= temp.size()) {
		    return temp;
		}
		return to_string(temp.size()/pos) + '['+ dp[i][i+pos-1]+']';
	}
public:
    string encode(string s) {
        int n = s.size();
		dp = vector<vector<string>>(n, vector<string>(n, ""));
		for (int step = 1; step <= n; step++) {
			for (int i = 0; i + step - 1 < n; i++) {
				int j = i + step - 1;
				dp[i][j] = s.substr(i, step);
				for (int k = i; k < j; k++) {
					auto left = dp[i][k];
					auto right = dp[k + 1][j];
					if (left.size() + right.size() < dp[i][j].size()) {
						dp[i][j] = left + right;
					}
				}
				string replace = collapse(s, i, j);
				if (replace.size() < dp[i][j].size()) {
					dp[i][j] = replace;
				}
			}
		}
		return dp[0][n - 1];
    }
};
```

**Solution 3: (DP Top-Down)**

    "aaaaaaaaaa"
    -> a9[a]

```
Runtime: 59 ms, Beats 33.33%
Memory: 26.20 MB, Beats 33.33%
```
```c++
class Solution {
    int numRepetition(string &s, string &t) {
        int cnt = 0, i = 0;
        while (i < s.length()) {
            if (s.substr(i, t.length()) != t) {
                break;
            }
            cnt += 1;
            i += t.length();
        }
        return cnt;
    }
    string dfs(string s, unordered_map<string,string> &mp) {
        if (s.length() < 5) {
            return s;
        }
        if (mp.count(s)) {
            return mp[s];
        }
        string res = s;
        for (int i = 0; i < s.length(); i++) {
            string s1 = s.substr(0, i+1);
            int cnt = numRepetition(s, s1);
            string t;
            for (int k = 1; k <= cnt; k++) {
                if (k == 1) {
                    t = s1 + dfs(s.substr(i + 1), mp);
                } else {
                    t = to_string(k) + "[" + dfs(s1, mp) + "]" + dfs(s.substr(k * s1.length()), mp);
                }
                if (t.length() < res.length()) {
                    res = t;
                }            
            }
        }
        mp[s] = res;
        return res;        
    }
public:
    string encode(string s) {
        unordered_map<string,string> mp;
        return dfs(s, mp);
    }
};
```
