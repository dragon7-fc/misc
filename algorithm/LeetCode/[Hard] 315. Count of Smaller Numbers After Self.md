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