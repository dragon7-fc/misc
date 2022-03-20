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

# Submissions
---
**Solution 1: (DFS, Divide and Conquer)**
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

**Solution 1: (DP, Top-Downr)**
```
Runtime: 0 ms
Memory Usage: 7.8 MB
```
```++
class Solution {
    bool noOps(string exp){
        for(int i=0;i<exp.size();i++){
            if(exp[i]=='+' or exp[i]=='-' or exp[i]=='*'){
                return false;
            }
        }
        return true;
    }
    unordered_map<string,vector<int>>dp;
    
public:
    vector<int> diffWaysToCompute(string expression) {
        vector<int>ans;
        if(noOps(expression)){
            ans.push_back(stoi(expression));
            return ans;
        } else if(dp.count(expression)!=0){
            return dp[expression];
        } else {
            for(int i=0;i<expression.size();i++){
                if(expression[i]-'0'>=0 and expression[i]-'0'<=9){
                    continue;
                } else {
                    vector<int>left=diffWaysToCompute(expression.substr(0,i));
                    vector<int>right=diffWaysToCompute(expression.substr(i+1));
                    vector<int>tmp;
                    switch(expression[i]){
                        case '+':{
                            for(int l=0;l<left.size();l++){
                                for(int r=0;r<right.size();r++){
                                    tmp.push_back(left[l]+right[r]);
                                }
                            }
                        }
                            break;
                        case '*': {
                            for(int l=0;l<left.size();l++){
                                for(int r=0;r<right.size();r++){
                                    tmp.push_back(left[l]*right[r]);
                                }
                            }
                        }
                            break;
                        case '-': {
                            for(int l=0;l<left.size();l++){
                                for(int r=0;r<right.size();r++){
                                    tmp.push_back(left[l]-right[r]);
                                }
                            }
                        }
                            break;
                    }
                    for(int j=0;j<tmp.size();j++){
                        ans.push_back(tmp[j]);
                    }
                }
            }
            return dp[expression]=ans;
        }
    }
};
```
