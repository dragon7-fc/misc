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

> **Solution 3: (Merge Sort, TC: O(n log n), SC: O(n))**
```
Runtime: 49 ms, Beats 72.51%
Memory: 72.99 MB, Beats 65.82%
```
```c++
class Solution {
    // Function to merge two sub-arrays in sorted order.
    void merge(vector<int> &arr, int left, int mid, int right, vector<int> &tempArr) {
        // Calculate the start and sizes of two halves.
        int start1 = left;
        int start2 = mid + 1;
        int n1 = mid - left + 1;
        int n2 = right - mid;
        
        // Copy elements of both halves into a temporary array.
        for (int i = 0; i < n1; i++) {
            tempArr[start1 + i] = arr[start1 + i];
        }
        for (int i = 0; i < n2; i++) {
            tempArr[start2 + i] = arr[start2 + i];
        }

        // Merge the sub-arrays 'in tempArray' back into the original array 'arr' in sorted order.
        int i = 0, j = 0, k = left;
        while (i < n1 && j < n2) {
            if (tempArr[start1 + i] <= tempArr[start2 + j]) {
                arr[k] = tempArr[start1 + i];
                i += 1;
            } else {
                arr[k] = tempArr[start2 + j];
                j += 1;
            }
            k += 1;
        }

        // Copy remaining elements
        while (i < n1) {
            arr[k] = tempArr[start1 + i];
            i += 1;
            k += 1;
        }
        while (j < n2) {
            arr[k] = tempArr[start2 + j];
            j += 1;
            k += 1;
        }
    }

    // Recursive function to sort an array using merge sort
    void mergeSort(vector<int> &arr, int left, int right, vector<int> &tempArr) {
        if (left >= right) {
            return;
        }
        int mid = (left + right) / 2;
        // Sort first and second halves recursively.
        mergeSort(arr, left, mid, tempArr);
        mergeSort(arr, mid + 1, right, tempArr);
        // Merge the sorted halves.
        merge(arr, left, mid, right, tempArr);
    }
public:
    vector<int> sortArray(vector<int>& nums) {
        vector<int> temporaryArray(nums.size());
        mergeSort(nums, 0, nums.size() - 1, temporaryArray);
        return nums;
    }
};
```

**Solution 4: (Quick Sort)**
```
Runtime: 32 ms
Memory Usage: 15.9 MB
```
```c++
class Solution {
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
public:
    vector<int> sortArray(vector<int>& nums) {
        int n=nums.size(), low=0, high=n-1;
        quickSort(nums, low, high);
        return nums;
    }
};
```

**Solution 5: (Heap sort, max heap, TC: O(n log n), SC: O(log n))**
```
Runtime: 59 ms, Beats 64.09%
Memory: 70.80 MB, Beats 92.93%
```
```c++
class Solution {
    // Function to heapify a subtree (in top-down order) rooted at index i.
    void heapify(vector<int>& arr, int n, int i) {
        // Initialize largest as root 'i'.
        int largest = i; 
        int left = 2 * i + 1;
        int right = 2 * i + 2; 

        // If left child is larger than root.
        if (left < n && arr[left] > arr[largest]) {
            largest = left;
        }

        // If right child is larger than largest so far.
        if (right < n && arr[right] > arr[largest]) {
            largest = right;
        }

        // If largest is not root swap root with largest element
        // Recursively heapify the affected sub-tree (i.e. move down).
        if (largest != i) {
            swap(arr[i], arr[largest]); 
            heapify(arr, n, largest);
        }
    }

    void heapSort(vector<int>& arr) {
        int n = arr.size();
        // Build heap; heapify (top-down) all elements except leaf nodes.
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }

        // Traverse elements one by one, to move current root to end, and
        for (int i = n - 1; i >= 0; i--) {
            swap(arr[0], arr[i]);
            // call max heapify on the reduced heap.
            heapify(arr, i, 0);
        }
    }
public:
    vector<int> sortArray(vector<int>& nums) {
        heapSort(nums);
        return nums;
    }
};
```

**Solution 6: (Counting Sort, TC: O(n + k), SC: O(n))**
```
Runtime: 87 ms, Beats 58.38%
Memory: 96.48 MB, Beats 48.35%
```
```c++
class Solution {
    void countingSort(vector<int> &arr) {
        // Create the counting hash map.
        unordered_map<int, int> counts;
        // Find the minimum and maximum values in the array.
        int minVal = *min_element(arr.begin(), arr.end());
        int maxVal = *max_element(arr.begin(), arr.end());

        // Update element's count in the hash map.
        for (auto& val : arr) {
            counts[val]++;
        }
        
        int index = 0;
        // Place each element in its correct position in the array.
        for (int val = minVal; val <= maxVal; ++val) {
            // Append all 'val's together if they exist.
            if (counts.find(val) != counts.end()) {
                while (counts[val] > 0) {
                    arr[index] = val;
                    index += 1;
                    counts[val] -= 1;
                }
            }
        }
    }
public:
    vector<int> sortArray(vector<int>& nums) {
        countingSort(nums);
        return nums;
    }
};
```

**Solution 7: (Radix Sort, TC: O(d * (n + k)), SC: O(n + k))**
```
Runtime: 35 ms, Beats 78.87%
Memory: 103.92, MB Beats 46.56%
```
```c++
class Solution {
    // Bucket sort function for each place value digit.
    void bucketSort(vector<int>& arr, int placeValue) {
        vector<vector<int>> buckets(10, vector<int>());
        // Store the respective number based on its digit.
        for (int& val : arr) {
            int digit = abs(val) / placeValue;
            digit = digit % 10;
            buckets[digit].push_back(val);
        }

        // Overwrite 'arr' in sorted order of current place digits.
        int index = 0;
        for (int digit = 0; digit < 10; ++digit) {
            for (int& val : buckets[digit]) {
                arr[index] = val;
                index++;
            }
        }
    }
    
    // Radix sort function.
    void radixSort(vector<int>& arr) {
        // Find the absolute maximum element to find max number of digits.
        int maxElement = arr[0];
        for (int& val : arr) {
            maxElement = max(abs(val), maxElement);
        }
        int maxDigits = 0;
        while (maxElement > 0) {
            maxDigits += 1;
            maxElement /= 10;
        }

        // Radix sort, least significant digit place to most significant.
        int placeValue = 1;
        for (int digit = 0; digit < maxDigits; ++digit) {
            bucketSort(arr, placeValue);
            placeValue *= 10;
        }

        // Seperate out negatives and reverse them. 
        vector<int> negatives, positives;
        for (int& val : arr) {
            if (val < 0) {
                negatives.push_back(val);
            } else {
                positives.push_back(val);
            }
        }
        reverse(negatives.begin(), negatives.end());
        // Final 'arr' will be 'negative' elements, then 'positive' elements.
        merge(negatives.begin(), negatives.end(), positives.begin(), positives.end(), arr.begin());
    }
public:
    vector<int> sortArray(vector<int>& nums) {
        radixSort(nums);
        return nums;
    }
};
```
