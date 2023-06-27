import string
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

# 1 有效的括号
def T1():
    lst = list(str(input()))
    p = {')': '(', '}': '{', ']': '['}
    s = Stack()
    for item in lst:
        if item in "({[":
            s.push(item)
        else:
            if not s.isEmpty() and s.peek() == p[item]:
                s.pop()
            else:
                print('False')
                return
    if s.isEmpty():
        print('True')
    else:
        print('False')

# 2 一维开心消消乐
def T2():
    lst = list(str(input()))
    s = Stack()
    for item in lst:
        if s.isEmpty():
            s.push(item)
        elif item == s.peek():
            s.pop()
        else:
            s.push(item)
    if s.isEmpty():
        print(None)
    else:
        print(*s.items, sep='')

# 3 强迫症老板和他的洗碗工0
def T3():
    lst = list(str(input()))
    s = Stack()
    pt = 0
    for item in lst:
        if not s.isEmpty() and s.peek() == item:
            s.pop()
        elif pt > int(item):
            print('No')
            return
        else:
            while pt <= int(item):
                s.push(str(pt))
                pt += 1
            s.pop()
    print('Yes')

if __name__ == "__main__":
    T3()


