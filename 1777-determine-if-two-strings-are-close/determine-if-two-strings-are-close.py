from collections import Counter

class Solution:
    def closeStrings(self, word1, word2):
        # Both strings must have same unique characters
        if set(word1) != set(word2):
            return False

        # Count frequency of each character
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        # Frequency counts must match after sorting
        return sorted(freq1.values()) == sorted(freq2.values())