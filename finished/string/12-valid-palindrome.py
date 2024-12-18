# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# i think ive done this one so i timed myself this time
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # will take more than just reversing and checking equality since they use full sentences
        # return s[::-1] == s
        
        # go through string and add them to a res string, from there check if it is the same backwards with return above
        res = ''
        for char in s:
            if char.isalnum():
                res = res + char
        res = res.lower()
        return res[::-1] == res

#neetcode shows a way to do it with two pointers instead of rewriting the whole list, if the character is valid 
# then it should match the opposite pointer, iterate until pointers meet or the characters are different 
class optimalSolutionAttempt:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()

        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left] is not s[right]:
                    print(s[left],s[right])
                    return False
                left += 1
                right -= 1
            else:
                if not s[left].isalnum():
                    left += 1
                if not s[right].isalnum():
                    right -= 1
            
        return True
    
# The way to do it without isalnum() is to use ascii values and create your own function
# in place of isalnum

sol = optimalSolutionAttempt()

print(sol.isPalindrome('A man, a plan, a canal: Panama'))

print(sol.isPalindrome('Fuck123'))