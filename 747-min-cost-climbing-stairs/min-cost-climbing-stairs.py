class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)

        dp0, dp1 = cost[0], cost[1]

        for i in range(2, n):
            current = cost[i] + min(dp0, dp1)
            dp0, dp1 = dp1, current

        return min(dp0, dp1)