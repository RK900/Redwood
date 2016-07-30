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

##
Note: Redwood is not binary. Nodes can have multiple branches.
