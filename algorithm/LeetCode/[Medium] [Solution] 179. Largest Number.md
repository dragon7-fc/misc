179. Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

**Example 1:**
```
Input: [10,2]
Output: "210"
```

**Example 2:**
```
Input: [3,30,34,5,9]
Output: "9534330"
```

**Note:** The result may be very large, so you need to return a string instead of an integer.

# Solution
---
## Approach #1 Sorting via Custom Comparator [Accepted]
**Intuition**

To construct the largest number, we want to ensure that the most significant digits are occupied by the largest digits.

**Algorithm**

First, we convert each integer to a string. Then, we sort the array of strings.

While it might be tempting to simply sort the numbers in descending order, this causes problems for sets of numbers with the same leading digit. For example, sorting the problem example in descending order would produce the number $9534303$, while the correct answer can be achieved by transposing the $3$ and the $30$. Therefore, for each pairwise comparison during the sort, we compare the numbers achieved by concatenating the pair in both orders. We can prove that this sorts into the proper order as follows:

Assume that (without loss of generality), for some pair of integers $a$ and $b$, our comparator dictates that $a$ should precede $b$ in sorted order. This means that $a\frown b > b\frown a$ (where $\frown$ represents concatenation). For the sort to produce an incorrect ordering, there must be some $c$ for which $b$ precedes $c$ and $c$ precedes $a$. This is a contradiction because $a\frown b > b\frown a$ and $b\frown c > c\frown b$ implies $a\frown c > c\frown a$. In other words, our custom comparator preserves transitivity, so the sort is correct.

Once the array is sorted, the most "signficant" number will be at the front. There is a minor edge case that comes up when the array consists of only zeroes, so if the most significant number is $0$, we can simply return $0$. Otherwise, we build a string out of the sorted array and return it.

```python
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
```

**Complexity Analysis**

* Time complexity : $\mathcal{O}(nlgn)$

Although we are doing extra work in our comparator, it is only by a constant factor. Therefore, the overall runtime is dominated by the complexity of sort, which is $\mathcal{O}(nlgn)$ in Python and Java.

* Space complexity : $\mathcal{O}$

Here, we allocate $\mathcal{O}(n)$ additional space to store the copy of nums. Although we could do that work in place (if we decide that it is okay to modify nums), we must allocate $\mathcal{O}(n)$ space for the final return string. Therefore, the overall memory footprint is linear in the length of nums.

# Submissions
---
**Solution 1: (Sorting via Custom Comparator)**
```
Runtime: 32 ms
Memory Usage: 12.8 MB
```
```python
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
```

**Solution 2: (Quick Sort)**
```
Runtime: 16 ms
Memory: 15.65 MB
```
```c++
class Solution {
    void quickSort(vector<int>& nums, int left, int right) {
        // Base case: if the range has one or no elements, it is already sorted
        if (left >= right) return;
        // Partition the array and get the pivot index
        int pivotIndex = partition(nums, left, right);
        // Recursively sort the sub-arrays
        quickSort(nums, left, pivotIndex - 1);
        quickSort(nums, pivotIndex + 1, right);
    }

    int partition(vector<int>& nums, int left, int right) {
        int pivot = nums[right];
        int lowIndex = left;
        // Rearrange elements so that those greater than the pivot are on the
        // left
        for (int i = left; i < right; ++i) {
            if (compare(nums[i], pivot)) {
                swap(nums[i], nums[lowIndex]);
                ++lowIndex;
            }
        }
        // Place the pivot in its correct position
        swap(nums[lowIndex], nums[right]);
        return lowIndex;
    }

    bool compare(int firstNum, int secondNum) {
        // Compare concatenated strings to decide the order
        return to_string(firstNum) + to_string(secondNum) >
               to_string(secondNum) + to_string(firstNum);
    }
public:
    string largestNumber(vector<int>& nums) {
        // Sort the numbers using Quick Sort
        quickSort(nums, 0, nums.size() - 1);
        // Concatenate sorted numbers to form the largest number
        string largestNum;
        for (int num : nums) {
            largestNum += to_string(num);
        }
        // Handle the case where the largest number is zero
        return largestNum[0] == '0' ? "0" : largestNum;
    }
};
```

**Solution 3: (Merge Sort)**
```
Runtime: 3 ms
Memory: 19.97 MB
```
```c++
class Solution {
    vector<int> mergeSort(vector<int>& nums, int left, int right) {
        // Base case: a single element is already sorted
        if (left >= right) return {nums[left]};
        int mid = left + (right - left) / 2;
        // Recursively sort the left and right halves
        vector<int> leftHalf = mergeSort(nums, left, mid);
        vector<int> rightHalf = mergeSort(nums, mid + 1, right);
        // Merge the sorted halves
        return merge(leftHalf, rightHalf);
    }

    vector<int> merge(vector<int>& leftHalf, vector<int>& rightHalf) {
        vector<int> sortedNums;
        int leftIndex = 0, rightIndex = 0;
        // Merge the two halves based on custom comparison
        while (leftIndex < leftHalf.size() && rightIndex < rightHalf.size()) {
            if (compare(leftHalf[leftIndex], rightHalf[rightIndex])) {
                sortedNums.push_back(leftHalf[leftIndex++]);
            } else {
                sortedNums.push_back(rightHalf[rightIndex++]);
            }
        }
        // Append remaining elements from left half
        while (leftIndex < leftHalf.size())
            sortedNums.push_back(leftHalf[leftIndex++]);
        // Append remaining elements from right half
        while (rightIndex < rightHalf.size())
            sortedNums.push_back(rightHalf[rightIndex++]);
        return sortedNums;
    }

    bool compare(int firstNum, int secondNum) {
        // Compare concatenated strings to decide the order
        return to_string(firstNum) + to_string(secondNum) >
               to_string(secondNum) + to_string(firstNum);
    }
public:
    string largestNumber(vector<int>& nums) {
        // Sort the numbers using Merge Sort
        nums = mergeSort(nums, 0, nums.size() - 1);
        // Concatenate sorted numbers to form the largest number
        string largestNum;
        for (int num : nums) {
            largestNum += to_string(num);
        }
        // Handle the case where the largest number is zero
        return largestNum[0] == '0' ? "0" : largestNum;
    }
};
```

**Solution 4: (HeapSort)**
```
Runtime: 8 ms
Memory: 17.48 MB
```
```c++
class Solution {
    // Private helper function to compare two strings
    static bool compare(const string& first, const string& second) {
        return (first + second) < (second + first);
    }
public:
    string largestNumber(vector<int>& nums) {
        // Priority queue to order numbers using the custom comparison
        // function
        priority_queue<string, vector<string>, decltype(&Solution::compare)>
            maxHeap(&Solution::compare);

        int totalLength = 0;

        // Convert integers to strings and push them into the priority queue
        for (const int num : nums) {
            string strNum = to_string(num);
            totalLength += strNum.size();
            maxHeap.push(strNum);
        }

        // Build the result string from the priority queue
        string result;
        result.reserve(totalLength);  // Reserve space for efficiency
        while (!maxHeap.empty()) {
            result += maxHeap.top();
            maxHeap.pop();
        }

        // Handle edge case where the result might be "000...0"
        if (result.empty() || result[0] == '0') {
            return "0";
        }

        return result;
    }
};
```

**Solution 5: (TimSort)**
```
Runtime: 12 ms
Memory: 15.69 MB
```
```c++
class Solution {
    const int RUN = 32;

    void insertionSort(vector<int>& nums, int left, int right) {
        for (int i = left + 1; i <= right; ++i) {
            int temp = nums[i];
            int j = i - 1;
            while (j >= left && compare(temp, nums[j])) {
                nums[j + 1] = nums[j];
                --j;
            }
            nums[j + 1] = temp;
        }
    }

    void merge(vector<int>& nums, int left, int mid, int right) {
        vector<int> leftArr(nums.begin() + left, nums.begin() + mid + 1);
        vector<int> rightArr(nums.begin() + mid + 1, nums.begin() + right + 1);

        int i = 0, j = 0, k = left;
        while (i < leftArr.size() && j < rightArr.size()) {
            if (compare(leftArr[i], rightArr[j])) {
                nums[k++] = leftArr[i++];
            } else {
                nums[k++] = rightArr[j++];
            }
        }
        while (i < leftArr.size()) nums[k++] = leftArr[i++];
        while (j < rightArr.size()) nums[k++] = rightArr[j++];
    }

    void timSort(vector<int>& nums) {
        int n = nums.size();
        // Sort small runs with insertion sort
        for (int i = 0; i < n; i += RUN) {
            insertionSort(nums, i, min(i + RUN - 1, n - 1));
        }
        // Merge sorted runs
        for (int size = RUN; size < n; size = 2 * size) {
            for (int left = 0; left < n; left += 2 * size) {
                int mid = left + size - 1;
                int right = min(left + 2 * size - 1, n - 1);
                if (mid < right) {
                    merge(nums, left, mid, right);
                }
            }
        }
    }

    bool compare(int firstNum, int secondNum) {
        return to_string(firstNum) + to_string(secondNum) >
               to_string(secondNum) + to_string(firstNum);
    }
public:
    string largestNumber(vector<int>& nums) {
         // Sort the numbers using Tim Sort
        timSort(nums);
        // Concatenate sorted numbers to form the largest number
        string largestNum;
        for (int num : nums) {
            largestNum += to_string(num);
        }
        // Handle the case where the largest number is zero
        return largestNum[0] == '0' ? "0" : largestNum;
    }
};
```

**Solution 7: (String)**
```
Runtime: 12 ms
Memory Usage: 11.2 MB
```
```c++
class Solution {
public:
    string largestNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end(), [](int a, int b){
            string s1 = to_string(a), s2 = to_string(b);
            return s1+s2 > s2+s1;
        });
        string ans;
        for (auto num: nums) {
            ans += to_string(num);
        }
        return ans[0] == '0' ? "0" : ans;
    }
};
```
