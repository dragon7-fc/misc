431. Encode N-ary Tree to Binary Tree

Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree to get the original N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. Similarly, a binary tree is a rooted tree in which each node has no more than 2 children. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that an N-ary tree can be encoded to a binary tree and this binary tree can be decoded to the original N-nary tree structure.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See following example).

For example, you may encode the following 3-ary tree to a binary tree in this way:

![431_narytreebinarytreeexample.png](img/431_narytreebinarytreeexample.png)

Input: root = [1,null,3,2,4,null,5,6]
Note that the above is just an example which might or might not work. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

**Example 1:**
```
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]
```

**Example 2:**
```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
```

**Example 3:**
```
Input: root = []
Output: []
```

**Constraints:**

* The number of nodes in the tree is in the range `[0, 10^4]`.
* `0 <= Node.val <= 10^4`
* The height of the n-ary tree is less than or equal to 1000
* Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.

# Submissions
---
**Solution 1: (BFS)**
```
Runtime: 29 ms, Beats 31.67%
Memory: 179.04 MB, Beats 85.00%
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

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Codec {
public:
    // Encodes an n-ary tree to a binary tree.
    TreeNode* encode(Node* root) {
        if(!root)
            return NULL;
        
        //create pointers for current binary tree node and Nary tree node and initialise the latter with root
        TreeNode* currBTnode = new TreeNode(root->val);
        TreeNode* BTroot = currBTnode;
        Node* currNTnode = root;
        
        //declare queue of Binary and Nary Tree to perform BFS
        queue<TreeNode*>BT;
        queue<Node*>NT;
        
        BT.push(currBTnode);
        NT.push(currNTnode);
        
        while(!NT.empty()){
            //iterate over all Nary Tree nodes
            for(int i=0,sz=NT.size();i<sz;i++){
                 currNTnode = NT.front(); NT.pop();
                 currBTnode = BT.front(); BT.pop();
                
                //if it is first child of Nary Node put it to left of Binary tree node
                 if(currNTnode->children.size()>0){
                     TreeNode* child = new TreeNode(currNTnode->children[0]->val);
                     currBTnode->left = child;
                     //push child and Nary Node in queue for BFS
                     BT.push(child);
                     NT.push(currNTnode->children[0]);
                
                     //if it is siblings of child of Nary Node put it to right of Binary tree node
                     for(int c=1;c<currNTnode->children.size();c++){
                         child->right = new TreeNode(currNTnode->children[c]->val);
                         // shift Binary tree pointer to right for adding sibling nodes
                         child = child->right;
                         //push child and Nary Node in queue for BFS
                         BT.push(child);
                         NT.push(currNTnode->children[c]);
                     }
                 }
            }
        }
        return BTroot; 
    }
	
    // Decodes your binary tree to an n-ary tree.
    Node* decode(TreeNode* root) {
        if(!root)
            return NULL;
        
        //create pointers for current binary tree node and Nary tree node and initialise the former with root
        Node* currNTnode = new Node(root->val);
        Node* NTroot = currNTnode;
        TreeNode* currBTnode = root;
        
        //declare queue of Binary and Nary Tree to perform BFS
        queue<Node*>NT;
        queue<TreeNode*>BT;
        
        BT.push(currBTnode);
        NT.push(currNTnode);
        
        while(!BT.empty()){
            //iterate over all Binary Tree nodes
            for(int i=0,sz=BT.size();i<sz;i++){
                currBTnode = BT.front(); BT.pop();
                currNTnode = NT.front(); NT.pop();
                
                // if binary node has a left means current Nary Node has children nodes
                if(currBTnode->left != NULL){
                    //iterate over left nodes of binary tree and add them to children of curr Nary Node
                    currBTnode = currBTnode->left;
                    Node* child = new Node(currBTnode->val);
                    currNTnode->children.push_back(child);
                    //push child and Nary Node in queue for BFS
                    BT.push(currBTnode);
                    NT.push(child);
                    
                    currBTnode= currBTnode->right;
                    while(currBTnode !=NULL){
                        child = new Node(currBTnode->val);
                        currNTnode->children.push_back(child);
                        //push child and Nary Node in queue for BFS
                        BT.push(currBTnode);
                        NT.push(child);
                        //shift pointer to next sibling node
                        currBTnode= currBTnode->right;
                    }
                }
            }
        }
        return NTroot;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(root));
```

**Solution 2: (DFS)**

                    1
               /    |    \
              3     2     4
            /   \
           5     6


                    1
                  /
                3
              /  \
            5     2
             \     \
              6     4

```
Runtime: 28 ms, Beats 45.00%
Memory: 180.51 MB, Beats 26.67%
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

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Codec {
public:
    // Encodes an n-ary tree to a binary tree.
    TreeNode* encode(Node* root) {
        if (!root) {
            return nullptr;
        }
        TreeNode* BTroot = new TreeNode(root->val);
        if (root->children.size() > 0){
            BTroot->left = encode(root->children[0]);
        }
        TreeNode* currBTnode = BTroot->left;
        for (int i = 1; i < root->children.size(); i++){
            currBTnode->right = encode(root->children[i]);
            currBTnode = currBTnode->right;
        }
        return BTroot;
    }
	
    // Decodes your binary tree to an n-ary tree.
    Node* decode(TreeNode* root) {
        if (!root) {
            return nullptr;
        }
        Node* NTroot = new Node(root->val);
        Node* currNTroot = NTroot;
        TreeNode* currBTnode = root->left;
        while (currBTnode!=NULL){
            currNTroot->children.push_back(decode(currBTnode));
            currBTnode = currBTnode->right;
        }
        return NTroot;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(root));
```
