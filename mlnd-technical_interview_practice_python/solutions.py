""" 
Question1:
Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.
 """
def question1(s, t):
    pos1 = 0
    found = 0
    target = len(t)
    list_t = list(t)
    while pos1 < len(s):
        pos2 = 0
        while pos2 < len(t):
            if s[pos1] == list_t[pos2]:
                found += 1
                list_t[pos2] = None
                break
            pos2 += 1
        pos1 += 1
    

    if target != 0 and found == target:
        return True
    else:
        return False

""" 
Test Case 1: ("udacity", "ad")
 """
print question1("udacity", "ad")
# True

""" 
Test Case 2: ("udacity", "")
 """
print question1("udacity", "")
# False

""" 
Test Case 3: ("udacity", "ada")
 """
print question1("udacity", "ada")
# False


""" 
Question2:
Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), and return a string.
 """
def question2(a):
    n = len(a)
    palindrom_begin_at = 0
    max_len = 0
    palindrom = [[0 for x in range(n)] for y in range(n)]

    # trivial case: single letter palindroms
    for i in range(n):
        palindrom[i][i] = True
        max_len = 1

    # finding palindroms of 2 characters
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            palindrom[i][i + 1] = True
            palindrom_begin_at = i
            max_len = 2

    # finding palindroms of length 3 to n and saving the longest
    for cur_len in range(3, n+1):
        for i in range(n - cur_len + 1):
            j = i + cur_len - 1

            # the first last character should match
            # and rest of the substring should be a palindrom
            if a[i] == a[j] and palindrom[i + 1][j - 1] == True: 
                palindrom[i][j] = True
                palindrom_begin_at = i
                max_len = cur_len


    if max_len > 1:
        return a[palindrom_begin_at:max_len]
    else:
        return ""

""" 
Test Case 1: BANANA
 """
print question2("BANANA")
# output: ANAN

""" 
Test Case 2: ABCD
 """
print question2("ABCD")
# output: 

""" 
Test Case 3: forgeeksskeegfor
 """
print question2("forgeeksskeegfor")
# output: geekssk


""" 
Question3:
Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree 
connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}

Vertices are represented as unique strings. The function definition should be question3(G)
 """

# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected, 
# undirected and weighted graph
 
from collections import defaultdict
 
#Class to represent a graph
class Graph:
 
    def __init__(self):
        self.V= 0 #No. of vertices
        self.vertices = set()
        self.graph = [] # default dictionary 
                                # to store graph
  
    # function to add an edge to graph
    def addEdge(self,u,v,w):
        self.graph.append([u, v, w])
        self.vertices.add(u)
        self.vertices.add(v)
        self.V = len(self.vertices)
 
    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == -1:
            return i
        return self.find(parent, parent[i])
 
    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        # Attach smaller rank tree under root of 
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
 
        # If ranks are same, then make one as root 
        # and increment its rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1
 
    # The main function to construct MST using Kruskal's 
        # algorithm
    def KruskalMST(self):
 
        result = defaultdict(list) #This will store the resultant MST
 
        i = 0 # An index variable, used for sorted edges
        e = 0 # An index variable, used for result[]
 
        # Step 1:  Sort all the edges in non-decreasing 
        # order of their
        # weight.  If we are not allowed to change the 
        # given graph, we can create a copy of graph
        self.graph = sorted(self.graph, key=lambda item: item[2])
        
        parent = defaultdict(int)
        rank = defaultdict(int)
        for j in self.vertices:
            parent[j] = -1
            rank[j] = 0

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1 :
 
            # Step 2: Pick the smallest edge and increment 
            # the index for next iteration
            u, v, w =  self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)

            # If including this edge does't cause cycle, 
            # include it in result and increment the index
            # of result for next edge
            if x != y:
                e = e + 1    
                result[u].append([v, w])
                self.union(parent, rank, x, y)            
            # Else discard the edge

        # print the contents of result[] to display the built MST
        # print "Following are the edges in the constructed MST"
        return dict(result)

def question3(G):
    return G.KruskalMST()

""" 
Test Case 1:

            6
       A ------ C
   10 /  \ 5  / 4  
    /     \  /
  B ------- D
      15
 """    
G = Graph()
G.addEdge('A', 'B', 10)
G.addEdge('A', 'C', 6)
G.addEdge('A', 'D', 5)
G.addEdge('B', 'D', 15)
G.addEdge('C', 'D', 4)
print question3(G)
# output: {'A': [['D', 5], ['B', 10]], 'C': [['D', 4]]}

""" 
Test Case 2:

"""
G = Graph()
print question3(G)
# output: {}

""" 
Test Case 3:

             8       7
         B ----- C ----- D
     4  /|     2 | \     |  \ 9
      /  |       |  \ 4  |    \
    A    | 11    I   \   | 14  E
      \  |    /  | 6  \  |    /
     8 \ |  / 7  |     \ |  / 10
         H ----- G ----- F
             1       2
"""
G = Graph()
G.addEdge('A', 'B', 4)
G.addEdge('A', 'H', 8)
G.addEdge('B', 'H', 11)
G.addEdge('B', 'C', 8)
G.addEdge('C', 'I', 2)
G.addEdge('H', 'I', 7)
G.addEdge('G', 'I', 6)
G.addEdge('G', 'H', 1)
G.addEdge('C', 'D', 7)
G.addEdge('D', 'F', 14)
G.addEdge('C', 'F', 4)
G.addEdge('F', 'G', 2)
G.addEdge('D', 'E', 9)
G.addEdge('E', 'F', 10)
print question3(G)
# output {'A': [['B', 4], ['H', 8]], 'C': [['I', 2], ['F', 4], ['D', 7]], 'D': [['E', 9]], 'G': [['H', 1]], 'F': [['G', 2]]}


""" 
Question4:
Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)

and the answer would be 3.
 """
def getParent(T, n):
    for row in range(len(T)):
        if T[row][n] == 1:
             return row
    return -1

def question4(T, r, n1, n2):
    lca = []
    p = None
    while p != r:
        p = getParent(T, n1)
        if p < 0:
            return 'NO LEAST COMMON ANCESTOR!!!'
        
        if p >= n1:
            lca.append(p)
        n1 = p

    p = None
    while p != r:
        p = getParent(T, n2)

        if p < 0:
            return 'NO LEAST COMMON ANCESTOR!!!'

        if p <= n2:
            for i in range(len(lca)):
                if p == lca[i]:
                    return p
        n2 = p
    
    return 'NO LEAST COMMON ANCESTOR!!!'

""" 
Test Case 1:

        3        2
      /   \
    0      4
     \
       1
 """
print question4([[0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]],
                3,
                1,
                4)
# output: 3

""" 
Test Case 2:

        3        2
      /   \
    0      4
     \
       1
 """
print question4([[0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]],
                3,
                1,
                2)
# output: NO LEAST COMMON ANCESTOR!!!

"""
Test Case 3:

                   10
                 /    \
               /        \
             /            \
           /                \
          5                  15
        /   \               /   \
      2       7           /       \
     / \     / \         12        18 
    1   4   6   8       /  \       /  \
   /   /         \    11   13    17   19
  0   3           9          \   /       \
                             14 16        20
 """
print question4([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # node 0
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # node 1
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # node 2
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # node 3
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # node 4
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # node 5
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # node 6
                [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # node 7
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # node 8
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # node 9
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],   # node 10
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # node 11
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],   # node 12
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],   # node 13
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # node 14
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],   # node 15
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # node 16
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],   # node 17
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],   # node 18
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   # node 19
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],   # node 20        
                10,
                9,
                16)
# output: 10


""" 
Question5:
Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
 """
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

def question5(ll, m):
    data = []
    current = ll.head
    while current:
        data.append(current.data)
        current = current.next
    
    if m > len(data):
        return 'ERROR: OUT OF RANGE!!!'
    else:
        return data[-m]

""" 
Test Case 1:

1 -> 2 -> 3 -> 4 -> 5 -> None
 """
node = Node(1)
ll = LinkedList(node)
node = Node(2)
ll.append(node)
node = Node(3)
ll.append(node)
node = Node(4)
ll.append(node)
node = Node(5)
ll.append(node)
    
print question5(ll, 3)
# output: 3

""" 
Test Case 2:

1 -> None
 """
node = Node(1)
ll = LinkedList(node)
    
print question5(ll, 2)
# output: 3

""" 
Test Case 3:

2 -> 1 -> 0 -> -1 -> -2 -> -3 -> -4 -> -5 -> -6 -> -7 -> None
 """
node = Node(2)
ll = LinkedList(node)
node = Node(1)
ll.append(node)
node = Node(0)
ll.append(node)
node = Node(-1)
ll.append(node)
node = Node(-2)
ll.append(node)
node = Node(-3)
ll.append(node)
node = Node(-4)
ll.append(node)
node = Node(-5)
ll.append(node)    
print question5(ll, 5)
# output: -1
