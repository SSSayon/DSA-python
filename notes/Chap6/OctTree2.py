from PIL import Image
import sys
import heapq

class OctTree:
    def __init__(self):
        self.root = None
        self.maxLevel = 5
        self.numLeaves = 0
        self.heap = []

    def insert(self, r, g, b):
        if not self.root:
            self.root = self.otNode(outer=self)
        self.root.insert(r, g, b, 0, self)

    def find(self, r, g, b):
        if self.root:
            return self.root.find(r, g, b, 0)

    def reduce(self, maxCubes):
        while len(self.heap) > maxCubes:
            smallest = self.findMinCube()
            smallest.parent.merge()
            heapq.heappush(self.heap, smallest.parent)
            self.numLeaves += 1

    def findMinCube(self):
        return heapq.heappop(self.heap)

    class otNode:
        def __init__(self, parent=None, level=0, outer=None):
            self.red = 0
            self.green = 0
            self.blue = 0
            self.count = 0
            self.parent = parent
            self.level = level
            self.oTree = outer
            self.children = [None] * 8

        def insert(self, r, g, b, level, outer):
            if level < self.oTree.maxLevel:
                idx = self.computeIndex(r, g, b, level)
                if self.children[idx] is None:
                    self.children[idx] = outer.otNode(parent=self, level=level+1, outer=outer)
                self.children[idx].insert(r, g, b, level+1, outer)
            else:
                if self.count == 0:
                    self.oTree.numLeaves += 1
                    heapq.heappush(self.oTree.heap, self)
                self.red += r
                self.green += g
                self.blue += b
                self.count += 1

        def computeIndex(self, r, g, b, level):
            shift = 8 - level
            rc = (r >> (shift - 2)) & 0x4
            gc = (g >> (shift - 1)) & 0x2
            bc = (b >> shift) & 0x1
            return rc | gc | bc

        def find(self, r, g, b, level):
            if level < self.oTree.maxLevel:
                idx = self.computeIndex(r, g, b, level)
                if self.children[idx]:
                    return self.children[idx].find(r, g, b, level + 1)
                elif self.count > 0:
                    return self.getAverageColor()
                else:
                    print("error: No leaf node for this color")
            else:
                return self.getAverageColor()

        def merge(self):
            for i in self.children:
                if i:
                    if i.count == 0:
                        self.oTree.numLeaves -= 1
                        self.oTree.heap.remove(i)
                        heapq.heapify(self.oTree.heap)
                    else:
                        i.merge()
                    self.count += i.count
                    self.red += i.red
                    self.green += i.green
                    self.blue += i.blue
            for i in range(8):
                self.children[i] = None

        def getAverageColor(self):
            return self.red // self.count, self.green // self.count, self.blue // self.count
    
        def __lt__(self, other):
            return self.count < other.count

def buildAndDisplay():
    im = Image.open('Path_of_the_file')
    w, h = im.size
    ot = OctTree()

    for row in range(0, h):
        for col in range(0, w):
            r, g, b = im.getpixel((col, row))
            ot.insert(r, g, b)

    ot.reduce(256)

    for row in range(0, h):
        for col in range(0, w):
            r, g, b = im.getpixel((col, row))
            nr, ng, nb = ot.find(r, g, b)
            im.putpixel((col, row), (nr, ng, nb))

    im.save('Path_to_save')

buildAndDisplay()
