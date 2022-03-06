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
Runtime: 29 ms
Memory Usage: 15.9 MB
```
```c++
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n = nums.size();
        vector<int> myvec;
        int ele1 = -1 , ele2 = -1, count1 = 0 , count2 = 0;

        for(auto it : nums){

            if(ele1 == it) count1++;
            else if(ele2 == it) count2++;

            else if(count1 == 0) {
                ele1 = it;
                count1 = 1;
            }
            else if(count2 == 0) {
                ele2 = it;
                count2 = 1;
            }

            else {
                count1--;
                count2--;
            }
        }

        count1 =0;
        count2 = 0;
        for(auto it : nums){
            if(it == ele1) count1++;
            else if(it == ele2) count2++;
        }
        if(count1 > n/3) myvec.push_back(ele1);
        if(count2 > n/3) myvec.push_back(ele2);
        return myvec;
    }
};
```
