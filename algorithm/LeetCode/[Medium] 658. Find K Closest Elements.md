658. Find K Closest Elements

Given a sorted array, two integers `k` and `x`, find the `k` closest elements to `x` in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

**Example 1:**
```
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
```

**Note:**

* The value `k` is positive and will always be smaller than the length of the sorted array.
* Length of the given array is positive and will not exceed `104`
* Absolute value of elements in the array and x will not exceed `104`

**UPDATE (2017/9/19):**

* The `arr` parameter had been changed to an array of integers (instead of a list of integers). Please reload the code definition to get the latest changes.

# Submissions
---
**Solution 1:**
```
Runtime: 328 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # left pointer and right pointer
        i, j = 0, len(arr)-1
        while j-i+1 != k:
            # will stop once we have k elements
            # else keep shifting pointers towards minimum difference
            left_diff = abs(arr[i] - x)
            right_diff = abs(arr[j] - x)
            if left_diff > right_diff:
                i += 1
            else:
                j -= 1
        return arr[i:j+1]
            
```

**Solution 2:**

**Disclaimer** - *Although the solution is same others on leetcode, I am trying to explain it in a way that helped me understand it better. *

We need to return `k` elements that are closest to `x`. The input array is sorted in ascending order. So, we will try to find the starting point of these `k` elements i.e. the first element in this list of `k` elements which will make it easier to return the `k` elements. Let's call this first element of the output list `start`.

Obviously, `start` will lie between indices `0` and `length - k` where length is the length of the array. So, it makes sense to perform binary search on this section only. Therfore, we initialize `left=0` and `right = len(arr) - k`

Because we have to return `k` elements, it also makes sense to consider a window of `k` elements for comparison.

Consider the following boundaries for the element `x`
```
left ......... mid ......... mid + k ......... right
```

1. `x <= arr[mid]`
1. `arr[mid + k] <= x`
1. `arr[mid] < x < arr[mid + k]`

* **Case 1 :** `x <= arr[mid]`

If x is less than `arr[mid]` then it's clear that `arr[mid + k]` cannot be a part of our output `k` elements. This is because there are `k + 1` elements between `arr[mid]` and `arr[mid + k]` inclusive. So, the `start` will either be `mid` or towards the left of it.

* **Case 2 :** `arr[mid + k] <= x`
Similar to previous case, `arr[mid]` cannot be a part of our output `k` elements because of the `k + 1` elements we have in between. Therefore, `start` will lie towards the right of `mid`

* **Case 3 :** `arr[mid] < x < arr[mid + k]`
This is more like a combination of the above two cases.

    * If x is closer to `arr[mid]` then just like our case 1, `arr[mid + k]` cannot be a part of our output `k` elements. Therefore, our `start` will either be `mid` or towards the left of it.

    * If x is closer to `arr[mid + k]`, then just like case 2, `arr[mid]` cannot be a part of our output `k` elements, which means that our `start` will lie towards the right of `mid`.

Let's implement this
```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k
        
        while left < right:
            mid = left + (right - left)//2

            if x <= arr[mid]:
                right = mid
            elif x >= arr[mid + k]:
                left = mid + 1
            elif x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left : left + k]
```

The interesting part is that the first two if-elif conditions are handled by the last two conditionals. So, we can simply eliminate them.
```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k
        
        while left < right:
            mid = left + (right - left)//2

            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left : left + k]
```

```
Runtime: 296 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k
        
        while left < right:
            mid = left + (right - left)//2

            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left : left + k]
```

**Solution 3: (Queue)**
```
Runtime: 24 ms
Memory Usage: 31.8 MB
```
```python
class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        deque<int> closest;
        
        for(int i = 0; i < arr.size(); ++i){
            closest.push_back(arr[i]);
            while(closest.size() > k) {
                int front = abs(closest.front() - x);
                int back = abs(closest.back() - x);
                
                if(front < back || (front == back && closest.front() < closest.back())){
                    closest.pop_back();
                } else {
                    closest.pop_front();
                }
            }
        }
        
        return vector<int>(begin(closest),end(closest));
    }
};
```