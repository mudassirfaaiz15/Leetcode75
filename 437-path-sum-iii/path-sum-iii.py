# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def pathSum(self, root, targetSum):

        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(node, current_sum):

            if not node:
                return 0

            current_sum += node.val

            # Number of valid paths ending at current node
            count = prefix[current_sum - targetSum]

            # Add current prefix sum
            prefix[current_sum] += 1

            # Explore left and right subtree
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)

            # Backtrack
            prefix[current_sum] -= 1

            return count

        return dfs(root, 0)