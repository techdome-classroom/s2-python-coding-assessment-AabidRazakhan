class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:  
            return 0
        
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        
        result = 0
        for i in range(len(s)):
            if i > 0 and roman_values[s[i]] > roman_values[s[i - 1]]:
                result += roman_values[s[i]] - 2 * roman_values[s[i - 1]]
            else:
                result += roman_values[s[i]]
        
        return result


# Example usage:
solution = Solution()
print(solution.romanToInt("III"))  # Output: 3
print(solution.romanToInt("LVIII"))  # Output: 58
print(solution.romanToInt("MCMXCIV"))  # Output: 1994
print(solution.romanToInt(""))  # Output: 0
