820. Short Encoding of Words

Given a list of `words`, we may encode it by writing a reference string `S` and a list of indexes `A`.

For example, if the list of words is `["time", "me", "bell"]`, we can write it as `S = "time#bell#"` and `indexes = [0, 2, 5]`.

Then for each index, we will recover the word by reading from the reference string from that index until we reach a `"#"` character.

What is the length of the shortest reference string S possible that encodes the given words?

**Example:**
```
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].
```

**Note:**

* `1 <= words.length <= 2000`.
* `1 <= words[i].length <= 7`.
* Each word has only lowercase letters.

# Solution
---
## Approach #1: Store Prefixes [Accepted]
**Intuition**

If a word `X` is a suffix of `Y`, then it does not need to be considered, as the encoding of `Y` in the reference string will also encode `X`. For example, if `"me"` and `"time"` is in words, we can throw out `"me"` without changing the answer.

If a word `Y` does not have any other word `X` (in the list of `words`) that is a suffix of `Y`, then `Y` must be part of the reference string.

Thus, the goal is to remove words from the list such that no word is a suffix of another. The final answer would be `sum(word.length + 1 for word in words)`.

**Algorithm**

Since a word only has up to 7 suffixes (as `words[i].length <= 7`), let's iterate over all of them. For each suffix, we'll try to remove it from our `words` list. For efficiency, we'll make `words` a set.

```python
class Solution(object):
    def minimumLengthEncoding(self, words):
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])

        return sum(len(word) + 1 for word in good)
```

**Complexity Analysis**

* Time Complexity: $O(\sum w_i^2)$, where $w_i$ is the length of `words[i]`.

* Space Complexity: $O(\sum w_i)$, the space used in storing suffixes.

## Approach #2: Trie [Accepted]
**Intuition**

As in Approach #1, the goal is to remove words that are suffixes of another word in the list.

**Algorithm**

To find whether different words have the same suffix, let's put them backwards into a trie (prefix tree). For example, if we have `"time"` and `"me"`, we will put `"emit"` and `"em"` into our trie.

After, the leaves of this trie (nodes with no children) represent words that have no suffix, and we will count `sum(word.length + 1 for word in words)`.

```python
class Solution(object):
    def minimumLengthEncoding(self, words):
        words = list(set(words)) #remove duplicates
        #Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)
```

**Complexity Analysis**

* Time Complexity: $O(\sum w_i)$, where $w_i$ is the length of `words[i]`.

* Space Complexity: $O(\sum w_i)$, the space used by the trie.

# Submissions
---
**Solution 1: (Store Prefixes)**
```
Runtime: 140 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])

        return sum(len(word) + 1 for word in good)
```

**Solution 2: (Trie)**
```
Runtime: 272 ms
Memory Usage: 16.3 MB
```
```python
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words)) #remove duplicates
        #Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)
```

**Solution 3: (Trie, Suffix)**
```
Runtime: 124 ms
Memory Usage: 43.6 MB
```
```c++
struct Node{
    map<char,Node*> next;
    bool isleaf;
    Node(){
        next.clear();
        isleaf=false;
    }
};

bool comp(string a,string b){
    return a.length()>b.length();
}

class Solution {
    int ans;
    void insert(Node* root,string s){
        Node* temp=root;
        int i=s.length()-1;
        ans+=s.length()+1;
        for(;i>=0;i--){
            if(temp->next.find(s[i])==temp->next.end())
                temp->next[s[i]]=new Node();
            temp=temp->next[s[i]];
        }
        temp->isleaf=true;
    }
    
    bool check(Node* root,string s){
        int i=s.length()-1;
        Node* temp=root;
        for(;i>=0;i--){
            if(temp->next.find(s[i])==temp->next.end())
                return 0;
            temp=temp->next[s[i]];
        }
        return 1;
    }
    
public:
    int minimumLengthEncoding(vector<string>& words) {
        // sort in decreasing order of length
        sort(words.begin(),words.end(),comp);        
        Node* root=new Node();
        ans=0;
        insert(root,words[0]);
        int i,n=words.size();
		
        for(i=1;i<n;i++){
			// if this string does not occur as suffix of any of the previously inserted strings then insert it
            if(!check(root,words[i]))
                insert(root,words[i]);
        }
        return ans;
    }
};
```

**Solution 4: (sort and find)**
```
Runtime: 556 ms
Memory Usage: 14.5 MB
```
```c++
class Solution {
public:
    int minimumLengthEncoding(vector<string>& words) {
        string ans;
        sort(words.begin(),words.end(),[](string &a,string &b){return a.size() > b.size();});
        for(string &s:words)
            if(ans.find(s + "#") == string::npos) ans += s + "#";
        return ans.size();
    }
};
```
