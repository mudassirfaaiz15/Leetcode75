class Solution:
    def longestOnes(self, nums, k):
        left = 0
        zeros = 0
        max_length = 0

        for right in range(len(nums)):
            # Count zeros in the window
            if nums[right] == 0:
                zeros += 1

            # If zeros exceed k, shrink window
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # Update maximum length
            max_length = max(max_length, right - left + 1)

        return max_length