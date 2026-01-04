354. Russian Doll Envelopes

You have a number of envelopes with widths and heights given as a pair of integers `(w, h)`. One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

**Note:**

Rotation is not allowed.

**Example:**
```
Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
```

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 192 ms
Memory Usage: 15.2 MB
```
```python
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:    
        # sort in one property and find the longest increasing subsequence
        # in the other property, that's it
        # to avoid cases such as [(3, 4), (3, 6)] - output should be 1
        # sort the (w) in ascending and (h) in descending

        #let's sort in second property(h) and then find LIS using first property(w)
        ln = len(envelopes)
        if ln <= 1:
            return ln

        envelopes = sorted(envelopes, key=lambda x:(x[1], -x[0]))
        #now find the LIS
        q = [envelopes[0][0]]
        
        def upperbound(ls, num):
            ln = len(ls)
            s, e = 0, ln-1
            while s <= e:
                mid = (e-s)//2 + s
                if ls[mid] == num:
                    #we can or we don't have to replace this
                    return mid
                elif ls[mid] < num:
                    if mid+1 < ln and ls[mid+1] > num:
                        return mid+1
                    s = mid + 1
                else:
                    if mid == 0:
                        return mid
                    e = mid-1

        for i in range(1, ln):
            num = envelopes[i][0]
            if q[-1] < num:
                q.append(num)
            elif q[-1] > num:
                # use binary search 
                idx = upperbound(q, num)
                q[idx] = num

        return len(q)
```

**Solution 2: (Binary Search)**
```
Runtime: 168 ms
Memory Usage: 15.4 MB
```
```python
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:    
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights = [0x3f3f3f3f] * len(envelopes)
        for _, h in envelopes:
            heights[bisect.bisect_left(heights, h)] = h
        return bisect.bisect_right(heights, 0x3f3f3f3f - 1)
```

**Solution 3: (Sort, Binary Search)**
```
Runtime: 144 ms
Memory Usage: 16.4 MB
```
```python
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # sort increasing in first dimension and decreasing on second
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        def lis(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)
        # extract the second dimension and run the LIS
        return lis([e[1] for e in envelopes])
```

**Solution 4: (Sort, Binary Search)**

    envelopes = [[5,4],[6,4],[6,7],[2,3]]
    sort      =  [2,3] [5,4] [6,7] [6,4]
    (x, -y)
    inc dec
                    y
                    3     4     7    4
                                     ^
    ans          [2,3] [5,4] [6,7]
                             [6,4]
    LIS on y
```
Runtime: 518 ms
Memory Usage: 77.6 MB
```
```c++
class Solution {
    static bool cmp(vector<int>& a, vector<int>& b){
        if(a[0]==b[0]) return a[1] > b[1];
        return a[0] < b[0];
    }
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        int n = envelopes.size();
        
        // sorting by height & if we encounter same height
        // sort by descending order of width
        sort(envelopes.begin(), envelopes.end(), cmp);
        
        // e.g. -> env => (3,8) (4,5) (2,1) (2,6) (7,8) (5,3) (5,7)
        // sorted version => (2,6) (2,1) (3,8) (4,5) (5,7) (5,3) (7,8)
        
        // Now, we only need to care about width
        // So, as of now we only need to look upon v[i][1]
        // [ 6, 1, 8, 5, 7, 3, 8 ]
        
        // Now, we can only put envolop a in envolop b another if width of a is
        // less than width of b, or we can say we need an envolop whose width
        // is just greater than envolop a ( height we have already handled )
        // So, we can think of lower_bound and Longest Increasing Subsequence
        
        // because we have sorted all envolopes of a particular height
        // by descending order of width, one envolope will not interfare with 
        // another envolop of same height, if we apply lower_bound
        // i.e. first elem greater than equal to itself in lis
        
        vector<int> lis;
        
        for(int i = 0;i<envelopes.size();i++){
            int ele = envelopes[i][1];
            
            int idx = lower_bound(lis.begin(), lis.end(), ele) - lis.begin();
            
            if(idx >= lis.size()) lis.push_back(ele);
            else lis[idx] = ele;
        }
        
        return lis.size();
    }
};
```
