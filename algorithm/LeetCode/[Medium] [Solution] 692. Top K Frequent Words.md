692. Top K Frequent Words

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

**Example 1:**
```
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
```

**Example 2:**
```
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
```

**Note:**

1. You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
1. Input words contain only lowercase letters.

# Solution
---
## Approach #1: Sorting [Accepted]
**Intuition and Algorithm**

Count the frequency of each word, and sort the words with a custom ordering relation that uses these frequencies. Then take the best `k` of them.

```python
class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key = lambda w: (-count[w], w))
        return candidates[:k]
```

**Complexity Analysis**

* Time Complexity: $O(N \log{N})$, where $N$ is the length of words. We count the frequency of each word in $O(N)$ time, then we sort the given words in $O(N \log{N})$ time.

* Space Complexity: $O(N)$, the space used to store our candidates.

## Approach #2: Heap [Accepted]
**Intuition and Algorithm**

Count the frequency of each word, then add it to heap that stores the best `k` candidates. Here, "best" is defined with our custom ordering relation, which puts the worst candidates at the top of the heap. At the end, we pop off the heap up to `k` times and reverse the result so that the best candidates are first.

In Python, we instead use `heapq.heapify`, which can turn a list into a heap in linear time, simplifying our work.

```python
class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in xrange(k)]
```

**Complexity Analysis**

* Time Complexity: $O(N \log{k})$, where $N$ is the length of words. We count the frequency of each word in $O(N)$ time, then we add $N$ words to the heap, each in $O(\log {k})$ time. Finally, we pop from the heap up to $k$ times. As $k \leq N$, this is $O(N \log{k})$ in total.

In Python, we improve this to $O(N + k \log {N})$: our heapq.heapify operation and counting operations are $O(N)$, and each of $k$ heapq.heappop operations are $O(\log {N})$.

* Space Complexity: $O(N)$, the space used to store our count.

# Submissions
---
**Solution: (Heap)**
```
Runtime: 48 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
```

**Solution 2: (Hash, Sort)**
```
Runtime: 7 ms
Memory Usage: 7.9 MB
```
```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

// if strlen < 6 key will be unic
int string_key(char *s)
{
    int len = strlen(s);
    int key = 7;
    if (len > 5) len = 5; // the key will not be uniq
    for (int i = 0; i < len; i++)
        key = key*31 + s[i];

    return(key);       
}


struct DataItem {
    char* s;   
    int   key;
    int   count;
    struct DataItem* next;
};

struct DataItem **init(int size)
{
    struct DataItem** hash=malloc(sizeof(struct DataItem*)*size);
    for (int i=0; i<size; i++)
        hash[i]= 0;
    return hash;
};

int hashCode(int key,int size) {
    return key % size;
}

void insert(char* s, struct DataItem** hashArray,int size)
{
    int key = string_key(s);
   //get the hash 
   int hashIndex = hashCode(key,size);

   struct DataItem** item = &hashArray[hashIndex];
   //move in array until an empty 
   while((*item) != NULL)
   {
       if ((*item)->key == key &&
           !strcmp(s,(*item)->s))
       {
           (*item)->count++;
           return;
       }
       
       item = &(*item)->next;
   }
   (*item) = (struct DataItem*) malloc(sizeof(struct DataItem));
   (*item)->s    = s;  
   (*item)->key  = key;
   (*item)->count  = 1;
   (*item)->next = 0;
}

struct Result
{
    char* s;
    int count;
};
int cmpfunc(const void* a_, const void* b_)
{ 
    struct Result* a = (struct Result*)a_;
    struct Result* b = (struct Result*)b_;
    if (a->count == b->count)
    {
        int i = 0;
        while (a->s[i] && b->s[i] && a->s[i]== b->s[i]) i++;
        return (a->s[i] - b->s[i]);
    }
   return (((struct Result*)b)->count - ((struct Result*)a)->count);
}
struct Result* destroy(struct DataItem** hashArray,int size,int* count)
{
    struct Result* result= malloc(sizeof(struct Result)*size);
    memset(result,0,sizeof(struct Result)*size);
    for(int i = 0; i<size; i++)
    {
	
        if(hashArray[i] != NULL)
        {
            struct DataItem* item = hashArray[i];
            while (item)
            {                
                result[*count].s = item->s;
                result[*count].count = item->count;
                (*count)++;
                
                struct DataItem* temp = item;
                item = item->next;
                free(temp);
            }
        }
    }
    free(hashArray);
    return result;
}

char ** topKFrequent(char ** words, int wordsSize, int k, int* returnSize){
    if (!wordsSize)
    {
        *returnSize = 0;
        return 0;
    }

    int size = wordsSize;
            
    struct DataItem** hashArray = init(wordsSize);
    for(int i = 0; i<wordsSize; i++)
        insert(words[i],hashArray,size);


    int count = 0;
    struct Result* result = destroy(hashArray,size,&count);
    qsort(result,count,sizeof(struct Result),cmpfunc);
    int i;
    if (k<count) count = k;
    char **list = malloc(sizeof(char*)*count);
    for(i=0; i<count; i++)
    {
        int len = strlen(result[i].s)+1;
        list[i]=  malloc(sizeof(char)*len);
        strcpy(list[i],result[i].s);
    }
    free(result);
     *returnSize = count;
    return list;
}
```

**Solution 3: (Heap)**
```
Runtime: 18 ms
Memory Usage: 12.6 MB
```
```c++
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> wordCountMap;
        for (string &word : words) {
            wordCountMap[word]++;
        }
        
        auto cmp = [](pair<int, string> &a, pair<int, string> &b) {
            if (a.first > b.first) {
                return true;
            }
            if (a.first == b.first && a.second < b.second) {
                return true;
            }
            return false;
        };
        
        priority_queue<pair<int, string>, vector<pair<int, string>>, decltype(cmp)> PQ(cmp);
        for (auto &it : wordCountMap) {
            PQ.push({ it.second, it.first });
            if (PQ.size() > k) {
                PQ.pop();
            }
        }
        
        vector<string> result;
        for (; !PQ.empty() && k > 0; PQ.pop(), k--) {
            result.push_back(PQ.top().second);
        }
        
        reverse(begin(result), end(result));
        return result;
    }
};
```

**Solution 4: (Heap)**
```
Runtime: 15 ms
Memory Usage: 13.3 MB
```
```c++
class Solution {
    static bool comp(pair<int,string> p1,pair<int,string> p2)
    {
        if(p1.first==p2.first)
        {
            return p1.second<p2.second;
        }
        return p1.first>p2.first;
    }
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        int n=words.size();
        // creating an unordered map to store string and its frequency
        unordered_map<string,int> m;
        for(int i=0;i<n;i++)
        {
            m[words[i]]++;
        }
        // creating a max heap
        priority_queue <pair<int,string>> pq;
        // traversing through map and pushing the pair<int,string> into heap
        // this heap will automatically sort the string in descending order
        // of their frequency
        for(auto x:m)
        {
            string s=x.first;
            int b=x.second;
            pq.push(make_pair(b,s));
        }
        // creating a vector of <int,string>
        vector<pair<int,string>> v;
        // pushing all the elements from heap into the vector
        while(!pq.empty())
        {
            pair<int,string> p1=pq.top();
            pq.pop();
            v.push_back(make_pair(p1.first,p1.second));
        }
        // now we will sort the elements of vector according to frequency of string
        // and if frequency of two strings are same then we will sort them lexographically
        // comp is the static function declared upwards and peforms the sorting task as specified
        sort(v.begin(),v.end(),comp);
        vector<string> ans;
        // now we create the ans vector and push the top k elements
        for(int i=0;i<k;i++)
        {
            ans.push_back(v[i].second);
        }
        return ans;
    }
};
```
