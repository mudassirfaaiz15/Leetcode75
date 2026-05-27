class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        last_lower = {}
        first_upper = {}

        for i, ch in enumerate(word):

            if ch.islower():
                last_lower[ch] = i

            else:
                low = ch.lower()

                if low not in first_upper:
                    first_upper[low] = i

        count = 0

        for ch in last_lower:

            if ch in first_upper and last_lower[ch] < first_upper[ch]:
                count += 1

        return count