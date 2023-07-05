# 1:二叉树复原
def T1():
    lst = [0] + eval(input())
    for i in range(1, len(lst)):
        if lst[i] == None:
            lst[i] = 'None'

    def recover(lst: list):
        i = 1
        while 2 * i + 1 <= len(lst):
            if lst[i] == 'None':
                lst.insert(2 * i, 'None')
                lst.insert(2 * i + 1, 'None')
            else:
                if lst[2 * i] != 'None':
                    if 2 * i + 1 >= len(lst):
                        lst.insert(2 * i + 1, 'None')
            i += 1

    def inorder(lst, root):
        res = []
        if root * 2 < len(lst):
            res += inorder(lst, root * 2)
        if lst[root]:
            res.append(lst[root])
        if root * 2 + 1 < len(lst):
            res += inorder(lst, root * 2 + 1)
        return res
    
    recover(lst)
    res = [i for i in inorder(lst, 1) if i != 'None']
    print(*res, sep=' ')

# 2:翻转二叉树
def T2():
    lst = [0] + list(map(int, input().split()))
    n = len(lst) - 1

    def postinorder(root):
        res = []
        if root * 2 + 1 <= n:
            res += postinorder(root*2+1)
        res.append(lst[root])
        if root * 2 <= n:
            res += postinorder(root*2)
        return res
    
    print(*postinorder(1), sep=' ')

# 3:多叉树遍历
def T3():
    lst = eval(input())
    def postorder(lst):
        res= []
        if len(lst) > 1:
            childs = lst[1:]
            for child in childs:
                res += postorder(child)
        res.append(lst[0])
        return res
    print(*postorder(lst), sep=' ')



if __name__ == '__main__':
    T3()