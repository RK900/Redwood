# -*- coding: utf-8 -*-
"""
Created on Sat Jan 02 12:38:07 2016

@author: Rohan Koodli
"""

class Tree(object):
    "Generic tree node."
    def __init__(self, name='Aves', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
    def disp_tree(self):
        if self is not None:
            print self.name
            for child in self.children:
                if child is not None:
                    child.disp_tree()
                    
                    
                    


                    
#Tree("Root", [Tree("1")])
Root_node = Tree("This is the Root")
node1 = Tree("1")
node2 = Tree("2")
node21= Tree("2.1")
node3 = Tree("3")
Root_node.add_child(node1)
node1.add_child(node2)
node1.add_child(node21)
node2.add_child(node3)
#Root_node.disp_tree()
#print "The End"


def treefromFile(source):
    source.replace(',','')
    source = source.split() #Puts words in list
    root = Tree('Aves')
    temp = root
    for i in range(len(source)):
        temp2 = Tree(source[i])
        temp.add_child(temp2)
        temp = temp2
        
    return root


def append_trees(parent_tree,tree_children):
    #parent_tree is a Tree and tree_children is a list
    #print type(tempvar1)
    if tree_children:
        #print type(tempvar1)
        #parent_tree.disp_tree()
        #print 'separated node tree:'
        #parent_tree.disp_tree()
        #print '------END----------'
        parent_tree.add_child(tree_children[0])
        #print 'parent_tree: ',parent_tree
        #print 'inside append_trees: ',tree_children[0].name
        parent_tree = parent_tree.children[0]
        tree_children = tree_children[0].children
        #tempvar2 = tempvar2.children
  
def merge_trees(tree1,tree2):
    if (tree1 is not None) and (tree2 is not None):
        mergedTree = Tree('Aves_Merged') #root node
        mergedRoot = mergedTree
        flag = True
        iter1 = tree1.children
        iter2 = tree2.children
        #mergedTree = mergedTree.children
        #print (iter1)
        #print (iter2)
        # go thru each level of the tree
        while  iter1 and iter2:
            if iter1[0].name == iter2[0].name:
                #print "So far so good."
                #print 'Iter1[0]',iter1[0].name, 'Iter2[0]',iter2[0].name
                temp = Tree(iter1[0].name)
                mergedTree.add_child(temp)
                iter1 = iter1[0].children #moving iter to next node
                iter2 = iter2[0].children
                mergedTree = temp
                #print 'resetting: Iter1[0]',iter1[0].name, 'resetting: Iter2[0]',iter2[0].name
                continue
            else:
                flag = False
                temp1 = Tree(iter1[0].name)
                temp2 = Tree(iter2[0].name)
                mergedTree.add_child(temp1)
                mergedTree.add_child(temp2)
                #print 'mergedTree.name: ',mergedTree.name
                #print 'temp1: ',temp1
                break
        if flag == False:
            #print "Trees differ"
            #print 'now appending temp1'
            append_trees(temp1,iter1[0].children)
            #print 'tree 1: '
            #temp1.disp_tree()
            
            #print 'now appending temp2'
            append_trees(temp2,iter2[0].children)
            #print 'printting tree2'
            #temp2.disp_tree()
            #print 'end'
             
        else:
            print 'Trees are same'
        
        return mergedRoot
  
    