164. Maximum Gap

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

**Example 1:**
```
Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
```

**Example 2:**
```
Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
```

**Note:**

* You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
* Try to solve it in linear time/space.

# Solution
---
## Approach 1: Comparison Sorting
**Intuition**

Do what the question says.

**Algorithm**

Sort the entire array. Then iterate over it to find the maximum gap between two successive elements.

```c++
int maximumGap(vector<int>& nums)
{
    if (nums.empty() || nums.size() < 2)            // check if array is empty or small sized
        return 0;

    sort(nums.begin(), nums.end());                 // sort the array

    int maxGap = 0;

    for (int i = 0; i < nums.size() - 1; i++)
        maxGap = max(nums[i + 1] - nums[i], maxGap);

    return maxGap;
}
```

**Complexity Analysis**

* Time complexity: $O(n\log n)$.

Time taken to sort the array is $O(n\log n)$ (average case). Time taken for linear iteration through the array is of $O(n)$ complexity. Hence overall time complexity is $O(n\log n)$.

* Space complexity: No extra space needed, other than the input array (since sorting can usually be done in-place).

## Approach 2: Radix Sort
**Algorithm**

This approach is similar to Approach 1, except we use Radix Sort instead of a traditional comparison sort.

```c++
int maximumGap(vector<int>& nums)
{
    if (nums.empty() || nums.size() < 2)
        return 0;

    int maxVal = *max_element(nums.begin(), nums.end());

    int exp = 1;                                 // 1, 10, 100, 1000 ...
    int radix = 10;                              // base 10 system

    vector<int> aux(nums.size());

    /* LSD Radix Sort */
    while (maxVal / exp > 0) {                   // Go through all digits from LSD to MSD
        vector<int> count(radix, 0);

        for (int i = 0; i < nums.size(); i++)    // Counting sort
            count[(nums[i] / exp) % 10]++;

        for (int i = 1; i < count.size(); i++)   // you could also use partial_sum()
            count[i] += count[i - 1];

        for (int i = nums.size() - 1; i >= 0; i--)
            aux[--count[(nums[i] / exp) % 10]] = nums[i];

        for (int i = 0; i < nums.size(); i++)
            nums[i] = aux[i];

        exp *= 10;
    }

    int maxGap = 0;

    for (int i = 0; i < nums.size() - 1; i++)
        maxGap = max(nums[i + 1] - nums[i], maxGap);

    return maxGap;
}
```

**Complexity Analysis**

* Time complexity: $O(d \cdot (n + k)) \approx O(n)$.

Since a linear iteration over the array (once it is sorted) is of linear (i.e. $O(n)$) complexity, the performance of this approach is limited by the performance of Radix sort.

Radix sort uses Counting sort as a subroutine.

Counting sort runs in $O(n + k)$ time (where kk is the radix or base of the digits comprising the nn elements in the array). If $k \leq O(n)$, Counting sort would run in linear time. In our case, the radix is fixed (i.e. $k = 10$). Hence our Counting sort subroutine runs in $O(n)$ linear time.

Radix sort works by running $d$ passes of the Counting sort subroutine (where the elements are composed of, maximally, dd digits). Hence effective runtime of Radix sort would be $O(d \cdot (n + k))$). However, in our case an element can, maximally, be the maximum 32-bit signed integer 2,147,483,647. Hence $d \leq 10$ is a constant.

Thus Radix sort has a runtime performance complexity of about $O(n)$ for reasonably large input.

* Space complexity: $O(n + k) \approx O(n)$ extra space.

Counting sort requires $O(k)$ extra space. Radix sort requires an auxiliary array of the same size as input array. However given that kk is a small fixed constant, the space required by Counting sort can be ignored for reasonably large input.

## Approach 3: Buckets and The Pigeonhole Principle
**Intuition**

Sorting an entire array can be costly. At worst, it requires comparing each element with every other element. What if we didn't need to compare all pairs of elements? That would be possible if we could somehow divide the elements into representative groups, or rather, buckets. Then we would only need to compare these buckets.

>Digression: The Pigeonhole Principle The Pigeonhole Principle states that if nn items are put into mm containers, with n > mn>m, then at least one container must contain more than one item.

Suppose for each of the $n$ elements in our array, there was a bucket. Then each element would occupy one bucket. Now what if we reduced, the number of buckets? Some buckets would have to accommodate more than one element.

Now let's talk about the gaps between the elements. Let's take the best case, where all elements of the array are sorted and have a uniform gap between them. This means every adjacent pair of elements differ by the same constant value. So for $n$ elements of the array, there are $n-1$ gaps, each of width, say, $t$. It is trivial to deduce that $t = (max - min)/(n-1)$ (where $max$ and $min$ are the minimum and maximum elements of the array). This width is the maximal width/gap between two adjacent elements in the array; precisely the quantity we are looking for!

One can safely argue that this value of $t$, is in fact, the smallest value that $t$ can ever accomplish of any array with the same number of elements (i.e. $n$) and the same range (i.e. $(max - min)$). To test this fact, you can start with a uniform width array (as described above) and try to reduce the gap between any two adjacent elements. If you reduce the gap between $arr[i-1]$ and $arr[i]$ to some value $t - p$, then you will notice that the gap between $arr[i]$ and $arr[i+1]$ would have increased to $t + p$. Hence the maximum attainable gap would have become $t + p$ from $t$. Thus the value of the maximum gap $t$ can only increase.

**Buckets!**

Coming back to our problem, we have already established by application of the Pigeonhole Principle, that if we used buckets instead of individual elements as our base for comparison, the number of comparisons would reduce if we could accommodate more than one element in a single bucket. That does not immediately solve the problem though. What if we had to compare elements within a bucket? We would end up no better.

So the current motivation remains: somehow, if we only had to compare among the buckets, and not the elements within the buckets, we would be good. It would also solve our sorting problem: we would just distribute the elements to the right buckets. Since the buckets can be already ordered, and we only compare among buckets, we wouldn't have to compare all elements to sort them!

But if we only had buckets to compare, we would have to ensure, that the gap between the buckets itself represent the maximal gap in the input array. How do we go about doing that?

We could do that just by setting the buckets to be smaller than $t = (max - min)/(n-1)$ (as described above). Since the gaps (between elements) within the same bucket would only be $\leq t$, we could deduce that the maximal gap would indeed occur **only between two adjacent buckets**.

Hence by setting bucket size $b$ to be $1 < b \leq (max - min)/(n-1)$, we can ensure that at least one of the gaps between adjacent buckets would serve as the **maximal gap**.

**Clarifications**

A few clarifications are in order:

* **Would the buckets be of uniform size?** Yes. Each of them would be of the same size $b$.

* **But, then wouldn't the gap between them be uniform/constant as well?** Yes it would be. The gap between them would be $1$ integer unit wide. That means a two adjacent buckets of size $3$ could hold integers with values, say, $3 - 6$ and $7 - 9$. We avoid overlapping buckets.

* **Then what are you talking about when you say the gap between two adjacent buckets could be the maximal gap?** When we are talking about the size of a bucket, we are talking about its holding capacity. That is the range of values the bucket can represent (or hold). However the actual extent of the bucket are determined by the values of the maximum and minimum element a bucket holds. For example a bucket of size 55 could have a capacity to hold values between $6 - 10$. However, if it only holds the elements $7, 8$ and $9$, then its actual extent is only $(9 - 7) + 1 = 3$ which is not the same as the capacity of the bucket.

* **Then how do you compare adjacent buckets?** We do that by comparing their extents. Thus we compare the minimum element of the next bucket to the maximum element of the current bucket. For example: if we have two buckets of size 55 each, holding elements $[1, 2, 3]$ and $[9, 10]$ respectively, then the gap between the buckets would essentially refer to the value $9 - 3 = 6$ (which is larger than the size of either bucket).

* **But then aren't we comparing elements again?!** We are, yes! But only compare about twice the elements as the number of buckets (i.e. the minimum and maximum elements of each bucket). If you followed the above, you would realize that this amount is certainly less than the actual number of elements in the array, given a suitable bucket size was chosen.

**Algorithm**

* We choose a bucket size bb such that $1 < b \leq (max - min)/(n-1)$. Let's just choose $b = \lfloor (max - min)/(n-1) \rfloor$.

* Thus all the $n$ elements would be divided among $k = \lceil (max - min)/b \rceil$ buckets.

* Hence the $i^{th}$ bucket would hold the range of values: $\bigg [min + (i-1) * b, \space min + i*b \bigg )$ (1-based indexing).

* It is trivial to calculate the index of the bucket to which a particular element belongs. That is given by $\lfloor (num - min)/b \rfloor$ (0-based indexing) where $num$ is the element in question.

* Once all $n$ elements have been distributed, we compare $k-1$ adjacent bucket pairs to find the maximum gap.

```c++
class Bucket {
public:
    bool used = false;
    int minval = numeric_limits<int>::max();        // same as INT_MAX
    int maxval = numeric_limits<int>::min();        // same as INT_MIN
};

int maximumGap(vector<int>& nums)
{
    if (nums.empty() || nums.size() < 2)
        return 0;

    int mini = *min_element(nums.begin(), nums.end()),
        maxi = *max_element(nums.begin(), nums.end());

    int bucketSize = max(1, (maxi - mini) / ((int)nums.size() - 1));        // bucket size or capacity
    int bucketNum = (maxi - mini) / bucketSize + 1;                         // number of buckets
    vector<Bucket> buckets(bucketNum);

    for (auto&& num : nums) {
        int bucketIdx = (num - mini) / bucketSize;                          // locating correct bucket
        buckets[bucketIdx].used = true;
        buckets[bucketIdx].minval = min(num, buckets[bucketIdx].minval);
        buckets[bucketIdx].maxval = max(num, buckets[bucketIdx].maxval);
    }

    int prevBucketMax = mini, maxGap = 0;
    for (auto&& bucket : buckets) {
        if (!bucket.used)
            continue;

        maxGap = max(maxGap, bucket.minval - prevBucketMax);
        prevBucketMax = bucket.maxval;
    }

    return maxGap;
}
```

**Complexity Analysis**

* Time complexity: $O(n + b) \approx O(n)$.

Distributing the elements of the array takes one linear pass (i.e. $O(n)$ complexity). Finding the maximum gap among the buckets takes a linear pass over the bucket storage (i.e. $O(b)$ complexity). Hence overall process takes linear runtime.

* Space complexity: $O(2 \cdot b) \approx O(b)$ extra space.

Each bucket stores a maximum and a minimum element. Hence extra space linear to the number of buckets is required.

# Submissions
---
**Solution 1: (Comparison Sorting)**
```
Runtime: 16 ms
Memory Usage: 8.6 MB
```
```c++
class Solution {
public:
    int maximumGap(vector<int>& nums) {
        if (nums.empty() || nums.size() < 2)            // check if array is empty or small sized
            return 0;

        sort(nums.begin(), nums.end());                 // sort the array

        int maxGap = 0;

        for (int i = 0; i < nums.size() - 1; i++)
            maxGap = max(nums[i + 1] - nums[i], maxGap);

        return maxGap;
    }
};
```

**Solution 2: (Radix Sort)**
```
Runtime: 32 ms
Memory Usage: 9.2 MB
```
```c++
class Solution {
public:
    int maximumGap(vector<int>& nums) {
        if (nums.empty() || nums.size() < 2)
            return 0;

        int maxVal = *max_element(nums.begin(), nums.end());

        int exp = 1;                                 // 1, 10, 100, 1000 ...
        int radix = 10;                              // base 10 system

        vector<int> aux(nums.size());

        /* LSD Radix Sort */
        while (maxVal / exp > 0) {                   // Go through all digits from LSD to MSD
            vector<int> count(radix, 0);

            for (int i = 0; i < nums.size(); i++)    // Counting sort
                count[(nums[i] / exp) % 10]++;

            for (int i = 1; i < count.size(); i++)   // you could also use partial_sum()
                count[i] += count[i - 1];

            for (int i = nums.size() - 1; i >= 0; i--)
                aux[--count[(nums[i] / exp) % 10]] = nums[i];

            for (int i = 0; i < nums.size(); i++)
                nums[i] = aux[i];

            exp *= 10;
        }

        int maxGap = 0;

        for (int i = 0; i < nums.size() - 1; i++)
            maxGap = max(nums[i + 1] - nums[i], maxGap);

        return maxGap;
    }
};
```

**Solution 3: (Buckets and The Pigeonhole Principle)**
```
Runtime: 12 ms
Memory Usage: 9.1 MB
```
```c++
class Bucket {
public:
    bool used = false;
    int minval = numeric_limits<int>::max();        // same as INT_MAX
    int maxval = numeric_limits<int>::min();        // same as INT_MIN
};


class Solution {
public:
    int maximumGap(vector<int>& nums) {
        if (nums.empty() || nums.size() < 2)
            return 0;

        int mini = *min_element(nums.begin(), nums.end()),
            maxi = *max_element(nums.begin(), nums.end());

        int bucketSize = max(1, (maxi - mini) / ((int)nums.size() - 1));        // bucket size or capacity
        int bucketNum = (maxi - mini) / bucketSize + 1;                         // number of buckets
        vector<Bucket> buckets(bucketNum);

        for (auto&& num : nums) {
            int bucketIdx = (num - mini) / bucketSize;                          // locating correct bucket
            buckets[bucketIdx].used = true;
            buckets[bucketIdx].minval = min(num, buckets[bucketIdx].minval);
            buckets[bucketIdx].maxval = max(num, buckets[bucketIdx].maxval);
        }

        int prevBucketMax = mini, maxGap = 0;
        for (auto&& bucket : buckets) {
            if (!bucket.used)
                continue;

            maxGap = max(maxGap, bucket.minval - prevBucketMax);
            prevBucketMax = bucket.maxval;
        }

        return maxGap;
    }
};
```

**Solution 4: (Bucket Sort)**
```
Runtime: 100 ms
Memory Usage: 15.2 MB
```
```python
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        ## RC ##
        ## APPROACH : BUCKET SORT ##
        ## LOGIC ##
        ## 1. lets say we have number from 1 to 10 like, 1,1.1,1.2,2.4,3.5,3.7,4,....10 (not in the same order)
        ## 2. we create n - 1 buckets, why n-1 ? (b1 -> [1-2] b2-> [2-3] b3->[3-4] ...so on 9 buckets)
        ## 3. we can say size of each bucket will be (10 - 1) // 9 i.e 1 ==> (maximum - mimimum) // (length - 1)
        ## 3. Instead of storing all the elements in the buckets, we store minvalue of that bucket and maximum value of that bucket
        ## 4. Maximum Gap can be Case 1: gap between min and max in the bucket itself (or) Case 2: Gap between bucket1 max and bucket2 and so on..
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##
        
        if len(nums) < 2 or min(nums) == max(nums):
            return 0
        minimum, maximum = min(nums), max(nums)
        size = ( maximum - minimum )//(len(nums) - 1) or 1
        buckets = [[None, None] for _ in range((maximum-minimum)//size + 1)]
        for num in nums:
            # getting the bucket number in which it falls into
            bucket = buckets[(num - minimum)//size]
            bucket[0] = num if bucket[0] is None else min(bucket[0], num)
            bucket[1] = num if bucket[1] is None else max(bucket[1], num)
        buckets = [bucket for bucket in buckets if bucket[0] is not None]
        return max(buckets[i][0]-buckets[i-1][1] for i in range(1, len(buckets)))
```