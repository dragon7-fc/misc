350. Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

**Example 1:**
```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
```

**Example 2:**
```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
```

**Note:**

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

**Follow up:**

* What if the given array is already sorted? How would you optimize your algorithm?
* What if nums1's size is small compared to nums2's size? Which algorithm is better?
* What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 52 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())
```

**Solution 2: (Hash Table)**
```
Runtime: 4 ms
Memory Usage: 10.4 MB
```
```c++
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> freq;
        vector<int> res;
        
        for (auto num : nums1) freq[num]++;
        
        for (auto num : nums2) {
            if (freq[num]) {
                res.push_back(num);
                freq[num]--;
            }
        }
        
        return res;
    }
};
```

**Solution 3: (Counting sort)**
```
Runtime: 4 ms
Memory: 12.80 MB
```
```c++
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> dp(1001), ans;
        for (int i = 0; i < nums1.size(); i ++) {
            dp[nums1[i]] += 1;
        }
        for (int i = 0; i < nums2.size(); i ++) {
            if (dp[nums2[i]] > 0) {
                ans.push_back(nums2[i]);
            }
            dp[nums2[i]] -= 1;
        }
        return ans;
    }
};
```
