class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        res_stack = []
        c = 0
        while c < len(tokens):
            if tokens[c] != '+' and tokens[c] != '-' and tokens[c] != '*' and tokens[c] != '/':
                res_stack.append(tokens[c])
            elif tokens[c] == '+':
                print('+')
                print(res_stack[-2:])
                res = int(res_stack[-2]) + int(res_stack[-1])
                res_stack.pop()
                res_stack.pop()
                res_stack.append(res)
            elif tokens[c] == '-':
                print('-')
                print(res_stack[-2:])
                res = int(res_stack[-2]) - int(res_stack[-1])
                res_stack.pop()
                res_stack.pop()
                res_stack.append(res)
            elif tokens[c] == '*':
                print('*')
                print(res_stack[-2:])
                res = int(res_stack[-2]) * int(res_stack[-1])
                res_stack.pop()
                res_stack.pop()
                res_stack.append(res)
            elif tokens[c] == '/':
                print('/')
                print(res_stack[-2:])
                res = int(res_stack[-2]) / int(res_stack[-1])
                res_stack.pop()
                res_stack.pop()
                res_stack.append(res)
            c += 1
        return int(res_stack[-1])
