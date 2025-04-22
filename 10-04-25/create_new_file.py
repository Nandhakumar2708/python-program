class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip(" ")
        x = 1
        number_string = ""
        
        for char in s:
            if char.isdigit() and (char or number_string):
                number_string += char

            elif not number_string and char in '+-':
                x = -1 if char == '-' else 1
                number_string += '0'

            elif not char.isdigit():
                break

        number = int(number_string) * x if number_string else 0
        number = (2 ** 31) - 1 if number > (2 ** 31) - 1 else number
        number = -(2 ** 31) if number < -(2 ** 31) else number

        return number
