import string

# 1 有序队列
def T1(s):
    ss = s * 2
    ans = s
    n = len(s)
    for i in range(1, n):
        if ss[i:i+n] < ans:
            ans = ss[i:i+n]
    return ans

class Queue():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

# 2 最近的请求次数
def T2(lst):
    output = []
    q = Queue()
    n = len(lst)
    for i in range(n):
        q.enqueue(lst[i])
        pt, cnt = i+1, 0
        while pt < n and lst[pt] == lst[i]:
            cnt += 1
            pt += 1
        while q.items[0] < lst[i] - 10000:
            q.dequeue()
        output.append(q.size() + cnt)
    return output

# 3 基数排序
def T3(lst):
    max_len = len(str(max(lst)))
    for i in range(max_len):
        queues = [Queue() for _ in range(10)]
        for item in lst:
            digit = int(item/(10**i) % 10)
            queues[digit].enqueue(item)
        lst = []
        for q in queues:
            while not q.isEmpty():
                lst.append(q.dequeue())
    return lst

if __name__ == "__main__":
    lst = eval(input())
    print(T3(lst))
