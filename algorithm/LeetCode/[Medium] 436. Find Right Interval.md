436. Find Right Interval

Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

**Note:**

* You may assume the interval's end point is always bigger than its start point.
* You may assume none of these intervals have the same start point.
 

**Example 1:**
```
Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.
```

**Example 2:**
```
Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.
```

**Example 3:**
```
Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.
```

**NOTE:** input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

# Submissions
---
**Solution 1: (Sort by start, search by end interval)**
```
Runtime: 304 ms
Memory Usage: 18.7 MB
```
```python
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        N = len(intervals)
        d = {}
        start_idx = {start:i for i, (start, _) in enumerate(intervals)}
        sorted_start = sorted(start for start, _ in intervals)
        for i, (start, end) in enumerate(intervals):
            idx = bisect.bisect_left(sorted_start, end)  # search every end in every sorted_start
            d.setdefault(start, start_idx[sorted_start[idx]] if idx != N else -1)
        
        return list(map(lambda x: d[x[0]], intervals))
```

**Solution 2: (Sort, Binary Search)**
```
Runtime: 105 ms
Memory Usage: 25.6 MB
```
```c++
class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        int n = intervals.size();
        if(n==1){
            return {-1};
        }
        vector<int> ans;
        vector<pair<int,int>> arr;
        // creating array to store index and start point 
        for(int i = 0;i<n;i++){
            arr.push_back({intervals[i][0],i});
        }
        // sorting the array to apply binary search 
        sort(arr.begin(),arr.end());
        for(int i =0;i<n;i++){
            int s = 0;
            int e = n-1;
            pair<int,int> pp={-1,-1};
            //defining an intial value for ans that needs to be pushed 
            while(s<=e){
                int m = (s+e)/2;//finding the mid 
                if(arr[m].first==intervals[i][1]){
                    ans.push_back(arr[m].second);
                    break;
                }
                else if(arr[m].first<intervals[i][1]){
                    s = m+1;
                }
                else{
                    e = m-1;
                    pp = arr[m];//just greater than end point 
                }
            }
            if(ans.size()-1!=i){//if the element is already pushed 
                if(pp.first<=intervals[i][1]){// if all the the end point are smaller then the start 
                    ans.push_back(-1);
                }
                else{
                    ans.push_back(pp.second);
                }
            }
        }
        return ans;
    }
};
```
