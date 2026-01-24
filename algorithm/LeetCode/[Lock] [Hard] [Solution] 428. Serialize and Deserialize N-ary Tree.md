428. Serialize and Deserialize N-ary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following `3-ary tree`


![428_narytreeexample.png](img/428_narytreeexample.png)

as `[1 [3[5 6] 2 4]]`. Note that this is just an example, you do not necessarily need to follow this format.

Or you can follow LeetCode's level order traversal serialization format, where each group of children is separated by the null value.


![428_sample_4_964.png](img/428_sample_4_964.png)

For example, the above tree may be serialized as `[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]`.

You do not necessarily need to follow the above suggested formats, there are many more different formats that work so please be creative and come up with different approaches yourself.

 

**Constraints:**

* The number of nodes in the tree is in the range `[0, 104]`.
* `0 <= Node.val <= 10^4`
* The height of the n-ary tree is less than or equal to 1000
* Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.

# Submissions
---
**Solution 1: (Parent Child relationships)**
```
Runtime: 84 ms
Memory Usage: 18.3 MB
```
```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class WrappableInt:
    def __init__(self, x):
        self.value = x
    def getValue(self):
        return self.value
    def increment(self):
        self.value += 1
            
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        serializedList = []
        self._serializeHelper(root, serializedList, WrappableInt(1), None)
        return "".join(serializedList)
    
    def _serializeHelper(self, root, serializedList, identity, parentId):
        if not root:
            return
        
        # Own identity
        serializedList.append(chr(identity.getValue() + 48))
        
        # Actual value
        serializedList.append(chr(root.val + 48))
        
        # Parent's identity
        serializedList.append(chr(parentId + 48) if parentId else 'N')
        
        parentId = identity.getValue()
        for child in root.children:
            identity.increment()
            self._serializeHelper(child, serializedList, identity, parentId)
        
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        
        return self._deserializeHelper(data)
        
    def _deserializeHelper(self, data):
        
        nodesAndParents = {}
        for i in range(0, len(data), 3):
            identity = ord(data[i]) - 48
            orgValue = ord(data[i + 1]) - 48
            parentId = ord(data[i + 2]) - 48
            nodesAndParents[identity] = (parentId, Node(orgValue, []))
            
        for i in range(3, len(data), 3):
            
            # Current node
            identity = ord(data[i]) - 48
            node = nodesAndParents[identity][1]
            
            # Parent node
            parentId = ord(data[i + 2]) - 48;
            parentNode = nodesAndParents[parentId][1];
            
            # Attach!
            parentNode.children.append(node);
            
        return nodesAndParents[ord(data[0]) - 48][1]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```

**Solution 2: (Depth First Search with Children Sizes!)**
```
Runtime: 68 ms
Memory Usage: 17.3 MB
```
```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class WrappableInt:
    def __init__(self, x):
        self.value = x
    def getValue(self):
        return self.value
    def increment(self):
        self.value += 1
            
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        serializedList = []
        self._serializeHelper(root, serializedList)
        return "".join(serializedList)
    
    def _serializeHelper(self, root, serializedList):
        if not root:
            return
        
        # Actual value
        serializedList.append(chr(root.val + 48))
        
        # Number of children
        serializedList.append(chr(len(root.children) + 48))
        
        for child in root.children:
            self._serializeHelper(child, serializedList)
        
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        
        return self._deserializeHelper(data, WrappableInt(0))
        
    def _deserializeHelper(self, data, index):
        
        if index.getValue() == len(data):
            return None
        
        # The invariant here is that the "index" always
        # points to a node and the value next to it 
        # represents the number of children it has.
        node = Node(ord(data[index.getValue()]) - 48, [])
        index.increment()
        numChildren = ord(data[index.getValue()]) - 48
        for _ in range(numChildren):
            index.increment()
            node.children.append(self._deserializeHelper(data, index))
        return node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```

**Solution 3: (Depth First Search with a Sentinel)**
```
Runtime: 76 ms
Memory Usage: 17.3 MB
```
```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class WrappableInt:
    def __init__(self, x):
        self.value = x
    def getValue(self):
        return self.value
    def increment(self):
        self.value += 1
            
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        serializedList = []
        self._serializeHelper(root, serializedList)
        return "".join(serializedList)
    
    def _serializeHelper(self, root, serializedList):
        if not root:
            return
        
        # Actual value
        serializedList.append(chr(root.val + 48))
        
        for child in root.children:
            self._serializeHelper(child, serializedList)
            
        # Add the sentinel to indicate that all the children
        # for the current node have been processed 
        serializedList.append('#')
        
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        
        return self._deserializeHelper(data, WrappableInt(0))
        
    def _deserializeHelper(self, data, index):
        
        if index.getValue() == len(data):
            return None
        
        node = Node(ord(data[index.getValue()]) - 48, [])
        index.increment()
        while (data[index.getValue()] != '#'):
            node.children.append(self._deserializeHelper(data, index))
        
        
        # Discard the sentinel. Note that this also moves us
        # forward in the input string. So, we don't have the index
        # progressing inside the above while loop!
        index.increment()
        return node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```

**Solution 4: (Level order traversal)**
```
Runtime: 64 ms
Memory Usage: 17.3 MB
```
```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def _serializeHelper(self, root, serializedList):

        queue = collections.deque() 
        queue.append(root)
        queue.append(None)
        
        while queue:
            
            # Pop a node
            node = queue.popleft();
            
            # If this is an "endNode", we need to add another one
            # to mark the end of the current level unless this
            # was the last level.
            if (node == None):
                
                # We add a sentinal value of "#" here
                serializedList.append('#');
                if queue:
                    queue.append(None);  
                    
            elif node == 'C':
                
                # Add a sentinal value of "$" here to mark the switch to a
                # different parent.
                serializedList.append('$');
                
            else:
                
                # Add value of the current node and add all of it's
                # children nodes to the queue. Note how we convert
                # the integers to their corresponding ASCII counterparts.
                serializedList.append(chr(node.val + 48));
                for child in node.children:
                    queue.append(child);
                
                # If this not is NOT the last one on the current level, 
                # add a childNode as well since we move on to processing
                # the next node.
                if queue[0] != None:
                    queue.append('C');
    
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ""
        
        serializedList = []
        self._serializeHelper(root, serializedList)
        return "".join(serializedList)
        
    def _deserializeHelper(self, data, rootNode):
        
        # We move one level at a time and at every level, we need access
        # to the nodes on the previous level as well so that we can form
        # the children arrays properly. Hence two arrays.
        prevLevel, currentLevel = collections.deque(), collections.deque()
        currentLevel.append(rootNode);
        parentNode = rootNode;
        
        # Process the characters in the string one at a time.
        for i in range (1, len(data)):
            if data[i] == '#':
                
                # Special processing for end of level. We need to swap the
                # array lists. Here, we simply re-initialize the "currentLevel"
                # arraylist rather than clearing it.
                prevLevel = currentLevel;
                currentLevel = collections.deque()
                
                # Since we move one level down, we take the parent as the first
                # node on the current level.
                parentNode = prevLevel.popleft() if prevLevel else None;
                
            else:
                if data[i] == '$':
                    
                    # Special handling for change in parent on the same level
                    parentNode = prevLevel.popleft() if prevLevel else None;
                else:
                    childNode = Node(ord(data[i]) - 48, []);    
                    currentLevel.append(childNode);
                    parentNode.children.append(childNode);

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        
        rootNode = Node(ord(data[0]) - 48, [])
        self._deserializeHelper(data, rootNode)
        return rootNode

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```

**Solution 5: (DFS, deque)**

            1
      /     |     \
    3       2      4
   /  \   
  5    6

    1,3,5,#,6,#,#,2,#,4,#,#
        --- ---   --- ---
      -----------
    -----------------------
            1
           / \ \
         3    2  4
        / \
        5  6

```
Runtime: 31 ms, Beats 64.12%
Memory: 186.64 MB, Beats 16.03%
```
```c++
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(Node* root) {
        if (!root) {
            return "";
        }
        string rst = to_string(root->val);
        rst += ",";
        for (auto &child: root->children) {
            rst += serialize(child);
            rst += ",";
        }
        rst += "#";
        return rst;
    }
	
    Node *dfs(deque<int> &dq) {
        if (dq.front() == -1) {
            dq.pop_front();
            return nullptr;
        }
        auto a = dq.front();
        dq.pop_front();
        Node *node = new Node(a), *child;
        while ((child = dfs(dq)) != nullptr) {
            node->children.push_back(child);
        }
        return node;
    }

    // Decodes your encoded data to tree.
    Node* deserialize(string data) {
        if (data == "") {
            return nullptr;
        }
        deque<int> dq;
        stringstream ss(data);
        string s;
        while (getline(ss, s, ',')) {
            if (s != "#") {
                dq.push_back(stoi(s));
            } else {
                dq.push_back(-1);
            }
        }
        return dfs(dq);
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
```

**Solution 6: (DFS)**
```
Runtime: 32 ms, Beats 56.49%
Memory: 186.74 MB, Beats 16.03%
```
```c++
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(Node* root) {
        if (!root) {
            return "";
        }
        string rst = to_string(root->val);
        rst += ",";
        for (auto &child: root->children) {
            rst += serialize(child);
            rst += ",";
        }
        rst += "#";
        return rst;
    }
	
    Node *dfs(int &i, vector<int> &dp) {
        if (dp[i] == -1) {
            i += 1;
            return nullptr;
        }
        Node *node = new Node(dp[i]), *child;
        i += 1;
        while ((child = dfs(i, dp)) != nullptr) {
            node->children.push_back(child);
        }
        return node;
    }

    // Decodes your encoded data to tree.
    Node* deserialize(string data) {
        if (data == "") {
            return nullptr;
        }
        vector<int> dp;
        stringstream ss(data);
        string s;
        while (getline(ss, s, ',')) {
            if (s != "#") {
                dp.push_back(stoi(s));
            } else {
                dp.push_back(-1);
            }
        }
        int i = 0;
        return dfs(i, dp);
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
```

**Solution 7: (DFS, Two Pointes)**

            1
      /     |     \
    3       2      4
   /  \   
  5    6

serialize:    1,3,5,#,6,#,#,2,#,4,#,#
deserialize:
                                      i

              1
            / |  \
          3   2   4
        /  \  x   x
       5    6
       x    x
```
Runtime: 30 ms, Beats 67.18%
Memory: 183.60 MB, Beats 22.90%
```
```c++
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(Node* root) {
        if (!root) {
            return "";
        }
        string rst = to_string(root->val);
        rst += ",";
        for (auto &child: root->children) {
            rst += serialize(child);
            rst += ",";
        }
        rst += "#";
        return rst;
    }
	
    Node *dfs(int &i, string &data) {
        if (i == data.size()) {
            return nullptr;
        }
        int j = i;
        while (j < data.size() && data[j] != ',') {
            j += 1;
        }
        string s = data.substr(i, j - i);
        i = j + 1;
        if (s == "#") {
            return nullptr;
        }
        Node *node = new Node(stoi(s)), *child;
        while ((child = dfs(i, data)) != nullptr) {
            node->children.push_back(child);
        }
        return node;
    }

    // Decodes your encoded data to tree.
    Node* deserialize(string data) {
        int i = 0;
        return dfs(i, data);
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
```
