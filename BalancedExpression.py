class Stack:
    def __init__(self):
        self.items = []
        self.front = -1

    def push(self,item):
        self.front += 1
        self.items.append(item)

    def pop(self):
        if self.front < 0:
            print("Stack Is empty")
        else:
            item = self.items[self.front]
            self.items.pop(self.front)
            self.front -= 1
            return item
        
    def isStackEmpty(self):
        if self.front > -1 :
            return False
        else:
            return True
    
def isBalanced(str):
    stack = Stack()
    for i in range(len(str)):
        if str[i] == '(' or str[i] == '{' or str[i] == '[':
            stack.push(str[i])
        else:
            if stack.isStackEmpty():
                return False
            top = stack.pop()
            if (str[i] == ')' and top != '(') or  (str[i] == '}' and top != '{') or (str[i] == ']' and top != '['):
                return False
            
    return stack.isStackEmpty()

def postFixEval(str):
    stack = Stack()
    for i in range(len(str)):
        if str[i] == '+' or str[i] == '*' or str[i] == '/' or str[i] == '-':
            secondeItem = stack.pop()
            firstItem = stack.pop()
            stack.push(evaluateExpressoin(int(firstItem),int(secondeItem),str[i]))
        else:
            stack.push(str[i])

    return stack.pop()

def evaluateExpressoin(first,second,operator):
    if operator == '+':
        return int(first + second)
    if operator == '-':
        return int(first - second)
    if operator == '*':
        return int(first * second)
    if operator == '/':
        return int(first / second)         

print(postFixEval("525*+5/"))
#print(isBalanced("[{({}"))

# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# stack.push(40)
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
