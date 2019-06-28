"""
作者(github账号)：GoddessLuBoYan
内容：将四则运算的中缀表达式转换成后缀表达式并计算
要求：每个数字必须都是一位数，我没有考虑多位数和小数的情况
"""


# 基本容器定义

class Container:
    def __init__(self, iterator=None):
        self._list = []
        if iterator:
            for i in iterator:
                self.push(i)
        
    def __len__(self):
        return self._list.__len__()
    
    def __str__(self):
        return self._list.__str__()
    
    def __repr__(self):
        return self._list.__repr__()
    
    def isempty(self):
        return self._list.__len__() == 0
        
    def push(self, u):
        pass
        
    def get(self):
        pass
    
    def pop(self):
        pass
    
class Stack(Container):
    def push(self, u):
        self._list = [u] + self._list
        
    def get(self):
        return self._list[0] if not self.isempty() else None
    
    def pop(self):
        return self._list.pop(0) if not self.isempty() else None
    
class Queue(Container):
    def push(self, u):
        self._list = self._list + [u]
        
    def get(self):
        return self._list[-1] if not self.isempty() else None
    
    def pop(self):
        return self._list.pop(0) if not self.isempty() else None
        


# 解析中缀表达式并转换成后缀表达式
        
ex = "5+9-8*7+6*(5-4+(3*2))"
def level(v):
    if v in '$':
        return 0
    elif v in '+-':
        return 1
    elif v in '*/':
        return 2
    elif v in '()':
        return 0
    raise Exception(v)

def compare(v1, v2):
    return level(v1) - level(v2)

def parse(ex):
    ops = Stack("$")
    exp = Queue()
    for c in (ex + "$"):
        if c in '1234567890':
            exp.push(c)
        elif c == '(':
            ops.push('(')
        elif c == ')':
            while True:
                top = ops.pop()
                if top == '(':
                    break
                if top == '$':
                    raise
                exp.push(top)
        elif c in '+-*$':
            top = ops.get()
            l1 = level(c)
            l2 = level(top)
            while l1 <= l2:
                if c == '$' and top == '$':
                    return exp, ops
                exp.push(ops.pop())
                top = ops.get()
                l2 = level(top)
            ops.push(c)

        print(ops)
        print(exp)
        print()
        
exp, ops = parse(ex)


# 计算后缀表达式，并使用eval验算原中缀表达式

curr = Stack()
while not exp.isempty():
    t = exp.pop()
    if t in "123456789":
        curr.push(t)
    elif t in '()':
        continue
    else:
        t2 = curr.pop()
        t1 = curr.pop()
        result = eval(str(t1) + str(t) + str(t2))
        print(str(t1) + str(t) + str(t2), '=', result)
        curr.push(result)
print(curr)
print(eval(ex))