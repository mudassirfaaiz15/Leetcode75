class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, target, path):
            if target == 0:
                res.append(path[:])
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])

                # same index because we can reuse the number
                backtrack(i, target - candidates[i], path)

                path.pop()

        backtrack(0, target, [])
        return res