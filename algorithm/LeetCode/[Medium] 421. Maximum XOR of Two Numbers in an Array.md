421. Maximum XOR of Two Numbers in an Array

Given a non-empty array of numbers, `a0, a1, a2, … , an-1`, where `0 ≤ ai < 231`.

Find the maximum result of `ai XOR aj`, where `0 ≤ i, j < n`.

Could you do this in O(n) runtime?

**Example:**
```
Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
```

# Submissions
---
**Solution 1: (Bit Manipulation, Trie)**

The goal is to find 2 numbers in num that will produce the largest XOR, e.g. a number that has the most 1's to the left in its binary representation. We can do this by first building a trie that represents the binary form of the numbers in nums, then, for each num in nums, traverse the trie to find the number that will produce the largest XOR with it.

```
Runtime: 404 ms
Memory Usage: 105.1 MB
```
```python
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        # need to know the largest binary representation
        # bin prepends '0b', ignore
        L = len(bin(max(nums))) - 2

        # preprocess step - left-pad zeros to ensure each number has L bits
        # (x >> i) & 1 produces the bit at position i for number x
        # x's value is moved right by i bits, we & 1 to produce 0 or 1
        # e.g., if L = 5, then 3 = [0, 0, 0, 1, 1], so the steps to get there are:
        # (3 >> 4) & 1 = 0
        # (3 >> 3) & 1 = 0
        # (3 >> 2) & 1 = 0
        # (3 >> 1) & 1 = 1
        # (3 >> 0) & 1 = 1
        nums_bits = [[(x >> i) & 1 for i in reversed(range(L))] for x in nums]
        root = {}
        # build the trie
        for num, bits in zip(nums, nums_bits):
            node = root
            for bit in bits:
                node = node.setdefault(bit, {})
            node["#"] = num

        max_xor = 0
        for num, bits in zip(nums, nums_bits):
            node = root
            # we want to find the node that will produce the largest XOR with num
            for bit in bits:
                # our goal is to find the opposite bit, e.g. bit = 0, we want 1
                # this is our goal because we want as many 1's as possible
                toggled_bit = 1 - bit
                if toggled_bit in node:
                    node = node[toggled_bit]
                else:
                    node = node[bit]
            # we're at a leaf node, now we can do the XOR computation
            max_xor = max(max_xor, node["#"] ^ num)


        return max_xor
```

**Solution 2: (Bitwise Prefixes in HashSet)**
```
Runtime: 1259 ms
Memory Usage: 33.3 MB
```
```python
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # length of max number in a binary representation
        L = len(bin(max(nums))) - 2
        max_xor = 0
        for i in range(L)[::-1]:
            # go to the next bit by the left shift
            max_xor <<= 1
            # set 1 in the smallest bit
            curr_xor = max_xor | 1
            # compute all existing prefixes 
            # of length (L - i) in binary representation
            prefixes = {num >> i for num in nums}
            # Update max_xor, if two of these prefixes could result in curr_xor.
            # Check if p1^p2 == curr_xor, i.e. p1 == curr_xor^p2
            max_xor |= any(curr_xor^p in prefixes for p in prefixes)
                    
        return max_xor
```

**Solution 3: (Bitwise Trie)**
```
Runtime: 3030 ms
Memory Usage: 97.5 MB
```
```python
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Compute length L of max number in a binary representation
        L = len(bin(max(nums))) - 2
        # zero left-padding to ensure L bits for each number
        nums = [[(x >> i) & 1 for i in range(L)][::-1] for x in nums]
        
        max_xor = 0
        trie = {}
        for num in nums:
            node = trie
            xor_node = trie
            curr_xor = 0
            for bit in num:
                # insert new number in trie
                if not bit in node:
                    node[bit] = {}
                node = node[bit]
                
                # to compute max xor of that new number 
                # with all previously inserted
                toggled_bit = 1 - bit
                if toggled_bit in xor_node:
                    curr_xor = (curr_xor << 1) | 1
                    xor_node = xor_node[toggled_bit]
                else:
                    curr_xor = curr_xor << 1
                    xor_node = xor_node[bit]
                    
            max_xor = max(max_xor, curr_xor)

        return max_xor
```

**Solution 4: (Trie)**
```
Runtime: 583 ms
Memory Usage: 65.3 MB
```
```c++
class TrieNode{
private:
    TrieNode* bits[2] = {NULL};   
public:
    bool contains(int key){
        return bits[key]!=NULL;
    }
    TrieNode* get(int key){
        return bits[key];
    }
    void put(int key){
        bits[key] = new TrieNode;
    }  
};

class Trie{
private:    
    TrieNode* root;   
public:
    Trie(){
        root = new TrieNode;
    }
    void insert(int num){
        auto cur = root;
        for(int i = 31; i >= 0; i--){
            int bit = (num>>i) & 1;
            if(!cur->contains(bit)){
                cur->put(bit);
            }
            cur = cur->get(bit);
        }
    }
    int getMax(int num){
        int maxNum = 0;
        auto node = root;
        for(int i = 31 ; i >= 0; i--){
            int bit = (num>>i) & 1;
            if(node->contains(!bit)){
                maxNum = maxNum | (1<<i);
                node = node->get(!bit);
            }else{
                node = node->get(bit);
            }
        }
        return maxNum;
    }
};

class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        int ans = 0;
        Trie trie;
        for(auto &n : nums) trie.insert(n);
        for(auto &n : nums) ans = max(ans, trie.getMax(n));
        return ans;
    }
};
```
