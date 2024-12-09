# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# try to do it in o(n)
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        # sort the array, since its a given that the array will always be an odd length and will always have a majority just return what is in the middle
        sortNum = sorted(nums)
        # double // is integer division, which drops the decimal and lets us get midpoint of odd list
        return sortNum[len(nums) // 2]

# answer is o(n) memory complexity

# Boyer-Moore Algorithm for good memory and linear time -from neetcode
# https://stackoverflow.com/questions/6207819/boyer-moore-algorithm-understanding-and-example
class optimalSolution:
    def majorityElement(self, nums: list[int]) -> int:
        result = 0
        count = 0

        for n in nums:
            # cant be majority if count goes to 0
            if count == 0:
                result = n
            # increase count by one if the n value is the same as result, decrement if different
            count += (1 if n == result else -1)

sol = Solution()

test = [3, 2, 3]

test2 = [2,2,1,1,1,2,2]


print(sol.maxProfit(test))

print(sol.maxProfit(test2))

