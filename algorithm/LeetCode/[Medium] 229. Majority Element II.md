229. Majority Element II

Given an integer array of size `n`, find all elements that appear more than `⌊ n/3 ⌋` times.

**Note:** The algorithm should run in linear time and in $O(1)$ space.

**Example 1:**
```
Input: [3,2,3]
Output: [3]
```
**Example 2:**
```
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
```

**Constraints:**

* `1 <= nums.length <= 5 * 10^4`
* `-10^9 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Boyer-Moore Voting Algorithm)**
```
Runtime: 204 ms
Memory Usage: 15 MB
```
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # 1st pass
        count1, count2, candidate1, candidate2 = 0, 0, None, None
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        # 2nd pass
        result = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums)//3:
                result.append(c)
        
        return result
```

**Solution 2: (Hash Table)**
```
Runtime: 19 ms
Memory Usage: 16 MB
```
```c++
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n = nums.size();
        vector<int> myvec;
        unordered_map<int,int> mymap;
        for(auto it : nums) mymap[it]++;
        for(auto it : mymap)
            if(it.second > n/3) myvec.push_back(it.first);

        return myvec;
    }
};
```

**Solution 3: (Boyer-Moore Voting Algorithm)**
```
Runtime: 11 ms
Memory: 16.4 MB
```
```c++
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> result;
        int candidate1 = 0, candidate2 = 1, count1 = 0, count2 = 0;

        for (int num : nums) {
            if (num == candidate1) count1++;
            else if (num == candidate2) count2++;
            else if (count1 == 0) candidate1 = num, count1 = 1;
            else if (count2 == 0) candidate2 = num, count2 = 1;
            else count1--, count2--;
        }

        count1 = count2 = 0;

        for (int num : nums) {
            if (num == candidate1) count1++;
            if (num == candidate2) count2++;
        }

        if (count1 > nums.size() / 3) result.push_back(candidate1);
        if (count2 > nums.size() / 3) result.push_back(candidate2);

        return result;
    }
};
```
