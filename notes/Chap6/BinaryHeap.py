class BinaryHeap:
    def __init__(self):
        self.heapList = [0] # 二叉堆编号从 1 开始
        self.size = 0

    def percUp(self, i):
        while i > 1:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i //= 2
    def insert(self, key):
        self.heapList.append(key)
        self.size += 1
        self.percUp(self.size)

    def percDown(self, i):
        def getMinChild(i):
            if i * 2 + 1 > self.size:
                return i * 2
            else:
                if self.heapList[i*2] < self.heapList[i*2+1]:
                    return i * 2
                else:
                    return i * 2 + 1
        while (i * 2) <= self.size:
            minChild = getMinChild(i)
            if self.heapList[i] > self.heapList[minChild]:
                self.heapList[i], self.heapList[minChild] = self.heapList[minChild], self.heapList[i]
            i = minChild
    def delMin(self):
        minKey = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.size -= 1
        self.heapList.pop()
        self.percDown(1)
        return minKey
    
    def buildHeap(self, lst):
        i = len(lst) // 2
        self.size = len(lst)
        self.heapList = [0] + lst[:]
        while i > 0:
            self.percDown(i)
            i -= 1
    
