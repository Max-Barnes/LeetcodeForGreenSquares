# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example
# Input: nums = [1,2,3,1]

# Output: true

# Explanation: The element 1 occurs at the indices 0 and 3.
# this solution works in O(n log n) since I used sorted
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # this lets me create a placeholder incase 0 is in the array
        onDeck = None
        #update onDeck to the number you are looking at, if onDeck = n then you can return true otherwise keep going through the array
        for n in sorted(nums):
            if (n == onDeck):
                return True
            else:
                onDeck = n
        #if you go through the entire list, there are no duplicates
        return False

# using a hashset solution takes less time but more space. Change answer depending on requirements

sol = Solution()

test = [3, 2, 3] # True

test2 = [1,2,3] # False


print(sol.containsDuplicate(test))

print(sol.containsDuplicate(test2))
