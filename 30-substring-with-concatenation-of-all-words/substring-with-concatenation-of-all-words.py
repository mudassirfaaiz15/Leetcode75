from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words

        word_count = Counter(words)

        result = []

        # Try every possible starting offset
        for i in range(word_len):

            left = i
            curr_count = {}
            count = 0

            # Move window word by word
            for j in range(i, len(s) - word_len + 1, word_len):

                word = s[j:j + word_len]

                if word in word_count:

                    curr_count[word] = curr_count.get(word, 0) + 1
                    count += 1

                    # If word appears too many times
                    while curr_count[word] > word_count[word]:

                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        count -= 1
                        left += word_len

                    # Valid window found
                    if count == total_words:
                        result.append(left)

                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        count -= 1
                        left += word_len

                else:
                    # Reset window
                    curr_count.clear()
                    count = 0
                    left = j + word_len

        return result