1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

**Example:**
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

# Solution
---
# Approach 1: Brute Force
The brute force approach is simple. Loop through each element $x$ and find if there is another value that equals to $target - x$.
```java
public int[] twoSum(int[] nums, int target) {
    for (int i = 0; i < nums.length; i++) {
        for (int j = i + 1; j < nums.length; j++) {
            if (nums[j] == target - nums[i]) {
                return new int[] { i, j };
            }
        }
    }
    throw new IllegalArgumentException("No two sum solution");
}
```

**Complexity Analysis**

* Time complexity : $O(n^2)$. For each element, we try to find its complement by looping through the rest of array which takes $O(n)$ time. Therefore, the time complexity is $O(n^2)$.

* Space complexity : $O(1)$.

## Approach 2: Two-pass Hash Table
To improve our run time complexity, we need a more efficient way to check if the complement exists in the array. If the complement exists, we need to look up its index. What is the best way to maintain a mapping of each element in the array to its index? A hash table.

We reduce the look up time from $O(n)$ to $O(1)$ by trading space for speed. A hash table is built exactly for this purpose, it supports fast look up in near constant time. I say "near" because if a collision occurred, a look up could degenerate to $O(n)$ time. But look up in hash table should be amortized $O(1)$ time as long as the hash function was chosen carefully.

A simple implementation uses two iterations. In the first iteration, we add each element's value and its index to the table. Then, in the second iteration we check if each element's complement $(target - nums[i]$ exists in the table. Beware that the complement must not be $nums[i]$ itself!

```java
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        map.put(nums[i], i);
    }
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement) && map.get(complement) != i) {
            return new int[] { i, map.get(complement) };
        }
    }
    throw new IllegalArgumentException("No two sum solution");
}
```

**Complexity Analysis:**

* Time complexity : $O(n)$. We traverse the list containing $n$ elements exactly twice. Since the hash table reduces the look up time to $O(1)$, the time complexity is O(n)O(n).

* Space complexity : $O(n)$. The extra space required depends on the number of items stored in the hash table, which stores exactly $n$ elements.

## Approach 3: One-pass Hash Table
It turns out we can do it in one-pass. While we iterate and inserting elements into the table, we also look back to check if current element's complement already exists in the table. If it exists, we have found a solution and return immediately.

```java
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement)) {
            return new int[] { map.get(complement), i };
        }
        map.put(nums[i], i);
    }
    throw new IllegalArgumentException("No two sum solution");
}
```

**Complexity Analysis:**

* Time complexity : $O(n)$. We traverse the list containing $n$ elements only once. Each look up in the table costs only $O(1)$ time.

* Space complexity : $O(n)$. The extra space required depends on the number of items stored in the hash table, which stores at most $n$ elements.

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 60 ms
Memory Usage: 15.2 MB
```
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for i in range(len(nums)):
            if target-nums[i] in sum_dict:
                return [i, sum_dict[target-nums[i]]]
            else:
                sum_dict[nums[i]] = i
```

**Solution 2: (Hash Table)**
```
Runtime: 4 ms
Memory Usage: 8.9 MB
```
```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> m;
        for(int i = 0; i <nums.size(); i++)
        {
            if(m.find(target - nums[i]) != m.end())
                return {m[target - nums[i]],i};
        else
            m[nums[i]] = i;
        }
        return {0,0};
    }
};
```

**Solution 3: (Hash Table)**
```
Runtime: 8 ms
Memory Usage: 8.1 MB
```
```c
typedef struct {
	int num;
	int idx;
	// Makes structure hashable
	UT_hash_handle hh;
} num_t;

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int* res = calloc((*returnSize = 2), sizeof(int));
	num_t *numsHash = NULL, *num = NULL, *tmp = NULL;

	for(int i = 0; i < numsSize; ++i){
		int toFind = target - nums[i];
		HASH_FIND_INT(numsHash, &toFind, num);

		if (num != NULL){
			res[0] = num->idx;
			res[1] = i;

			break;
		} else {
			num = malloc(sizeof(num_t));
			num->num = nums[i]; num->idx = i;

			HASH_ADD_INT(numsHash, num, num);
		}
	}

	HASH_ITER(hh, numsHash, num, tmp) {
		HASH_DEL(numsHash, num); free(num); 
	}

	return res;
}
```

**Solution 4: (Hash Table)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 14.90 MB, Beats 21.63%
```
```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size(), i;
        unordered_map<int,int> m;
        for (i = 0; i < n; i ++) {
            if (m.count(target - nums[i])) {
                return {m[target - nums[i]], i};
            }
            m[nums[i]] = i;
        }
        return {-1, -1};
    }
};
```
