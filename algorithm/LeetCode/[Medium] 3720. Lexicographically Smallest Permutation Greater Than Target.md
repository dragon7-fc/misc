3720. Lexicographically Smallest Permutation Greater Than Target

You are given two strings `s` and `target`, both having length `n`, consisting of lowercase English letters.

Return the **lexicographically smallest permutation** of `s` that is **strictly** greater than `target`. If no permutation of s is lexicographically strictly greater than `target`, return an empty string.

A string `a` is lexicographically strictly greater than a string `b` (of the same length) if in the first position where `a` and `b` differ, string `a` has a letter that appears later in the alphabet than the corresponding letter in `b`.

 

**Example 1:**
```
Input: s = "abc", target = "bba"

Output: "bca"

Explanation:

The permutations of s (in lexicographical order) are "abc", "acb", "bac", "bca", "cab", and "cba".
The lexicographically smallest permutation that is strictly greater than target is "bca".
```

**Example 2:**
```
Input: s = "leet", target = "code"

Output: "eelt"

Explanation:

The permutations of s (in lexicographical order) are "eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", and "tlee".
The lexicographically smallest permutation that is strictly greater than target is "eelt".
```

**Example 3:**
```
Input: s = "baba", target = "bbaa"

Output: ""

Explanation:

The permutations of s (in lexicographical order) are "aabb", "abab", "abba", "baab", "baba", and "bbaa".
None of them is lexicographically strictly greater than target. Therefore, the answer is "".
```

**Constraints:**

* `1 <= s.length == target.length <= 300`
* `s` and `target` consist of only lowercase English letters.

# Submissions
---
**Solution 1: (Backtracking, Pruning)**

Intuition
We are asked to find the lexicographically smallest permutation of s that is strictly greater than a given string target.

My first thought was to try generating all permutations of s and comparing them to target, but this is infeasible for large strings (n ≤ 300) because the number of permutations is n!.

Instead, I realized we could use backtracking with pruning:

Build the permutation character by character.

Keep track of the characters left to use using a frequency array.

Stop exploring branches that cannot possibly be strictly greater than target.

This ensures we find the lexicographically smallest valid permutation efficiently.

Approach
Count the frequency of each character in s using a cnt[26] array.
Use a backtracking function to build the permutation step by step:

path stores the current prefix.

big is a boolean indicating whether the current prefix is already strictly greater than target.

At each step i in the permutation:

Iterate over characters 'a' to 'z'.

Skip any character that is not available (cnt[c] == 0).

If big == false (prefix equals target so far), skip characters < target[i].

Choose a character, decrement its count, and recursively call the function with updated big.

Once a full permutation is formed:
If big == true (prefix is strictly greater than target), record it as ans and stop recursion.

Return ans. If no valid permutation exists, ans remains empty.

This way we prune unnecessary branches, avoid generating all permutations and getting the lexicographically smallest valid string.

Complexity
Time complexity:
In the worst case, we may explore all permutations, but pruning significantly reduces the search space.

Practically, it is much faster than O(n!) because we skip branches that cannot exceed target.

The exact worst-case is difficult to express, but the effective complexity is much less than O(n!).

Space complexity: O(n)

```
Runtime: 0 ms, Beats 100.00%
Memory: 11.02 MB, Beats 37.50%
```
```c++
class Solution {
    bool bt(vector<char> &path, vector<int> &cnt, string &target, bool big, string &ans){
        int n = target.size();
        if (!ans.empty()) {
            return true;
        }
        if (path.size() == n){
            if (big) {
                ans = string(path.begin(), path.end());
                return true;
            }
            return false;
        }
        int i = path.size();
        for (int c = 0; c < 26; c++){
            if (cnt[c] == 0) {
                continue;
            }
            if (!big && c + 'a' < target[i]) {
                continue;
            }
            path.push_back(c + 'a');
            cnt[c] -= 1;
            bool newbig = big || (c + 'a' > target[i]);
            if (bt(path, cnt, target, newbig, ans)) {
                return true;
            }
            path.pop_back();
            cnt[c] += 1;
        }
        return false;
    }
public:
    string lexGreaterPermutation(string s, string target) {
        vector<int> cnt(26);
        string ans;
        for (char &c: s) {
            cnt[c-'a'] += 1;
        }
        vector<char> path;
        bt(path, cnt, target, false, ans);
        return ans;
    }
};
```

**Solution 2: (Backtracking, Pruning, try to fill first larger character as earliest as possible)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 9.84 MB, Beats 82.17%
```
```c++
class Solution {
    bool bt(string &path, vector<int> &cnt, bool big, string &ans, string &target){
        int n = target.size();
        if (path.size() == n){
            if (big) {
                ans = move(path);
                return true;
            }
            return false;
        }
        int i = path.size();
        for (int j = 0; j < 26; j ++){
            if (cnt[j] == 0) {
                continue;
            }
            if (!big && j + 'a' < target[i]) {
                continue;
            }
            path += j + 'a';
            cnt[j] -= 1;
            bool nbig = big || (j + 'a' > target[i]);
            if (bt(path, cnt, nbig, ans, target)) {
                return true;
            }
            cnt[j] += 1;
            path.pop_back();
        }
        return false;
    }
public:
    string lexGreaterPermutation(string s, string target) {
        vector<int> cnt(26);
        for (char &c: s) {
            cnt[c-'a'] += 1;
        }
        string path;
        string ans;
        bool big = false;
        bt(path, cnt, big, ans, target);
        return ans;

    }
};
```

**Solution 3: (Greedy, try to fill first larger character as earliest as possible then sort rest)**


```
Runtime: 3 ms, Beats 69.43%
Memory: 9.60 MB, Beats 98.73%
```
```c++
class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        int n = s.length();
        vector<int> freq(26, 0);
        for (char ch : s) {
            freq[ch - 'a']++;
        }

        int best_pivot = -1;
        char best_char = ' ';

        // 1. Try to match prefix target[0...k]
        for (int k = 0; k < n; ++k) {
            // Check if we can pick a character larger than target[k] at index k
            int target_char = target[k] - 'a';
            for (int c = target_char + 1; c < 26; ++c) {
                if (freq[c] > 0) {
                    best_pivot = k;
                    best_char = 'a' + c;
                    break; // Pick the smallest possible character > target[k]
                }
            }

            // Try to match target[k] to continue matching prefix further
            if (freq[target_char] > 0) {
                freq[target_char]--;
            } else {
                // Cannot match target[k], stop prefix matching loop
                break;
            }
        }

        // No pivot point found where we can make string > target
        if (best_pivot == -1) {
            return "";
        }

        // 2. Reconstruct original frequency count
        vector<int> rem_freq(26, 0);
        for (char ch : s) {
            rem_freq[ch - 'a']++;
        }

        string result = "";
        
        // Match prefix target[0 ... best_pivot - 1]
        for (int k = 0; k < best_pivot; ++k) {
            result += target[k];
            rem_freq[target[k] - 'a']--;
        }

        // Place best_char at best_pivot
        result += best_char;
        rem_freq[best_char - 'a']--;

        // Fill remaining suffix with leftover characters in ascending order
        for (int c = 0; c < 26; ++c) {
            while (rem_freq[c] > 0) {
                result += ('a' + c);
                rem_freq[c]--;
            }
        }

        return result;
    }
};
````

**Solution 4: (Greedy, try to fill first larger character as earliest as possible then sort rest)**

                 best_i
target  ====== [   .    ] xxx
ans     ====== [ larger ] ...
         equal            sort
        longest

```
Runtime: 0 ms, Beats 100.00%
Memory: 9.63 MB, Beats 94.90%
```
```c++
class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        int n = s.length();
        vector<int> cnt(26, 0);
        for (auto const &c : s) {
            cnt[c - 'a'] += 1;
        }
        int big_i = -1;
        char big_char = ' ';
        for (int i = 0; i < n; i ++) {
            int j = target[i] - 'a';
            for (int cj = j + 1; cj < 26; cj ++) {
                if (cnt[cj] > 0) {
                    big_i = i;
                    big_char = cj + 'a';
                    break;
                }
            }
            if (cnt[j] > 0) {
                cnt[j] -= 1;
            } else {
                break;
            }
        }
        if (big_i == -1) {
            return "";
        }
        fill(cnt.begin(), cnt.end(), 0);
        for (const auto &c : s) {
            cnt[c - 'a'] += 1;
        }
        string ans = "";
        for (int i = 0; i < big_i; i ++) {
            ans += target[i];
            cnt[target[i] - 'a'] -= 1;
        }
        ans += big_char;
        cnt[big_char - 'a'] -= 1;
        for (int j = 0; j < 26; j ++) {
            while (cnt[j] > 0) {
                ans += (j + 'a');
                cnt[j] -= 1;
            }
        }
        return ans;
    }
};
```
