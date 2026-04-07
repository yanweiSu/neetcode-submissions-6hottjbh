class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack_pointer = -1
        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False

                compare = stack[-1]
                if ch == ')' and compare != '(':
                    return False
                if ch == ']' and compare != '[':
                    return False
                if ch == '}' and compare != '{':
                    return False

                stack.pop()

        if len(stack) > 0:
            return False

        return True
