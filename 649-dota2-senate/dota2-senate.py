from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        radiant = deque()
        dire = deque()

        # Store indices of senators
        for i, ch in enumerate(senate):
            if ch == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        # Process rounds
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            # The senator with smaller index acts first
            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)

        return "Radiant" if radiant else "Dire"