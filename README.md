# Algorithms Lab Experiments

## Exp 1: Merge Sort

**File:** `exp1_merge_sort.py`

**Example run:**

```
Enter array elements (space separated): 38 27 43 3 9 82 10
Original array: [38, 27, 43, 3, 9, 82, 10]
Sorted array  : [3, 9, 10, 27, 38, 43, 82]
```

## Exp 2: Hash Function

**File:** `exp2_hash_function.py`

**Example run:**

```
Enter table size M: 10
Enter number of keys: 4
Enter key: 25
  hash(25) = 5
Enter key: hello
  hash('hello') = 2
Enter key: 7
  hash(7) = 7
Enter key: world
  hash('world') = 2

Hash table:
  [0] -> []
  [1] -> []
  [2] -> ['hello', 'world']
  [3] -> []
  [4] -> []
  [5] -> [25]
  [6] -> []
  [7] -> [7]
  [8] -> []
  [9] -> []
```

## Exp 3: Binary Tree Traversals

**File:** `exp3_tree_traversals.py`

**Example run:**

```
Enter the root node:
Enter data (-1 for no node): 1
Enter left child of 1
Enter data (-1 for no node): 2
Enter left child of 2
Enter data (-1 for no node): 4
Enter left child of 4
Enter data (-1 for no node): -1
Enter right child of 4
Enter data (-1 for no node): -1
Enter right child of 2
Enter data (-1 for no node): 5
Enter left child of 5
Enter data (-1 for no node): -1
Enter right child of 5
Enter data (-1 for no node): -1
Enter right child of 1
Enter data (-1 for no node): 3
Enter left child of 3
Enter data (-1 for no node): -1
Enter right child of 3
Enter data (-1 for no node): -1

Pre-order  traversal: 1 2 4 5 3 
In-order   traversal: 4 2 5 1 3 
Post-order traversal: 4 5 2 3 1 
```

## Exp 4: Binary Tree Traversals and Search

**File:** `exp4_tree_search.py`

**Example run:**

```
Enter the root node:
Enter data (-1 for no node): 1
Enter left child of 1
Enter data (-1 for no node): 2
Enter left child of 2
Enter data (-1 for no node): 4
Enter left child of 4
Enter data (-1 for no node): -1
Enter right child of 4
Enter data (-1 for no node): -1
Enter right child of 2
Enter data (-1 for no node): 5
Enter left child of 5
Enter data (-1 for no node): -1
Enter right child of 5
Enter data (-1 for no node): -1
Enter right child of 1
Enter data (-1 for no node): 3
Enter left child of 3
Enter data (-1 for no node): -1
Enter right child of 3
Enter data (-1 for no node): -1

Pre-order  traversal: 1 2 4 5 3 
In-order   traversal: 4 2 5 1 3 
Post-order traversal: 4 5 2 3 1 

Enter key to search: 5
Key 5 FOUND in the tree.
```

## Exp 5: Breadth First Search (BFS)

**File:** `exp5_bfs.py`

**Example run:**

```
Enter number of vertices: 5
Enter adjacency matrix (row by row, space separated):
0 1 1 0 0
1 0 0 1 0
1 0 0 1 1
0 1 1 0 0
0 0 1 0 0
Enter start vertex: 0
BFS Traversal: 0 1 2 3 4 
```

## Exp 6: Optimal Storage on Tape

**File:** `exp6_tape_storage.py`

**Example run:**

```
Enter number of files: 3
Enter length of file 1: 5
Enter length of file 2: 10
Enter length of file 3: 3
Optimal order          : [3, 5, 10]
Total Retrieval Time   : 29
Average Retrieval Time : 9.67
```

## Exp 7: Prim's Algorithm (Minimum Spanning Tree)

**File:** `exp7_prims_mst.py`

**Example run:**

```
Enter number of vertices: 5
Enter weighted adjacency matrix (0 = no edge):
0 2 0 6 0
2 0 3 8 5
0 3 0 0 7
6 8 0 0 9
0 5 7 9 0
Edge 	Weight
0 - 1 	2
1 - 2 	3
0 - 3 	6
1 - 4 	5
Total weight of MST: 16
```

## Exp 8: Longest Common Subsequence (LCS)

**File:** `exp8_lcs.py`

**Example run:**

```
Enter first string : AGGTAB
Enter second string: GXTXAYB
Length of LCS: 4
LCS          : GTAB
```

## Exp 10: Floyd-Warshall Algorithm

**File:** `exp10_floyd_warshall.py`

**Example run:**

```
Enter number of vertices: 4
Enter adjacency matrix (use INF for no edge):
0 3 INF 7
8 0 2 INF
5 INF 0 1
2 INF INF 0
Shortest distance matrix:
   0    3    5    6
   5    0    2    3
   3    6    0    1
   2    5    7    0
```
