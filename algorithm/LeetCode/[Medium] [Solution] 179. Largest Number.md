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

**Solution 2: (String)**
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
