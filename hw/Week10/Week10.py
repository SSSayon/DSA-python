# 1:字符串中所有重排
def T1():
    s = input()
    p = input()
    n, m = len(s), len(p)
    ans = []
    for i in range(n-m+1):
        if set(p) == set(s[i:i+m]):
            ans.append(i)
    if ans == []:
        print('none')
    else:
        print(*ans, sep=' ')

# 2:列表出现最频繁的元素
def T2():
    lst = eval(input())
    k = int(input())
    dic = {}
    for item in lst:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
    dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    print(*[x[0] for x in dic[:k]], sep=' ')

# 3:散列表
class HashTable:
    def __init__(self, size=11):
        self.size = size
        self.slots = [None] * self.size
        self.ans = []

    def put(self, key):
        hashvalue = self.hashfunction(key, self.size)

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.ans.append(hashvalue)
        else:
            if self.slots[hashvalue] == key:
                self.ans.append(hashvalue)
            else:
                times, flag = 1, True
                nextslot = self.rehash(hashvalue, times, self.size)
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    if times > self.size:
                        flag = False
                        break
                    times += 1
                    nextslot = self.rehash(hashvalue, times, self.size)
                if flag:
                    if self.slots[nextslot] == None:
                        self.slots[nextslot] = key
                    self.ans.append(nextslot)
                else:
                    self.ans.append('-')

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, times, size):
        return (oldhash + times ** 2) % size

def T3():
    from math import sqrt
    def createHashTable(n):
        if n == 1:
            return 2
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return createHashTable(n + 1)
        return n
    
    n = int(input())
    nums = list(map(int, input().split()))
    table = createHashTable(n)
    htable = HashTable(table)
    for item in nums:
        htable.put(item)
    print(*htable.ans, sep=' ')


if __name__ == '__main__':
    T3()