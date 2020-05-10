1442. Count Triplets That Can Form Two Arrays of Equal XOR

Given an array of integers `arr`.

We want to select three indices `i`, `j` and `k` where (`0 <= i < j <= k < arr.length`).

Let's define `a` and `b` as follows:

* a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
* b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]

Note that ^ denotes the **bitwise-xor** operation.

Return the number of triplets (`i`, `j` and `k`) Where `a == b`.

 

**Example 1:**
```
Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
```

**Example 2:**
```
Input: arr = [1,1,1,1,1]
Output: 10
```

**Example 3:**
```
Input: arr = [2,3]
Output: 0
```

**Example 4:**
```
Input: arr = [1,3,5,7,9]
Output: 3
Example 5:

Input: arr = [7,11,12,9,5,2,7,17,22]
Output: 8
```

**Constraints:**

* `1 <= arr.length <= 300`
* `1 <= arr[i] <= 10^8`

# Submissions
---
**Solution 1: (Brute Force with XOR)**

Calculate all prefix of bitwise-xor operation.  
prefix[0] = 0  
prefix[i] = A[0]^A[1]^...^A[i - 1]  
So that for each (i, j),  
we can get A[i]^A[i+1]^...^A[j] by prefix[j+1]^prefix[i]  
in O(1) time

* Time O(N^3)
* Space O(N)
* Space O(1) if changing the input

```
Runtime: 7288 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        N = len(arr)
        pre = [0]
        for i in range(N):
            pre += [pre[-1] ^ arr[i]]
        ans = 0
        for i in range(N-1):
            for j in range(i+1, N):
                for k in range(j, N):
                    a = pre[j]^pre[i]
                    b = pre[k+1]^pre[j]
                    if a == b:
                        ans += 1
        return ans
```

**Solution 1: (Prefix XOR)**

* `a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]`
* `b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]`

Assume a == b, thus  
a ^ a = b ^ a, thus  
0 = b ^ a, thus  
arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1] ^ arr[j] ^ arr[j + 1] ^ ... ^ arr[k] = 0  
prefix[k+1] = prefix[i]

We only need to find out how many pair (i, k) of prefix value are equal.  
So we can calculate the prefix array first,  
Then brute force count the pair.  

Because we once we determine the pair (i,k),  
`j` can be any number that i < j <= k,  
so we need to plus `k - i - i` to the result res.

* Time O(N^2)
* Space O(N)
* Space O(1) if changing the input

```
Runtime: 48 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        arr.insert(0, 0)
        n = len(arr)
        for i in range(n - 1):
            arr[i + 1] ^= arr[i]
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] == arr[j]:
                    res += j - i - 1
        return res
```

**Solution 2: (Prefix XOR, O(N))**

The problem now is, given an array,  
find out the sum of index distance with A[i] = A[j].  
Let me know if there is a duplicate problem on LeetCode,  
so I can attach a link to help explain.

Basicly, for the same value in the array,
we need to count the frequncy and the total value at the same time.

* Time O(N)
* Space O(N)
* Space O(1) if changing the input

```
Runtime: 36 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = cur = 0
        count = {0: [1, -1]}
        for k, a in enumerate(arr):
            cur ^= a
            if cur not in count:
                count[cur] = [0, 0]
            n, total = count[cur]
            res += (k - 1) * n - total
            count[cur] = [n + 1, total + k]
        return res
```