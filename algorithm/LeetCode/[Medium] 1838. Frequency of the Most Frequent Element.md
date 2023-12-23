1838. Frequency of the Most Frequent Element

The **frequency** of an element is the number of times it occurs in an array.

You are given an integer array `nums` and an integer `k`. In one operation, you can choose an index of `nums` and increment the element at that index by `1`.

Return the **maximum possible frequency** of an element after performing at most `k` operations.

 

**Example 1:**
```
Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
```

**Example 2:**
```
Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
```

**Example 3:**
```
Input: nums = [3,9,6], k = 2
Output: 1
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^5`
* `1 <= k <= 10^5`

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 1060 ms
Memory Usage: 28.1 MB
```
```python
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        lo, mx = 0, 0
        for hi, n in enumerate(nums):
            if hi > 0:
                k -= (n - nums[hi - 1]) * (hi - lo)
            if k < 0:
                k += n - nums[lo]     
                lo += 1
            if k >= 0:
                mx = max(mx, hi - lo + 1)
        return mx
```

**Solution 2: (Sliding Window)**
```
Runtime: 157 ms
Memory: 99.3 MB
```
```c++
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int left = 0;
        int ans = 0;
        long curr = 0;
        
        for (int right = 0; right < nums.size(); right++) {
            long target = nums[right];
            curr += target;
            
            while ((right - left + 1) * target - curr > k) {
                curr -= nums[left];
                left++;
            }
            
            ans = max(ans, right - left + 1);
        }
        
        return ans;
    }
};
```

**Solution 3: (Advanced Sliding Window)**
```
Runtime: 146 ms
Memory: 99.4 MB
```
```c++
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int left = 0;
        long curr = 0;
        
        for (int right = 0; right < nums.size(); right++) {
            long target = nums[right];
            curr += target;
            
            if ((right - left + 1) * target - curr > k) {
                curr -= nums[left];
                left++;
            }
        }
        
        return nums.size() - left;
    }
};
```

**Solution 4: (Binary Search)**
```
Runtime: 319 ms
Memory: 121 MB
```
```c++
class Solution {
    int check(int i, int k, vector<int>& nums, vector<long>& prefix) {
        int target = nums[i];
        int left = 0;
        int right = i;
        int best = i;
        
        while (left <= right) {
            int mid = (left + right) / 2;
            long count = i - mid + 1;
            long finalSum = count * target;
            int originalSum = prefix[i] - prefix[mid] + nums[mid];
            int operationsRequired = finalSum - originalSum;
            
            if (operationsRequired > k) {
                left = mid + 1;
            } else {
                best = mid;
                right = mid - 1;
            }
        }
        
        return i - best + 1;
    }
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        vector<long> prefix;
        prefix.push_back(nums[0]);
        
        for (int i = 1; i < nums.size(); i++) {
            prefix.push_back(nums[i] + prefix.back());
        }
        
        int ans = 0;
        for (int i = 0; i < nums.size(); i++) {
            ans = max(ans, check(i, k, nums, prefix));
        }
        
        return ans;
    }
};
```

**Solution 5: (Sliding Window)**
```
Runtime: 161 ms
Memory: 99.5 MB
```
```c++
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int i = 0;
        long long cur = 0;
        for (int j = 0; j < nums.size(); j ++) {
            if (j) {
                cur += (nums[j]-(long long)nums[j-1]) * (j-i);
            }
            if (cur > k) {
                cur -= nums[j] - nums[i];
                i += 1;
            }
        }
        return nums.size() - i;
    }
};
```
