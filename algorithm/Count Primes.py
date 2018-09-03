""" 
Count Primes

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

"""


""" Solution: 232 ms """
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        prime = [True]*n
        prime[0] = prime[1] = False
        for i in range(2, int(n**0.5)+1):
            if prime[i]:
                prime[i*i: n: i] = [False] * len(prime[i*i: n: i])
        return sum(prime)