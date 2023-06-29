# 1:铺瓷砖
def T1():
    n = int(input())
    ans_lst = [1, 1, 2, 4, 8]
    for i in range(5, n+1):
        ans_lst.append(ans_lst[i-1] + ans_lst[i-2] + ans_lst[i-3] + ans_lst[i-4])
    print(ans_lst[n])

# 2:分发糖果
def T2():
    rating = eval(input())
    n = len(rating)
    res = [1] * n
    for i in range(1, n):
        if rating[i] > rating[i-1]:
            res[i] = res[i-1] + 1
    for i in range(n-2, -1, -1):
        if rating[i] > rating[i+1]:
            res[i] = max(res[i], res[i+1] + 1)
    print(sum(res))

# 3:表达式按不同顺序求值
def T3():
    nums, ops = [], []
    def findWays(expr):
        num = 0
        for c in expr:
            if '0' <= c <= '9':
                num = num * 10 + ord(c) - 48
            else:
                ops.append(c)
                nums.append(num)
                num = 0
        else:
            nums.append(num)
    expr = input()
    findWays(expr)

    def calc(a, b, opr):
        if opr == '+':
            return a + b
        elif opr == '-':
            return a - b
        else:
            return a * b
        
    def helper(_nums, _ops):
        if _ops == []:
            return _nums
        _ans = []
        for i in range(len(_ops)):
            for _a in helper(_nums[:i+1], _ops[:i]):
                for _b in helper(_nums[i+1:], _ops[i+1:]):
                    _ans.append(calc(_a, _b, _ops[i]))
        return _ans

    ans = sorted(list(set(helper(nums, ops))))
    print(*ans, sep=',')


if __name__ == '__main__':
    T3()