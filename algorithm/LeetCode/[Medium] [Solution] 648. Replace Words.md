648. Replace Words

In English, we have a concept called `root`, which can be followed by some other words to form another longer word - let's call this word `successor`. For example, the root `an`, followed by `other`, which can form another word `another`.

Now, given a dictionary consisting of many `roots` and a `sentence`. You need to replace all the `successor` in the `sentence` with the `root` forming it. If a `successor` has many roots can form it, replace it with the `root` with the shortest length.

You need to output the `sentence` after the replacement.

**Example 1:**
```
Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
```

**Note:**

1. The input will only have lower-case letters.
1. `1 <= dict words number <= 1000`
1. `1 <= sentence words number <= 1000`
1. `1 <= root length <= 100`
1. `1 <= sentence words length <= 1000`

# Solution
---
## Approach #1: Prefix Hash [Accepted]
**Intuition**

For each word in the sentence, we'll look at successive prefixes and see if we saw them before.

**Algorithm**

Store all the roots in a Set structure. Then for each word, look at successive prefixes of that word. If you find a prefix that is a root, replace the word with that prefix. Otherwise, the prefix will just be the word itself, and we should add that to the final sentence answer.

```python
def replaceWords(self, roots, sentence):
    rootset = set(roots)

    def replace(word):
        for i in xrange(1, len(word)):
            if word[:i] in rootset:
                return word[:i]
        return word

    return " ".join(map(replace, sentence.split()))
```

**Complexity Analysis**

* Time Complexity: $O(\sum w_i^2)$ where $w_i$ is the length of the $i$-th word. We might check every prefix, the $i$-th of which is $O(w_i^2)$ work.

* Space Complexity: $O(N)$ where $N$ is the length of our sentence; the space used by rootset.

## Approach #2: Trie [Accepted]
**Intuition and Algorithm**

Put all the roots in a trie (prefix tree). Then for any query word, we can find the smallest root that was a prefix in linear time.

```python
class Solution(object):
    def replaceWords(self, roots, sentence):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for root in roots:
            reduce(dict.__getitem__, root, trie)[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur: break
                cur = cur[letter]
            return cur.get(END, word)

        return " ".join(map(replace, sentence.split()))
```

**Complexity Analysis**

* Time Complexity: $O(N)$ where $N$ is the length of the `sentence`. Every query of a word is in linear time.

* Space Complexity: $O(N)$, the size of our trie.

# Submissions
---
**Solution 1: (Prefix Hash)**
```
Runtime: 192 ms
Memory Usage: 16.8 MB
```
```python
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        rootset = set(dict)

        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))
```

**Solution 2: (Trie)**
```
Runtime: 84 ms
Memory Usage: 27.6 MB
```
```python
import functools
class Solution:
    def replaceWords(self, roots: List[str], sentence: str) -> str:
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for root in roots:
            functools.reduce(dict.__getitem__, root, trie)[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur: break
                cur = cur[letter]
            return cur.get(END, word)

        return " ".join(map(replace, sentence.split()))
```

**Solution 3: (Trie)**
```
Runtime: 60 ms
Memory Usage: 26.7 MB
```
```python
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trie = {}
        
        def insert(word):
            curr = trie
            for ch in word:
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]
            curr['#'] = word
                
        for word in dict:
            insert(word)
        words = sentence.split(" ")

        def replace(word):
            curr = trie
            for ch in word:
                if '#' in curr:
                    return True, curr['#']
                elif ch not in curr:
                    return False, word
                else:
                    curr = curr[ch]
            return False, word
        
        for index, word in enumerate(words):
            status, newWord = replace(word)
            if status:
                words[index] = newWord
        
        return " ".join(words)
```

**Solution 4: (trie)**
```
Runtime: 70 ms
Memory Usage: 49.6 MB
```
```c++
class Solution {
public:
    struct Node{
        Node* arr[26];
        string str;
        Node(){
            for(int i=0;i<26;i++){
                arr[i]=NULL;
            }
            str="";
                
        }
    };
    void insert(string word,Node* root){
        Node* curr=root;
        for(int i=0;i<word.size();i++){
            if(curr->arr[word[i]-'a']==NULL){
                curr->arr[word[i]-'a']=new Node();
            }
            curr=curr->arr[word[i]-'a'];
        }
        curr->str=word;
    }
    string find(string word,Node* root)
    {
        Node* curr=root;
        for(int i=0;i<word.size();i++){
            if(curr->arr[word[i]-'a']==NULL){
                return word;
            }
            curr=curr->arr[word[i]-'a'];
            if(curr->str!=""){
                return curr->str;
            }
        }
        return word;
    }
    string replaceWords(vector<string>& dictionary, string sentence) {
        Node* root=new Node();
        for(auto it:dictionary){
            insert(it,root);
        }
        string word="",ans="";
        for(int i=0;i<sentence.size();i++){
            if(sentence[i]==' '){
                if(word.size()>0){
                    ans+=find(word,root);word="";
                    ans+=" ";
                }
            }else{
                word+=sentence[i];
            }
        }
        if(word.size()>0){
             ans+=find(word,root);
        }
        return ans;
    }
};
```
