645. Set Mismatch

The set `S` originally contains numbers from `1` to `n`. But unfortunately, due to the data error, one of the numbers in the set got duplicated to **another** number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

**Example 1:**
```
Input: nums = [1,2,2,4]
Output: [2,3]
```

**Note:**

* The given array size will in the range `[2, 10000]`.
* The given array's numbers won't have any order.

# Solution
---
## Approach 1: Brute Force
The most naive solution is to consider each number from $1$ to $n$, and traverse over the whole $nums$ array to check if the current number occurs twice in $nums$ or doesn't occur at all. We need to set the duplicate number, $dup$ and the missing number, $missing$, appropriately in such cases respectively.

```java
public class Solution {
    public int[] findErrorNums(int[] nums) {
        int dup = -1, missing = -1;
        for (int i = 1; i <= nums.length; i++) {
            int count = 0;
            for (int j = 0; j < nums.length; j++) {
                if (nums[j] == i)
                    count++;
            }
            if (count == 2)
                dup = i;
            else if (count == 0)
                missing = i;
        }
        return new int[] {dup, missing};
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n^2)$. We traverse over the $nums$ array of size $n$ for each of the numbers from $1$ to $n$.

* Space complexity : $O(1)$. Constant extra space is used.

## Approach 2: Better Brute Force
In the last approach, we continued the search process, even when we've already found the duplicate and the missing number. But, as per the problem statement, we know that only one number will be repeated and only one number will be missing. Thus, we can optimize the last approach to some extent, by stopping the search process as soon as we find these two required numbers.

```java
public class Solution {
    public int[] findErrorNums(int[] nums) {
        int dup = -1, missing = -1;;
        for (int i = 1; i <= nums.length; i++) {
            int count = 0;
            for (int j = 0; j < nums.length; j++) {
                if (nums[j] == i)
                    count++;
            }
            if (count == 2)
                dup = i;
            else if (count == 0)
                missing = i;
            if (dup > 0 && missing > 0)
                break;
        }
        return new int[] {dup, missing};
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n^2)$. We traverse over the $nums$ array of size $n$ for each of the numbers from $1$ to $n$, in the worst case.

* Space complexity : $O(1)$. Constant extra space is used.

## Approach 3: Using Sorting
**Algorithm**

One way to further optimize the last approach is to sort the given $nums$ array. This way, the numbers which are equal will always lie together. Further, we can easily identify the missing number by checking if every two consecutive elements in the sorted $nums$ array are just one count apart or not.

```java
public class Solution {
    public int[] findErrorNums(int[] nums) {
        Arrays.sort(nums);
        int dup = -1, missing = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1])
                dup = nums[i];
            else if (nums[i] > nums[i - 1] + 1)
                missing = nums[i - 1] + 1;
        }
        return new int[] {dup, nums[nums.length - 1] != nums.length ? nums.length : missing};
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n\log n)$. Sorting takes $O(n\log n)$ time.

* Space complexity : $O(\log n)$. Sorting takes $O(\log n)$ space.

## Approach 4: Using Map
**Algorithm**

The given problem can also be solved easily if we can somehow keep a track of the number of times each element of the $nums$ array occurs. One way to do so is to make an entry for each element of $nums$ in a HashMap $map$. This $map$ stores the entries in the form $(num_i, count_i)$. Here, $num$ refers to the $i^{th}$ element in $nums$ and $count_i$ refers to the number of times this element occurs in $nums$. Whenever, the same element occurs again, we can increment the count corresponding to the same.

After this, we can consider every number from $1$ to $n$, and check for its presence in mapmap. If it isn't present, we can update the $missing$ variable appropriately. But, if the $count$ corresponding to the current number is $2$, we can update the $dup$ variable with the current number.

```java
public class Solution {
    public int[] findErrorNums(int[] nums) {
        Map < Integer, Integer > map = new HashMap();
        int dup = -1, missing = 1;
        for (int n: nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        for (int i = 1; i <= nums.length; i++) {
            if (map.containsKey(i)) {
                if (map.get(i) == 2)
                    dup = i;
            } else
                missing = i;
        }
        return new int[]{dup, missing};
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n)$. Traversing over $nums$ of size $n$ takes $O(n)$ time. Considering each number from $1$ to $n$ also takes $O(n)$ time.

* Space complexity : $O(n)$. $map$ can contain atmost $n$ entries for each of the numbers from $1$ to $n$.

## Approach 5: Using Extra Array
**Algorithm**

In the last approach, we make use of a $map$ to store the elements of $nums$ along with their corresponding counts. But, we can note, that each entry in $map$ requires two entries. Thus, putting up $n$ entries requires $2n$ space actually. We can reduce this space required to $n$ by making use of an array, $arr$ instead. Now, the indices of $arr$ can be used instead of storing the elements again. Thus, we make use of $arr$ in such a way that, $arr[i]$ is used to store the number of occurences of the element $i+1$. The rest of the process remains the same as in the last approach.

```java
public class Solution {
    public int[] findErrorNums(int[] nums) {
        int[] arr = new int[nums.length + 1];
        int dup = -1, missing = 1;
        for (int i = 0; i < nums.length; i++) {
            arr[nums[i]] += 1;
        }
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] == 0)
                missing = i;
            else if (arr[i] == 2)
                dup = i;
        }
        return new int[]{dup, missing};
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n)$. Traversing over $nums$ of size $n$ takes $O(n)$ time. Considering each number from $1$ to $n$ also takes $O(n)$ time.

* Space complexity : $O(n)$. $arr$ can contain atmost $n$ elements for each of the numbers from $1$ to $n$.

## Approach 6: Using Constant Space
**Algorithm**

We can save the space used in the last approach, if we can somehow, include the information regarding the duplicacy of an element or absence of an element in the $nums$ array. Let's see how this can be done.

We know that all the elements in the given $nums$ array are positive, and lie in the range $1$ to $n$ only. Thus, we can pick up each element $i$ from $nums$. For every number $i$ picked up, we can invert the element at the index $\left|i\right|$. By doing so, if one of the elements $j$ occurs twice, when this number is encountered the second time, the element $nums[\left|i\right|]$ will be found to be negative. Thus, while doing the inversions, we can check if a number found is already negative, to find the duplicate number.

After the inversions have been done, if all the elements in $nums$ are present correctly, the resultant $nums$ array will have all the elements as negative now. But, if one of the numbers, $j$ is missing, the element at the $j^{th}$ index will be positive. This can be used to determine the missing number.

```java
public class Solution {
    public int[] findErrorNums(int[] nums) {
        int dup = -1, missing = 1;
        for (int n: nums) {
            if (nums[Math.abs(n) - 1] < 0)
                dup = Math.abs(n);
            else
                nums[Math.abs(n) - 1] *= -1;
        }
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > 0)
                missing = i + 1;
        }
        return new int[]{dup, missing};
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n)$. Two traversals over the $nums$ array of size $n$ are done.

* Space complexity : $O(1)$. Constant extra space is used.

## Approach 7: Using XOR
**Algorithm**

Before we dive into the solution to this problem, let's consider a simple problem. Consider an array with n-1n−1 elements containing numbers from $1$ to $n$ with one number missing out of them. Now, how to we find out this missing element. One of the solutions is to take the XOR of all the elements of this array with all the numbers from $1$ to $n$. By doing so, we get the required missing number. This works because XORing a number with itself results in a 0 result. Thus, only the number which is missing can't get cancelled with this XORing.

Now, using this idea as the base, let's take it a step forward and use it for the current problem. By taking the XOR of all the elements of the given $nums$ array with all the numbers from $1$ to $n$, we will get a result, xorxor, as $x^y$. Here, $x$ and $y$ refer to the repeated and the missing term in the given $nums$ array. This happens on the same grounds as in the first problem discussed above.

Now, in the resultant $xor$, we'll get a 1 in the binary representation only at those bit positions which have a 1 in one out of the numbers $x$ and $y$, and a 0 at the same bit position in the other one. In the current solution, we consider the rightmost bit which is 1 in the $xor$, although any bit would work. Let's say, this position is called the $rightmostbit$.

If we divide the elements of the given $nums$ array into two parts such that the first set contains the elements which have a 1 at the $rightmostbit$ position and the second set contains the elements having a 0 at the same position, we'll get one out of $x$ or $y$ in one set and the other one in the second set. Now, our problem has reduced somewhat to the simple problem discussed above.

To solve this reduced problem, we can find out the elements from $1$ to $n$ and consider them as a part of the previous sets only, with the allocation of the set depending on a 1 or 0 at the $righmostbit$ position.

Now, if we do the XOR of all the elements of the first set, all the elements will result in an XOR of 0, due to cancellation of the similar terms in both $nums$ and the numbers $(1:n)$, except one term, which is either $x$ or $y$.

For the other term, we can do the XOR of all the elements in the second set as well.

Consider the example `[1 2 4 4 5 6]`

![645_Set_Mismatch.png](img/645_Set_Mismatch.png)

One more traversal over the $nums$ can be used to identify the missing and the repeated number out of the two numbers found.

```java
public class Solution {
    public int[] findErrorNums(int[] nums) {
        int xor = 0, xor0 = 0, xor1 = 0;
        for (int n: nums)
            xor ^= n;
        for (int i = 1; i <= nums.length; i++)
            xor ^= i;
        int rightmostbit = xor & ~(xor - 1);
        for (int n: nums) {
            if ((n & rightmostbit) != 0)
                xor1 ^= n;
            else
                xor0 ^= n;
        }
        for (int i = 1; i <= nums.length; i++) {
            if ((i & rightmostbit) != 0)
                xor1 ^= i;
            else
                xor0 ^= i;
        }
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == xor0)
                return new int[]{xor0, xor1};
        }
        return new int[]{xor1, xor0};
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n)$. We iterate over $n$ elements five times.

* Space complexity : $O(1)$. Constant extra space is used.

# Submisssions
---
**Solution 1: (Using Constant Space)**
```
Runtime: 236 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = -1
        missing = 1
        for num in nums:
            if nums[abs(num) - 1] < 0:
                dup = abs(num);
            else:
                nums[abs(num) - 1] *= -1
        
        for i in range(1, len(nums)):
            if nums[i] > 0:
                missing = i + 1
        return [dup, missing]
```

**Solution 2: (Math)**
```
Runtime: 169 ms
Memory: 29.5 MB
```
```c++
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        int a = accumulate(nums.begin(), nums.end(), 0);
        unordered_set<int> st(nums.begin(), nums.end());
        int b = accumulate(st.begin(), st.end(), 0);
		int s = n*(n+1)/2;
        return {a-b, s-b};
    }
};
```
