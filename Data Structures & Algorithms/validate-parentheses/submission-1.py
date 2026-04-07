class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)

            else:
                if len(stack) == 0:
                    return False
                if ch == ')' and stack[-1] != '(':
                    return False
                if ch == ']' and stack[-1] != '[':
                    return False
                if ch == '}' and stack[-1] != '{':
                    return False
                
                stack = stack[:-1]

        if len(stack) > 0:
            return False

        return True
