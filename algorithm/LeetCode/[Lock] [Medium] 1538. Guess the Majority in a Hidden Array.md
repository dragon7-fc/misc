1538. Guess the Majority in a Hidden Array

We have an integer array `nums`, where all the integers in `nums` are **0** or **1**. You will not be given direct access to the array, instead, you will have an **API** `ArrayReader` which have the following functions:

* `int query(int a, int b, int c, int d)`: where `0 <= a < b < c < d < ArrayReader.length()`. The function returns the distribution of the value of the 4 elements and returns:
    * **4** : if the values of the 4 elements are the same (0 or 1).
    * **2** : if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
    * **0** : if two element have a value equal to 0 and two elements have a value equal to 1.
* `int length():` Returns the size of the array.

You are allowed to call `query()` **2 * n times** at most where `n` is equal to `ArrayReader.length()`.

Return **any** index of the most frequent value in `nums`, in case of tie, return `-1`.

 

**Example 1:**
```
Input: nums = [0,0,1,0,1,1,1,1]
Output: 5
Explanation: The following calls to the API
reader.length() // returns 8 because there are 8 elements in the hidden array.
reader.query(0,1,2,3) // returns 2 this is a query that compares the elements nums[0], nums[1], nums[2], nums[3]
// Three elements have a value equal to 0 and one element has value equal to 1 or viceversa.
reader.query(4,5,6,7) // returns 4 because nums[4], nums[5], nums[6], nums[7] have the same value.
we can infer that the most frequent value is found in the last 4 elements.
Index 2, 4, 6, 7 is also a correct answer.
```

**Example 2:**
```
Input: nums = [0,0,1,1,0]
Output: 0
```

**Example 3:**
```
Input: nums = [1,0,1,0,1,0,1,0]
Output: -1
```

**Constraints:**

* `5 <= nums.length <= 10^5`
* `0 <= nums[i] <= 1`

**Follow up**: What is the minimum number of calls needed to find the majority element?

# Submissions
---
**Solution 1; (Math)**
```
Runtime: 157 ms
Memory Usage: 16.5 MB
```
```python
# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares 4 different elements in the array
#	 # return 4 if the values of the 4 elements are the same (0 or 1).
#	 # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
#	 # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
#    def query(self, a: int, b: int, c: int, d: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        #positions in arr doesn't matter
        n = reader.length()

        A = reader.query(0, 1, 2, 3)
        B = reader.query(0, 1, 2, 4)
        C = reader.query(0, 1, 3, 4)
        D = reader.query(0, 2, 3, 4)
        a, b = None, None
        #dirichlet principle
        if A == B:
            a, b = 3, 4
        elif A == C:
            a, b = 2, 4
        elif A == D:
            a, b = 1, 4
        elif B == C:
            a, b = 2, 3
        elif B == D:
            a, b = 1, 3
        elif C == D:
            a, b = 1, 2
        # print(a, b)
        set0 = [a, b]
        set1 = []
        i = 0
        while i < n:
            #(i, j) are next elements
            while i < n and (i == a or i == b):
                i += 1
            j = i + 1
            while j < n and (j == a or j == b):
                j += 1
            if j >= n:
                break
            # print(i, j)
            q = reader.query(*sorted([a, b, i, j]))
            if q == 4: #i, j are in the same set
                set0.append(i)
                set0.append(j)
            elif q == 0: #they are in different set
                set1.append(i)
                set1.append(j)
            else: #pass, one will be added into set0, another into set1
                pass
            i = j + 1
        if i < n and abs(len(set0) - len(set1)) <= 1: #one element left, only matter if difference of two sets is at most 1
            q = reader.query(*sorted([a, b, set1[0], i]))
            if q == 0: #i belongs to set1
                set1.append(i)
            else:
                set0.append(i)
                
        return set0[0] if len(set0) > len(set1) else set1[0] if len(set1) > len(set0) else -1
```
