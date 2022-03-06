2191. Sort the Jumbled Numbers

You are given a **0-indexed** integer array `mapping` which represents the mapping rule of a shuffled decimal system. `mapping[i] = j` means digit `i` should be mapped to digit `j` in this system.

The **mapped value** of an integer is the new integer obtained by replacing each occurrence of digit `i` in the integer with `mapping[i]` for all `0 <= i <= 9`.

You are also given another integer array `nums`. Return the array `nums` sorted in **non-decreasing** order based on the mapped values of its elements.

**Notes:**

* Elements with the same mapped values should appear in the **same relative order** as in the input.
* The elements of `nums` should only be sorted based on their mapped values and **not be replaced** by them.
 

**Example 1:**
```
Input: mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]
Output: [338,38,991]
Explanation: 
Map the number 991 as follows:
1. mapping[9] = 6, so all occurrences of the digit 9 will become 6.
2. mapping[1] = 9, so all occurrences of the digit 1 will become 9.
Therefore, the mapped value of 991 is 669.
338 maps to 007, or 7 after removing the leading zeros.
38 maps to 07, which is also 7 after removing leading zeros.
Since 338 and 38 share the same mapped value, they should remain in the same relative order, so 338 comes before 38.
Thus, the sorted array is [338,38,991].
```

**Example 2:**
```
Input: mapping = [0,1,2,3,4,5,6,7,8,9], nums = [789,456,123]
Output: [123,456,789]
Explanation: 789 maps to 789, 456 maps to 456, and 123 maps to 123. Thus, the sorted array is [123,456,789].
```

**Constraints:**

* `mapping.length == 10`
* `0 <= mapping[i] <= 9`
* All the values of `mapping[i]` are **unique**.
* `1 <= nums.length <= 3 * 10^4`
* `0 <= nums[i] < 10^9`

# Submissions
---
**SOlution 1: (Sort, String)**
```
Runtime: 2057 ms
Memory Usage: 20.3 MB
```
```python
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d = {str(i): str(v) for i, v in enumerate(mapping)}
        return sorted(nums, key=lambda num: int(''.join([d[c] for c in str(num)])))
```

**Solution 2: (Sort, String)**
```
Runtime: 1037 ms
Memory Usage: 83.9 MB
```
```python
class Solution {
public:
    vector<int> sortJumbled(vector<int>& mapping, vector<int>& nums) {
        vector<pair<int,int>>vec;
        
        for(int i = 0;i<nums.size();++i){
            int num = nums[i];
            string number = to_string(num); 
            string formed = "";
            for(int j= 0;j<number.size();++j){
                formed+=(to_string(mapping[number[j]-'0']));
            }
            int value = stoi(formed);
            vec.push_back({value,i});
        }
        
        sort(vec.begin(),vec.end());
        vector<int>ans;
        for(auto pa:vec){
            int found = nums[pa.second];
            ans.push_back(found);
        }
        
        return ans;
    }
};
```

**Solution 3: (Sort)**
```
Runtime: 538 ms
Memory Usage: 77 MB
```
```c++
class Solution {
public:
    vector<int> sortJumbled(vector<int>& mapping, vector<int>& nums) {
        vector<pair<int,int>> maped(nums.size());
        for(int i=0;i<nums.size();i++){
            int cur=nums[i],newnum=0; bool flag=false;
            for(int j=9;j>=0;j--){
                int digit=cur/pow(10,j);
                if(!digit && !flag && j!=0) continue;
                flag=true;
                newnum+=(mapping[digit]*pow(10,j));
                cur-=(digit*pow(10,j));
            }
            maped[i].first=newnum;
            maped[i].second=i;
        }
        sort(maped.begin(),maped.end(),[](pair<int,int>& a,pair<int,int>& b){
            if(a.first==b.first)
                return a.second<b.second;
            return a.first<b.first;
        });
        vector<int> res(nums.size());
        for(int i=0;i<maped.size();i++){
            res[i]=nums[maped[i].second];
        }
        return res;
    }
};
```
