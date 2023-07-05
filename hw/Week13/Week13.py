# 1:二叉查找树填空
def T1():
    class Node:
        def __init__(self, key, val=None, l=None, r=None):
            self.key = key
            self.val = val
            self.leftChild = l
            self.rightChild = r
    
    def genTree(n):
        nodes = [Node(i) for i in range(n)]
        for node in nodes:
            l, r = map(int, input().split())
            if l != -1:
                node.leftChild = nodes[l]
            if r != -1:
                node.rightChild = nodes[r]
        return nodes[0]
    
    def fillTree(root: Node):
        if root:
            fillTree(root.leftChild)
            root.val = lst.pop()
            fillTree(root.rightChild)

    def printTree(n):
        queue = [root]
        res = []
        for i in range(n):
            node = queue.pop(0)
            res.append(node.val)
            if node.leftChild:
                queue.append(node.leftChild)
            if node.rightChild:
                queue.append(node.rightChild)
        print(*res, sep=' ')        

    n = int(input())
    root = genTree(n)
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    fillTree(root)
    printTree(n)

# 2:完全二叉查找树
def T2():
    class Node:
        def __init__(self, key, val=None, l=None, r=None):
            self.key = key
            self.val = val
            self.leftChild = l
            self.rightChild = r
    
    def genTree(n):
        root = Node(1)
        queue = [root]
        cnt = 1
        while cnt < n:
            node = queue.pop(0)
            if cnt + 1 < n:
                cnt += 1
                node.leftChild = Node(cnt)
                queue.append(node.leftChild)
                cnt += 1
                node.rightChild = Node(cnt)
                queue.append(node.rightChild)
            else:
                cnt += 1
                node.leftChild = Node(cnt)
        return root
    
    def fillTree(root: Node):
        if root:
            fillTree(root.leftChild)
            root.val = lst.pop()
            fillTree(root.rightChild)

    def printTree(n):
        queue = [root]
        res = []
        for i in range(n):
            node = queue.pop(0)
            res.append(node.val)
            if node.leftChild:
                queue.append(node.leftChild)
            if node.rightChild:
                queue.append(node.rightChild)
        print(*res, sep=' ')        


    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    n = len(lst)
    root = genTree(n)
    fillTree(root)
    printTree(n)

# 3:从二叉搜索树到更大和树
def T3():
    class Node:
        def __init__(self, val, l=None, r=None):
            self.val = val
            self.leftChild = l
            self.rightChild = r
        def put(self, val):
            if val < self.val:
                if self.leftChild:
                    self.leftChild.put(val)
                else:
                    self.leftChild = Node(val)
            else:
                if self.rightChild:
                    self.rightChild.put(val)
                else:
                    self.rightChild = Node(val)
    def genTree():
        root = Node(lst[0])
        for i in lst[1:]:
            root.put(i)
        return root
    def printAddedTree():
        res = []
        queue = [root]
        for _ in range(len(lst)):
            node = queue.pop(0)
            total = 0
            for i in lst:
                if i >= node.val:
                    total += i
            res.append(total)
            if node.leftChild:
                queue.append(node.leftChild)
            if node.rightChild:
                queue.append(node.rightChild)
        print(*res, sep=' ')

    lst = list(map(int, input().split()))
    root = genTree()
    printAddedTree()

if __name__ == '__main__':
    T3()