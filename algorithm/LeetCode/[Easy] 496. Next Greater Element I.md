496. Next Greater Element I

You are given two arrays (**without duplicates**) `nums1` and `nums2` where `nums1`’s elements are subset of `nums2`. Find all the next greater numbers for `nums1`'s elements in the corresponding places of `nums2`.

The Next Greater Number of a number **x** in `nums1` is the first greater number to its right in `nums2`. If it does not exist, output `-1` for this number.

**Example 1:**
```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
```

**Example 2:**
```
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
```

**Note:**

* All elements in `nums1` and `nums2` are unique.
* The length of both `nums1` and `nums2` would not exceed `1000`.

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 48 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        d = {}
        for i, n2 in enumerate(nums2):
            for ng in nums2[i:]:
                if ng > n2:
                    d[n2] = ng
                    break
        for n1 in nums1:
            if n1 in d:
                ans.append(d[n1])
            else:
                ans.append(-1)
                
        return ans
```

**Solution 2: (Array, index as value)**
```
Runtime: 9 ms
Memory Usage: 6.4 MB
```
```c


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* nextGreaterElement(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize){
    int * result = (int *)malloc(nums1Size*sizeof(int));
    *returnSize = nums1Size;
    int count = 0;
    int temp[10000] = {0};
    for(int i=0; i<nums2Size; i++)
        temp[nums2[i]] = i;
    for(int i=0; i<nums1Size; i++)
    {
        int j;
        for(j=temp[nums1[i]]+1; j<nums2Size; j++)
            if(nums2[j] > nums1[i])
            {
                result[count++] = nums2[j];
                break;
            }
        if(j == nums2Size) result[count++] = -1;
    }
    return result;
}
```

**Solution 3: (Hash Table, mono stack)**

    nums1 = [4,1,2], 
    nums2 = [1,3,4,2]
    stk            
                 4
               43
            431

```
Runtime: 0 ms, Beats 100.00%
Memory: 13.35 MB, Beats 15.06%
```
```c++
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size(), n = nums2.size(), i;
        vector<int> dp(10001, -1), ans(m);
        stack<int> stk;
        for (i = n - 1; i >= 0; i --) {
            while (stk.size() && stk.top() < nums2[i]) {
                stk.pop();
            }
            if (stk.size()) {
                dp[nums2[i]] = stk.top();
            }
            stk.push(nums2[i]);
        }
        for (i = 0; i < m; i ++) {
            ans[i] = dp[nums1[i]];
        }
        return ans;
    }
};
```
