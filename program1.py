class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[]
        matching_parentheses = {')':'(','}':'{',']':'['}
        for char in s:
            if char in matching_parentheses:

            
            if stack else '#'
        if matching_parentheses[char]!=top_element:
            return False
        else:
            stack.append(char)
            return not stack
        pass







    



  

