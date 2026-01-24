297. Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

**Example:** 
```
You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
```
**Clarification:** The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

**Note:** Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

# Submissions
---
**Solution 1: (Tree, DFS)**
```
Runtime: 172 ms
Memory Usage: 22.8 MB
```
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def rserialize(root, string):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string
        
        return rserialize(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None
                
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```

**Solution 2: (Tree, BFS)**
```
Runtime: 108 ms
Memory Usage: 17.3 MB
```
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def tree2list(root):
            level = [root]
            while level:
                for n in level: yield str(n.val) if n else ''
                level = [c for n in level for c in ([n.left, n.right] if n else [])]
        
        if root:
            return ','.join(tree2list(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def list2tree(data):
            root = TreeNode(data[0])
            level, used = [root], 1
            while level:
                for i in range(len(level)*2):
                    if i % 2:
                        level[i//2].right = TreeNode(int(data[used+i])) if data[used+i] else None
                    else:
                        level[i//2].left = TreeNode(int(data[used+i])) if data[used+i] else None
                used += 2*len(level)
                level = [c for n in level for c in [n.left, n.right] if c]
            return root
        
        if data:
            return list2tree(data.split(','))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```

**Solution 3: (DFS)**
```
Runtime: 28 ms
Memory Usage: 27.4 MB
```
```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void preorder(struct TreeNode* root, char *arr, int *index) {
    int len;
    if(root == NULL) {

        arr[(*index)++] = '#';
        return;
    }
    len = sprintf(arr+*index, "%d", root->val);
    arr[(*index)+len]='*';//end of marker
    (*index) = (*index)+len+1;
    preorder(root->left,arr,index);
    preorder(root->right,arr,index);
}

/** Encodes a tree to a single string. */
char* serialize(struct TreeNode* root) {
    int count=0;
    int size=0;
    char *arr;
    if(root == NULL)
    return NULL;

    arr = (char *)malloc(sizeof(char)*100000);
    preorder(root,arr,&size);
    return arr;
}

//create node
struct TreeNode *node(int val) {
    struct TreeNode *temp;
    temp = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    temp->val = val;
    temp->left = temp->right = NULL;
    return temp;
}
//helper function for deserialze
struct TreeNode *helper(char *data, int *len) {

    struct TreeNode *root;
    if(data[(*len)] == '#') {
        (*len)++;
        return NULL;
    }

    root = node(atoi(data+(*len)));
    while(data[*len]!='*')
        (*len)++;
    (*len)++;
    root->left = helper(data,len);
    root->right = helper(data,len);

    return root;
}

/** Decodes your encoded data to tree. */
struct TreeNode* deserialize(char* data) {
    int len=0;

    if(data == NULL)
        return NULL;

    return helper(data,&len);
}

// Your functions will be called as such:
// char* data = serialize(root);
// deserialize(data);
```

**Solution 4: (DFS)**

            1
          /    \
        2        3
               /   \
              4     5
            

serialize:     1,2,,,3,4,,,5,,,
               0   1   2   3   4   5   6   7   8   9  10
dp:            1   2  ""  ""   3   4  ""   ""  5  ""  ""
                   i

                1
              /   \
            2       3
          /   \    /  \
         x     x  4    5
                 / \  /  \
                 x x  x  x
```
Runtime: 37 ms, Beats 19.08%
Memory: 44.72 MB, Beats 15.39%
```
```c++
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

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (!root) {
            return ",";
        }
        return to_string(root->val) + "," + serialize(root->left) + serialize(root->right);
    }

    TreeNode *dfs(int &i, vector<string> &dp) {
        if (dp[i] == "") {
            i += 1;
            return nullptr;
        }
        TreeNode *node = new TreeNode(stoi(dp[i]));
        i += 1;
        node->left = dfs(i, dp);
        node->right = dfs(i, dp);
        return node;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        stringstream ss(data);
        string s;
        vector<string> dp;
        int i = 0;
        while (getline(ss, s, ',')) {
            dp.push_back(s);
        }
        return dfs(i, dp);
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));
/*
```
