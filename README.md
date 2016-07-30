# Redwood

This repo contains files that make tree data types in Python. Functions include reading trees from files, creating trees, adding trees, merging trees, and writing trees.

###License
MIT

#To use
Clone/download the repository.

##Making a Simple Tree
```python
from Redwood import Tree
tree1 = Tree('this is the root node')
tree1.add_child('left node')
tree1.add_child('right node')
```

##Merging Trees
```python
from Redwood import Tree
from Redwood import append_trees
A = Tree('A')
A.add_child('B')
A.add_child('C')

X = Tree('X')
X.add_child('Y')

newTree = append_trees(A,X)
```
The result:
    A
  /   \
B       C
           \
            X
              \
                Y
Note: Redwood is not binary. Nodes can have multiple branches.
