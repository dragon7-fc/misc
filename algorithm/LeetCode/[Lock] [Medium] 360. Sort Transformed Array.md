360. Sort Transformed Array

Given a **sorted** integer array `nums` and three integers `a`, `b` and `c`, apply a quadratic function of the form `f(x) = ax2 + bx + c` to each element `nums[i]` in the array, and return the array in a sorted order.

 

**Example 1:**
```
Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
```

**Example 2:**
```
Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
```

**Constraints:**

* `1 <= nums.length <= 200`
* `-100 <= nums[i], a, b, c <= 100`
* `nums` is sorted in **ascending** order.

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 50 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        return sorted(map(lambda x: a*(x**2)+(b*x)+(c),nums))
```

**Solution 2: (Math)**
```
Runtime: 36 ms
Memory Usage: 14.5 MB
```
```python
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        #origin = -b/2a
        mid = -1*b/(2*a) if a != 0 else 0
        
        left, right = collections.deque([]), collections.deque([])
        
        #apply the function
        def fn(num):
            return a*num*num + b*num +c
        
        #print('mid: ', mid)
        for num in nums:
            if num< mid: left.append(fn(num))
                
            else: right.append(fn(num))
        
        ans  =[]
        #merge both
        while left or right:
            if left and right:
                if left[-1]<= min(right[0], left[0], right[-1]):
                    ans.append(left.pop())
                    
                elif left[0]<= min(right[0], left[-1], right[-1]):
                    ans.append(left.popleft())
                
                elif right[-1]<= min(right[0], left[0], left[-1]):
                    ans.append(right.pop())
                
                else: 
                    #right[0] smallest
                    ans.append(right.popleft())
                    
            elif left:
                if left[-1]< left[0]:
                    ans.append(left.pop())
                else: ans.append(left.popleft())
                
            else:
                if right[-1]< right[0]:
                    ans.append(right.pop())
                
                else:
                    ans.append(right.popleft())
                    
        return ans
```

**Solution 3: (Math)**
```
Runtime: 0 ms
Memory Usage: 9.4 MB
```
```c++
class Solution {
public:
    vector<int> sortTransformedArray(vector<int>& nums, int a, int b, int c) {
        std::vector<int> res(nums.size(), 0);
        double d0 = static_cast<double>(-b) / (2.0 * a);
        int l = 0;
        int r = nums.size() - 1;
        int idx = 0;
        int x = 0;
        
        while (l <= r) {
            if (std::abs(d0 - nums[l]) < std::abs(d0 - nums[r])) {
                x = nums[r];
                --r;
            } else {
                x = nums[l];
                ++l;
            }
            res[idx++] = a * x * x + b * x + c;
        }
		// Depending on the sign of a. The results will be sorted in as/dsending order.
        if (res[0] > res.back()) {
            std::reverse(res.begin(), res.end());
        }
        return res;
    }
};
```
