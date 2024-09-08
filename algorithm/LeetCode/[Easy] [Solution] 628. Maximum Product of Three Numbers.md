628. Maximum Product of Three Numbers

Given an integer array, find three numbers whose product is maximum and output the maximum product.

**Example 1:**
```
Input: [1,2,3]
Output: 6
```

**Example 2:**
```
Input: [1,2,3,4]
Output: 24
```

**Note:**

1. The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
1. Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

# Submissions
---
## Approach 1: Brute Force
The simplest solution is to consider every triplet out of the given $nums$ array and check their product and find out the maximum product out of them.

**Complexity Analysis**

* Time complexity : $O(n^3)$. We need to consider every triplet from $nums$ array of length $n$.

* Space complexity : $O(1)$. Constant extra space is used.

## Approach 2: Using Sorting
**Algorithm**

Another solution could be to sort the given $nums$ array(in ascending order) and find out the product of the last three numbers.

But, we can note that this product will be maximum only if all the numbers in $nums$ array are positive. But, in the given problem statement, negative elements could exist as well.

Thus, it could also be possible that two negative numbers lying at the left extreme end could also contribute to lead to a larger product if the third number in the triplet being considered is the largest positive number in the $nums$ array.

Thus, either the product $nums[0] \times nums[1] \times nums[n-1]$ or $nums[n-3] \times nums[n-2] \times nums[n-1]$ will give the required result. Thus, we need to find the larger one from out of these values.

```java
public class Solution {
    public int maximumProduct(int[] nums) {
        Arrays.sort(nums);
        return Math.max(nums[0] * nums[1] * nums[nums.length - 1], nums[nums.length - 1] * nums[nums.length - 2] * nums[nums.length - 3]);
    }
}
```

**Complexity Analysis**

* Time complexity : $O\big(n\log n\big)$. Sorting the $nums$ array takes $n\log n$ time.

* Space complexity : $O(\log n)$. Sorting takes $O(\log n)$ space.

## Approach 3: Single Scan
**Algorithm**

We need not necessarily sort the given $nums$ array to find the maximum product. Instead, we can only find the required 2 smallest values($min1$ and $min2$) and the three largest values($max1, max2, max3$) in the $nums$ array, by iterating over the $nums$ array only once.

At the end, again we can find out the larger value out of $min1 \times min2 \times max1$ and max1 $\times max2 \times max3$ to find the required maximum product.

```java
public class Solution {
    public int maximumProduct(int[] nums) {
        int min1 = Integer.MAX_VALUE, min2 = Integer.MAX_VALUE;
        int max1 = Integer.MIN_VALUE, max2 = Integer.MIN_VALUE, max3 = Integer.MIN_VALUE;
        for (int n: nums) {
            if (n <= min1) {
                min2 = min1;
                min1 = n;
            } else if (n <= min2) {     // n lies between min1 and min2
                min2 = n;
            }
            if (n >= max1) {            // n is greater than max1, max2 and max3
                max3 = max2;
                max2 = max1;
                max1 = n;
            } else if (n >= max2) {     // n lies betweeen max1 and max2
                max3 = max2;
                max2 = n;
            } else if (n >= max3) {     // n lies betwen max2 and max3
                max3 = n;
            }
        }
        return Math.max(min1 * min2 * max1, max1 * max2 * max3);
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n)$. Only one iteration over the $nums$ array of length $n$ is required.

* Space complexity : $O(1)$. Constant extra space is used.

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 316 ms
Memory Usage: 14.8 MB
```
```python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[0] * nums[1] * nums[-1]
        b = nums[-1] * nums[-2] * nums[-3]
        return max(a, b)
```

**Solution 2: (Heap)**
```
Runtime: 296 ms
Memory Usage: 15.2 MB
```
```puython
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        largest = heapq.nlargest(3, nums)
        smallest = heapq.nsmallest(2, nums)

        return max(largest[0] * largest[1] * largest[2], largest[0] * smallest[0] * smallest[1])
```

**Solution 3: (Sort)**
```
Runtime: 36 ms
Memory: 31.42 MB
```
```c++
class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        return max(nums[0]*nums[1]*nums[n-1], nums[n-1]*nums[n-2]*nums[n-3]);
    }
};

```
