280. Wiggle Sort

Given an unsorted array `nums`, reorder it **in-place** such that `nums[0] <= nums[1] >= nums[2] <= nums[3]....`

**Example:**
```
Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
```

# Solution
---
## Approach #1 (Sorting) [Accepted]
The obvious solution is to just sort the array first, then swap elements pair-wise starting from the second element. For example:
```
   [1, 2, 3, 4, 5, 6]
       ↑  ↑  ↑  ↑
       swap  swap

=> [1, 3, 2, 5, 4, 6]
```
```java
public void wiggleSort(int[] nums) {
    Arrays.sort(nums);
    for (int i = 1; i < nums.length - 1; i += 2) {
        swap(nums, i, i + 1);
    }
}

private void swap(int[] nums, int i, int j) {
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}
```

**Complexity analysis**

* Time complexity : $O(n \log n)$. The entire algorithm is dominated by the sorting step, which costs $O(n \log n)$ time to sort $n$ elements.

* Space complexity : $O(1)$. Space depends on the sorting implementation which, usually, costs $O(1)$ auxiliary space if heapsort is used.

## Approach #2 (One-pass Swap) [Accepted]
Intuitively, we should be able to reorder it in one-pass. As we iterate through the array, we compare the current element to its next element and if the order is incorrect, we swap them.
```java
public void wiggleSort(int[] nums) {
    boolean less = true;
    for (int i = 0; i < nums.length - 1; i++) {
        if (less) {
            if (nums[i] > nums[i + 1]) {
                swap(nums, i, i + 1);
            }
        } else {
            if (nums[i] < nums[i + 1]) {
                swap(nums, i, i + 1);
            }
        }
        less = !less;
    }
}
```
We could shorten the code further by compacting the condition to a single line. Also observe the boolean value of less actually depends on whether the index is even or odd.
```
public void wiggleSort(int[] nums) {
    for (int i = 0; i < nums.length - 1; i++) {
        if (((i % 2 == 0) && nums[i] > nums[i + 1])
                || ((i % 2 == 1) && nums[i] < nums[i + 1])) {
            swap(nums, i, i + 1);
        }
    }
}
```
Here is another amazing solution by @StefanPochmann who came up with originally here.
```java
public void wiggleSort(int[] nums) {
    for (int i = 0; i < nums.length - 1; i++) {
        if ((i % 2 == 0) == (nums[i] > nums[i + 1])) {
            swap(nums, i, i + 1);
        }
    }
}
```

**Complexity analysis**

* Time complexity : $O(n)$. In the worst case we swap at most $n \over 2$ times. An example input is `[2,1,3,1,4,1]`.

* Space complexity : $O(1)$.

# Submissions
---
**Solution 1: (One-pass Swap)**
```
Runtime: 100 ms
Memory Usage: 14.5 MB
```
```python
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            if (i % 2 == 0) == (nums[i] > nums[i + 1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]
```

**Solution 2: (Sort)**
```
Runtime: 96 ms
Memory Usage: 14.8 MB
```
```python
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = sorted(nums)
        nums[::2], nums[1::2] = s[:(len(s)+1)//2], s[(len(s)+1)//2:]
```