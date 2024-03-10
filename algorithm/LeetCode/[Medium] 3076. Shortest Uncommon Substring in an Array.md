3076. Shortest Uncommon Substring in an Array

You are given an array `arr `of size `n` consisting of non-empty strings.

Find a string array `answer` of size `n` such that:

* `answer[i]` is the shortest **substring** of `arr[i]` that does not occur as a substring in any other string in `arr`. If multiple such substrings exist, `answer[i]` should be the **lexicographically smallest**. And if no such substring exists, `answer[i]` should be an empty string.

Return the array `answer`.

 

**Example 1:**
```
Input: arr = ["cab","ad","bad","c"]
Output: ["ab","","ba",""]
Explanation: We have the following:
- For the string "cab", the shortest substring that does not occur in any other string is either "ca" or "ab", we choose the lexicographically smaller substring, which is "ab".
- For the string "ad", there is no substring that does not occur in any other string.
- For the string "bad", the shortest substring that does not occur in any other string is "ba".
- For the string "c", there is no substring that does not occur in any other string.
```

**Example 2:**
```
Input: arr = ["abc","bcd","abcd"]
Output: ["","","abcd"]
Explanation: We have the following:
- For the string "abc", there is no substring that does not occur in any other string.
- For the string "bcd", there is no substring that does not occur in any other string.
- For the string "abcd", the shortest substring that does not occur in any other string is "abcd".
```

**Constraints:**

* `n == arr.length`
* `2 <= n <= 100`
* `1 <= arr[i].length <= 20`
* `arr[i]` consists only of lowercase English letters.

# Submissions
---
**Solution 1: (Hash Table, brute force all combination)**
```
Runtime: 344 ms
Memory: 131.64 MB
```
```c++
class Solution {
public:
    vector<string> shortestSubstrings(vector<string>& arr) {
        unordered_map<string, int> cnt;
        set<string> st;
        for (auto a: arr) {
            st.clear();
            for (int i = 0; i < a.size(); i ++) {
                for (int k = 1; i+k <= a.size(); k ++) {
                    st.insert(a.substr(i, k));
                }
            }
            for (auto s: st) {
                cnt[s] += 1;
            }
        }
        vector<string> ans;
        string cur;
        for (auto a: arr) {
            cur = "";
            for (int k = 1; k <= a.size(); k ++) {
                st.clear();
                for (int i = 0; i+k <= a.size(); i ++) {
                    st.insert(a.substr(i, k));
                }
                for (auto s: st) {
                    if (cnt[s] == 1) {
                        if (cur == "") {
                            cur = s;
                            break;
                        }
                    }
                }
                if (cur != "") {
                    break;
                }
            }
            ans.push_back(cur);
        }
        return ans;
    }
};
```
