class Solution:
    def maxVowels(self, s, k):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Count vowels in the first window
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        
        max_count = count

        # Sliding window
        for i in range(k, len(s)):
            # Remove left character
            if s[i - k] in vowels:
                count -= 1

            # Add right character
            if s[i] in vowels:
                count += 1

            max_count = max(max_count, count)

        return max_count