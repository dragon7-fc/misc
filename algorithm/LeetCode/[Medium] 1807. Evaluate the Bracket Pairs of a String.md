1807. Evaluate the Bracket Pairs of a String

You are given a string `s` that contains some bracket pairs, with each pair containing a **non-empty** key.

* For example, in the string `"(name)is(age)yearsold"`, there are two bracket pairs that contain the keys `"name"` and `"age"`.

You know the values of a wide range of keys. This is represented by a 2D string array `knowledge` where each `knowledge[i] = [keyi, valuei]` indicates that key `keyi` has a value of `valuei`.

You are tasked to evaluate all of the bracket pairs. When you evaluate a bracket pair that contains some key `keyi`, you will:

* Replace `keyi` and the bracket pair with the key's corresponding `valuei`.
* If you do not know the value of the key, you will replace keyi and the bracket pair with a question mark `"?"` (without the quotation marks).

Each key will appear at most once in your `knowledge`. There will not be any nested brackets in `s`.

Return the resulting string after evaluating all of the bracket pairs.

 

**Example 1:**
```
Input: s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]
Output: "bobistwoyearsold"
Explanation:
The key "name" has a value of "bob", so replace "(name)" with "bob".
The key "age" has a value of "two", so replace "(age)" with "two".
```

**Example 2:**
```
Input: s = "hi(name)", knowledge = [["a","b"]]
Output: "hi?"
Explanation: As you do not know the value of the key "name", replace "(name)" with "?".
```

**Example 3:**
```
Input: s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]
Output: "yesyesyesaaa"
Explanation: The same key can appear multiple times.
The key "a" has a value of "yes", so replace all occurrences of "(a)" with "yes".
Notice that the "a"s not in a bracket pair are not evaluated.
```

**Example 4:**
```
Input: s = "(a)(b)", knowledge = [["a","b"],["b","a"]]
Output: "ba"
```

**Constraints:**

* `1 <= s.length <= 10^5`
* `0 <= knowledge.length <= 10^5`
* `knowledge[i].length == 2`
* `1 <= keyi.length, valuei.length <= 10`
* `s` consists of lowercase English letters and round brackets `'('` and `')'`.
* Every open bracket `'('` in `s` will have a corresponding close bracket `')'`.
* The key in each bracket pair of `s` will be non-empty.
* There will not be any nested bracket pairs in `s`.
* `keyi` and valuei consist of lowercase English letters.
* Each `keyi` in knowledge is unique.

# Submissions
---
**Solution 1: (String, Hash Table)**
```
Runtime: 936 ms
Memory Usage: 54.8 MB
```
```python
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {k: v for k, v in knowledge}
        res = []
        cur = ''
        going = False
        for c in s:
            if c == '(':
                going = True
            elif c == ')':
                going = False
                res.append(d.get(cur, '?'))
                cur = ''
            elif going:
                cur += c
            else:
                res.append(c)
        return ''.join(res)
```
**Solution 2: (String, Hash Table)**
```
Runtime: 284 ms
Memory: 120.92 MB
```
```c++
class Solution {
public:
    string evaluate(string s, vector<vector<string>>& knowledge) {
        string result = "";

        string currentKey = "";

        unordered_map<string, string> knowledgeMap;
        for (int i = 0; i < knowledge.size(); i++) {
            knowledgeMap[knowledge[i][0]] = knowledge[i][1];
        }

        for (int i = 0; i < s.size(); i++) {
            if (s[i] != '(') { // if regular character append to result the character
                result.push_back(s[i]);
            } else { // if open parenthesis
                while (s[++i] != ')') { // loop until closing parenthesis to extract the key
                    currentKey.push_back(s[i]);
                }
                if (knowledgeMap.find(currentKey) != knowledgeMap.end()) { // if key is in the hashmap append its value 
                    result.append(knowledgeMap[currentKey]);
                } else { // otherwise append "?"
                    result.push_back('?');
                }
                currentKey = ""; // reset current key for next key
            }
        }
        return result;
    }
};
```
