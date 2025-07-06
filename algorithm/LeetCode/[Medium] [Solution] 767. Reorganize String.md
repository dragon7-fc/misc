767. Reorganize String

Given a string `S`, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

**Example 1:**
```
Input: S = "aab"
Output: "aba"
```

**Example 2:**
```
Input: S = "aaab"
Output: ""
```

**Note:**

* `S` will consist of lowercase letters and have length in range `[1, 500]`.

# Solution
---
## Approach #1: Sort by Count [Accepted]
**Intuition**

If we should make no two `'a'`s adjacent, it is natural to write `"aXaXaXa..."` where `"X"` is some letter. For now, let's assume that the task is possible (ie. the answer is not `""`.)

Let's sort the string `S`, so all of the same kind of letter occur in continuous blocks. Then when writing in the following interleaving pattern, like `S[3], S[0], S[4], S[1], S[5], S[2]`, adjacent letters never touch. (The specific interleaving pattern is that we start writing at index 1 and step by 2; then start from index 0 and step by 2.)

The exception to this rule is if `N` is odd, and then when interleaving like `S[2], S[0], S[3], S[1], S[4]`, we might fail incorrectly if there is a block of the same 3 letters starting at `S[0]` or `S[1]`. To prevent failing erroneously in this case, we need to make sure that the most common letters all occur at the end.

Finally, it is easy to see that if `N` is the length of the string, and the count of some letter is greater than `(N+1) / 2`, the task is impossible.

**Algorithm**

Find the count of each character, and use it to sort the string by count.

If at some point the number of occurrences of some character is greater than `(N + 1) / 2`, the task is impossible.

Otherwise, interleave the characters in the order described above.

```python
class Solution(object):
    def reorganizeString(self, S):
        N = len(S)
        A = []
        for c, x in sorted((S.count(x), x) for x in set(S)):
            if c > (N+1)/2: return ""
            A.extend(c * x)
        ans = [None] * N
        ans[::2], ans[1::2] = A[N/2:], A[:N/2]
        return "".join(ans)
```

**Complexity Analysis**

* Time Complexity: $O(\mathcal{A}(N + \log{\mathcal{A}}))$, where $N$ is the length of $S$, and $\mathcal{A}$ is the size of the alphabet. In Java, our implementation is $O(N + \mathcal{A} \log {\mathcal{A}})$. If $\mathcal{A}$ is fixed, this complexity is $O(N)$.

* Space Complexity: $O(N)$. In Java, our implementation is O(N + \mathcal{A})O(N+A)

## Approach #2: Greedy with Heap [Accepted]
**Intuition**

One consequence of the reasoning in Approach #1, is that a greedy approach that tries to write the most common letter (that isn't the same as the previous letter written) will work.

The reason is that the task is only impossible if the frequency of a letter exceeds `(N+1) / 2`. Writing the most common letter followed by the second most common letter keeps this invariant.

A heap is a natural structure to repeatedly return the current top 2 letters with the largest remaining counts.

**Approach**

We store a heap of `(count, letter)`. [In Python, our implementation stores negative counts.]

We pop the top two elements from the heap (representing different letters with positive remaining count), and then write the most frequent one that isn't the same as the most recent one written. After, we push the correct counts back onto the heap.

Actually, we don't even need to keep track of the most recent one written. If it is possible to organize the string, the letter written second can never be written first in the very next writing.

At the end, we might have one element still on the heap, which must have a count of one. If we do, we'll add that to the answer too.

**Proof of Invariant**

The invariant mentioned in the [Intuition] section seems true when playing with it, but here is a proof. Let $C_i$ be the count of each letter yet to be written, and $N$ be the number of letters left to write. We want to show this procedure maintains the invariant $2 * \max\limits_i(C_i) \leq N+1$.

Say $C'_i$ are the counts after one writing step.

* If $\max(C_i) > \text{3rdmax}(C_i)$, then $\max(C'_i) \leq \max(C_i) - 1$, and so $2\max(C'_i) \leq 2\max(C_i) - 2 \leq N-1$ as desired.

* If $M = \max(C_i) = \text{3rdmax}(C_i)$, then $3M \leq N$. Also, because $M \geq 1$, $N \geq 3$. Then, $2M \leq \frac{2N}{3} \leq N-1$ as desired.

This completes the proof of this invariant.

```python
class Solution(object):
    def reorganizeString(self, S):
        pq = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pq)
        if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
            return ""

        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            #This code turns out to be superfluous, but explains what is happening
            #if not ans or ch1 != ans[-1]:
            #    ans.extend([ch1, ch2])
            #else:
            #    ans.extend([ch2, ch1])
            ans.extend([ch1, ch2])
            if nct1 + 1: heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 + 1: heapq.heappush(pq, (nct2 + 1, ch2))

        return "".join(ans) + (pq[0][1] if pq else '')
```

**Complexity Analysis**

* Time Complexity: $O(N \log{\mathcal{A}}))$, where $N$ is the length of $S$, and $\mathcal{A}$ is the size of the alphabet. If $\mathcal{A}$ is fixed, this complexity is $O(N)$.

* Space Complexity: $O(\mathcal{A})$. If $\mathcal{A}$ is fixed, this complexity is $O(1)$.

# Submissions
---
**Solution: (Greedy with Heap)**
```
Runtime: 24 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def reorganizeString(self, S: str) -> str:
        pq = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pq)
        if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
            return ""

        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            ans.extend([ch1, ch2])
            if nct1 + 1: heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 + 1: heapq.heappush(pq, (nct2 + 1, ch2))

        return "".join(ans) + (pq[0][1] if pq else '')
```

**Solution 1: (Greedy)**
```
Runtime: 4 ms
Memory Usage: 5.5 MB
```
```c
char find_max(int hist[26] , char c){
    int max = 0;
    char out = '\0' ;
    for(int i=0 ; i < 26 ; i++){
        if(i+'a' != c && hist[i] > max){
            max = hist[i];
            out = i + 'a';
        }
    }
    return out;
}

char * reorganizeString(char * s){
    int hist[26] = {0};
    if(strlen(s) == 0)
        return s;
    for(int i=0 ; i < strlen(s) ; i++){
        hist[s[i] - 'a']++;
    }
    char biggest = find_max(hist , '\0');
    char last;
    int index = 0;
    char* out = (char*)malloc(sizeof(char)*(strlen(s)+1));
    while(biggest != '\0'){
        out[index++] = biggest;
        last = biggest;
        hist[last - 'a']--;
        biggest = find_max(hist,last);
    }
    if(index != strlen(s)){
        free(out);
        return "";
    }
    out[index] = '\0';
	strcpy(s, out);
	free(out);
    return s;
}
```

**Solution 2: (Heap, push prev)**
```
Runtime: 6 ms
Memory Usage: 6.3 MB
```
```c++
class Solution {
public:
    string reorganizeString(string s) {
        int count[26]={0};
        // freq array
        for(auto i: s) count[i-'a']++;
        
        priority_queue<pair<int,char>>pq;
        // storing max freq char first 
        for(int i=0;i<26;i++){
           if(count[i]) pq.push({count[i],i+'a'});
        }
        // storing values alternatively
        string str;
        pair<int,char> prev({-1,' '});
        while(!pq.empty()){
            pair<int,char> p=pq.top();
            pq.pop();
            str+=p.second;
            p.first--;
            if(prev.first>0) pq.push(prev);
            prev=p;
        }
        // if size of both string r equal means we get our ans
        return (str.size()==s.size())?str:"";                                                
    }
};
```

**Solution 3: (Heap)**
```
Runtime: 3 ms
Memory: 6.4 MB
```
```c++
class Solution {
public:
    string reorganizeString(string s) {
        int n = s.size();
        unordered_map<char, int> freq;
        for (char c: s) {
            freq[c] += 1;
        }
        priority_queue<pair<int, char>> q;
        for (auto [c, f]: freq) {
            if (f > (n+1)/2) {
                return "";
            }
            q.push({f, c});
        }
        string ans;
        while (q.size() >= 2) {
            auto [f1, c1] = q.top();
            q.pop();
            auto [f2, c2] = q.top();
            q.pop();
            ans += c1;
            ans += c2;
            if (f1 > 1) {
                q.push({f1-1, c1});
            }
            if (f2 > 1) {
                q.push({f2-1, c2});
            }
        }
        if (!q.empty()) {
            ans += q.top().second;
        }
        return ans;
    }
};
```

**Solution 4: (Heap)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 8.39 MB, Beats 70.55%
```
```c++
class Solution {
public:
    string reorganizeString(string s) {
        unordered_map<char,int> cnt;
        priority_queue<pair<int,char>> pq;
        string ans;
        for (auto c: s) {
            cnt[c] += 1;
        }
        for (auto [c, k]: cnt) {
            pq.push({k, c});
        }
        while (pq.size() >= 2) {
            auto [k1, c1] = pq.top();
            pq.pop();
            auto [k2, c2] = pq.top();
            pq.pop();
            ans += c1;
            ans += c2;
            if (k1 > 1) {
                pq.push({k1-1, c1});
            }
            if (k2 > 1) {
                pq.push({k2-1, c2});
            }
        }
        if (pq.size()) {
            auto [k, c] = pq.top();
            if (k > 1) {
                return "";
            }
            ans += c;
        }
        return ans;
    }
};
```
