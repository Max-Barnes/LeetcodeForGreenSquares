# leetcode 12 integer to roman numerals

# M = 1000 D = 500 C = 100 L = 50 X = 10 V = 5 I = 1

#just do it like making change check if each can work.

# problem doing the 1 before rule 
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        returnStr = ''

        while num >= 0:
            if (num == 0):
                return returnStr
            elif (num - 1000 >= 0):
                num = num - 1000
                returnStr = f'{returnStr}M'
            elif (num - 500 >= 0):
                num = num - 500
                returnStr = f'{returnStr}D'
            elif (num - 100 >= 0):
                num = num - 100
                returnStr = f'{returnStr}C'
            elif (num - 50 >= 0):
                num = num - 50
                returnStr = f'{returnStr}L'
            elif (num - 10 >= 0):
                num = num - 10
                returnStr = f'{returnStr}X'
            elif (num - 5 >= 0):
                num = num - 5
                returnStr = f'{returnStr}V'
            elif (num - 1 >= 0):
                num = num - 1
                returnStr = f'{returnStr}I'




sol = Solution()

# 115 should be CXV
test = 115

print(sol.intToRoman(test))