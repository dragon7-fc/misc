679. 24 Game

You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through `*`, `/`, `+`, `-`, `(`, `)` to get the value of 24.

**Example 1:**
```
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
```

**Example 2:**
```
Input: [1, 2, 1, 2]
Output: False
```

**Note:**

* The division operator `/` represents real division, not integer division. For example, `4 / (1 - 2/3) = 12`.
* Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with `[1, 1, 1, 1]` as input, the expression `-1 - 1 - 1 - 1` is not allowed.
* You cannot concatenate numbers together. For example, if the input is `[1, 2, 1, 2]`, we cannot write this as `12 + 12`.

# Solution
---
## Approach #1: Backtracking [Accepted]
**Intuition and Algorithm**

There are only 4 cards and only 4 operations that can be performed. Even when all operations do not commute, that gives us an upper bound of $12 * 6 * 2 * 4 * 4 * 4 = 9216$ possibilities, which makes it feasible to just try them all. Specifically, we choose two numbers (with order) in 12 ways and perform one of 4 operations (12 * 4). Then, with 3 remaining numbers, we choose 2 of them and perform one of 4 operations (6 * 4). Finally we have two numbers left and make a final choice of 2 * 4 possibilities.

We will perform 3 binary operations (`+, -, *, /` are the operations) on either our numbers or resulting numbers. Because `-` and `/` do not commute, we must be careful to consider both `a / b` and `b / a`.

For every way to remove two numbers `a`, `b` in our list, and for each possible result they can make, like `a+b`, `a/b`, etc., we will recursively solve the problem on this smaller list of numbers.

```python
from operator import truediv, mul, add, sub

class Solution(object):
    def judgePoint24(self, A):
        if not A: return False
        if len(A) == 1: return abs(A[0] - 24) < 1e-6

        for i in xrange(len(A)):
            for j in xrange(len(A)):
                if i != j:
                    B = [A[k] for k in xrange(len(A)) if i != k != j]
                    for op in (truediv, mul, add, sub):
                        if (op is add or op is mul) and j > i: continue
                        if op is not truediv or A[j]:
                            B.append(op(A[i], A[j]))
                            if self.judgePoint24(B): return True
                            B.pop()
        return False
```

**Complexity Analysis**

* Time Complexity: $O(1)$. There is a hard limit of 9216 possibilities, and we do $O(1)$ work for each of them.

* Space Complexity: $O(1)$. Our intermediate arrays are at most 4 elements, and the number made is bounded by an $O(1)$ factor.

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 152 ms
Memory Usage: 13.9 MB
```
```python
from operator import truediv, mul, add, sub

class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums: return False
        if len(nums) == 1: return abs(nums[0] - 24) < 1e-6

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    B = [nums[k] for k in range(len(nums)) if i != k != j]
                    for op in (truediv, mul, add, sub):
                        if (op is add or op is mul) and j > i: continue
                        if op is not truediv or nums[j]:
                            B.append(op(nums[i], nums[j]))
                            if self.judgePoint24(B): return True
                            B.pop()
        return False
```

**Solution 2: (Backtracking)**
```
Runtime: 60 ms
Memory Usage: 13.7 MB
```
```c++
/*
the idea is that
1. it does not matter how the prethesis groups the operations
2. the computation is alreasy between two operands
example: input: [4,1,8,7]
1. we could choose first 4 and 1 for any of the operations: *, /, +, -, to get a number say 5 from addition operation
2. then we will do the next operation choosing oprands between 5 and other not used numbers in the input array
3. we repeat this process until there is only one number left in the array and that number is 24 or not.

the important thing is to not let the prethesis get in the way of computation
example1: the process of evaluating expression (4+1/8)*7 is:
1. first doing 1/8, and we get 0.125
2. second doing 4+0.125 = 4.125
3. thrid doing 4.125*7 = ~

example2: the process of evaluating expression (8-4) * (7-1) is:
1. first doing 8-4 = 4
2. second doing 7-1 = 6
3. third doing 4+6 = ~

*/
class Solution {
public:
    bool judgePoint24(vector<int>& nums) {
        if(nums.empty()) {return false;}
        int len = nums.size();
        vector<double> cp;
        for(int i = 0; i < len; i++){
            cp.emplace_back(nums[i]);
        }
        return find(cp);
    }
    //T(n) = O(1), bc there are only 4 operands
    bool find(vector<double> nums){
        if(nums.size()==1 && abs(nums[0]-24) < 0.001){
            return true;
        }
        if (nums.size() == 1 && !(abs(nums[0] - 24) < 0.001)) {
            return false;
        }        
        int len = nums.size();
        vector<double> tmp;
        for(int i = 0; i < len; i++){
            for(int j = i+1; j < len; j++){
                //the two for loops above is to select all possible pairs in the array
                
                //the for loop below is to record all other eles in array not participating in the computation
                //at this round/iteration
                for(int k = 0; k < len; k++){
                    if(k!=i && k!=j){
                        tmp.emplace_back(nums[k]);
                    }
                }
                //do the computation and try all possible combinations
                for(auto it: compute(nums[i],nums[j])){
                    tmp.emplace_back(it);
                    if(find(tmp)){return true;}
                    tmp.pop_back();//back track, important
                }
                //back track, important
                tmp.clear();
            }
        }
        return false;
    }
    //O(n) = O(1)
    vector<double> compute(double& a, double& b){
        vector<double> res = {a+b,a-b,b-a,a*b,a/b,b/a};
        return res;
    }
};
```

**Solution 3: (Backtracking, try all solution)**

    1  2  3  4
        +
       ----
     /
    -------
            *
    ----------

```
Runtime: 25 ms, Beats 40.60%
Memory: 18.31 MB, Beats 36.60%
```
```c++
class Solution {
    bool bt(vector<double> arr) {
        if (arr.size() == 1) {
            if (abs(arr[0]-24) <= 0.001) {
                return true;
            }
            return false;
        }
        int n = arr.size(), i, j, k;
        vector<double> pre, cur;
        for (i = 0; i < n; i ++) {
            for (j = i+1; j < n; j ++) {
                for (k = 0; k < n; k ++) {
                    if (k != i && k != j) {
                        cur.push_back(arr[k]);
                    }
                }
                pre = getab(arr[i], arr[j]);
                for (auto a: pre) {
                    cur.push_back(a);
                    if (bt(cur)) {
                        return true;
                    }
                    cur.pop_back();
                }
                cur.clear();
            }
        }
        return false;
    }
    vector<double> getab(double a, double b) {
        return {a+b, a-b , b-a, a*b, a/b, b/a};
    }
public:
    bool judgePoint24(vector<int>& cards) {
        vector<double> dp(cards.begin(), cards.end());
        return bt(dp);
    }
};
```
