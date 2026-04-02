class Solution:
    def generateParenthesis(self, n: int):
        res = []

        def isValid(ans):
            stack = []
            for val in ans:
                if val == '(':
                    stack.append(val)
                else:
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0

        def helperfunction(length, temp):
            if length == 2 * n:
                if isValid(temp):
                    res.append(temp)
                return
            
            helperfunction(length + 1, temp + '(')
            helperfunction(length + 1, temp + ')')

        helperfunction(0, "")
        return res