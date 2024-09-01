590. N-ary Tree Postorder Traversal

Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

**Follow up:**

Recursive solution is trivial, could you do it iteratively?

 

**Example 1:**

![590_narytreeexample.png](img/590_narytreeexample.png)
```
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
```

**Example 2:**

![590_sample_4_964.png](img/590_sample_4_964.png)
```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
``` 

**Constraints:**

* The height of the n-ary tree is less than or equal to `1000`
* The total number of nodes is between `[0, 10^4]`

# Submissions
---
**Solution 1:**
```
Runtime: 40 ms
Memory Usage: 14.7 MB
```
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.ans = []
        def dfs(node):
            if not node:
                return
            for c in node.children:
                dfs(c)
            self.ans.append(node.val)
        dfs(root)
        return self.ans
```

**Solution 2:**
```
Runtime: 48 ms
Memory Usage: 14.6 MB
```
```
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = collections.deque([])
        stack = root and [root]
        while stack:
            node = stack.pop()
            ans.appendleft(node.val)
            stack.extend([c for c in node.children if c])
        return ans
```

**Solution 3: (Recursive)**
```
Runtime: 13 ms
Memory: 15.17 MB
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

class Solution {
    void traversePostorder(Node* currentNode, vector<int>& postorderList) {
        if (currentNode == nullptr) {
            return;
        }

        // First, visit all children
        for (Node* childNode : currentNode->children) {
            traversePostorder(childNode, postorderList);
        }

        // Then, add the current node's value
        postorderList.push_back(currentNode->val);
    }
public:
    vector<int> postorder(Node* root) {
        vector<int> result;
        if (root == nullptr) {
            return result;
        }
        traversePostorder(root, result);
        return result;
    }
};
```

**Solution 4: (Iterative (Explicit Reversal))**
```
Runtime: 11 ms
Memory: 15.19 MB
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

class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> result;

        // If the root is null, return the empty list
        if (root == nullptr) return result;

        stack<Node*> nodeStack;
        nodeStack.push(root);

        // Traverse the tree using the stack
        while (!nodeStack.empty()) {
            Node* currentNode = nodeStack.top();
            nodeStack.pop();

            result.push_back(currentNode->val);
            // Push all the children of the current node to the stack
            for (Node* child : currentNode->children) nodeStack.push(child);
        }

        // Reverse the result list to get the correct postorder traversal
        reverse(result.begin(), result.end());
        return result;
    }
};
```

**Solution 5: (Iterative (Two Stacks))**
```
Runtime: 11 ms
Memory: 15.47 MB
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

class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> result;

        // If the root is nullptr, return the empty vector
        if (root == nullptr) return result;

        stack<Node*> nodeStack;     // Stack for traversal
        stack<Node*> reverseStack;  // Stack to reverse the order

        nodeStack.push(root);

        // Traverse the tree using the nodeStack
        while (!nodeStack.empty()) {
            Node* currentNode = nodeStack.top();
            nodeStack.pop();
            reverseStack.push(currentNode);

            // Push all the children of the current node to nodeStack
            for (Node* child : currentNode->children) {
                nodeStack.push(child);
            }
        }

        // Pop nodes from reverseStack and add their values to the result vector
        while (!reverseStack.empty()) {
            Node* currentNode = reverseStack.top();
            reverseStack.pop();
            result.push_back(currentNode->val);
        }

        return result;
    }
};
```

**Solution 6: (Iterative (Without Reverse))**
```
Runtime: 16 ms
Memory: 15.46 MB
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

class Solution {
    // Helper class to pair a node with its visited status
    struct NodeVisitPair {
        Node* node;
        bool isVisited;

        NodeVisitPair(Node* n, bool visited) : node(n), isVisited(visited) {}
    };
public:
    vector<int> postorder(Node* root) {
        vector<int> result;
        // If the root is null, return the empty vector
        if (root == nullptr) return result;

        stack<NodeVisitPair> nodeStack;
        nodeStack.push(NodeVisitPair(root, false));

        while (!nodeStack.empty()) {
            NodeVisitPair currentPair = nodeStack.top();
            nodeStack.pop();

            if (currentPair.isVisited) {
                // If the node has been visited, add its value to the result
                result.push_back(currentPair.node->val);
            } else {
                // Mark the current node as visited and push it back to the
                // stack
                currentPair.isVisited = true;
                nodeStack.push(currentPair);

                // Push all children to the stack in reverse order
                vector<Node*>& children = currentPair.node->children;
                for (int i = children.size() - 1; i >= 0; i--) {
                    nodeStack.push(NodeVisitPair(children[i], false));
                }
            }
        }

        return result;
    }
};
```
