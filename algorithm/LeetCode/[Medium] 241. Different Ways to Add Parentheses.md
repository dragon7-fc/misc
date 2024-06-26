241. Different Ways to Add Parentheses

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are `+`, `-` and `*`.

**Example 1:**
```
Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
```

**Example 2:**
```
Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
```

**Constraints:**

* `1 <= expression.length <= 20`
* `expression` consists of digits and the operator `'+'`, `'-'`, and `'*'`.
* All the integer values in the input expression are in the range `[0, 99]`.

# Submissions
---
**Solution 1: (DFS, Divide and Conquer, backtracking)**
```
Runtime: 28 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit(): return [int(input)]
        rst, tmp = [], 0
        for i in range(len(input)):
            if input[i] in '+-*':
                a, b = input[:i], input[i+1:]
                l, r = self.diffWaysToCompute(a), self.diffWaysToCompute(b)
                for p in l: 
                    for q in r:
                        if input[i] == '+': tmp = p + q
                        elif input[i] == '-': tmp = p - q
                        else: tmp = p * q
                        rst.append(tmp)
        return rst
```

**Solution 2: (DFS, Divide and Conquer, backtracking)**
```
Runtime: 3 ms
Memory: 11.9 MB
```
```c++
class Solution {
public:
    vector<int> diffWaysToCompute(string expression) {
        vector<int> ans;
        int n = expression.size();
        for (int i = 0; i < n; i++){
            char c = expression[i];
            if (c == '+' || c == '-' || c == '*'){
                vector<int> left = diffWaysToCompute(expression.substr(0,i));
                vector<int> right = diffWaysToCompute(expression.substr(i+1));
                for (int l: left){
                    for (int r: right){
                        if (c == '+') ans.push_back(l+r);
                        else if(c == '-') ans.push_back(l-r);
                        else if(c == '*') ans.push_back(l*r);
                    }
                }
            }
        }
        if (ans.empty()) {
            ans.push_back(stoi(expression));
        }
        return ans;
    }
};
```
