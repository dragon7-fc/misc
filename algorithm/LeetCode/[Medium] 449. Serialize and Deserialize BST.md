449. Serialize and Deserialize BST

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a **binary search tree** can be serialized to a string and this string can be deserialized to the original tree structure.

**The encoded string should be as compact as possible.**

**Note:** Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

# Submissions
---
**Solution 1: (DFS, Queue)**
```
Runtime: 56 ms
Memory Usage: 17.4 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        def dfs(node):
            nonlocal res
            if not node:
                res += ['null']
                return 
            res += [str(node.val)]
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        res = ','.join(res)
        return res

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        q = collections.deque(data.split(','))
        def dfs(data_list):
            if data_list[0] == 'null':
                data_list.popleft()
                return None
            node = TreeNode(int(data_list[0]))
            data_list.popleft()
            node.left = dfs(data_list)
            node.right = dfs(data_list)
            return node
            
        root = dfs(q)    
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```

**Solution 2: (DFS, String)**
```
Runtime: 64 ms
Memory Usage: 18.2 MB
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        rst = ''
        def dfs(node):
            nonlocal rst
            if not node:
                rst += 'N'
                return
            else:
                rst += '[' + str(node.val)
                dfs(node.left)
                dfs(node.right)
                rst += ']'
        dfs(root)
        return rst

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        N = len(data)
        if N == 1: return
        
        def dfs(i):
            if i < N:
                if data[i].isdigit():
                    j = i+1
                    while data[j].isdigit():
                        j += 1
                    val = int(data[i:j])
                    node = TreeNode(val)
                    node.left, j = dfs(j)
                    node.right, j = dfs(j)
                    return node, j
                elif data[i] == 'N':
                    return None, i+1
                elif data[i] == '[' or data[i] == ']':
                    return dfs(i+1)
            else:
                return None, N
        return dfs(0)[0]
        
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
```

**Solution 3: (DFS)**
```
Runtime: 59 ms
Memory Usage: 28.7 MB
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
void ser(struct TreeNode* root, char* cser){
    if(!root){
        strcat(cser, "-1/");
        return;
    }
    char tmp[6];
    sprintf(tmp, "%d/", root->val);
    strcat(cser, tmp);
    ser(root->left, cser);
    ser(root->right, cser);
    return;
    
}

void deser(struct TreeNode* root, int *v, int len, int *pos, int dir){
    if(*pos >= len || v[*pos] == -1){
        root = NULL;
        (*pos)++;
        return;
    }
    if(dir == 1)
        root = root->right = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    if(dir == -1)
        root = root->left  = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = v[(*pos)++];   
    root->right = NULL;
    root->left = NULL;
    deser(root, v, len, pos, -1);
    deser(root, v, len, pos, 1);
    return;
}

/** Encodes a tree to a single string. */
char* serialize(struct TreeNode* root) {
    char *cser = (char*)calloc(sizeof(char), 100000);
    ser(root, cser);
    return cser;
}

/** Decodes your encoded data to tree. */
struct TreeNode* deserialize(char* data) {
    struct TreeNode *new, *head = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    new = head;
    char t[2]="/", *token;
    int v[100000], i=0, pos=0;
    token = strtok(data, t);
    
    while(token!=NULL){
        v[i++] = atoi(token);
        token = strtok(NULL, t);
    }
    if(i == 1) return NULL;
    deser(head, v, i,&pos, 0);
    return new;
}

// Your functions will be called as such:
// char* data = serialize(root);
// deserialize(data);
```

**Solution 4: (BFS)**
```
Runtime: 24 ms
Memory Usage: 25.3 MB
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
        string s="";
        
        if(!root)
            return s;
        queue<TreeNode *>q;
        q.push(root);
        while(!q.empty())
        {
            TreeNode *curr=q.front();
            q.pop();
            
            if(curr==NULL)
                s.append("#,");
            else
                s.append(to_string(curr->val)+',');
            if(curr)
            {
                q.push(curr->left);
                q.push(curr->right);
            }
        }
        return s;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if(data.size()==0)
            return NULL;
        
        stringstream s(data);
        string str;
        getline(s,str,',');
        TreeNode *root=new TreeNode(stoi(str));
        queue<TreeNode *>q;
        q.push(root);
        
        while(!q.empty())
        {
            TreeNode *curr=q.front();
            q.pop();
            
            getline(s,str,',');
            if(str=="#")
            {
                curr->left=NULL;
            }
            else
            {
                TreeNode *lnode=new TreeNode(stoi(str));
                curr->left=lnode;
                q.push(curr->left);
            }
            
             getline(s,str,',');
            if(str=="#")
            {
                curr->right=NULL;
            }
            else
            {
                TreeNode *rnode=new TreeNode(stoi(str));
                curr->right=rnode;
                q.push(curr->right);
            }
            
            
        }
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec* ser = new Codec();
// Codec* deser = new Codec();
// string tree = ser->serialize(root);
// TreeNode* ans = deser->deserialize(tree);
// return ans;
```
**Solution 5: (DFS)**
```
Runtime: 31 ms
Memory: 31.81 MB
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
    TreeNode* decode(stringstream& take,string res = ""){
        getline(take,res,'#');
        if(res.empty())return NULL;
        
        TreeNode* root= new TreeNode(stoi(res));
        root->left = decode(take), root->right = decode(take);
        return root;
    }
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if(!root)return "#";
        return to_string(root->val)+"#"+serialize(root->left) + serialize(root->right);
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        stringstream take(data);
        return decode(take);
    }
};

// Your Codec object will be instantiated and called as such:
// Codec* ser = new Codec();
// Codec* deser = new Codec();
// string tree = ser->serialize(root);
// TreeNode* ans = deser->deserialize(tree);
// return ans;
```
