895. Maximum Frequency Stack

Implement `FreqStack`, a class which simulates the operation of a stack-like data structure.

`FreqStack` has two functions:

* `push(int x)`, which pushes an integer `x` onto the stack.
* `pop()`, which removes and returns the most frequent element in the stack.
    * If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.
 

**Example 1:**
```
Input: 
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].
``` 

**Note:**

* Calls to `FreqStack.push(int x)` will be such that `0 <= x <= 10^9`.
* It is guaranteed that `FreqStack.pop()` won't be called if the stack has zero elements.
* The total number of `FreqStack.push` calls will not exceed `10000` in a single test case.
* The total number of `FreqStack.pop` calls will not exceed `10000` in a single test case.
* The total number of `FreqStack.push` and `FreqStack.pop` calls will not exceed `150000` across all test cases.

# Submissions
---
## Approach 1: Stack of Stacks
**Intuition**

Evidently, we care about the frequency of an element. Let `freq` be a Map from $x$ to the number of occurrences of $x$.

Also, we (probably) care about `maxfreq`, the current maximum frequency of any element in the stack. This is clear because we must pop the element with the maximum frequency.

The main question then becomes: among elements with the same (maximum) frequency, how do we know which element is most recent? We can use a stack to query this information: the top of the stack is the most recent.

To this end, let `group` be a map from frequency to a stack of elements with that frequency. We now have all the required components to implement `FreqStack`.

**Algorithm**

Actually, as an implementation level detail, if `x` has frequency `f`, then we'll have `x` in all `group[i] (i <= f)`, not just the top. This is because each `group[i]` will store information related to the ith copy of `x`.

Afterwards, our goal is just to maintain `freq`, `group`, and `maxfreq` as described above.

```python
class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self):
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x
```

**Complexity Analysis**

* Time Complexity: $O(1)$ for both push and pop operations.

* Space Complexity: $O(N)$, where `N` is the number of elements in the `FreqStack`.

# Submissions
---
**Solution: (Stack of Stacks)**
```
Runtime: 428 ms
Memory Usage: 21.5 MB
```
```python
class FreqStack:

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x: int) -> None:
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self) -> int:
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
```

**Solution 2: (Stack)**
```
Runtime: 452 ms
Memory Usage: 87 MB
```
```c++
class FreqStack {
public:
    int maxfreq;
    unordered_map<int,int>mp;
    unordered_map<int,stack<int>>mymap;
    FreqStack() {
        maxfreq = 0;    
    }
    
    void push(int x) {
        if (mp.count(x)){
            mp[x]++;
        } else {
            mp[x] = 1;
        }
        
        mymap[mp[x]].push(x);
        maxfreq = max(maxfreq, mp[x]);
        return;
    }
    
    int pop() {
        int ans = mymap[maxfreq].top();
        mp[ans]--;
        mymap[maxfreq].pop();
        if (mymap[maxfreq].empty()) maxfreq = maxfreq-1;
        return ans;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 */
```

**Solution 3: (Hash Table, Priority Queue)**
```
Runtime: 244 ms
Memory Usage: 64.1 MB
```
```c
#define MAP_SIZE 10001

typedef struct mapNode
{
	int key;
	int val;
	struct mapNode *next;
} mapNode;

typedef struct hashMap
{
	int size;
	struct mapNode **list;
} hashMap;

hashMap *createMap(int size)
{
	struct hashMap *map = malloc(sizeof(hashMap));
	map->size = size;
	map->list = malloc(sizeof(mapNode *) * size);

	for (int i = 0; i < size; i++)
		map->list[i] = NULL;

	return map;
}

int hashCode(hashMap *map, int key)
{
	if (key < 0)
		return -(key % map->size);

	return key % map->size;
}

void put(hashMap *map, int key, int val)
{
	int pos = hashCode(map, key);
	mapNode *list = map->list[pos];
	mapNode *newNode = malloc(sizeof(mapNode));
	mapNode *temp = list;

	while (temp)
	{
		if (temp->key == key)
		{
			temp->val = val;
			return;
		}

		temp = temp->next;
	}

	newNode->key = key;
	newNode->val = val;
	newNode->next = list;
	map->list[pos] = newNode;
}

int get(hashMap *map, int key)
{
	int pos = hashCode(map, key);
	mapNode *list = map->list[pos];
	mapNode *temp = list;

	while (temp)
	{
		if (temp->key == key)
			return temp->val;

		temp = temp->next;
	}

	return 0;
}

void freeMap(hashMap *map)
{
	for (int i = 0; i < map->size; i++)
		free(map->list[i]);

	free(map->list);
	free(map);
}

typedef int(*compare)(const void *element1, const void *element2);

typedef struct PQ
{
	int capacity;
	int n;
	void **array;
	compare cmp;
} PQ;

static const int initialSize = 16;

static void swap(PQ *pq, int index1, int index2)
{
	void *tmp = pq->array[index1];
	pq->array[index1] = pq->array[index2];
	pq->array[index2] = tmp;
}

static void rise(PQ *pq, int k) 
{
	while (k > 1 && pq->cmp(pq->array[k / 2], pq->array[k]) < 0)
	{
		swap(pq, k, k / 2);
		k = k / 2;
	}
}

static void fall(PQ *pq, int k) 
{
	while (2 * k <= pq->n) 
	{
		int child = 2 * k;
		if (child < pq->n && pq->cmp(pq->array[child], pq->array[child + 1]) < 0) 
			child++;

		if (pq->cmp(pq->array[k], pq->array[child]) < 0) 
			swap(pq, k, child);

		k = child;
	}
}

static void **arrayResize(void **array, int newlength) 
{
	return realloc(array, newlength * sizeof(void *));
}

PQ *pqInit(int(*compare)(const void *element1, const void *element2)) 
{
	PQ *pq = malloc(sizeof(PQ));
	pq->array = NULL;
	pq->capacity = 0;
	pq->n = 0;
	pq->cmp = compare;

	return pq;
}

void pqInsert(PQ *pq, void *el)
{

	if (pq->capacity == 0) 
	{
		pq->capacity = initialSize;
		pq->array = arrayResize(pq->array, pq->capacity + 1);
	}
	else if (pq->n == pq->capacity)
	{
		pq->capacity *= 2;
		pq->array = arrayResize(pq->array, pq->capacity + 1);
	}

	pq->array[++pq->n] = el;
	rise(pq, pq->n);
}

void *pqPop(PQ *pq) 
{
	if (pq->capacity > initialSize && pq->n < pq->capacity / 4)
	{
		pq->capacity /= 2;
		pq->array = arrayResize(pq->array, pq->capacity + 1);
	}

	void *el = pq->array[1];
	swap(pq, 1, pq->n--);
	pq->array[pq->n + 1] = NULL; 
	fall(pq, 1);

	return el;
}

void pqFree(PQ *pq) 
{
	free(pq->array);
	free(pq);
}

typedef struct 
{
	int val;
	int idx;
	int cnt;
} pqNode;

pqNode *addPQNode(int x, int idx, int cnt)
{
	pqNode *n = calloc(1, sizeof(pqNode));
	n->val = x;
	n->idx = idx;
	n->cnt = cnt;

	return n;
}

int comp(const void *a, const void *b) 
{
	const pqNode *node1 = a;
	const pqNode *node2 = b;
	if (node2->cnt == node1->cnt)
		return node1->idx - node2->idx;

	return node1->cnt - node2->cnt;
}


typedef struct {
    PQ *pq;
	hashMap *map;
	int index;
} FreqStack;


FreqStack* freqStackCreate() {
    FreqStack *obj = calloc(1, sizeof(FreqStack));
	obj->index = 1;
	obj->pq = pqInit(comp);
	obj->map = createMap(MAP_SIZE);

	return obj;
}

void freqStackPush(FreqStack* obj, int val) {
    put(obj->map, val, get(obj->map, val) + 1);
	pqInsert(obj->pq, addPQNode(val, obj->index++, get(obj->map, val)));
}

int freqStackPop(FreqStack* obj) {
    pqNode *top = pqPop(obj->pq);
	put(obj->map, top->val, get(obj->map, top->val) - 1);

	return top->val;
}

void freqStackFree(FreqStack* obj) {
    freeMap(obj->map);
	pqFree(obj->pq);
	free(obj);
}

/**
 * Your FreqStack struct will be instantiated and called as such:
 * FreqStack* obj = freqStackCreate();
 * freqStackPush(obj, val);
 
 * int param_2 = freqStackPop(obj);
 
 * freqStackFree(obj);
*/
```

**Solution 4: (Counter, stack)**

cnt
    5,3
    7,2
    4,1
g
    1: 5,7,4
    2: 5,7
mx> 3: 5

```
Runtime: 60 ms, Beats 45.45%
Memory: 100.68 MB, Beats 78.46%
```
```c++
class FreqStack {
    unordered_map<int, int> cnt;
    unordered_map<int,vector<int>> g;
    int mx = 0;
public:
    FreqStack() {
        
    }
    
    void push(int val) {
        cnt[val] += 1;
        g[cnt[val]].push_back(val);
        mx = max(mx, cnt[val]);
    }
    
    int pop() {
        int rst = g[mx].back();
        g[mx].pop_back();
        cnt[rst] -= 1;
        if (g[mx].size() == 0) {
            g.erase(mx);
            mx -= 1;
        }
        return rst;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(val);
 * int param_2 = obj->pop();
 */
```
