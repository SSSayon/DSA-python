# 基本数据结构

## 栈

- 后进先出 (LIFO, last-in first-out)

### 栈操作与实现
- 栈操作
    - `Stack()` 创建一个空栈。
    - `push(item)` 将`item`添加到栈的顶端。
    - `pop()` 将栈顶端的元素移除，并返回该元素。
    - `peek()` 返回栈顶端的元素，但是并不移除该元素。
    - `isEmpty()` 检查栈是否为空。
    - `size()` 返回栈中元素的数目。
    
- Python 实现

    ```python
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
    ```

### 栈的应用

#### 括号匹配，进制转换

#### 前序、中序和后序表达式

- 前序表达式和后序表达式都不需要括号，*中序表达式是最不理想的算式表达式！*

- 中序表达式转换为后序表达式

  - 算法：

    1. 创建用于保存运算符的空栈`opstack`，以及一个用于保存结果的空列表。
    2. 使用字符串方法`split`将输入的中序表达式转换成一个列表。
    3. 从左往右扫描这个标记列表，
       - 如果标记是*操作数*，将其添加到结果列表的末尾；
       - 如果标记是*左括号*，将其压入`opstack`栈中；
       - 如果标记是*右括号*，反复从`opstack`栈中移除元素，直到移除对应的左括号。将从栈中取出的每一个运算符都添加到结果列表的末尾；
       - 如果标记是*运算符*，将其压入`opstack`栈中。**但是，在这之前，需要先从栈中取出优先级更高或相同的运算符，并将它们添加到结果列表的末尾。** 
    4. 当处理完输入表达式以后，检查`opstack`。将其中所有残留的运算符全部添加到结果列表的末尾。

    **idea:** 括号内可看作独立部分（通过 3-2 & 3-3 独立解决），于是只需考虑最基本的两种情况：

    - `A + B * C` $\to$ `A B C * +` 
    - `A * B + C` $\to$ `A B * C +` 

    可以发现，对于第二种情况，若未考虑 3-4 **加粗部分**，由于栈的 LIFO 性质，`+` 将在 `*` 之前，违背了优先顺序。事实上，处理某个运算符时，可将栈内的优先级更高的运算符视为在括号内，于是同 3-3 操作，将其取出并添加到结果列表末尾。

  - Python 实现

    ```python
    import Stack, string
    def infixToPostfix(infixexpr):
        prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
        opStack = Stack()
        postfixList = []
        tokenList = infixexpr.split()
    
        for token in tokenList:
            if token in string.ascii_uppercase:
                postfixList.append(token)
            elif token == '(':
                opStack.push(token)
            elif token == ')':
                topToken = opStack.pop()
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            else:
                while (not opStack.isEmpty()) and \
                (prec[opStack.peek()] >= prec[token]):
                    postfixList.append(opStack.pop())
                opStack.push(token)
    
        while not opStack.isEmpty():
            postfixList.append(opStack.pop())
    
        return " ".join(postfixList)
    ```
  
- 计算后序表达式

  - 非常 trivial ，两个两个取操作数，注意从栈中取出后要颠倒顺序。

  - Python 实现

    ```python
    import Stack
    def postfixEval(postfixExpr):
        operandStack = Stack()
        tokenList = postfixExpr.split()
    
        for token in tokenList:
            if token in "0123456789":
                operandStack.push(int(token))
            else:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop() # 注意顺序
                result = doMath(token, operand1, operand2)
                operandStack.push(result)
    
        return operandStack.pop()
    
    def doMath(op, op1, op2):
        if op == "*":
            return op1 * op2
        elif op == "/":
            return op1 / op2
        elif op == "+":
            return op1 + op2
        else:
            return op1 - op2
    ```





