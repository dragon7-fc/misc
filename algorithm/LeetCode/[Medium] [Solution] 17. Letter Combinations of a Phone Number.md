17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![17_200px-Telephone-keypad2.svg.png](img/17_200px-Telephone-keypad2.svg.png)

**Example:**
```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

**Note:**

* Although the above answer is in lexicographical order, your answer could be in any order you want.

# Solution
---
## Approach 1: Backtracking
Backtracking is an algorithm for finding all solutions by exploring all potential candidates. If the solution candidate turns to be not a solution (or at least not the last one), backtracking algorithm discards it by making some changes on the previous step, i.e. backtracks and then try again.

Here is a backtrack function `backtrack(combination, next_digits)` which takes as arguments an ongoing letter combination and the next digits to check.

* If there is no more digits to check that means that the current combination is done.
* If there are still digits to check :
    * Iterate over the letters mapping the next available digit.
        * Append the current letter to the current combination `combination = combination + letter`.
        * Proceed to check next digits : `backtrack(combination + letter, next_digits[1:])`.

![17_1_1.png](img/17_1_1.png)
![17_1_2.png](img/17_1_2.png)
![17_1_3.png](img/17_1_3.png)
![17_1_4.png](img/17_1_4.png)
![17_1_5.png](img/17_1_5.png)
![17_1_6.png](img/17_1_6.png)
![17_1_7.png](img/17_1_7.png)
![17_1_8.png](img/17_1_8.png)
![17_1_9.png](img/17_1_9.png)
![17_1_10.png](img/17_1_10.png)
![17_1_11.png](img/17_1_11.png)
![17_1_12.png](img/17_1_12.png)
![17_1_13.png](img/17_1_13.png)
![17_1_14.png](img/17_1_14.png)

```python
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])
                    
        output = []
        if digits:
            backtrack("", digits)
        return output
```

**Complexity Analysis**

* Time complexity : $\mathcal{O}(3^N \times 4^M)$ where `N` is the number of digits in the input that maps to 3 letters (e.g. `2, 3, 4, 5, 6, 8`) and `M` is the number of digits in the input that maps to 4 letters (e.g. `7, 9`), and `N+M` is the total number digits in the input.

* Space complexity : $\mathcal{O}(3^N \times 4^M)$ since one has to keep $3^N \times 4^M$ solutions.

# Submissions
---
**Solution 1: (Backtracking, Hash Table)**
```
Runtime: 28 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output
```

**Solution 2: (Backtracking)**
```
Runtime: 32 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If the input is empty, immediately return an empty answer array
        if len(digits) == 0: 
            return []
        
        # Map all the digits to their corresponding letters
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def backtrack(index, path):
            # If the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return # Backtrack
            
            # Get the letters that the current digit maps to, and loop through them
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                # Add the letter to our current path
                path.append(letter)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving onto the next
                path.pop()

        # Initiate backtracking with an empty path and starting index of 0
        combinations = []
        backtrack(0, [])
        return combinations
```

**Solution 3: (itertools)**
```
Runtime: 24 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        letters = list(map(lambda d: phone[d], digits))
        return [''.join(p) for p in itertools.product(*letters)]
```

**Solution 4: (Backtracking)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 9.10 MB, Beats 74.90%
```
```c++
class Solution {
    void bt(int i, vector<string> &dp, string &digits, string &p, vector<string> &ans) {
        if (i == digits.size()) {
            ans.push_back(p);
            return;
        }
        for (auto &c: dp[digits[i]-'0']) {
            p += c;
            bt(i+1, dp, digits, p, ans);
            p.pop_back();
        }
    }
public:
    vector<string> letterCombinations(string digits) {
        if (digits == "") {
            return {};
        }
        vector<string> dp = {
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        };
        string p;
        vector<string> ans;
        bt(0, dp, digits, p, ans);
        return ans;
    }
};
```

**Solution 5: (Iterative)**
```
Runtime: 0 ms
Memory: 7.79 MB
```
```c++
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits == "") {
            return {};
        }
        vector<string> m = {
            "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
        };
        vector<string> ans = {""};
        int sz;
        for (int i = 0; i < digits.size(); i ++) {
            sz = ans.size();
            for (int j = 0; j < sz; j ++) {
                for (int k = 0; k < m[digits[i]-'0'].size(); k ++) {
                    ans.push_back(*ans.begin() + m[digits[i]-'0'][k]);
                }
                ans.erase(ans.begin());
            }
        }
        return ans;
    }
};
```
