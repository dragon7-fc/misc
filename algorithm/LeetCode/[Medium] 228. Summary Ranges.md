228. Summary Ranges

Given a sorted integer array without duplicates, return the summary of its ranges.

**Example 1:**
```
Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
```
**Example 2:**
```
Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
```

# Submissions
---
**Solution 1: (Two Pointers)**
```
Runtime: 28 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        N = len(nums)
        i, j = 0, 0
        ans = []
        while i < N:
            while j + 1 < N and nums[j + 1] == nums[j] + 1:
                j += 1
            if i != j:
                ans.append('{}->{}'.format(nums[i], nums[j]))
            else:
                ans .append('{}'.format(str(nums[i])))
            j = j + 1
            i = j
            
        
        return ans
```

**Solution 2: (Two Pointers)**
```
Runtime: 48 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        N = len(nums)
        if N <= 1: return list(map(str,nums))
        i = j = 0
        ans = []
        while j < N:
            while j < N-1 and nums[j]+1 == nums[j+1]:
                j += 1
            if i == j:
                ans += [str(nums[i])]
            else:
                ans += [str(nums[i]) + "->" + str(nums[j])]
            i = j = j+1
        return ans
```

**Solution 2: (Two Pointers, one target one index)**
```
Runtime: 0 ms
Memory Usage: 7 MB
```
```c++
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        // resultant string
        vector<string> result;
        
        int n = nums.size();
		// if size happens to be  zero return empty string
        if(n == 0 )
                return result;
        
		// assigning first element to a
        int a = nums[0];
        
        for(int i = 0; i<n; i++)
        {
			// if one of both is true
            if( i == n-1 || nums[i]+1 != nums[i+1])
            {
			    // if current element is not equals a
				// this means we have found a range.
                if(nums[i] != a)
                    result.push_back(to_string(a)+ "->"+ to_string(nums[i]));
					
				// this means we have reached to the end of string and now
				// we have to add a that should be the last element
                else
                        result.push_back(to_string(a));
						
				// checking  for this condition so that a got updated for next range
				// also n-1 so that a doesn't contain out of bound value
                if(i != n-1)
                    a = nums[i+1];
            }
        }
		// return result
        return result;
    }
};
```
