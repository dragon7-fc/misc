163. Missing Ranges

Share
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

**Example:**
```
Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
```

# Submissions
---
**Solution 1: (Array, Greedy)**
```
Runtime: 28 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # 1. empty arr
        if not nums: return [str(lower)+'->'+str(upper)] if lower != upper else  [str(lower)]
        ans=[]
        
        # 2. process start section
        if nums[0] > lower:
            ans.append(str(lower) if nums[0] == lower+1 else str(lower)+'->'+str(nums[0]-1))
        end=nums[0]
        
        # 3. process mid section
        for v in nums[1:]:
            if v==end or v==end+1:
                end=v
            else:
                ans.append(str(end+1) if v-end == 2 else str(end+1)+'->'+str(v-1))
                end=v
                
        # 4. process end section
        if end < upper:
            ans.append(str(end+1) if end+1==upper else str(end+1)+'->'+str(upper))
  
        return ans
```

**Solution 2: (Array, Greedy)**
```
Runtime: 0 ms
Memory Usage: 7 MB
```
```c++
class Solution {
public:
    string formRange(int low, int high){
        if(low == high)
            return to_string(low);
        else{
            return to_string(low) + "->" + to_string(high);
        }
    }
    vector<string> findMissingRanges(vector<int>& nums, int lower, int upper) {
        vector<string> res;
        if(nums.size() == 0){
            res.push_back(formRange(lower, upper));
            return res;
        }
        
        if(nums[0] > lower){
            res.push_back(formRange(lower, nums[0] - 1));
        }
        
        for(int i = 1; i < nums.size(); i++){
            if(nums[i] != nums[i -1] && nums[i] > nums[i -1] + 1)
                res.push_back(formRange(nums[i -1] + 1, nums[i] - 1));
        }
        
        if(nums[nums.size() - 1] < upper)
            res.push_back(formRange(nums[nums.size() - 1] + 1, upper));     
        return res;
    }
};
```