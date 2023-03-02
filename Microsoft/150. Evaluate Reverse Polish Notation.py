class Solution:
    def evalRPN(self, tokens):
        stack  =[]
        for  i in tokens:
            if i not in "+/-*":
                stack.append(int(i))
            else:
                # print(stack,i)
                n2 = stack.pop()
                n1 = stack.pop()
                if i == "+":
                    stack.append(int(n1) + int(n2))
                elif i == "-":
                    stack.append(int(n1) - int(n2))
                elif i == "/":
                    stack.append(int(int(n1)/int(n2)))
                elif i == "*":
                    stack.append(int(n1) * int(n2))
                # print(stack)
        return stack.pop()