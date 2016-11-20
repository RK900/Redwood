# Redwood
[![Github release](https://img.shields.io/badge/release-v0.1-brightgreen.svg)](https://github.com/RK900/Redwood/releases)
[![Python27](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/download/releases/2.7/)
[![License](https://img.shields.io/cocoapods/l/EasyQL.svg?style=flat)](https://github.com/RK900/Redwood/blob/master/LICENSE.txt)
[![Twitter](https://img.shields.io/badge/twitter-@RohanKoodli-blue.svg?style=flat)](http://twitter.com/RohanKoodli)

Dealing with tree data types in Python. Functions include reading trees from files, creating trees, adding trees, merging trees, and writing trees.

###License
Redwood is available under the [MIT License](https://github.com/RK900/Redwood/blob/master/LICENSE.txt).

## To use
Clone/download the repository.

###Making a Simple Tree
```python
from Redwood import Tree

tree1 = Tree('this is the root node')
tree1.add_child('left node')
tree1.add_child('right node')
```

###Appending Trees
```python
from Redwood import Tree
from Redwood import append_trees

A = Tree('A')
A.add_child('B')
A.add_child('C')

X = Tree('X')
X.add_child('Y')

newTree = append_trees(A,X)

The result:
    A
  /   \
B       C
          \
            X
              \
                Y
```
###Merging Trees
This function merges trees at the highest shared node.
```python
from Redwood import Tree
from Redwood import merge_trees

tree1 = Tree('A')
B = A.add_child('B')
C = A.add_child('C')
D = C.add_child('D')

tree2 = Tree('C')
E = tree2.add_child('E')
F = E.add_child('F')
G = E.add_child('G')

newTree = merge_trees(A,X)

The result:
    A
  /   \
B       C
      /   \
     D      E
           /  \
          G     F

```
Note: Redwood is not binary. Nodes can have multiple branches.
