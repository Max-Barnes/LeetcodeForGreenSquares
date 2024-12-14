# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # hint is quicksort
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l] # this python code allows you to move two numbers at once
                l += 1
sol = Solution()

test1 = [0,1,0,3,13]

test2 = [0,0,1]

test3 = [1]

# sol.moveZeroes(test1)

sol.moveZeroes(test2)

# sol.moveZeroes(test3)