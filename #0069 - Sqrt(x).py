#Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
#
#You must not use any built-in exponent function or operator.
#
#For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
#
#Example 1:
#Input: x = 4
#Output: 2
#Explanation: The square root of 4 is 2, so we return 2.
#
#Example 2:
#Input: x = 8
#Output: 2
#Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


class Solution(object):
    def mySqrt(self, x):
        L, R = 0, x+1
        while L < R:
            M = int( L + (R-L)/2)
            if M*M <= x and (M+1)*(M+1) > x:
                return M
            elif M*M > x:
                R = M
            else :
                L = M + 1
        return 0
    
