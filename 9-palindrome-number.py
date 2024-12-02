# Leet code question 9

# Given an integer x, return true if x is a palindrome, and false otherwise. IE 121 true -121 false

# turn x into string, split this into char array

# go through the char array backwards to create a reversed version of x

# return x = reversed x

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)

        # [x for x in string] just creates a char array in python
        xChar = [band for band in string]

        # char array of x created now we can use reversed() and join() to get the opposite as a string

        reversedXChar = reversed(xChar)

        reversedX = "".join(reversedXChar)


        # use string == reversedX not x == reversedX since they will not be equal due to typing
        return string == reversedX

        






sol = Solution()

test = 121

print(sol.isPalindrome(test))