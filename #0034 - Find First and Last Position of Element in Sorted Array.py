#Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#
#If target is not found in the array, return [-1, -1].
#
#You must write an algorithm with O(log n) runtime complexity.
#
#
#Example 1:
#Input: nums = [5,7,7,8,8,10], target = 8
#Output: [3,4]
#
#Example 2:
#Input: nums = [5,7,7,8,8,10], target = 6
#Output: [-1,-1]
#
#Example 3:
#Input: nums = [], target = 0
#Output: [-1,-1]

class Solution(object):
     def searchRange(self, nums, target):
        L,R = 0,len(nums)
        R1,R2=-1,-1
        while L < R:
            M = L + (R-L)/2
            if nums[M] < target:
                L = M+1
            elif nums[M] > target or (nums[M] == target and not M-1==-1 and nums[M-1] == target):
                R = M
            else:
                R1=M
                L=R   
        L,R = 0,len(nums)
        while L < R:
            M = L + (R-L)/2
            if nums[M] < target or (nums[M] == target and not M+1==len(nums) and nums[M+1] == target):
                L = M+1
            elif nums[M] > target :
                R = M
            else:
                R2=M
                L=R
        return (R1,R2)  
