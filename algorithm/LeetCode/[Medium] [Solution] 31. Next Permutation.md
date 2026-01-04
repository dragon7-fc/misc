31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

```
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
```

# Summary
We need to find the next lexicographic permutation of the given list of numbers than the number formed by the given array.

# Solution
---
## Approach 1: Brute Force
**Algorithm**

In this approach, we find out every possible permutation of list formed by the elements of the given array and find out the permutation which is just larger than the given one. But this one will be a very naive approach, since it requires us to find out every possible permutation which will take really long time and the implementation is complex. Thus, this approach is not acceptable at all. Hence, we move on directly to the correct approach.

Complexity Analysis

* Time complexity : $O(n!)$. Total possible permutations is n!n!.
* Space complexity : $O(n)$. Since an array will be used to store the permutations.

## Approach 2: Single Pass Approach
**Algorithm**

First, we observe that for any given sequence that is in descending order, no next larger permutation is possible. For example, no next permutation is possible for the following array:

`[9, 5, 4, 3, 1]`
We need to find the first pair of two successive numbers $a[i]$ and $a[i-1]$, from the right, which satisfy $a[i] > a[i-1]$. Now, no rearrangements to the right of $a[i-1]$ can create a larger permutation since that subarray consists of numbers in descending order. Thus, we need to rearrange the numbers to the right of $a[i-1]$ including itself.

Now, what kind of rearrangement will produce the next larger number? We want to create the permutation just larger than the current one. Therefore, we need to replace the number $a[i-1]$ with the number which is just larger than itself among the numbers lying to its right section, say $a[j]$.

![nums_graph](img/31_nums_graph.png)

We swap the numbers $a[i-1]$ and $a[j]$. We now have the correct number at index $i-1$. But still the current permutation isn't the permutation that we are looking for. We need the smallest permutation that can be formed by using the numbers only to the right of $a[i-1]$. Therefore, we need to place those numbers in ascending order to get their smallest permutation.

But, recall that while scanning the numbers from the right, we simply kept decrementing the index until we found the pair $a[i]$ and $a[i-1]$ where, $a[i] > a[i-1]$. Thus, all numbers to the right of $a[i-1]$ were already sorted in descending order. Furthermore, swapping $a[i-1]$ and $a[j]$ didn't change that order. Therefore, we simply need to reverse the numbers following $a[i-1]$ to get the next smallest lexicographic permutation.

The following animation will make things clearer:

![Next_Permutation](img/31_Next_Permutation.gif)

```java
public class Solution {
    public void nextPermutation(int[] nums) {
        int i = nums.length - 2;
        while (i >= 0 && nums[i + 1] <= nums[i]) {
            i--;
        }
        if (i >= 0) {
            int j = nums.length - 1;
            while (j >= 0 && nums[j] <= nums[i]) {
                j--;
            }
            swap(nums, i, j);
        }
        reverse(nums, i + 1);
    }

    private void reverse(int[] nums, int start) {
        int i = start, j = nums.length - 1;
        while (i < j) {
            swap(nums, i, j);
            i++;
            j--;
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n)$. In worst case, only two scans of the whole array are needed.

* Space complexity : $O(1)$. No extra space is used. In place replacements are done.

# Submissions
---
**Solution 1: (Two Pointers)**
```
Runtime: 44 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # first decreasing element from right
        i = len(nums) - 2
        while (i >= 0 and nums[i+1] <= nums[i]):
            i -= 1

        # nums[j] = element just greater than nums[i]
        if i >= 0:
            j = len(nums)-1
            while (j >= 0 and nums[j] <= nums[i]):
                j -= 1

            # swap nums[i], nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # reverse nums[i+1],...
        nums[i+1:] = nums[i+1:][::-1]
```

**Solution 2: (Two Pointers)**
```
Runtime: 8 ms
Memory Usage: 6.5 MB
```
```c

static inline void __swap(int *a, int v, int m)
{       
    int x = a[m];
    a[m] = a[v];
    a[v] = x;
}

void nextPermutation(int* nums, int numsSize){
    if (numsSize <= 1) {
        return;
    }
    if (numsSize == 2) {
        __swap(nums, 0, 1);
        return;
    }

    // find first number of descending part from the right
    int firstDesc = numsSize;
    for (int j = numsSize - 1, i = j - 1; j >= 0; j--, i--) {
        if (i < 0 || nums[i] < nums[j]) {
            firstDesc = j;
            break;
        }
    }

    // if there is a number before descending part, swap it with just larger
    // number in descending part to get next larger number of permutation
    if (firstDesc > 0) {
        int justHigherNum = firstDesc;
        for (int i = firstDesc; i < numsSize; i++) {
            if (nums[i] > nums[firstDesc - 1]) {
                justHigherNum = i;
            }
        }
        __swap(nums, firstDesc - 1, justHigherNum);
    }

    // no matter we increase number before descending part or not, we need to
    // reverse descending part to get the next permutation
    int start = firstDesc;
    int end   = numsSize - 1;
    while (start < end) {
        __swap(nums, start++, end--);
    }
}
```

**Solution 2: (Two Pointers)**

setp 1: find next valley x from back
8         .
7             . 
6               .
5       .         .
4          [x]
3                   .
2       
1     .               .
      1 5 8 4 7 6 5 3 1
            ^i
                 <-----
step 2: find first y greater thant x from back
8         .
7             . 
6               .
5       .        [y]
4          [x]
3                   . 
2       
1     .               .
      1 5 8 4 7 6 5 3 1
            ^i    ^j
                  <-----
step 3: swap
8         .
7             . 
6               .
5       .  [y]
4                [x]
3                   . 
2       
1     .               .
      1 5 8 5 7 6 4 3 1
            ^i    ^j

step 4: reverse i+1 to end
8         .
7                     .
6                   .
5       .   y      
4                 x
3               .     
2       
1     .       .
      1 5 8 5 1 3 4 6 7
            ^i
              --------->
```
Runtime: 15 ms
Memory Usage: 11.9 MB
```
```c++
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int i = nums.size() - 2;
        while (i >= 0 && nums[i + 1] <= nums[i]) {
            i--;
        }
        if (i >= 0) {
            int j = nums.size() - 1;
            while (nums[j] <= nums[i]) {
                j--;
            }
            swap(nums[i], nums[j]);
        }
        reverse(nums.begin() + i + 1, nums.end());
    }
};
```
