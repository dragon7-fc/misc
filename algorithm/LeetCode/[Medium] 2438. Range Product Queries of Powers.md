2438. Range Product Queries of Powers

Given a positive integer `n`, there exists a **0-indexed** array called `powers`, composed of the minimum number of powers of `2` that sum to `n`. The array is sorted in **non-decreasing** order, and there is **only one** way to form the array.

You are also given a **0-indexed** 2D integer array `queries`, where `queries[i] = [lefti, righti]`. Each `queries[i]` represents a query where you have to find the product of all `powers[j]` with `lefti <= j <= righti`.

Return an array `answers`, equal in length to `queries`, where `answers[i]` is the answer to the `i`th query. Since the answer to the `i`th query may be too large, each `answers[i]` should be returned **modulo** `10^9 + 7`.

 

**Example 1:**
```
Input: n = 15, queries = [[0,1],[2,2],[0,3]]
Output: [2,4,64]
Explanation:
For n = 15, powers = [1,2,4,8]. It can be shown that powers cannot be a smaller size.
Answer to 1st query: powers[0] * powers[1] = 1 * 2 = 2.
Answer to 2nd query: powers[2] = 4.
Answer to 3rd query: powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64.
Each answer modulo 109 + 7 yields the same answer, so [2,4,64] is returned.
```

**Example 2:**
```
Input: n = 2, queries = [[0,0]]
Output: [2]
Explanation:
For n = 2, powers = [2].
The answer to the only query is powers[0] = 2. The answer modulo 109 + 7 is the same, so [2] is returned.
```

**Constraints:**

* `1 <= n <= 10^9`
* `1 <= queries.length <= 10^5`
* `0 <= starti <= endi < powers.length`

# Submissions
---
**Solution 1: (Prefix Sum)**
```
Runtime: 3922 ms
Memory: 51.5 MB
```
```python
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = (10**9)+7
        binary = bin(n)[2:]
        powers = []
        result = []
        for index, val in enumerate(binary[::-1]):
            if val == "1":
                powers.append(2**index)
                
        for index in range(1, len(powers)):
            powers[index] = powers[index] * powers[index - 1]    
        
        for l,r in queries:
            if l == 0:
                result.append(powers[r]%MOD)
            else:
                result.append((powers[r]//powers[l-1])%MOD)
                
        return result
```

**Solution 2: (Bit Manipulation)**
```
Runtime: 930 ms
Memory: 143 MB
```
```c++
class Solution {
public:
    vector<int> productQueries(int n, vector<vector<int>>& queries) {
        vector<int> pow;
        long long mod = 1e9+7;
        
        //if bit is set insert in the power array
        for(int i =0;i<32;i++)
        {
            if(n&(1<<i))
                pow.push_back(1<<i);
        }
        vector<int> ans;
        
        //solving for the query
        for(int i =0;i<queries.size();i++)
        {
            long long temp=1;
            for(int j =queries[i][0];j<=queries[i][1];j++)
            {
                temp=((temp%mod)*pow[j])%mod;
            }
            ans.push_back(temp);
        }
        return ans;
    }
};
```
