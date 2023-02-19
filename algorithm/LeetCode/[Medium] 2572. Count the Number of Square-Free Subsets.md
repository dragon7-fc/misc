2572. Count the Number of Square-Free Subsets

You are given a positive integer **0-indexed** array `nums`.

A subset of the array nums is **square-free** if the product of its elements is a **square-free integer**.

A **square-free integer** is an integer that is divisible by no square number other than `1`.

Return the number of square-free non-empty subsets of the array `nums`. Since the answer may be too large, return it modulo `10^9 + 7`.

A **non-empty subset** of `nums` is an array that can be obtained by deleting some (possibly `none` but not all) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

 

**Example 1:**
```
Input: nums = [3,4,4,5]
Output: 3
Explanation: There are 3 square-free subsets in this example:
- The subset consisting of the 0th element [3]. The product of its elements is 3, which is a square-free integer.
- The subset consisting of the 3rd element [5]. The product of its elements is 5, which is a square-free integer.
- The subset consisting of 0th and 3rd elements [3,5]. The product of its elements is 15, which is a square-free integer.
It can be proven that there are no more than 3 square-free subsets in the given array.
```

**Example 2:**
```
Input: nums = [1]
Output: 1
Explanation: There is 1 square-free subset in this example:
- The subset consisting of the 0th element [1]. The product of its elements is 1, which is a square-free integer.
It can be proven that there is no more than 1 square-free subset in the given array.
```

**Constraints:**

* `1 <= nums.length <= 1000`
* `1 <= nums[i] <= 30`

# Submissions
---
**Solution 1: (Map and GCD | Similar to using a Bitmask)**

__Approach__

This approach is actually doing the same thing as using a bitmask for the prime numbers. I'm storing the product of the prime numbers in the map instead of a bitmask. Here I find the GCD of the subset and the number, if the GCD is 1, then it means that there are no common factors and hence there can't be a square number that divides their product.

```
Runtime: 858 ms
Memory: 129.3 MB
```
```c++
class Solution {
public:
    int squareFreeSubsets(vector<int>& nums) {
        using ll = long long;
        map<ll,ll> mp;
        int MOD = 1e9 + 7;
        
        for(int num : nums) {
            bool flag = false;
            
            for(int i=2; i<=5; i++) {
                if(num % (i*i) == 0) {
                    flag = true;
                    break;
                }
            }
            
            if(flag) continue;
            
            vector<pair<ll,ll>> temp;
            
            for(auto [k, v] : mp) {
                if(__gcd(k, (ll)num) == 1) {
                    temp.push_back({k*num, v});
                }
            }
            
            for(auto [k, v] : temp) {
                mp[k] = (mp[k] + v)%MOD;
            }
            
            mp[num] = (mp[num] + 1)%MOD;
        }
        
        int result = 0;
        
        for(auto [k, v] : mp) {
            result = (result + v)%MOD;
        }
        
        return result;
    }
};
```
