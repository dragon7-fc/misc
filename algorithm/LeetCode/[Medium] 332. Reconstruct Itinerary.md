332. Reconstruct Itinerary

Given a list of airline tickets represented by pairs of departure and arrival airports `[from, to]`, reconstruct the itinerary in order. All of the tickets belong to a man who departs from `JFK`. Thus, the itinerary must begin with `JFK`.

**Note:**

* If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`.
* All airports are represented by three capital letters (IATA code).
* You may assume all tickets form at least one valid itinerary.

**Example 1:**
```
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
```

**Example 2:**
```
Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
```

# Submissions
---
**Solution 1: (DFS, Graph)**
```
Runtime: 88 ms
Memory Usage: 13.2 MB
```
```python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        
        for departure, arrival in tickets:
             graph[departure].append(arrival)
                
        for airport in graph:
            graph[airport].sort()
                
        total = len(tickets) + 1
        
        def dfs(ticket, way):
            if len(way) == total:
                return way
            
            for i in range(len(graph[ticket])):
                if graph[ticket][i] == None:
                    continue
                    
                arrival = graph[ticket][i]
                graph[ticket][i] = None
                
                reconstruction = dfs(arrival, way + [arrival])
                if reconstruction:
                    return reconstruction
                
                graph[ticket][i] = arrival
                
        return dfs('JFK', ['JFK'])
```

**Solution 2: (DFS)**
```
Runtime: 48 ms
Memory Usage: 15.4 MB
```
```c++
class Solution {
public:
    void dfs(string src,unordered_map<string,vector<string>>& m,vector<string>& ans){
        while(!m[src].empty()){
            string s=m[src].back();
            m[src].pop_back();
            dfs(s,m,ans);
        }
        ans.push_back(src);
    }
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string,vector<string>> m;
        // Create Graph
        for(auto i:tickets)
            m[i[0]].push_back(i[1]);
        // Sorting in descending order since we will be popping elements from the end
        for(auto &i:m)
            sort(i.second.begin(),i.second.end(),greater<string>());  

        vector<string> ans;
        dfs("JFK",m,ans);
        reverse(ans.begin(),ans.end());
        return ans;
    }
};
```

**Solution 3: (Trie)**
```
Runtime: 16 ms
Memory Usage: 9.3 MB
```
```c
typedef struct  _TRIE      TRIE;
typedef struct  _TICKET    TICKET;

struct  _TICKET {
  char    *Name;
  TICKET  *Next;
};

struct     _TRIE {
  TICKET  *Next;
  char    *Name;
  TRIE    *Trie[26];
};


int MyStrCmp (char *Src, char *Dst) {
  int Index;

  for (Index = 0; Index < 3; Index++) {
    if (Src[Index] > Dst[Index]) {
      return 1;
    } else if (Src[Index] < Dst[Index]) {
      return -1;
    }
  }
  return 0;
}

void TrieInsert(TRIE* Head, char * Word) {
  TICKET   *Ticket;
  TICKET   *Node;
  TICKET   *Pre;

  Ticket = (TICKET *)calloc (1, sizeof (TICKET));
  Ticket->Name = Word;

  if (Head->Next == NULL) {
    Head->Next = Ticket;
    return;
  }
  Node = Head->Next;
  Pre = NULL;
  while (Node != NULL) {
    if (MyStrCmp (Node->Name, Ticket->Name) == 1) {
      if (Pre == NULL) {
        Ticket->Next = Head->Next;
        Head->Next   = Ticket;
      } else {
        Ticket->Next = Pre->Next;
        Pre->Next    = Ticket;
      }
      return;
    }
    Pre = Node;
    Node = Node->Next;
  }
  Pre->Next = Ticket;
}

TRIE * TrieCreate(TRIE* Head, char * Word) {
  int  Index;

  for (Index = 0; Index < 3; Index++) {
    if (Head->Trie[Word[Index] - 'A'] == NULL) {
      Head->Trie[Word[Index] - 'A'] = calloc (1, sizeof (TRIE));
    }
    Head =  Head->Trie[Word[Index] - 'A'];
  }
  Head->Name = Word;
  return Head;
}

TRIE * TrieSearch(TRIE  *Head, char *Word) {
  int  Index;

  for (Index = 0; Index < 3; Index++) {
    if (Head->Trie[Word[Index] - 'A'] == NULL) {
      return NULL;
    }
    Head = Head->Trie[Word[Index] - 'A'];
  }
  return Head;
}

bool Dfs (TRIE  *Head, char *Word, char **ReturnBuffer, int UsedSize, int Totalsize) {
  TRIE     *Trie;
  TICKET   *Node;
  TICKET   *Pre;
  TICKET   *Current;

  Trie = TrieSearch (Head, Word);
  Node = NULL;
  if (Trie != NULL) {
    Node = Trie->Next;
  }
  if (Node == NULL) {
    if (UsedSize != Totalsize) {
      return false;
    }
    return true;
  }

  Pre = NULL;
  while (Node != NULL) {
    Current = Node;
    //
    // remove node to indicate the node has been used.
    //
    if (Pre == NULL) {
      Trie->Next = Current->Next;
    } else {
      Pre->Next = Current->Next;
    }
    ReturnBuffer[UsedSize] = Current->Name;
    if (Dfs (Head, Current->Name, ReturnBuffer, UsedSize + 1, Totalsize)) {
      return true;
    }
    //
    // Insert node back to indicate the node has been not used.
    //
    if (Pre == NULL) {
      Current->Next = Trie->Next;
      Trie->Next = Current;
    } else {
      Current->Next = Pre->Next;
      Pre->Next     = Current;
    }
    Pre = Node;
    Node = Node->Next;
  }
  return false;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** findItinerary(char *** tickets, int ticketsSize, int* ticketsColSize, int* returnSize){
    TRIE     *Head;
    TRIE     *Node;
    char     **ReturnBuffer;
    char     *Start;
    int      Index;

    *returnSize = ticketsSize + 1;
    ReturnBuffer = (char **)malloc (*returnSize * sizeof (char *));

    //
    // Init graph.
    // 1. Using TRIE to store node because it only has 3 uupper case English letters.
    // 2. Sort from smaller lexical to higher lexical.
    // 3. Using List to store it so we can easy to remove and it back.
    //
    Head = (TRIE *)calloc (1, sizeof (TRIE));
    for (Index = 0; Index < ticketsSize; Index++) {
    Node = TrieSearch (Head, tickets[Index][0]);
    if (Node == NULL) {
      Node = TrieCreate(Head, tickets[Index][0]);
    }
    TrieInsert (Node, tickets[Index][1]);
    }
    //
    // Using DFS to find result, Once the first one is found. it must be the smallest
    // lexical order result so return true directly to terminate the search.
    //
    Start = (char *)malloc (4 * sizeof (char));
    strcpy (Start, "JFK");
    ReturnBuffer[0] = Start;
    Dfs (Head, Start, ReturnBuffer, 1, *returnSize);

    return ReturnBuffer;
}
```

**Solution 4: (DFS, iterative)**
```
Runtime: 7 ms
Memory: 15.2 MB
```
```c++
class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        std::unordered_map<std::string, std::vector<std::string>> graph;
        
        for (auto& ticket : tickets) {
            graph[ticket[0]].push_back(ticket[1]);
        }
        
        for (auto& [_, dests] : graph) {
            std::sort(dests.rbegin(), dests.rend());
        }
        
        std::vector<std::string> stack = {"JFK"};
        std::vector<std::string> itinerary;
        
        while (!stack.empty()) {
            std::string curr = stack.back();
            if (graph.find(curr) != graph.end() && !graph[curr].empty()) {
                stack.push_back(graph[curr].back());
                graph[curr].pop_back();
            } else {
                itinerary.push_back(stack.back());
                stack.pop_back();
            }
        }
        
        std::reverse(itinerary.begin(), itinerary.end());
        return itinerary;
    }
};
```

**Solution 5: (DFS)**
```
Runtime: 11 ms
Memory: 14.6 MB
```
```c++
class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string, vector<string>> graph;
        
        for (auto& ticket : tickets) {
            graph[ticket[0]].push_back(ticket[1]);
        }
        
        for (auto& [_, destinations] : graph) {
            sort(destinations.rbegin(), destinations.rend());
        }
        
        vector<string> itinerary;
        
        function<void(const string&)> dfs = [&](const string& airport) {
            while (!graph[airport].empty()) {
                string next = graph[airport].back();
                graph[airport].pop_back();
                dfs(next);
            }
            itinerary.push_back(airport);
        };
        
        dfs("JFK");
        reverse(itinerary.begin(), itinerary.end());

        return itinerary;
    }
};
```
