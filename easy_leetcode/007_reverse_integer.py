__author__ = 'mad&pudding'

# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-integer/
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# https://leetcode.com/problems/reverse-integer/
# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321
# Repeatedly multiply previous result by 10 and add last digit.
# Time - O(n) where n is the number of digits.
# Space - O(n), same number of digits in output as input.

class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        negative = x < 0
        x = abs(x)
        rev = 0
        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10
        if rev > 2**31 - 1:
            return 0
        else:
            return rev if not negative else -rev
