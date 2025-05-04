3491. Phone Number Prefix

You are given a string array `numbers` that represents phone numbers. Return `true` if no phone number is a prefix of any other phone number; otherwise, return `false`.

 

**Example 1:**
```
Input: numbers = ["1","2","4","3"]

Output: true

Explanation:

No number is a prefix of another number, so the output is true.
```

**Example 2:**
```
Input: numbers = ["001","007","15","00153"]

Output: false

Explanation:

The string "001" is a prefix of the string "00153". Thus, the output is false.
```
 

**Constraints:**

* `2 <= numbers.length <= 50`
* `1 <= numbers[i].length <= 50`
* All numbers contain only digits `'0'` to `'9'`.

# Submissions
---
**Solution 1: (Trie)**
```
Runtime: 13 ms, Beats 28.66%
Memory: 43.62 MB, Beats 14.65%
```
```c++
class Solution {
    struct TrieNode {
        struct TrieNode *child[10] = {nullptr};
        bool is_end = false;
    };
    TrieNode *root;
    bool build(string s) {
        TrieNode *node = root;
        for (auto c: s) {
            if (!node->child[c-'0']) {
                node->child[c-'0'] = new TrieNode();
            }
            node = node->child[c-'0'];
            if (node->is_end) {
                return true;
            }
        }
        node->is_end = true;
        return false;
    }
public:
    bool phonePrefix(vector<string>& numbers) {
        root = new TrieNode();
        sort(numbers.begin(), numbers.end());
        for (auto num: numbers) {
            if (build(num)) {
                return false;
            }
        }
        return true;
    }
};
```

**Solution 2: (String, starts_with)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 30.42 MB, Beats 52.87%
```
```c++
class Solution {
public:
    bool phonePrefix(vector<string>& numbers) {
        sort(numbers.begin(), numbers.end());
        for (int i = 1; i < numbers.size(); i++)
        if (numbers[i].starts_with(numbers[i - 1]))
            return false;
    return true;
    }
};
```
