2232. Minimize Result by Adding Parentheses to Expression

You are given a **0-indexed** string `expression` of the form `"<num1>+<num2>"` where `<num1>` and `<num2>` represent positive integers.

Add a pair of parentheses to `expression` such that after the addition of parentheses, `expression` is a **valid** mathematical expression and evaluates to the **smallest** possible value. The left parenthesis must be added to the left of `'+'` and the right parenthesis must be added to the right of `'+'`.

Return `expression` after adding a pair of parentheses such that `expression` evaluates to the **smallest** possible value. If there are multiple answers that yield the same result, return any of them.

The input has been generated such that the original value of `expression`, and the value of `expression` after adding any pair of parentheses that meets the requirements fits within a signed 32-bit integer.

 

**Example 1:**
```
Input: expression = "247+38"
Output: "2(47+38)"
Explanation: The expression evaluates to 2 * (47 + 38) = 2 * 85 = 170.
Note that "2(4)7+38" is invalid because the right parenthesis must be to the right of the '+'.
It can be shown that 170 is the smallest possible value.
```

**Example 2:**
```
Input: expression = "12+34"
Output: "1(2+3)4"
Explanation: The expression evaluates to 1 * (2 + 3) * 4 = 1 * 5 * 4 = 20.
```

**Example 3:**
```
Input: expression = "999+999"
Output: "(999+999)"
Explanation: The expression evaluates to 999 + 999 = 1998.
```

**Constraints:**

* `3 <= expression.length <= 10`
* `expression` consists of digits from `'1'` to `'9'` and `'+'`.
* `expression` starts and ends with digits.
* `expression` contains exactly one `'+'`.
* The original value of `expression`, and the value of `expression` after adding any pair of parentheses that meets the requirements fits within a signed 32-bit integer.

# Submissions
---
**Solution 1: (String, Brute Force)**
```
Runtime: 62 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus_index, n, ans = expression.find('+'), len(expression), [float(inf),expression] 
        def evaluate(exps: str):
            return eval(exps.replace('(','*(').replace(')', ')*').lstrip('*').rstrip('*'))
        for l in range(plus_index):
            for r in range(plus_index+1, n):
                exps = f'{expression[:l]}({expression[l:plus_index]}+{expression[plus_index+1:r+1]}){expression[r+1:n]}'
                res = evaluate(exps)
                if ans[0] > res:
                    ans[0], ans[1] = res, exps
        return ans[1]
```

**Solution 2: (String, Brute Force)**
```
Runtime: 0 ms
Memory: 6.4 MB
```
```c++
class Solution {
public:
    string minimizeResult(string expression) {
        int plus = expression.find('+');
        vector<int> v;
        vector<pair<int, int>> lp, rp;
        for (int l = stoi(expression.substr(0, plus)), mul = 10; l * 10 >= mul; mul *= 10)
            lp.push_back({ l / mul, l % mul}); 
        for (int r = stoi(expression.substr(plus + 1)), mul = 1; r / mul > 0; mul *= 10)
            rp.push_back({ r % mul, r / mul }); 
        for (auto [m1, s1] : lp)
            for (auto [m2, s2]: rp)
                if (v.empty() || max(1, m1) * (s1 + s2) * max(1, m2) < max(1, v[0]) * (v[1] + v[2]) * max(1, v[3]))
                    v = {m1, s1, s2, m2};
        return (v[0] ? to_string(v[0]) : "") + "(" + to_string(v[1]) 
            + "+" + to_string(v[2]) + ")" + (v[3] ? to_string(v[3]) : "");
    }
};
```
