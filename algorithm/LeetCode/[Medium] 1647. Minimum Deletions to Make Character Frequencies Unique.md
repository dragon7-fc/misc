1647. Minimum Deletions to Make Character Frequencies Unique

A string `s` is called **good** if there are no two different characters in `s` that have the same **frequency**.

Given a string `s`, return the **minimum** number of characters you need to delete to make `s` **good**.

The **frequency** of a character in a string is the number of times it appears in the string. For example, in the string `"aab"`, the frequency of `'a'` is `2`, while the **frequency** of `'b'` is `1`.

 

**Example 1:**
```
Input: s = "aab"
Output: 0
Explanation: s is already good.
```

**Example 2:**
```
Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
```

**Example 3:**
```
Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
```

**Constraints:**

* `1 <= s.length <= 105`
* `s` contains only lowercase English letters.

# Submissions
---
**Solution: (Decrement Each Duplicate Until it is Unique)**
```
Runtime: 85 ms
Memory Usage: 17.5 MB
```
```c++
class Solution {
public:
    int minDeletions(string s) {
        // Store the frequency of each character
        vector<int> frequency(26, 0);
        for (char c : s) {
            frequency[c - 'a']++;
        }
        
        int deleteCount = 0;
        // Use a set to store the frequencies we have already seen
        unordered_set<int> seenFrequencies;
        for (int i = 0; i < 26; i++) {
            // Keep decrementing the frequency until it is unique
            while (frequency[i] && seenFrequencies.find(frequency[i]) != seenFrequencies.end()) {
                frequency[i]--;
                deleteCount++;
            }
            // Add the newly occupied frequency to the set
            seenFrequencies.insert(frequency[i]);
        }
        
        return deleteCount;
    }
};
```

**Solution: (Priority Queue)**
```
Runtime: 112 ms
Memory Usage: 17.4 MB
```
```c++
class Solution {
public:
    int minDeletions(string s) {
        // Store the frequency of each character
        vector<int> frequency(26, 0);
        for (char c : s) {
            frequency[c - 'a']++;
        }
        
        // Add the frequencies to priority queue
        priority_queue<int> pq;
        for (int i = 0; i < 26; i++) {
            if (frequency[i] > 0) {
                pq.push(frequency[i]);
            }
        }
        
        int deleteCount = 0;
        while (pq.size() > 1) {
            int topElement  = pq.top();
            pq.pop();
            
            // If the top two elements in the priority queue are the same
            if (topElement == pq.top()) {
                // Decrement the popped value and push it back into the queue
                if (topElement - 1 > 0) {
                    pq.push(topElement - 1);
                }
                deleteCount++;
            }
        }
        
        return deleteCount;
    }
};
```

**Solution: (Sorting)**
```
Runtime: 91 ms
Memory Usage: 17.1 MB
```
```c++
class Solution {
public:
    int minDeletions(string s) {
        // Store the frequency of each character
        vector<int> frequency(26, 0);
        for (char c : s) {
            frequency[c - 'a']++;
        }
        
        sort(frequency.begin(), frequency.end(), greater<int>());
        
        int deleteCount = 0;
        // Maximum frequency the current character can have
        int maxFreqAllowed = s.size();
        
        // Iterate over the frequencies in descending order
        for (int i = 0; i < 26 && frequency[i] > 0; i++) {
            // Delete characters to make the frequency equal the maximum frequency allowed
            if (frequency[i] > maxFreqAllowed) {
                deleteCount += frequency[i] - maxFreqAllowed;
                frequency[i] = maxFreqAllowed;
            }
            // Update the maximum allowed frequency
            maxFreqAllowed = max(0, frequency[i] - 1);
        }
        
        return deleteCount;
    }
};
```

**Solution 1: (Sort, Reverse count)**
```
Runtime: 108 ms
Memory Usage: 14.7 MB
```
```python
class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = collections.Counter(s)
        vals = sorted(cnt.values(), reverse=True)
        s = set()
        ans = 0
        for v in vals:
            while v in s:
                v -= 1
                ans += 1
            if v:
                s.add(v)
        
        return ans
```

**Solution 2: (Counter)**
```
Runtime: 78 ms
Memory: 23.8 MB
```
```c++
class Solution {
public:
    int minDeletions(string s) {
        vector<int> freq(26);
        int max_freq = 0, ans = 0;
        for (int i = 0; i < s.size(); i ++) {
            freq[s[i] - 'a'] += 1;
            max_freq = max(max_freq, freq[s[i] - 'a']);
        }
        unordered_map<int ,int> freq_count;
        for (int i = 0; i < freq.size(); i ++) {
            if (freq[i]) {
                freq_count[freq[i]] += 1;
            }
        }
        for (int i = max_freq; i > 0; i --) {
            if (freq_count[i] > 1) {
                ans += (freq_count[i] -1);
                freq_count[i-1] += (freq_count[i] - 1);
            }
        }
        return ans;
    }
};
```
