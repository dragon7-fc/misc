402. Remove K Digits

Given a non-negative integer `num` represented as a string, remove `k` digits from the number so that the new number is the smallest possible.

**Note:**

* The length of `num` is less than 10002 and will be ≥ k.
* The given `num` does not contain any leading zero.

**Example 1:**
```
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
```

**Example 2:**
```
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
```

**Example 3:**
```
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
```

# Submissions
---
**Solution 1: (Greedy, Stack)**
```
Runtime: 32 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        
        result = []
        for c in num:
            while k > 0 and result and result[-1] > c:
                result.pop()
                k -= 1
            result.append(c)
        if k > 0:
            result = result[:-k]
        ans = "".join(result)
        return ans.lstrip("0") or "0"
```

**Solution 2: (Greedy, Stack)**
```
Runtime: 0 ms
Memory Usage: 7.1 MB
```
```c++
class Solution {
public:
    string removeKdigits(string num, int k) {
        if (num.size() == k)
            return "0";
        string ans;
        for (auto c: num) {
            while (k > 0 && !ans.empty() && ans.back() > c) {
                ans.pop_back();
                k -= 1;
            }
            ans.push_back(c);
        }
        while (k > 0 && !ans.empty()) {
            ans.pop_back();
            k -= 1;
        }
        int i;
        for(i = 0; i < ans.size(); i++)//remove leading zeroes
            if(ans[i]!='0') break;
        ans= ans.substr(i); 
        return ans == "" ? "0": ans;  //empty string=> 0
    }
};
```
