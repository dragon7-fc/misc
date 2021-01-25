1437. Check If All 1's Are at Least Length K Places Away

Given an array `nums` of 0s and 1s and an integer `k`, return `True` if all 1's are at least `k` places away from each other, otherwise return `False`.

 

**Example 1:**

![1437_sample_1_1791.png](img/1437_sample_1_1791.png)
```
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
```

**Example 2:**

![1437_sample_2_1791.png](img/1437_sample_2_1791.png)
```
Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.
```

**Example 3:**
```
Input: nums = [1,1,1,1,1], k = 0
Output: true
```

**Example 4:**
```
Input: nums = [0,1,0,1], k = 1
Output: true
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `0 <= k <= nums.length`
* `nums[i] is 0 or 1`

# Submissions
---
**Solution 1: (One Pass + Count)**
```
Runtime: 544 ms
Memory Usage: 17 MB
```
```python
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # initialize the counter of zeros to k
        # to pass the first 1 in nums
        count = k
        
        for num in nums:
            # if the current integer is 1
            if num == 1:
                # check that number of zeros in-between 1s
                # is greater than or equal to k
                if count < k:
                    return False
                # reinitialize counter
                count = 0
            # if the current integer is 0
            else:
                # increase the counter
                count += 1
                
        return True
```

**Solution 2: (Bit Manipulation)**
```
Runtime: 888 ms
Memory Usage: 16.8 MB
```
```python
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # convert binary array into int
        x = 0
        for num in nums:
            x = (x << 1) | num
        
        # base case
        if x == 0 or k == 0:
            return True
        
        # remove trailing zeros
        while x & 1 == 0:
            x = x >> 1
        
        while x != 1:
            # remove trailing 1-bit
            x = x >> 1
            
            # count trailing zeros
            count = 0
            while x & 1 == 0:
                x = x >> 1
                count += 1
                
            # number of zeros in-between 1-bits
            # should be greater than or equal to k
            if count < k:
                return False
        
        return True
```

**Solution 3: (Brute Force)**
```
Runtime: 1008 ms
Memory Usage: 20.2 MB
```
```python
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        path = [i for i, num in enumerate(nums) if num == 1]
        if all (b-a > k for a, b in zip(path[:], path[1:])):
            return True
        else:
            return False
```

**Solution 4: (Two Pointers)**
```
Runtime: 600 ms
Memory Usage: 16.5 MB
```
```python
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i = 0   
        for j in range(i+1,len(nums)):
            if nums[j] == 1:
                if nums[i] != 1:
                    i = j
                elif j-i-1>=k:
                    i = j
                elif j-i-1<k:
                    return False
                
        return True
```

**Solution 5: (Greedy)**
```
Runtime: 628 ms
Memory Usage: 19.4 MB
```
```python
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        idx = []
        for i in range(len(nums)):
            if nums[i] == 1:
                idx.append(i)
            if len(idx) > 1 and idx[-1] - idx[-2] - 1 < k:
                return False

        return True
```