3998. Transform Binary String Using Subsequence Sort

You are given a binary string `s`.

You are also given an array of strings `strs`, where each `strs[i]` has the same length as `s` and consists of characters `'0'`, `'1'`, and `'?'`. Each `'?'` can be replaced by either `'0'` or `'1'`.

You may perform the following operation any number of times (including zero):

* Choose any **subsequence** `sub` of `s`.
* Sort `sub` in **non-decreasing** order.
* Replace the chosen subsequence in `s` with the sorted `sub`, keeping all other characters unchanged.

Return a boolean array ans, where `ans[i]` is `true` if it's possible to replace all `'?'` in `strs[i]` with `'0'` or `'1'` and transform `s` into the resulting string using the allowed operation above, otherwise return `false`.

 

**Example 1:**
```
Input: s = "101", strs = ["1?1","0?1","0?0"]

Output: [true,true,false]

Explanation:

i	strs[i]	Replacement	Result strs[i]	Operation(s)	Result
0	"1?1"	? → 0	"101"	Matches s.	true
1	"0?1"	? → 1	"011"	Select the subsequence at indices [0..2] of s → "101".
Sort "101" to get "011" = strs[i].	true
2	"0?0"	? → 0 or 1	"000" or "010"	Not feasible.	false
Thus, ans = [true, true, false].
```

**Example 2:**
```
Input: s = "1100", strs = ["0011","11?1","1?1?"]

Output: [true,false,true]

Explanation:

i	strs[i]	Replacement	Result strs[i]	Operation(s)	Result
0	"0011"	-	"0011"	Select the subsequence at indices [0..3] of s → "1100".
Sort "1100" to get "0011" = strs[i].	true
1	"11?1"	? → 0	"1101"	Not feasible.	false
2	"1?1?"	First ? → 0
Second ? → 0	"1010"	Select the subsequence at indices [1, 2] of s → "10".
Sort "10" to get "01", so s = "1010".	true
Thus, ans = [true, false, true].
```

**Example 3:**
```
Input: s = "1010", strs = ["0011"]

Output: [true]

Explanation:

i	strs[i]	Replacement	Result strs[i]	Operation(s)	Result
0	"0011"	-	"0011"	Select the subsequence at indices [0, 2, 3] of s → "110".
Sort "110" to get "011", so s = "0011" = strs[i].	true
Thus, ans = [true].
```
 

**Constraints:**

* `1 <= n == s.length <= 2000`
* `s[i]` is either `'0'` or `'1'`.
* `1 <= strs.length <= 2000`
* `strs[i].length == n`
* `strs[i]` is either `'0'`, `'1'`, or `'?'`

# Submissions
---
**Solution 1: (Greedy, every 0 in t appear before its correspondence in s)**

__Intuition__
When we choose a subsequence and sort it, all selected 0s move before all selected 1s.

This means:

We can move a 0 to the left across some 1s, but we can never move a 1 to the left across a 0.

So a target string is possible if:

It has the same number of 0s and 1s as s.
Every 0 that appears in the target can be matched with a 0 from s that is at the same position or to the right.
Visual
Suppose:

s = 1010
Zero positions:

index: 0 1 2 3
value: 1 0 1 0
          ↑   ↑
Target:

t = 0011
Required zero positions:

index: 0 1
Match them:

target zero at 0  ← use s zero at 1
target zero at 1  ← use s zero at 3
Both source positions are ≥ target positions, so this is possible.

Impossible Example
s = 101
t = 110
Zero positions in s:

2
Target needs a zero at position:

2
This works.

But if target were:

011
Target needs a zero at position 0, but the only zero in s is at position 1.

1 > 0
A zero cannot move left, so this is impossible.

__Approach__
For every query string:

Step 1
Replace all ? characters.

We know the final string must have the same number of zeros as s, so we greedily fill ? with 0 until the required number of zeros is reached, then fill the rest with 1.

Step 2
Check counts.

If the number of zeros or ones does not match s, return false.

Step 3
Store the positions of zeros in both strings.

Step 4
For every zero:

source_zero_position >= target_zero_position
must hold.

If any zero in s is to the left of where the target needs it, the transformation is impossible.

__Complexity__
Time Complexity

```
Runtime: 108 ms, Beats 20.68%
Memory: 117.16 MB, Beats 18.88%
```
```c++
class Solution {
public:
    vector<bool> transformStr(string s, vector<string>& strs) {
        int n = s.size();
        int zero = count(s.begin(), s.end(), '0');
        vector<int> idx;
        for (int i = 0; i < n; i ++) {
            if (s[i] == '0') {
                idx.push_back(i);
            }
        }
        vector<bool> ans;
        for (string t: strs) {
            int question = count(t.begin(), t.end(), '?');
            int cZero = count(t.begin(), t.end(), '0');
            if (cZero > zero || cZero + question < zero) {
                ans.push_back(false);
                continue;
            }
            int need = zero - cZero;
            for (char &c: t) {
                if (c == '?'){
                    if (need) {
                        c = '0';
                        need -= 1;
                    } else {
                        c = '1';
                    }
                }
            }
            vector<int> cIdx;
            for (int i = 0; i < n; i ++) {
                if (t[i] == '0') {
                    cIdx.push_back(i);
                }
            }
            bool ok = true;
            for (int i = 0; i < zero; i ++) {
                if (idx[i] < cIdx[i]) {
                    ok = false;
                    break;
                }
            }
            ans.push_back(ok);
        }
        return ans;
    }
};
```
