2177. Find Three Consecutive Integers That Sum to a Given Number

Given an integer `num`, return three consecutive integers (as a sorted array) that **sum** to `num`. If `num` cannot be expressed as the sum of three consecutive integers, return an **empty** array.

 

**Example 1:**
```
Input: num = 33
Output: [10,11,12]
Explanation: 33 can be expressed as 10 + 11 + 12 = 33.
10, 11, 12 are 3 consecutive integers, so we return [10, 11, 12].
```

**Example 2:**
```
Input: num = 4
Output: []
Explanation: There is no way to express 4 as the sum of 3 consecutive integers.
```

**Constraints:**

* `0 <= num <= 10^15`

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 51 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3 != 0:
            return []
        return [num//3 - 1, num//3, num//3 + 1]
```

**Solution 2: (Math)**
```
Runtime: 3 ms
Memory Usage: 5.9 MB
```
```c++
class Solution {
public:
    vector<long long> sumOfThree(long long num) {
        if(num%3!=0)
            return {};
        
        long long mid=num/3;
        return {mid-1,mid,mid+1};
    }
};
```
