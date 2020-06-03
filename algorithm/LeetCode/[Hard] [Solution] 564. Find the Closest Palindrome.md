564. Find the Closest Palindrome

Given an integer `n`, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

**Example 1:**
```
Input: "123"
Output: "121"
```

**Note:**

1. The input **n** is a positive integer represented by string, whose length will not exceed 18.
1. If there is a tie, return the smaller one as answer.

# Solution
---
## Approach #1 Brute Force[Time Limit Exceeded]

The simplest solution is to consider every possible number smaller than the given number nn, starting by decrementing 1 from the given number and go on in descending order. Similarly, we can consider every possible number greater than nn starting by incrementing 1 from the given number and going in ascending order. We can continue doing so in an alternate manner till we find a number which is a palindrome.

**Java**
```java
public class Solution {
    public String nearestPalindromic(String n) {
        long num = Long.parseLong(n);
        for (long i = 1;; i++) {
            if (isPalindrome(num - i))
                return "" + (num - i);
            if (isPalindrome(num + i))
                return "" + (num + i);
        }
    }
    boolean isPalindrome(long x) {
        long t = x, rev = 0;
        while (t > 0) {
            rev = 10 * rev + t % 10;
            t /= 10;
        }
        return rev == x;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(\sqrt{n})$. Upto $2*\sqrt{n}$ numbers could be generated in the worst case.

* Space complexity : $O(1)$. Constant space is used.

## Approach #2 Using Math[Accepted]
**Algorithm

To understand this method, let's start with a simple illustration. Assume that the number given to us is "abcxy". One way to convert this number into a palindrome is to replicate one half of the string to the other half. If we try replicating the second half to the first half, the new palindrome obtained will be "yxcxy" which lies at an absolute of $\left|10000(a-y) + 1000(b-x)\right|$ from the original number. But, if we replicate the first half to the second half of the string, we obtain "abcba", which lies at an absolute difference of $\left|10(x-b) + (y-a)\right|$. Trying to change $c$ additionaly in either case would incur an additional value of atleast 100 in the absolute difference.

From the above illustration, we can conclude that if replication is used to generate the palindromic number, we should always replicate the first half to the second half. In this implementation, we've stored such a number in $a$ at a difference of $diff1$ from $n$.

But, there exists another case as well, where the digit at the middle index is incremented or decremented. In such cases, it could be profitable to make changes to the central digit only since such changes could lead to a palindrome formation nearer to the original digit. e.g. 10987. Using the above criteria, the palindrome obtained will be 10901 which is at a more difference from 10987 than 11011. A similar situation occurs if a 0 occurs at the middle digit. But, again as discussed previously, we need to consider only the first half digits to obtain the new palindrome. This special effect occurs with 0 or 9 at the middle digit since, only decrementing 0 and incrementing 9 at that digit place can lead to the change in the rest of the digits towards their left. In any other case, the situation boils down to the one discussed in the first paragraph.

Now, whenever we find a 0 near the middle index, in order to consider the palindromes which are lesser than nn, we subtract a 1 from the first half of the number to obtain a new palindromic half e.g. If the given number nn is 20001, we subtract a 1 from 200 creating a number of the form 199xx. To obtain the new palindrome, we replicate the first half to obtain 19991. Taking another example of 10000, (with a 1 at the MSB), we subtract a 1 from 100 creating 099xx as the new number transforming to a 9999 as the new palindrome. This number is stored in bb having a difference of $diff2$ from $n$

Similar treatment needs to be done with a 9 at the middle digit, except that this time we need to consider the numbers larger than the current number. For this, we add a 1 to the first half. e.g. Taking the number 10987, we add a 1 to 109 creating a number of the form 110xx(11011 is the new palindrome). This palindrome is stored in $c$ having a difference of $diff3$ from $n$.

Out of these three palindromes, we can choose the one with a minimum difference from nn. Further, in case of a tie, we need to return the smallest palindrome obtained. For resolving this tie's conflict, we can observe that a tie is possible only if one number is larger than nn and another is lesser than nn. Further, we know that the number bb is obtained by decreasing nn. Thus, in case of conflict between bb and any other number, we need to choose bb. Similarly, cc is obtained by increasing nn. Thus, in case of a tie between cc and any other number, we need to choose the number other than $c$.

**Java**
```java
public class Solution {
    public String mirroring(String s) {
        String x = s.substring(0, (s.length()) / 2);
        return x + (s.length() % 2 == 1 ? s.charAt(s.length() / 2) : "") + new StringBuilder(x).reverse().toString();
    }
    public String nearestPalindromic(String n) {
        if (n.equals("1"))
            return "0";

        String a = mirroring(n);
        long diff1 = Long.MAX_VALUE;
        diff1 = Math.abs(Long.parseLong(n) - Long.parseLong(a));
        if (diff1 == 0)
            diff1 = Long.MAX_VALUE;

        StringBuilder s = new StringBuilder(n);
        int i = (s.length() - 1) / 2;
        while (i >= 0 && s.charAt(i) == '0') {
            s.replace(i, i + 1, "9");
            i--;
        }
        if (i == 0 && s.charAt(i) == '1') {
            s.delete(0, 1);
            int mid = (s.length() - 1) / 2;
            s.replace(mid, mid + 1, "9");
        } else
            s.replace(i, i + 1, "" + (char)(s.charAt(i) - 1));
        String b = mirroring(s.toString());
        long diff2 = Math.abs(Long.parseLong(n) - Long.parseLong(b));


        s = new StringBuilder(n);
        i = (s.length() - 1) / 2;
        while (i >= 0 && s.charAt(i) == '9') {
            s.replace(i, i + 1, "0");
            i--;
        }
        if (i < 0) {
            s.insert(0, "1");
        } else
            s.replace(i, i + 1, "" + (char)(s.charAt(i) + 1));
        String c = mirroring(s.toString());
        long diff3 = Math.abs(Long.parseLong(n) - Long.parseLong(c));

        if (diff2 <= diff1 && diff2 <= diff3)
            return b;
        if (diff1 <= diff3 && diff1 <= diff2)
            return a;
        else
            return c;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(l)$. Scanning, insertion, deletion,, mirroring takes $O(l)$, where $l$ is the length of the string.

* Space complexity : $O(l)$. Temporary variables are used to store the strings.

# Submissions
---
**Solution 1: (String)**

For odd length strings, always omit the first position when flipping.

If after increasing by 1, the prefx has different length, like 9901, increment 1 on prefix(99) will be 100, 100 is 3-digit while 99 is 2-digit, we assign the candidate to be 10**len(n) + 1.

If after decreasing by 1, the prefx has different length, like 1000, increment 1 on prefix(10) will be 9, 10 is 2-digit while 9 is 1-digit, we assign the candidate to be all 9s, int("9" * (len(n) - 1)).

```
Runtime: 28 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if n == '1' or int(n) < 0: return "0"
        if n == '0': return 1
        minimal = float('inf')
        # get prefix, for example, prefix is "12" for "1234", and "123" for "12345".
        l_left = (len(n)+1)//2
        prefix = n[:l_left]
        
        # Option 1: simply flipping prefix
        # if odd number of digit, omit first index
        n1 = int(prefix + prefix[::-1][int(len(n)%2==1):])
        
        # Option 2: decrease prefix by 1 
        n2_prefix = str(int(prefix) - 1)
        if len(n2_prefix) != len(prefix) or n2_prefix == '0':
            n2 = int('9'*(len(n)-1))
        else:
            n2 = int(n2_prefix + n2_prefix[::-1][int(len(n)%2==1):])
        
        # Option3: increase prefix by 1
        n3_prefix = str(int(prefix) + 1)
        if len(n3_prefix) != len(prefix):
            n3 = 10**len(n) + 1
        else:
            n3 = int(n3_prefix + n3_prefix[::-1][int(len(n)%2==1):])
        
        #compare and get smallest
        ans = None
        for cand in [n3, n1, n2]:
            if abs(cand - int(n)) <= minimal and str(cand) != n:
                ans = cand
                minimal = abs(cand - int(n))
                
        return str(ans)
```