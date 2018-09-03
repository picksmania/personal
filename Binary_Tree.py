#Binary Tree's Insertion and traversal

class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


    def preorder(self,i=0):
        print "Level::%s Value::%s"%(i,self.data)
        if self.left:
            self.left.preorder(i=i+1)
        if self.right:
            self.right.preorder(i=1+1)


    def postorder(self,i=0):
        if self.left:
            self.left.postorder(i=i+1)
        if self.right:
            self.right.postorder(i=i+1)
        print "Level::%s Value::%s"%(i,self.data)


    def inorder(self,i=0):
        if self.data:
            if self.left:
                self.left.inorder(i=i+1)
            print "Level::%s Value::%s"%(i,self.data)
            if self.right:
                self.right.inorder(i=i+1)

    """ Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
    """
    def height(self,node):
        if node is None:
            return 0
        else:
            # Compute the height of each subtree
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            #Use the larger one
            if lheight > rheight :
                print "lehight::",lheight+1
                return lheight+1
            else:
                print "rheight::",rheight+1
                return rheight+1




c = Node(1)
c.left = Node(2)
c.right = Node(3)
c.left.left = Node(4)
c.left.right = Node(5)

print "*************PREORDER*************"
c.preorder()
print "*************POSTORDER*************"
c.postorder()
print "*************INORDER*************"
c.inorder()
print "*************HEIGHT*************"
c.height(c)

# =============================== END ========================

'''
# Binary Search Tree

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

    def get(self):
        return self.val


# A utility function to insert a new node with the given key

def insert(root,node):
    if root is None:
        root = node
    else:
        # print "ROOT VAL::",r.val
        # print "NODE VAL::",node.values
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

# A utility function to do inorder tree traversal
def inorder(root,i=0):
    if root:
        inorder(root.left,i=i+1)
        print "Level::%s Value::%s"%(i,root.val)
        inorder(root.right,i=1+1)

# A utility function to do preorder tree traversal
def preorder(root,i=0):
    print "Level::%s Value::%s"%(i,root.val)
    if root.left:
        preorder(root.left,i=i+1)
    if root.right:
        preorder(root.right,i=1+1)

# A utility function to do postorder tree traversal
def postorder(root,i=0):

    if root.left:
        postorder(root.left,i=i+1)
    if root.right:
        postorder(root.right,i=1+1)
    print "Level::%s Value::%s"%(i,root.val)

# A utility function to do SEARCH of NODE in a given tree
def lookup(root, data, parent=None):
    """
    Lookup node containing data
    @param data node data object to look up
    @param parent node's parent
    @returns node and node's parent if found or None, None
    """

    try:
        if data < root.val:
            if root.left is None:
                return None, None
            return lookup(root.left,data, root.val)
        elif data > root.val:
            if root.right is None:
                return None, None
            return lookup(root.right,data, root.val)
        else:
            return root.val, parent
    except Exception as e:
        print e


def child_count(root):
    count=0
    lchild=0
    rchild=0
    if root.left:
        child_count(root.left)
        count+=1
        lchild+=1
    if root.right:
        child_count(root.right)
        count+=1
        rchild+=1
    print count,lchild,rchild
    return count,lchild,rchild

r = Node(50)
#print r.get()

insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))
# print r.get()
insert(r,Node(-2))
# insert(r,Node(2))

node,parent = lookup(r,70)
print "SEARCHD NODE is::: %s and PARENT NODE of SEARCHED NODE is ::: %s"%(node, parent)


print "******* IN-ORDER ****************"
inorder(r)
print "================================"
print "******* PRE-ORDER ****************"
preorder(r)
print "================================"
print "******* POST-ORDER ****************"
postorder(r)

child_count(r)

'''