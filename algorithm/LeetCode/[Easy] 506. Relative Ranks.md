506. Relative Ranks

Given scores of **N** athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

**Example 1:**
```
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
```

**Note:**

* `N` is a positive integer and won't exceed `10,000`.
* All the scores of athletes are guaranteed to be unique.

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 72 ms
Memory Usage: 15 MB
```
```python
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        ranks = {val:idx for idx,val in enumerate(sorted(nums, reverse=True))}
        ans = []
        for i in range(len(nums)):
            cur_player = nums[i]
            if ranks[cur_player] == 0:
                ans.append('Gold Medal')
            elif ranks[cur_player] == 1:
                ans.append('Silver Medal')
            elif ranks[cur_player] == 2:
                ans.append('Bronze Medal')
            else:
                ans.append(str(ranks[cur_player]+1))
                
        return ans
```

**Solution 2: (Sort)**
```
Runtime: 24 ms
Memory Usage: 11.2 MB
```
```c++
class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& nums) {
        map<int,int,greater<int>> rates;
        vector <string> res(nums.size());
        for(int i = 0 ; i < nums.size();i++)
        {
            rates[nums[i]] = i;
        }
        int j = 1;
        string medals[3] = {"Gold Medal","Silver Medal", "Bronze Medal"};
        for(auto m : rates)
        {
           if(j < 4)
               res[m.second] = medals[j-1];
            else
            res[m.second] = to_string(j);

            j++;
        }

        return res;

    }
};
```