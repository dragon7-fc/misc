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
Runtime: 376 ms
Memory Usage: 19.8 MB
```
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) >1: 
            mid = len(nums)//2 #Finding the mid of the array 
            L = nums[:mid] # Dividing the array elements  
            R = nums[mid:] # into 2 halves 

            self.sortArray(L) # Sorting the first half 
            self.sortArray(R) # Sorting the second half 

            i = j = k = 0

            # Copy data to temp arrays L[] and R[] 
            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    nums[k] = L[i] 
                    i+=1
                else: 
                    nums[k] = R[j] 
                    j+=1
                k+=1

            # Checking if any element was left 
            while i < len(L): 
                nums[k] = L[i] 
                i+=1
                k+=1

            while j < len(R): 
                nums[k] = R[j] 
                j+=1
                k+=1
            
        return nums
```

**Solution 2: (Quick Sort)**
```
Runtime: 328 ms
Memory Usage: 19.7 MB
```
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def partition(arr,low,high): 
            i = ( low-1 )         # index of smaller element 
            pivot = arr[high]     # pivot 
            for j in range(low , high): 
                if   arr[j] <= pivot:
                    i = i+1 
                    arr[i],arr[j] = arr[j],arr[i] 
            arr[i+1],arr[high] = arr[high],arr[i+1] 
            return ( i+1 ) 
        
        def quickSort(arr, low, high): 
            if low < high:
                pi = partition(arr,low,high) 
                quickSort(arr, low, pi-1) 
                quickSort(arr, pi+1, high)
            return arr
            
        return quickSort(nums, 0, len(nums)-1)
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