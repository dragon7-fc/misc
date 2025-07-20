1233. Remove Sub-Folders from the Filesystem

Given a list of folders, remove all sub-folders in those folders and return in any order the folders after removing.

If a `folder[i]` is located within another `folder[j]`, it is called a sub-folder of it.

The format of a path is one or more concatenated strings of the form: `/` followed by one or more lowercase English letters. For example, `/leetcode` and `/leetcode/problems`are valid paths while an empty string and `/` are not.

 

**Example 1:**
```
Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
```

**Example 2:**
```
Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d/" will be removed because they are subfolders of "/a".
```

**Example 3:**
```
Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]
``` 

**Constraints:**

* `1 <= folder.length <= 4 * 10^4`
* `2 <= folder[i].length <= 100`
* `folder[i]` contains only lowercase letters and '/'
* `folder[i]` always starts with character '/'
* Each folder name is unique.

# Submissions
---
**Solution 1: (Greedy)**

```
Runtime: 208 ms
Memory Usage: 28.8 MB
```
```python
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder = sorted(folder)
        ans = []
        # Any special string you like to initialize cur. 
        # Just make p.startswith(cur + "/") false in the first iteration.
        cur = "*"
        for p in folder:
            if not p.startswith(cur + "/"):
                cur = p
                ans.append(cur)
                
        return ans
```

**Solution 2: (Sort, O(N * log N * L(word length)))**
```
Runtime: 69 ms
Memory: 51.49 MB
```
```c++
class Solution {
public:
    vector<string> removeSubfolders(vector<string>& folder) {
        sort(folder.begin(), folder.end());
        unordered_set<string> st;
        string cur;
        bool flag;
        vector<string> ans;
        for (auto f: folder) {
            flag = true;
            cur = "/";
            for (int i = 1; i < f.size(); i ++) {
                if (f[i] == '/' && st.count(cur)) {
                    flag = false;
                    break;
                }
                cur += f[i];
            }
            if (cur.size() == f.size() && cur.back() != '/' && st.count(cur)) {
                flag = false;
                break;
            }
            if (flag) {
                st.insert(f);
                ans.push_back(f);
            }
        }
        return ans;
    }
};
```

**Solution 3: (Trie, O(N * L))**
```
Runtime: 244 ms
Memory: 97.70 MB
```
```c++
class Solution {
    private:
    struct TrieNode {
        bool isEndOfFolder;
        unordered_map<string, TrieNode*> children;
        TrieNode() : isEndOfFolder(false) {}
    };

    TrieNode* root;

    // Recursively delete all TrieNodes to prevent memory leaks
    void deleteTrie(TrieNode* node) {
        if (node == nullptr) return;
        for (auto& pair : node->children) {
            deleteTrie(pair.second);
        }
        delete node;
    }

public:
    // Constructor initializes the root of the Trie
    Solution() : root(new TrieNode()) {}

    // Clean up memory
    // A destructor to recursively delete all TrieNodes and prevent memory
    // leaks.
    ~Solution() { deleteTrie(root); }

    vector<string> removeSubfolders(vector<string>& folder) {
        // Build Trie from folder paths
        for (string& path : folder) {
            TrieNode* currentNode = root;
            istringstream iss(path);
            string folderName;

            while (getline(iss, folderName, '/')) {
                // Skip empty folder names
                if (folderName.empty()) continue;
                // Create new node if it doesn't exist
                if (currentNode->children.find(folderName) ==
                    currentNode->children.end()) {
                    currentNode->children[folderName] = new TrieNode();
                }
                currentNode = currentNode->children[folderName];
            }
            // Mark the end of the folder path
            currentNode->isEndOfFolder = true;
        }

        // Check each path for subfolders
        vector<string> result;
        for (string& path : folder) {
            TrieNode* currentNode = root;
            istringstream iss(path);
            string folderName;
            bool isSubFolder = false;

            while (getline(iss, folderName, '/')) {
                // Skip empty folder names
                if (folderName.empty()) continue;
                TrieNode* nextNode = currentNode->children[folderName];
                // Check if the current folder path is a subfolder of an
                // existing folder
                if (nextNode->isEndOfFolder && iss.rdbuf()->in_avail() != 0) {
                    isSubFolder = true;
                    break;  // Found a sub-folder
                }
                currentNode = nextNode;
            }
            // If not a sub-folder, add to the result
            if (!isSubFolder) result.push_back(path);
        }

        return result;
    }
};
```

**Solution 4: (Trie, O(N * L))**
```
Runtime: 331 ms, Beats 5.80%
Memory: 137.21 MB, Beats 11.61%
```
```c++
class Solution {
    struct TrieNode {
        unordered_map<string,TrieNode*> child;
        bool isEnd = false;
    };
    TrieNode *root;
    void del_node(TrieNode* node) {
        for (auto &[_, nnode]: node->child) {
            del_node(nnode);
        }
        delete node;
    }
public:
    Solution(): root(new TrieNode()) {};
    ~Solution() {
        del_node(root);
    }
    vector<string> removeSubfolders(vector<string>& folder) {
        string s;
        stringstream ss;
        vector<string> p, ans;
        unordered_map<string,vector<string>> mp;
        TrieNode *root = new TrieNode(), *node;
        bool flag;
        for (auto &f: folder) {
            ss = stringstream(f);
            while (getline(ss, s, '/')) {
                if (s != "") {
                    p.push_back(s);
                }
            }
            mp[f] = p;
            p.clear();
        }
        for (auto &f: folder) {
            node = root;
            for (auto &cs: mp[f]) {
                if (!node->child.count(cs)) {
                    node->child[cs] = new TrieNode();
                }
                node = node->child[cs];
            }
            node->isEnd = true;
        }
        for (auto &f: folder) {
            node = root;
            flag = true;
            for (int i = 0; i < mp[f].size(); i ++) {
                if (!node->child.count(mp[f][i])) {
                    break;
                }
                node = node->child[mp[f][i]];
                if (node->isEnd && i != mp[f].size() - 1) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                ans.push_back(f);
            }
        }
        return ans;
    }
};
```
