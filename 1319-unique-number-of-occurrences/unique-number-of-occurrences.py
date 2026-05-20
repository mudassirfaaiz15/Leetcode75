class Solution:
    def uniqueOccurrences(self, arr):
        freq = {}

        # Count occurrences of each number
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        # Check if occurrence counts are unique
        occurrences = list(freq.values())

        return len(occurrences) == len(set(occurrences))