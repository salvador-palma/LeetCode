#You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.
#
#Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.
#
#Example 1:
#Input: letters = ["c","f","j"], target = "a"
#Output: "c"
#Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
#
#Example 2:
#Input: letters = ["c","f","j"], target = "c"
#Output: "f"
#Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
#
#Example 3:
#Input: letters = ["x","x","y","y"], target = "z"
#Output: "x"
#Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        L=0
        R=len(letters)-1
        while L < R:
            M = L + (R-L)/2
            if letters[M] <= target < letters[M+1]:
                return letters[M+1]
            elif letters[M] <= target:
                L = M +1
            elif letters[M] > target:
                R = M                
        return letters[0]
