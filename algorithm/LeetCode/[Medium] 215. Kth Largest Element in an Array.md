215. Kth Largest Element in an Array

Find the `k`th largest element in an unsorted array. Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.

**Example 1:**
```
Input: [3,2,1,5,6,4] and k = 2
Output: 5
```

**Example 2:**
```
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
```

**Note:**

* You may assume `k` is always valid, `1 ≤ k ≤ array's length`.

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 44 ms
Memory Usage: N/A
```
```python
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums)[-k]
```

**Solution 2: (Heap)**
```
Runtime: 48 ms
Memory Usage: N/A
```
```python
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1]
```

**Solution 3: (Divide and Conquer, Quick sort)**
```
Runtime: 2056 ms
Memory Usage: 115.1 MB
```
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[k-1]
        b = 0
        a = nums[-1]
        for i in range( len(nums)-1):
            if nums[i] < a:
                nums[i], nums[b] = nums[b], nums[i]
                b += 1
        nums[-1], nums[b] = nums[b], nums[-1]
        if len(nums)-b == k:
            return nums[b]
        elif k > len(nums)-b:
            return self.findKthLargest(nums[:b], k-len(nums)+b)
        else:
            return self.findKthLargest(nums[b+1:], k)
```

**Solution 4: (Sort)**
```
Runtime: 57 ms
Memory Usage: 6.4 MB
```
```c
int helper_sort(int* nums, int left, int right)
{
    int pivot  = nums[left];
    int temp,start=left;
    
    while(left<right)
    {
        while((left<right) && (nums[right] >= pivot))
            right--;
        while((left<right) && (nums[left] <= pivot))
            left++;
        if(left<right)
        {
            temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
        }
    }
    
    nums[start] = nums[right];
    nums[right] = pivot;
    
    return right;
}

int findKthLargest(int* nums, int numsSize, int k){
    int i,left=0,right=numsSize-1;
    int pos;
    
    if((nums==NULL) || (numsSize==0) || (k==0))
        return -1;
    
    k = numsSize - k;
    while(left<right)
    {
        pos = helper_sort(nums,left,right);
        if(pos < k)
        {
            left = pos + 1;
        }
        else if (pos > k)
        {
            right = pos - 1;
        }
        else
            break;
    }
    return nums[k];
}
```

**Solution 5: (Heap, min heap)**
```
Runtime: 4 ms
Memory Usage: 10.1 MB
```
```c++
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> q;
        int n = nums.size();
        for(auto num: nums)
        {
            q.push(num);
            if(q.size() > k)
                q.pop();
        }
        return q.top();
    }
};
```

**Solution 6: (Heap, max heap)**
```
Runtime: 10 ms
Memory Usage: 10.3 MB
```
```c++
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int> q;
        
        for (int i = 0; i < nums.size(); i++) {
            q.push(nums[i]);
            if (q.size() > (nums.size()+1-k)) {
                q.pop();
            }
        }
        
        return q.top();
    }
};
```

**Solution 7: (Sort)**
```
Runtime: 9 ms
Memory Usage: 9.9 MB
```
```c++
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        return nums[nums.size()-k];
    }
};
```
