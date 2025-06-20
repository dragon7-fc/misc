1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

Given an array of integers `nums` and an integer `limit`, return the size of the longest continuous subarray such that the absolute difference between any two elements is less than or equal to `limit`.

In case there is no subarray satisfying the given condition return 0.

 

**Example 1:**
```
Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
```

**Example 2:**
```
Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
```

**Example 3:**
```
Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`
* `0 <= limit <= 10^9`

# Submissions
---
**Solution 1: (Sliding Window, Min Max Queue)**
```
Runtime: 436 ms
Memory Usage: 24.1 MB
```
```python
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque, max_deque = deque(), deque()
        l = r = 0
        ans = 0
        while r < len(nums):
            while min_deque and nums[r] <= nums[min_deque[-1]]:
                min_deque.pop()
            while max_deque and nums[r] >= nums[max_deque[-1]]:
                max_deque.pop()
            min_deque.append(r)
            max_deque.append(r)
            
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                l += 1
                if l > min_deque[0]:
                    min_deque.popleft()
                if l > max_deque[0]:
                    max_deque.popleft()
            
            ans = max(ans, r - l + 1)
            r += 1
                
        return ans
```

**Solution 2: (Sliding Window, Min Max Queue)**
```
Runtime: 356 ms
Memory Usage: 24 MB
```
```python
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxd = collections.deque()
        mind = collections.deque()
        i = 0
        for a in nums:
            while len(maxd) and a > maxd[-1]: maxd.pop()
            while len(mind) and a < mind[-1]: mind.pop()
            maxd.append(a)
            mind.append(a)
            if maxd[0] - mind[0] > limit:
                if maxd[0] == nums[i]: maxd.popleft()
                if mind[0] == nums[i]: mind.popleft()
                i += 1
        return len(nums) - i
```

**Solution 3: (Sliding Window, sorted hash table)**
```
Runtime: 118 ms
Memory: 65.07 MB
```
```c++
class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        map<int,int> cnt;
        int i = 0, ans = 0;
        for (int j = 0; j < nums.size(); j ++) {
            cnt[nums[j]] += 1;
            while (cnt.size() && cnt.rbegin()->first - cnt.begin()->first > limit) {
                cnt[nums[i]] -= 1;
                if (cnt[nums[i]] == 0) {
                    cnt.erase(nums[i]);
                }
                i += 1;
            }
            ans = max(ans, j-i+1);
        }
        return ans;
    }
};
```

**Solution 4: (Two Deques)**

    8  2  4  7, limit = 4
             ^j
          ^i
    8  82 4  7
       x
    8  2  24 247
       ^     x

    10 1   2  4   7    2, limit = 5
                  ^j
           ^i
    10 101 2  4   7    72
        x
    10 1   12 124 1247 22

```
Runtime: 27 ms, Beats 65.60%
Memory: 77.49 MB, Beats 83.09%
```
```c++
class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        int n = nums.size(), i = 0, j, ans = 0;
        deque<int> maxq, minq;
        for (j = 0; j < n; j ++) {
            while (maxq.size() && nums[maxq.back()] < nums[j]) {
                maxq.pop_back();
            }
            maxq.push_back(j);
            while (minq.size() && nums[minq.back()] > nums[j]) {
                minq.pop_back();
            }
            minq.push_back(j);
            while (maxq.size() && minq.size() && nums[maxq.front()] - nums[minq.front()] > limit) {
                if (maxq.front() == i) {
                    maxq.pop_front();
                }
                if (minq.front() == i) {
                    minq.pop_front();
                }
                i += 1;
            }
            ans = max(ans, j-i+1);
        }
        return ans;
    }
};
```
