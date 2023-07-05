import operator

class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    
class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None
    def insertLeft(self, key):
        if self.leftChild == None:
            self.leftChild = BinaryTree(key)
        else:
            t = BinaryTree(key)
            t.leftChild = self.leftChild
            self.leftChild = t
    def insertRight(self, key):
        if self.rightChild == None:
            self.rightChild = BinaryTree(key)
        else:
            t = BinaryTree(key)
            t.rightChild = self.rightChild
            self.rightChild = t
    def setRootVal(self, key):
        self.key = key
    def getLeftChild(self):
        return self.leftChild
    def getRightChild(self):
        return self.rightChild
    def getRootVal(self):
        return self.key
    
def buildParseTree(fpexp: str):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i.isdigit():
            currentTree.setRootVal(int(i))
            currentTree = pStack.pop()
        elif i in '+-*/':
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError('Unknown Operator: {}'.format(i))
    return eTree

def evalParseTree(parseTree: BinaryTree):
    oprs = {'+': operator.add, '-': operator.sub,
           '*': operator.mul, '/': operator.truediv}
    leftChild = parseTree.getLeftChild()
    rightChild = parseTree.getRightChild()
    if leftChild and rightChild:
        opr = oprs[parseTree.getRootVal()]
        return opr(evalParseTree(leftChild), evalParseTree(rightChild))
    else:
        return parseTree.getRootVal()
    
def printParseTree(parseTree: BinaryTree):
    res = ''
    if parseTree:
        if not parseTree.getLeftChild():
            res = str(parseTree.getRootVal())
        else:
            res = '( ' + printParseTree(parseTree.getLeftChild()) \
                       + ' ' + str(parseTree.getRootVal()) + ' ' \
                       + printParseTree(parseTree.getRightChild()) + ' )'
    return res

