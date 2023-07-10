# 24748:二叉树路径
def T1():
    class Node():
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.leftChild = left
            self.rightChild = right
        def insert(self, key):
            if key < self.key:
                if self.leftChild:
                    self.leftChild.insert(key)
                else:
                    self.leftChild = Node(key)
            else:
                if self.rightChild:
                    self.rightChild.insert(key)
                else:
                    self.rightChild = Node(key)

    def gen():
        root = Node(lst[0])
        for i in lst[1:]:
            root.insert(i)
        return root

    def preorder(tree: Node, path):
        path += str(tree.key)
        if not tree.leftChild and not tree.rightChild:
            res.append(path)
        else:
            path += '->'
            if tree.leftChild:
                preorder(tree.leftChild, path)
            if tree.rightChild:
                preorder(tree.rightChild, path)

    lst = list(map(int, input().split()))
    root = gen()
    res = []
    preorder(root, '')
    for path in res:
        print(path)

# 24749:面基的最多人数
def T2():
    class Vertex:
        def __init__(self, id):
            self.id = id
            self.connected_to = []
        def addNeighbor(self, nbr):
            self.connected_to.append(nbr)
        def getNeighbor(self):
            return self.connected_to

    lst = eval(input())
    n = len(lst)
    graph = [Vertex(i) for i in range(n)]
    graph_reversed = [Vertex(i) for i in range(n)]
    for i in range(n):
        graph[lst[i]].addNeighbor(i)
        graph_reversed[i].addNeighbor(lst[i])

    double_linked = []
    for i in range(n):
        v = graph[i]
        for j in v.getNeighbor():
            nbr: Vertex = graph[j]
            if i in nbr.connected_to and i < j:
                double_linked.append((i, j))

    def calc_path(x, y):
        if len(graph[x].getNeighbor()) == 0:
            return 0
        else:
            return max([calc_path(c, x)+1 for c in graph[x].getNeighbor() if c != y], default=0)
    
    double_linked_path = []
    for i, j in double_linked:
        double_linked_path.append(2 + calc_path(i, j) + calc_path(j, i))

    if len(double_linked_path) == 1:
        ans = double_linked_path[0]
    elif len(double_linked_path) >= 2:
        double_linked_path.sort(reverse=True)
        ans = double_linked_path[0] + double_linked_path[1]
    else:
        ans = 1

    def calc_circ():
        max_length = 0
        for start in range(n):
            cur = start
            visited = set([start])
            length = 0
            while True:
                cur = graph_reversed[cur].getNeighbor()[0]
                length += 1
                if cur == start:
                    max_length = max(max_length, length)
                    break
                else:
                    if cur in visited:
                        break
                    visited.add(cur)
        return max_length
    
    ans = max(ans, calc_circ())
    print(ans)
    
# 24751:赶作业
def T3():
    from math import ceil
    n, M = map(int, input().split())
    lst = eval(input())
    k = ceil(max(lst) / (M-n+1))
    while True:
        m = sum([ceil(lst[i] / k) for i in range(n)])
        if m <= M:
            print(k)
            return
        k += 1

# 24752:斐波那契进制
def T4():
    n = int(input())
    fib = [1, 1]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])
    cnt = 0
    while n > 0:
        for i in range(len(fib) - 1, -1, -1):
            if fib[i] <= n:
                n -= fib[i]
                cnt += 1
                break
    print(cnt)

# 24753:第 K 个语法符号
def T5():
    def recursion(n, k):
        if n == 0:
            return 0
        upper = recursion(n - 1, k // 2)
        if upper == 0:
            if k % 2 == 0:
                return 0
            else:
                return 1
        else:
            if k % 2 == 0:
                return 1
            else:
                return 0
    n, k = map(int, input().split())
    print(recursion(n, k))


if __name__ == '__main__':
    T2()