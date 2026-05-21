from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        ans = []

        for spell in spells:
            target = (success + spell - 1) // spell
            
            idx = bisect_left(potions, target)
            
            ans.append(m - idx)

        return ans