# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 11:16:39 2015

@author: Rohan Koodli
"""

            
            
class Tree(object):#Version 2
    """
    Tree Node
    """
    def __init__(self, name='Aves', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self, level=0): #Makes printable representation of Tree
        ret = "\t"*level+repr(self.name)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret

    def add_child(self, node):
        """
        Adds node
        :param node: node to be added
        :return: void
        """
        self.children.append(node)

    def disp_tree(self):
        """
        Duplicate method of printing tree
        :return: Printable representation of a tree
        """

        if self is not None:
            print (self.name)
            for child in self.children:
                #print '---'
                if child is not None:
                    print ('\t', child.disp_tree())

    def disp_tree_v2(self,level=0):
        if self is not None:
            print (self.name)
            ret = '\t'*level
            for child in self.children:
                if child is not None:
                    print (child.disp_tree(level+1))

    def iterate(self):
        for i in self.name:
            print (i)
                    

'''                  
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
'''

def treefromFile(source):
    """
    Reads tree from a TXT file
    :param source: path
    :return: void
    """
    source.replace(',','')
    source = source.split() #Puts words in list
    root = Tree('Aves')
    temp = root
    for i in range(len(source)):
        temp2 = Tree(source[i])
        temp.add_child(temp2)
        temp = temp2
        
    return root


def merge_trees(tree1,tree2):
    """
    Merge 2 trees together
    :param tree1: Tree 1
    :param tree2: Tree 2
    :return: void
    """
    if (tree1 is not None) and (tree2 is not None):
        mergedTree = Tree('Aves') #root node
        mergedRoot = mergedTree
        flag = True
        iter1 = tree1.children
        iter2 = tree2.children
        #print 'Start with appending tree1 as is..'
        append_trees(mergedTree, iter1)

        child_iter = iter1
        while iter1 and iter2:
            i = 0            

            children_name_list = []
            for k in range(len(child_iter)):
                #print 'k =',k
                # Make the list of all the names of child_iter
                children_name_list.append(child_iter[k].name)
                
            #print 'List of children:', children_name_list
            
            if iter2[0].name in children_name_list:
                i = children_name_list.index(iter2[0].name)
                #print' Found a match:', child_iter[i].name, iter2[0].name
                #print "So far so good."
                mergedTree =  child_iter[i]
                child_iter = child_iter[i].children #moving iter to next node
                iter2 = iter2[0].children
                #print 'resetting: Iter2[0]',iter2[0].name
                
            else:
                #print 'child_iter', child_iter
                flag = False
                #print 'break out of while loop'           
                break
            iter1 = child_iter
        if flag == False:
            #print 'i, child_iter:',i,child_iter, 'Iter2',iter2
            temp2 = Tree(iter2[0].name)
            #print 'Adding child to mergedTree:', iter2[0].name
            mergedTree.add_child(temp2)
            append_trees(temp2,iter2[0].children)
            #print 'mergedTree.name: ',mergedTree.name
           
        return mergedRoot   
        
def append_trees(parent_tree,tree_children):
    """
    Adds 2 trees together
    :param parent_tree: Parent tree
    :param tree_children: Child tree
    :return: void
    """
    if tree_children:
        for j in range(len(tree_children)):
            #print 'j,tree_children[]: ',j, tree_children[j].name
            parent_tree.add_child(tree_children[j])
        parent_tree = parent_tree.children[0]
        tree_children = tree_children[0].children  
#First version of append_trees


def compare_node(parent_node,child_node): #parent and child are Tree objects
    """
    Compares 2 nodes
    :param parent_node: Node 1
    :param child_node: Node 2
    :return: Difference
    """
    differences = []
    parent = parent_node.name
    child_node = parent_node.children[0]
    child = child_node.name
    if len(parent) > len(child):
        for i in range(len(child)):
            if parent[i] != child[i]:
                differences.append(i)
        for k in range(i+1,len(parent)):
            differences.append(k)
        
    else:
        for i in range(len(parent)):
            if parent[i] != child[i]:
                differences.append(i)
        for k in range(i+1,len(child)):
            differences.append(k)

    print (len(differences))
    
def compare_strains(s1,s2):#both type bio.seq.seq
    differences = []
    if len(s1) < len(s2):
        pass
    #not finished yet

'''
def append_trees_v0(parent_tree ,tree_children):
    #parent_tree is a Tree and tree_children is a list
    tempvar1 = parent_tree
    tempvar2 = Tree(tree_children[0].name)
    #print type(tempvar1)
    while tree_children:
        #print type(tempvar1)
        #parent_tree.disp_tree()
        print 'separated node tree:'
        parent_tree.disp_tree()
        print '------END----------'
        parent_tree.add_child(tree_children[0])
        print 'parent_tree: ',parent_tree
        print 'inside append_trees: ',tree_children[0].name
        parent_tree = parent_tree.children[0]
        tree_children = tree_children[0].children
        #tempvar2 = tempvar2.children

def append_trees_v0(parent_tree,tree_children):
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
        print 'inside append_trees: ',tree_children[0].name
        parent_tree = parent_tree.children[0]
        tree_children = tree_children[0].children
        #tempvar2 = tempvar2.children
       
     
  
def merge_trees_alpha(tree1,tree2):
    if (tree1 is not None) and (tree2 is not None):
        mergedTree = Tree('Aves_Merged') #root node
        mergedRoot = mergedTree
        flag = True
        iter1 = tree1.children
        iter2 = tree2.children
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
  
    

def merge_trees_beta(tree1,tree2):
    print '[[[[[[[Inside v2]]]]]]]]]'
    #qwerty = input('Enter a key ')
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
        child_iter = iter1
        while  iter1 and iter2:
            #qwerty = raw_input('Enter a key a ')
            i = 0            
            print 'iter1:', iter1, 'iter2:', iter2
            #qwerty = raw_input('Enter a key b ')            
            #if child_iter[i].name == iter2[0].name:
            print 'No.of children is: ', len(child_iter)
            #while i < len(child_iter):
            children_name_list = []
            #print 'type-of--children-list----------',type(children_name_list)
            for k in range(len(child_iter)):
                print 'k =',k
                # Make the list of all the names of child_iter
                children_name_list.append(child_iter[k].name)
                
            print 'List of children:', children_name_list
            
            #qwerty = raw_input('Enter a key d ')
            if iter2[0].name in children_name_list:
                print' Comparing:', child_iter[i].name, iter2[0].name
                #if child_iter[i].name == iter2[0].name:
                i = children_name_list.index(iter2[0].name)
                print "So far so good."
                print 'child_iter[%s]'%i,child_iter[i].name, 'Iter2[0]',iter2[0].name
                temp = Tree(child_iter[i].name)
                mergedTree.add_child(temp)
                child_iter = child_iter[i].children #moving iter to next node
                iter2 = iter2[0].children
                mergedTree = temp
                #print 'resetting: child_iter',child_iter[i].name
                print 'resetting: Iter2[0]',iter2[0].name
                #qwerty = raw_input('Enter a key e ')
                
            else:
                child_iter = iter1
                print 'child_iter', child_iter
                flag = False
                print 'trying to break out of while loop'
                #qwerty = input('Enter a key c ')
                #qwerty = raw_input('Enter a key f ')
                break
            #i += 1
            iter1 = child_iter
        if flag == False:
            print 'i, child_iter:',i,child_iter, 'Iter2',iter2
            for k in range(len(child_iter)):
                temp1 = Tree(child_iter[k].name)
                mergedTree.add_child(temp1)
                print 'Adding child to mergedTree:', child_iter[k].name
                append_trees(temp1,child_iter[k].children)
            temp2 = Tree(iter2[0].name)
            print 'Adding child to mergedTree:', iter2[0].name
            mergedTree.add_child(temp2)
            append_trees(temp2,iter2[0].children)
            print 'mergedTree.name: ',mergedTree.name
            #print 'temp1: ',temp1

        return mergedRoot    
'''

