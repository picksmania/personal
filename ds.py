class BinaryTree():
    def __init__(self,rootobj):
        self.key = rootobj
        self.leftChild = None
        self.rightChild = None

    # We must consider two cases for insertion. The first case is characterized by a node with no existing left child.
    # When there is no left child, simply add a node to the tree. The second case is characterized by a node with an existing left child.
    # In the second case, we insert a node and push the existing child down one level in the tree.
    # The second case is handled by the else statement.
    #
    # The code for insertRight must consider a symmetric set of cases.
    # There will either be no right child, or we must insert the node between the root and an existing right child

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self,i=0):

        print "Level::%s Value::%s"%(i,self.key)
        if self.leftChild:
            self.leftChild.preorder(i=i+1)
        if self.rightChild:
            self.rightChild.preorder(i=1+1)

    def postorder(self,i=0):

        if self.leftChild:
            self.leftChild.postorder(i=i+1)
        if self.rightChild:
            self.rightChild.postorder(i=i+1)
        print "Level::%s Value::%s"%(i,self.key)

    def inorder(self,i=0):
        if self.key:
            if self.leftChild:
                self.leftChild.postorder(i=i+1)
                print "Level::%s Value::%s"%(i,self.key)
                self.rightChild.postorder(i=i+1)




c = BinaryTree('a')
print "1st time ROOTAVLUE :: ",c.getRootVal()
print "1st time GET LEFT CHILD::",c.getLeftChild()
print "**** INSERTING an elemnet to LEFT SIDE ****"
c.insertLeft('b')
print "after Inserting Value, calling GET LEFT CHILD:::",c.getLeftChild()
print "Calling GET ROOT VAL::",c.getRootVal()
print "After inserting LEFT CHILD, calling ROOTVALUE of LEFTCHILD::",c.getLeftChild().getRootVal()
print "calling GET RIGHT CHILD:::",c.getRightChild()
print "**** INSERTING 1st VALUE to RIGHT SIDE ****"
c.insertRight('c')
print "GET RIGHT CHILD:::",c.getRightChild()
print "GET RIGHT CHILD's ROOT VALUE::",c.getRightChild().getRootVal()
print "Setting Right Child's ROOTVALUE to HELLO...."
c.getRightChild().setRootVal('hello')
print "GET RIGHT CHILD's ROOT VALUE::",c.getRightChild().getRootVal()
print "**** INSERTING an elemnet to LEFT SIDE ****"
c.insertLeft('d')
print "After inserting LEFT CHILD, calling ROOTVALUE of LEFTCHILD::",c.getLeftChild().getRootVal()
print "calling GET LEFT CHILD:::",c.getLeftChild().getRootVal()
print "Getting Original LEFT CHILD::",c.getLeftChild().getLeftChild().getRootVal()
c.insertLeft('e')
print "*************PREORDER*************"
c.preorder()
print "*************POSTORDER*************"
c.postorder()
print "*************INORDER*************"
c.inorder()
# =======================================================================================================================



