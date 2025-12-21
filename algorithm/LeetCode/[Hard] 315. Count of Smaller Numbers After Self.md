315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. The counts array has the property where `counts[i]` is the number of smaller elements to the right of `nums[i]`.

**Example:**
```
Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
```

# Submissions
---
**Solution 1: (Sort, Greedy)**
```
Runtime: 1228 ms
Memory Usage: 15.8 MB
```
```python
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        ans = [None] * len(nums)
        for i in range(len(nums)):
            j = arr.index(nums[i])
            ans[i] = j
            arr.pop(j)
        return ans

        # find nums[i]'s index in the arr in each loop.
        # think of this index as a rank, so there are j elements smaller than nums[i]
        # nums[i] is no longer useful for nums[i+1],nums[i+2].... Since we only need to consider the elements to the right
        # so pop out nums[i] from the arr, and start the next loop		
```

**Solution 2: (Binary Search, Insertion Sort)**
```
Runtime: 108 ms
Memory Usage: 15.9 MB
```
```python
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        sortedNums = [nums[-1]]
        ans = [0 for _ in range(len(nums))]
        for i in range(len(nums) -2, -1, -1):
            index = bisect.bisect_left(sortedNums, nums[i])
            ans[i] = index
            sortedNums.insert(index, nums[i])
        return ans
```

**Solution 3: (Segment Tree)**
```
Runtime: 360 ms
Memory Usage: 18.9 MB
```
```python
class SegMentTreeNode:
    def __init__(self,start,end,val,left = None,right = None):
        self.start = start
        self.end = end
        self.val = val
        self.left = left
        self.right = right
def buildTree(start,end,array):
    if start == end:
        return SegMentTreeNode(start,end,array[start])
    mid = (start+end)//2
    left = buildTree(start,mid,array)
    right = buildTree(mid+1,end,array)
    return SegMentTreeNode(start,end,left.val+right.val,left,right)
def update(node,ind,val):
    if node.start == node.end == ind:
        node.val = val
        return 
    mid = (node.start + node.end)//2
    if ind>mid:
        update(node.right,ind,val)
    else:
        update(node.left,ind,val)
    node.val = node.left.val + node.right.val
def queryRange(node,start,end):
    if start>end:
        return 0
    if node.start == start and node.end == end:
        return node.val
    else:
        mid = (node.start + node.end) // 2
        if start>mid:
            return queryRange(node.right,start,end)
        elif end<=mid:
            return queryRange(node.left,start,end)
        else:
            return queryRange(node.left,start,mid)+queryRange(node.right,mid+1,end)
        
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        sortedNums = sorted(set(nums))
        wait =  {n:i for i,n in enumerate(sortedNums)}
        freq = [0 for i in range(len(sortedNums))]
        ans = []
        root = buildTree(0,len(freq) - 1,freq)
        for n in nums[::-1]:
            freq[wait[n]] += 1
            update(root,wait[n],freq[wait[n]])
            ans.append(queryRange(root,0,wait[n]-1))
        return ans[::-1]
```

**Solution 4: (Ordered Set)**
```
Runtime: 1050 ms
Memory Usage: 150.7 MB
```
```c++
#include <ext/pb_ds/assoc_container.hpp> // Common file
#include <ext/pb_ds/tree_policy.hpp>
#include <functional> // for less
#include <iostream>
using namespace __gnu_pbds;
using namespace std;
typedef tree<int, null_type, less_equal<int>, rb_tree_tag,
             tree_order_statistics_node_update>
    ordered_set;

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> ans(nums.size(),0);
        ordered_set s;
        for(int i=nums.size()-1;i>=0;i--){
            s.insert(nums[i]);
            ans[i] = s.order_of_key(nums[i]);
        }
        return ans;
    }
};
```

**Solution 5: (Merge Sort)**
```
Runtime: 779 ms
Memory Usage: 216.2 MB
```
```c++
class Solution {
    void merge(int left, int mid, int right, vector<pair<int, int>>& arr,vector<int>& count)
    {
        vector<pair<int, int>> temp(right - left + 1);
        
        int i = left;
        int j = mid + 1;
        int k = 0;
        
        while(i <= mid && j <= right)
        {
            if(arr[i].first <= arr[j].first)
            {
                temp[k++] = arr[j++]; 
            }
            else
            {
                count[arr[i].second] += (right - j + 1);
                
                temp[k++] = arr[i++];
            }
        }
        
        while(i <= mid)
        {
            temp[k++] = arr[i++];
        }
        
        while(j <= right)
        {
            temp[k++] = arr[j++];
        }
        
        for(int l = left; l <= right; l++)
        arr[l] = temp[l - left];
        
    }
                
    void mergeSort(int left, int right, vector<pair<int, int>>& arr, vector<int>& count)
    {
        if(left >= right)
        {
            return;
        }

        int mid = left + (right - left) / 2;
        
        mergeSort(left, mid, arr, count);
        mergeSort(mid + 1, right, arr, count);
        
        merge(left, mid, right, arr, count);
    }
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n=nums.size();
	    vector<pair<int, int>> arr;
        
	    for(int i = 0; i < n; i++)
	    {
	        arr.push_back({nums[i], i});
	    }
	    
	    vector<int> count(n, 0);
	    
	    mergeSort(0, n - 1, arr, count);
	    
	    return count;
    }
};
```

**Solution 6: (BIT)**
```
Runtime: 19 ms, Beats 98.47%
Memory: 91.65 MB, Beats 90.00%
```
```c++
class BIT {
    vector<int> pre;
public:
    BIT() {}
    void build(int n) {
        pre.resize(n + 1);
    }
    void update(int i, int val) {
        int j = i + 1;
        while (j < pre.size()) {
            pre[j] += val;
            j += j & (-j);
        }
    }
    int query(int i) {
        int rst = 0;
        int j = i;
        while (j > 0) {
            rst += pre[j];
            j -= j & (-j);
        }
        return rst;
    }
};

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size(), i;
        BIT bit;
        bit.build(20001);
        vector<int> ans(n);
        bit.update(nums[n - 1] + 10000, 1);
        for (i = n - 2; i >= 0; i --) {
            ans[i] = bit.query(nums[i] + 10000); // smaller elements to the right
            bit.update(nums[i] + 10000, 1);
        }
        return ans;
    }
};
```
