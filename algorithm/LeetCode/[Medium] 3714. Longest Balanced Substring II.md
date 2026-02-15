3714. Longest Balanced Substring II

You are given a string `s` consisting only of the characters `'a'`, `'b'`, and `'c'`.

A **substring** of `s` is called **balanced** if all distinct characters in the **substring** appear the **same** number of times.

Return the length of the **longest** balanced substring of `s`.

 

**Example 1:**
```
Input: s = "abbac"

Output: 4

Explanation:

The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.
```

**Example 2:**
```
Input: s = "aabcc"

Output: 3

Explanation:

The longest balanced substring is "abc" because all distinct characters 'a', 'b' and 'c' each appear exactly 1 time.
```

**Example 3:**
```
Input: s = "aba"

Output: 2

Explanation:

One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".
```
 

**Constraints:**

* `1 <= s.length <= 10^5`
* `s` contains only the characters `'a'`, `'b'`, and `'c'`.

# Submissions
---
**Solution 1: (Counter, Hash Table, case study)**

Explanation of Longest Balanced Substring Solution
This solution finds the length of the longest balanced substring in a string s consisting only of the characters 'a', 'b', and 'c'.

Step 1: Handle Consecutive Identical Characters
First, the algorithm checks for longest contiguous blocks of the same character.
Example: For s = "aaabb", the blocks "aaa" and "bb" are considered, giving a maximum length of 3.
This step ensures we account for cases where repeated characters themselves form the longest "balanced" substring.
Complexity:

Time: O(n)
Space: O(1)
Step 2: Find Longest Two-Character Balanced Substrings
A helper function is used to find the longest substring where two characters have equal counts, ignoring the third character.
For example, for characters 'a' and 'b' ignoring 'c', the function keeps track of the difference in counts (+1 for 'a', -1 for 'b').
A dictionary stores the first occurrence of each balance value, allowing quick calculation of substring lengths with equal counts.
This function is applied to all three possible pairs of characters:
'a' and 'b' (ignore 'c')
'a' and 'c' (ignore 'b')
'b' and 'c' (ignore 'a')
Complexity:

Time: O(n) per pair → O(n) overall
Space: O(n) for the balance dictionary
Step 3: Handle Substrings Balanced Across All Three Characters
To find substrings where counts of 'a', 'b', and 'c' are all equal, the algorithm uses cumulative counts: ca, cb, cc.
It stores the first occurrence of each pair (ca - cb, ca - cc) in a dictionary.
If the same pair occurs again at a later index, the substring between the previous index + 1 and the current index is balanced across all three characters.
The length of such substrings is tracked and the maximum is updated.
Complexity:

Time: O(n)
Space: O(n) for the dictionary
Step 4: Combine Results
The algorithm considers all three cases:
Longest single-character block
Longest two-character balanced substring
Longest three-character balanced substring
The maximum length among these is returned as the final answer.
Summary of Approach
Single-character blocks: Check for longest repeated character substring.
Two-character balances: For each pair of characters, find the longest substring where counts are equal ignoring the third character.
Three-character balances: Track cumulative counts to find substrings where 'a', 'b', and 'c' are equally represented.
Return the maximum length found from all cases.
Overall Complexity
Time Complexity: O(n)
Step 1: O(n)
Step 2: O(n) for each of 3 pairs → O(n)
Step 3: O(n)
Space Complexity: O(n)
For the dictionaries used in two-character and three-character balance tracking

    s = "a a b c c"
case1
a        ---
b            -
c              ---
case2:
ab         ---
ac
bc           ---
case3:
abc        -----

```
Runtime: 1170 ms Beats, 79.06%
Memory: 370.40 MB, Beats 23.07%
```
```c++
class Solution {
public:
    int longestBalanced(string s) {
        int n = s.size(), i, j, ka, kb, kc, ans = 0;
        i = 0;
        while (i < n) {
            j = i;
            while (j < n && s[j] == s[i]) {
                j += 1;
            }
            ans = max(ans, j - i);
            i = j;
        }
        auto best_2 = [&](char x, char _, char third) {
            int best = 0, bal;
            i = 0;
            while (i < n) {
                if (s[i] == third) {
                    i += 1;
                    continue; 
                }
                j = i;
                bal = 0;
                unordered_map<int, int> pre;
                pre[0] = j - 1;
                while (j < n && s[j] != third) {
                    bal += (s[j] == x ? 1 : -1);
                    if (!pre.count(bal)) {
                        pre[bal] = j;
                    } else {
                        best = max(best, j - pre[bal]);
                    }
                    j += 1;
                }
                i = j;
            }
            return best;
        };
        ans = max(ans, best_2('a', 'b', 'c'));
        ans = max(ans, best_2('a', 'c', 'b'));
        ans = max(ans, best_2('b', 'c', 'a'));
        ka = 0;
        kb = 0;
        kc = 0;
        map<pair<int, int>, int> pre2;
        pair<int, int> p;
        pre2[{0, 0}] = -1;
        for (i = 0; i < n; i ++){
            if (s[i] == 'a') {
                ka += 1;
            } else if (s[i] == 'b') {
                kb += 1;
            } else {
                kc += 1;
            }
            p = {kb - ka, kc - ka};
            if (pre2.count(p)) {
                ans = max(ans, i - pre2[p]);
            } else {
                pre2[p] = i;
            }
        }
        return ans;
    }
};
```
