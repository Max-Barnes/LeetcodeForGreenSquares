# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:

# Input: s = "()" s = "()[]{}" # Input: s = "([])"

# Output: true

# Example 3:

# Input: s = "(]" 

# Output: false

# hint is to use a stack

# if you see a closing character without looking for one, return false EX: "([)]" false

# if not stack returns true if stack is empty, false if it isnt
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # edge case if the first character is a closing or last is an opening
        if s[0] in ")]}" or s[-1] in "([{":
            return False
        for char in s:
            if char == ")":
                if not stack:
                    return False
                elif stack[len(stack) - 1] != "(":
                    return False
                else:
                    stack.pop()
            elif char == "]":
                if not stack:
                    return False
                elif stack[len(stack) - 1] != "[":
                    return False
                else:
                    stack.pop()
            elif char == "}":
                if not stack:
                    return False
                elif stack == False or stack[len(stack) - 1] != "{":
                    return False
                else:
                    stack.pop()
            # not a closing character therefore we can add it to the stack
            else:
                stack.append(char)

            
        # if you make it through the whole thing without returning false its true
        return len(stack) == 0

# needcodes solution uses a hashmap to hold the values and not need the whole ugly if else tree i did
class optimalSolution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
# same idea as what i made just using hashmap makes it much easier to read
    
sol = Solution()

test = "(((()))"

print(sol.isValid(test))