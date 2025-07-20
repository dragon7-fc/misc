303. Range Sum Query - Immutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

**Example:**
```
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
```

**Note:**

* You may assume that the array does not change.
* There are many calls to sumRange function.

# Solution
---
## Approach #1 (Brute Force) [Time Limit Exceeded]
Each time sumRange is called, we use a for loop to sum each individual element from index $i$ to $j$.

```java
private int[] data;

public NumArray(int[] nums) {
    data = nums;
}

public int sumRange(int i, int j) {
    int sum = 0;
    for (int k = i; k <= j; k++) {
        sum += data[k];
    }
    return sum;
}
```

**Complexity analysis:**

* Time complexity : $O(n)$ time per query. Each sumRange query takes $O(n)$ time.

* Space complexity : $O(1)$. Note that data is a reference to nums and is not a copy of it.

## Approach #2 (Caching) [Accepted]
Imagine that sumRange is called one thousand times with the exact same arguments. How could we speed that up?

We could trade in extra space for speed. By pre-computing all range sum possibilities and store its results in a hash table, we can speed up the query to constant time.

```java
public NumArray(int[] nums) {
    for (int i = 0; i < nums.length; i++) {
        int sum = 0;
        for (int j = i; j < nums.length; j++) {
            sum += nums[j];
            map.put(Pair.create(i, j), sum);
        }
    }
}

public int sumRange(int i, int j) {
    return map.get(Pair.create(i, j));
}
```

**Complexity analysis**

* Time complexity : $O(1)$ time per query, $O(n^2)$ time pre-computation. The pre-computation done in the constructor takes $O(n^2)$ time. Each sumRange query's time complexity is $O(1)$ as the hash table's look up operation is constant time.

* Space complexity : $O(n^2)$. The extra space required is $O(n^2)$ as there are $n$ candidates for both $i$ and $j$.

## Approach #3 (Caching) [Accepted]
The above approach takes a lot of space, could we optimize it?

Imagine that we pre-compute the cummulative sum from index $0$ to $k$. Could we use this information to derive $Sum(i, j)$?

Let us define $sum[k]$ as the cumulative sum for $nums[0 \cdots k-1]$ (inclusive):

$sum[k] = \left\{ \begin{array}{rl} \sum_{i=0}^{k-1}nums[i] & , k > 0 \\ 0 &, k = 0 \end{array} \right.$
 

Now, we can calculate sumRange as following:

$sumRange(i, j) = sum[j + 1] - sum[i]$

```java
private int[] sum;

public NumArray(int[] nums) {
    sum = new int[nums.length + 1];
    for (int i = 0; i < nums.length; i++) {
        sum[i + 1] = sum[i] + nums[i];
    }
}

public int sumRange(int i, int j) {
    return sum[j + 1] - sum[i];
}
```

Notice in the code above we inserted a dummy 0 as the first element in the sum array. This trick saves us from an extra conditional check in sumRange function.

**Complexity analysis**

* Time complexity : $O(1)$ time per query, $O(n)$ time pre-computation. Since the cumulative sum is cached, each sumRange query can be calculated in $O(1)$ time.

* Space complexity : $O(n)$.

# Submissions
---
**Solution 1: (Caching)**
```
Runtime: 68 ms
Memory Usage: N/A
```
```python
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.sum = [0] * (n+1)
        for i in range(n):
            self.sum[i+1] = self.sum[i] + nums[i]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum[j+1] - self.sum[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
```

**Solution 2: (Prefix Sum)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 23.91 MB, Beats 60.92%
```
```c++
class NumArray {
    vector<int> dp;
public:
    NumArray(vector<int>& nums) {
        int n = nums.size(), i;
        dp.resize(n+1);
        for (i = 0; i < n; i ++) {
            dp[i+1] = dp[i] + nums[i];
        }
    }
    
    int sumRange(int left, int right) {
        return dp[right+1] - dp[left];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */
```
