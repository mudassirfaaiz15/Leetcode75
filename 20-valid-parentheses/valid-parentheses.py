class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:

            # Opening bracket
            if ch in "([{":
                stack.append(ch)

            # Closing bracket
            else:
                if not stack or stack[-1] != brackets[ch]:
                    return False

                stack.pop()

        return len(stack) == 0