372. Super Pow

Your task is to calculate $a^{b}$ mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

**Example 1:**
```
Input: a = 2, b = [3]
Output: 8
```

**Example 2:**
```
Input: a = 2, b = [1,0]
Output: 1024
```

# Submissions
---
**Solution 1:**
```
Runtime: 92 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        ans2step, step2ans = collections.defaultdict(int), collections.defaultdict(int)
        b = int("".join(map(str,b)))
        ans = 1
        for step in range(min(1338, b)):
            ans = ans*a % 1337
            if ans in ans2step:
                loop_length = step - ans2step[ans]
                rest = (b - step - 1) % loop_length
                return step2ans[ans2step[ans]+rest]
            ans2step[ans] = step
            step2ans[step] = ans
        return ans
```

**Solution 2:**

This program is based on Euler's Theorem which states that: a^( phi(n) ) = 1 (mod n), where phi(n) is Euler's Totient Function, provided that a and n are relatively prime (meaning they have no common factors). In our case, n = 1337, which has prime factorization 1337 = 7 x 191. We know that phi(p) = p - 1 when p is prime and also that phi(p x q) = phi(p) x phi(q). Thus it follows that phi(1337) = phi(7 x 191) = phi(7) x phi(191) = 6 x 190 = 1140. Thus, using Euler's Theorem it follows that a^1140 = 1 (mod 1337), provided that a and 1337 have no common factors. Since 1337 only has two factors, 7 and 191, it follows that a^1140 = 1 (mod 1337), provided that a is not divisible by 7 or 191. This makes sense intuitively because one can only find an inverse of a number (mod n), if the number is relatively prime to n. No multiple of 7 or 191 will ever be congruent to 1 mod 1337 because they are factors of 1337. The closest you can get to 1 mod 1337, is getting 0 mod 1337. For this reason, it is very important that we never allow 1 to be the answer in the case when a is divisible by 7 or 9 since that doesn't make sense.

Since a^1140 = 1 (mod 1337), provided that a is not divisible by 7 or 191, it follows that if we write b = 1140q + r (where q is the quotient and r is the remainder after dividing b by 1140), then a^b = a^(1140q + r) = a^(1140q) x a^r = (a^1140)^q x a^r = 1^q x a^r = a^r (mod 1337). Thus if we reduce b (mod 1337) we can find the answer to a^b by instead just doing a^r (i.e. a^(b % 1337)). Furthermore since we want our answer mod 1337, it is wise to reduce a mod 1337 to keep the numbers smaller. Thus, provided that a is not divisible by 7 or 191, it follows by Euler's Theorem that a^b = (a %1337)^(b % 1140) % 1337.

However, we must carefuly reflect on the case when a is divisible by 7 or 191. If it is divisible by both, then obviously a mod 1337 is 0 and our answer is 0. However, if it is divisisble by one of them and if b = 0 mod 1140 (i.e. b is a multiple of 1140), then our problem would reduce to (7n)^0 = 1 (mod 1337) or (191m)^0 = 1 (mod 1337). These are obviously wrong because a multiple of 7 or 191 can never be congruent to 1 mod 1337. They are also an impermissible application of Euler's Theorem because Euler's Theorem requires that a and n be relatively prime. The way around this issue is to be careful to not use r = 0, which will occur when b is divisible by 1140. Using r = 0 will lead to an incorrect result. What we will do in this case is if b mod 1140 = 0, then we will use b = 1140 instead. This will keep the 0 from being in the exponent. However, we do not have to check it with an if statement, we can simply always add 1140 to b mod 1140 for all cases. This will give us the correct result in the cases when a and b are not divisible by 7 or 191 but will also protect us for the case when they are divisible by 7 or 191.

The program then simply converts the list b to a string then a long int. It then reduces b mod 1140 and adds 1140 to that result so we never have to worry about getting a 0 in the exponent. The program finally evaluates (a % 1337)^(1140 + b % 1140) % 1337 which gives us the correct final answer.

```
Runtime: 88 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return (a % 1337)**(1140 + int(''.join(map(str, b))) % 1140) % 1337
```