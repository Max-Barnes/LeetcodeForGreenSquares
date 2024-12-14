# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

#challenge: o(n) solution

# brute force
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for index, num in enumerate(nums):
            nums[index] = num * num
            
        return sorted(nums)

# 2nd attempt without sorted and after watching neetcode's video

# left pointer will stay at the start, right pointer at the end

# which ever pointer is the larger square put it in the end of a result array, and increment/decrement the pointer

# keep going until pointers meet

# leetcode says this is 0(n log n) if you wanted to do it in o(n) with less memory you would just need to add them to a list 
# and then return that list reversed instead of creating the result list and going backwards
class secondSolution:
    def sortedSquares(self,nums: list[int]) -> list[int]:
        right = len(nums) - 1
        left = 0
        # sets an array at length of right
        result = [0] * len(nums)
    # use a counter to set the items in the correct position
        counter = len(nums) - 1
        # while left != right is when they connect, i need it to be when they cross
        while right >= left or left <= right:
            # if the left number is the greater square
            if abs(nums[left]) > abs(nums[right]):
                result[counter] = nums[left] * nums[left]
                # decrement counter, increment left pointer
                counter -= 1
                left += 1
            # if it is neither then the right pointer is the larger square
            else:
                result[counter] = nums[right] * nums[right]
                counter -= 1
                right -=1


        return result

# #optimal solution
# class optimal:
#     def sortedSquares(self,nums: list[int]) -> list[int]:

sol = secondSolution()

test = [-7,-3,2,3,11]

print(sol.sortedSquares(test))