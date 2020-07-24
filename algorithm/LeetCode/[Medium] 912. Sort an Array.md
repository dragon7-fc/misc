912. Sort an Array

Given an array of integers `nums`, sort the array in ascending order.

 

**Example 1:**
```
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
```

**Example 2:**
```
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
```

**Constraints:**

* `1 <= nums.length <= 50000`
* `-50000 <= nums[i] <= 50000`

# Submissions
---
**Solution 1: (Merge Sort)**
```
Runtime: 408 ms
Memory Usage: 19.7 MB
```
```python
class Solution:
    max_length = 0
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > self.max_length:
            self.max_length = len(nums)
        if len(nums) > 1:
            mid = len(nums) // 2
            L = nums[:mid]
            R = nums[mid:]

            self.sortArray(L)
            self.sortArray(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1
        if len(nums) == self.max_length:
            return nums
```

**Solution 2: (Merge Sort)**
```
Runtime: 196 ms
Memory Usage: 90.1 MB
```
```c++
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        mergeSort(nums);
        return nums;
    }
    void mergeSortTwoVec(vector<int>& subVec1, vector<int>& subVec2, vector<int>& vec) {
        int i = 0;
        int j = 0;
        while (i < subVec1.size() && j < subVec2.size()) {
            if (subVec1[i] <= subVec2[j]) {
                vec.push_back(subVec1[i]);
                i++;
            } else {
                vec.push_back(subVec2[j]);
                j++;
            }
        }

        while (i < subVec1.size()) {
            vec.push_back(subVec1[i]);
            i++;
        }

        while (j < subVec2.size()) {
            vec.push_back(subVec2[j]);
            j++;
        }
    }

    void mergeSort(vector<int>& vec) {
        if (vec.size() < 2) {
            return; // When the vec size less than 2, jump out of recursion and solve directly.
        }

        vector<int> sub1;
        vector<int> sub2;
        int mid = vec.size() / 2;
        for (int i = 0; i < mid; i++) {
            sub1.push_back(vec[i]);
        }

        for (int i = mid; i < vec.size(); i++) {
            sub2.push_back(vec[i]);
        }

        mergeSort(sub1);
        mergeSort(sub2);
        vec.clear();
        mergeSortTwoVec(sub1, sub2, vec);
    }
};
```

**Solution 3: (Quick Sort)**
```
Runtime: 32 ms
Memory Usage: 15.9 MB
```
```c++
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        int n=nums.size(), low=0, high=n-1;
        quickSort(nums, low, high);
        return nums;
    }
    void swap(int &a, int &b)
    {
        int t=a;
        a = b;
        b = t;
    }
    int partition(vector<int>& nums, int low, int high)
    {
        int i=low-1, pivot=nums[high];
        for(int j=low; j<high; j++)
        {
            if(nums[j]<=pivot) 
            {
                i++;
                swap(nums[i], nums[j]);
            }
        }
        swap(nums[i+1], nums[high]);
        return i+1;
    }
    void quickSort(vector<int>& nums, int low, int high)
    {
        if(low<high)
        {
            int pivot=partition(nums, low, high);
            quickSort(nums, low, pivot-1);
            quickSort(nums, pivot+1, high);
        }
    }
};
```