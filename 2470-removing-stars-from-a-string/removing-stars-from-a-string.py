class Solution:
    def removeStars(self, s):
        stack = []

        for char in s:
            if char == '*':
                stack.pop()   # Remove closest non-star character
            else:
                stack.append(char)

        return "".join(stack)